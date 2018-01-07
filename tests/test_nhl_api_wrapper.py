from nhl_api import nhl


def test_schedule():
    """Tests a call to the schedule endpoint"""

    nhl_instance = nhl()
    response = nhl_instance.schedule_today()

    assert isinstance(response, list), "Schedule must be of type list"
    # need to add many more tests


def test_standings():
    """Tests a call to the standings endpoint"""
    nhl_instance = nhl()
    response = nhl_instance.standings()

    assert isinstance(response, dict), "Standings must be of type dict"
