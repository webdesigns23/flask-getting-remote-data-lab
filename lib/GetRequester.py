import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(url)
        return response.content

    def load_json(self):
        response = requests.get(url)
        data = response.json()
        return data

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"    

'''To check if displaying results, shows in plaintext format'''
# results = GetRequester(url).get_response_body()
# print(results)

'''To check if displaying results, shows in JSON format'''
# results_json = GetRequester(url).load_json()
# print(json.dumps(results_json, indent=1))