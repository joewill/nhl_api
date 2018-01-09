from nhl_api import nhl


def test_schedule():
    """Tests a call to the schedule endpoint"""

    nhl_instance = nhl()
    schedule_today = nhl_instance.schedule_today()

    assert isinstance(
        schedule_today, list), "Schedule_today must be of type list"
    # need to add many more tests


def test_standings():
    """Tests a call to the standings endpoint"""
    nhl_instance = nhl()
    standings = nhl_instance.standings()

    assert isinstance(standings, dict), "Standings must be of type dict"


def test_team():
    """Tests a call to the team endpoint"""
    nhl_instance = nhl()
    team = nhl_instance.team(22)

    assert isinstance(team, dict), "Team must be of type dict"


def test_player():
    """Tests a call to the player endpoint"""
    nhl_instance = nhl()
    player = nhl_instance.player(8479318)

    assert isinstance(player, dict), "Player must be of type dict"
