import pytest
import requests
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def test_categories_empty():


    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # response = session.get(f"{os.getenv('URL_HOST')}/v1/categories")
    response = session.get('http://127.0.0.1/v1/categories/')

    
    # response = requests.get(f"{os.getenv('URL_HOST')}/v1/categories",  headers = {'User-agent': 'your bot 0.1'})

    print (response)
    
    # Verificar que la respuesta tenga código de estado 200 (OK)
    assert response.status_code == 200
    
    # Verificar que la respuesta sea un array vacío
    assert response.json() == []