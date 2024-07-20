import requests
import json

class GetRequester:
    '''initializes with url returns lis-dict'''
    def __init__(self, url):
        '''initialize attributes'''
        self.url = url
    
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        '''return python list/dict'''
        response_dict = json.loads(self.get_response_body())

        return response_dict
    
    
target_data = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(target_data.load_json())