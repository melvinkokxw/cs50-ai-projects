import pytest

import degrees


@pytest.fixture
def load_small_database():
    degrees.load_data("small")


def test_small_0(load_small_database):
    result = degrees.shortest_path("102", "102")
    assert result == []


def test_small_1(load_small_database):
    result = degrees.shortest_path("102", "129")
    assert result == [("104257", "129")]


def test_small_2(load_small_database):
    result = degrees.shortest_path("102", "398")
    possibilities = [[("112384", "158"), ("109830", "398")], [("112384", "641"), ("109830", "398")]]
    assert result in possibilities
    