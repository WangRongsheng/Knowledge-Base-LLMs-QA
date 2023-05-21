import requests
import json

def process_text(text):
    data = {'text': text}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/llm_search', data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result['response']
    else:
        return None

if __name__ == '__main__':
    text = '青光眼是什么？'
    
    results = process_text(text)
    print(results)
