import requests
from bs4 import BeautifulSoup

from config import url, headers
from contollers.create_csv import create_table
from contollers.parser import get_persons_list


if __name__ == '__main__':
    r = requests.get(url=url, headers=headers)
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')

    # prepare
    for data in soup(['style', 'script']):
        data.decompose()

    all_text_blocks = soup.find_all('div', class_='tn-atom')
    persons = get_persons_list(all_text_blocks)

    create_table(['city', 'name', 'profession', 'email'], 'Persons.csv', persons)
