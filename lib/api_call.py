from requests import get
import time

def call_api(url):
    #Count failed calls 
    failed_api_calls = 0
    
    while failed_api_calls < 4:
        #Call api
        response = get(url=url)
        #Retrieve status code and response data
        status_code = response.status_code
        data = response.text

        #Return not found aka no more Pokemons to harvest
        if status_code == 404:
            return status_code, data
        #Retry api call on failure
        elif status_code != 200 and failed_api_calls < 4:
            time.sleep(10)
            failed_api_calls += 1
            continue

        return status_code, data

    raise RuntimeError('Api call to url', url, 'failed with status code:', status_code, 'and message:', data)