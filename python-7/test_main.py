from main import get_temperature
from unittest.mock import patch
import pytest

list_tests = [
    (-14.235004, -51.92528, 62, 16),
    (70.8565444, 45.644562, 86, 30),
    (90.7455683, -35.334732, 70, 21)
]


@patch("main.requests.get")
@pytest.mark.parametrize("lat,lng,temperature,expected", list_tests)
def test_get_temperature_by_lat_lng(mock_get, lat, lng, temperature, expected):

    temperature = {"currently": {"temperature": temperature}}

    mock_get.return_value.json.return_value = temperature
    result = get_temperature(lat, lng)

    assert result == expected
