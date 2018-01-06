import requests


class nhl():

    def __init__(self):
        self.endpoint = 'https://statsapi.web.nhl.com/api/v1'

    def get_schedule_today(self):
        path = self.endpoint + '/schedule'
        schedule = requests.get(path)
        return schedule.json()
