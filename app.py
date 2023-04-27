""" Author: Abeil Coelho Júnior | https://www.linkedin.com/in/abeil/
Creation date: 2023-04-27
Description: Example code to retry handle to web scraping process.
Version: 1
Modification date: 2023-04-27 """

import time
from bs4 import BeautifulSoup
import requests

MAX_RETRIES = 5
sessao = requests.Session()

LIST_OF_WORDS = ["python", "programming", "technology"]


def get_result(busca, session):
    """ Example function, fetches the HTML of the Google search results page. """
    for i in range(MAX_RETRIES):
        try:
            url = "https://www.google.com/search?&q={}".format(busca)

            response = session.get(url)
            response.raise_for_status()

            result_html = BeautifulSoup(response.text, "lxml")

            return result_html

        except (requests.exceptions.RequestException, ConnectionResetError) as erro:
            print(f"Attempt {i+1}: {str(erro)}")
            time.sleep(45)
            if i + 1 == MAX_RETRIES:
                result_html = "Error"

                return result_html


for word in LIST_OF_WORDS:
    result = get_result(word, sessao)
    sessao = requests.Session()
