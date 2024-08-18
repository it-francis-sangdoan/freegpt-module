import requests
import json

class GPT:

    def __init__(self, top_p=0.9, temperature=0.7, presence_penalty=0, frequency_penalty=0,
        model_name='gpt-4', instructor="", payloads=None, api=None, headers=None):

        self.top_p = top_p
        self.temperature = temperature
        self.presence_penalty = presence_penalty
        self.instructor = instructor
        self.frequency_penalty = frequency_penalty
        self.model_name = model_name
        self.payloads = payloads
        self.api = api
        self.headers = headers

        self.__setModel__()
    

    def __setModel__(self):
        if self.instructor != "":
            self.payloads['messages'][0]['content'] = self.instructor
        self.payloads['presence_penalty'] = self.presence_penalty
        self.payloads["temperature"] = self.temperature
        self.payloads["top_p"] = self.top_p
        self.payloads['frequency_penalty'] = self.frequency_penalty
        self.payloads['model'] = self.model_name
    

    def inference(self, text):
        self.payloads['messages'][1]['content'] = text
        response = requests.post(self.api, headers=self.headers, json=self.payloads)
        
        response_text = ""
        for r in response.text.splitlines():
            try:
                response_text += json.loads(r[6:])['choices'][0]['delta']['content']
            except:
                continue

        return response_text.encode("latin1", errors='replace').decode('utf-8', errors='replace')