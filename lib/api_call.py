from requests import get
import json

def call_api(url):
    response = get(url=url)
    status_code = response.status_code
    data = response.text

    if status_code != 200:
        raise RuntimeError('Api call to url', url, 'failed with status code:', status_code, 'and message:', data)

    data = json.loads(data)

    return status_code, data
