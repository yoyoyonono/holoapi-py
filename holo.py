from typing import Dict
from requests.sessions import Session

s = Session()
class Holo:
    def __init__(self, version: str):
        self.url = 'https://api.holotools.app/' + version + '/'
    def getLive(self, channel_id: int = None, max_upcoming_hours: int = None, lookback_hours: int = None, hide_channel_desc: bool = False) -> Dict:
        params = {}
        if bool(channel_id):
            params['channel_id'] = channel_id
        if bool(max_upcoming_hours):
            params['max_upcoming_hours'] = channel_id
        if bool(lookback_hours):
            params['lookback_hours'] = channel_id
        if hide_channel_desc:
            params['hide_channel_desc'] = 1
        return s.get(self.url + 'live').json()

if __name__ == "__main__":
    from pprint import pprint
    h = Holo('v1')
    pprint(h.getLive(hide_channel_desc=True))