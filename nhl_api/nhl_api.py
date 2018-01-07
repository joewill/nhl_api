import requests


class nhl():

    def __init__(self):
        self.endpoint = 'https://statsapi.web.nhl.com/api/v1'

    def schedule_today(self):
        path = self.endpoint + '/schedule'

        schedule = requests.get(path)
        schedule.raise_for_status()

        return schedule.json()['dates']

    def standings(self):
        path = self.endpoint + '/standings'

        standings = requests.get(path)
        standings.raise_for_status()

        return standings.json()
