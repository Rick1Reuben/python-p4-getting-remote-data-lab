import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            res = requests.get(self.url)
            res.raise_for_status()  # Raise an exception for HTTP errors
            return res.content
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def load_json(self):
        try:
            res_body = self.get_response_body()
            if res_body:
                return json.loads(res_body)
            else:
                return None
        except json.JSONDecodeError as e:
            print(f"JSON decode failed: {e}")
            return None