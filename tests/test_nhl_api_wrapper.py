from nhl_api import nhl


def test_schedule():
    """Tests a call to the schedule endpoint"""

    nhl_instance = nhl()
    response = nhl_instance.get_schedule_today()

    assert isinstance(response, dict)
