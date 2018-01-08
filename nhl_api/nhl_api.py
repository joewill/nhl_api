import requests
import json
from collections import namedtuple


class nhl():

    def __init__(self):
        self.endpoint = 'https://statsapi.web.nhl.com/api/v1'

    def schedule_today(self):
        path = self.endpoint + '/schedule'

        data = requests.get(path)
        data.raise_for_status()

        schedule = json.loads(data.text, object_hook=lambda s: namedtuple(
            'schedule', s.keys())(*s.values()))

        return schedule

#x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    def standings(self):
        path = self.endpoint + '/standings'

        standings = requests.get(path)
        standings.raise_for_status()

        return standings.json()
