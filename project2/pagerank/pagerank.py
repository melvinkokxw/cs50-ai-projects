import os
import random
import re
import sys
import numpy as np
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # Create empty probability distribution function
    prob_dist = dict.fromkeys(corpus.keys(), 0)

    # Get total number of pages in corpus
    total_pages = len(corpus)

    # Get number of linked pages on current page
    linked_pages = len(corpus[page])

    # If no linked pages, equal probability to visit all pages
    if linked_pages == 0:
        for key in prob_dist:
            prob_dist[key] += 1 / total_pages

    # Otherwise calculate based on damping factor
    else:
        for key in prob_dist:
            prob_dist[key] += (1-damping_factor) / total_pages
            if key in corpus[page]:
                prob_dist[key] += damping_factor / linked_pages

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Create pagerank dictionary
    pagerank = dict.fromkeys(corpus.keys(), 0)

    # Pre-generate transition models for all pages in corpus
    prob_dist_all = {}
    for key in corpus:
        prob_dist_all[key] = transition_model(corpus, key, damping_factor)

    # Generate random first page
    page = np.random.choice([*pagerank.keys()])
    pagerank[page] += 1

    # Get n-1 more samples
    for i in range(n-1):
        # Unpack into list literal
        keys = [*prob_dist_all[page].keys()]
        values = [*prob_dist_all[page].values()]

        page = np.random.choice(keys, p=values)
        pagerank[page] += 1

    # Divide pagerank values by n to get proportion
    for key in pagerank:
        pagerank[key] /= n

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Get total number of pages in corpus
    total_pages = len(corpus)

    # Create empty pagerank dictionary
    pagerank = dict.fromkeys(corpus.keys(), 1 / total_pages)

    # Iterate repeatedly until condition met
    while True:
        # Create empty copy of pagerank dict
        new_pagerank = dict.fromkeys(corpus.keys(), 0)

        for page in corpus:
            # Get number of linked pages on current page
            linked_pages = len(corpus[page])

            # Add to new pageranks according to formula
            if linked_pages != 0:
                for linked_page in corpus[page]:
                    new_pagerank[linked_page] += damping_factor * pagerank[page] / linked_pages

            # If no linked pages, treat as link to all pages
            else:
                for key in corpus:
                    new_pagerank[key] += damping_factor * pagerank[page] / total_pages

            # Add (1-d)/N to each pagerank
            new_pagerank[page] += (1 - damping_factor) / total_pages

        # Check if any value changed by more than 0.001
        iterate_again = False
        for key in new_pagerank:
            if new_pagerank[key] - pagerank[key] > 0.001:
                iterate_again = True
                break

        # Update pagerank according to new values
        pagerank = copy.deepcopy(new_pagerank)

        if iterate_again is False:
            break

    return pagerank


if __name__ == "__main__":
    main()
