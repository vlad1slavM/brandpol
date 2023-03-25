import re

from config import cites


def get_persons_list(blocks) -> list[dict]:
    """
    Считывает html страницу и парсить из нее информацию о сотрудниках
    :param blocks: html code
    :return: Вернет список словарей вида [{'city': '', 'name': '', 'profession': '', 'email': ''}]
    """
    flag = False
    city = ''
    profession = None
    email = None
    name = None
    reg = re.compile(r'[а-я А-Я-]+')
    persons_list = []
    for block in blocks:
        if block.get('field'):
            if block.text == 'Наша команда':
                flag = True
                continue
            if flag:
                txt = block.text
                if '<br' in str(block):
                    if block.find('a'):
                        email = block.find('a').text
                        profession = txt.replace(email, '')
                        profession = re.findall(reg, profession)[0]
                    else:
                        profession = txt
                        email = None
                else:
                    if txt == 'Вакансии':
                        break
                    else:
                        if txt in cites:
                            city = txt
                        else:
                            name = txt
                if name and profession:
                    persons_list.append({'city': city, 'name': name, 'profession': profession, 'email': email})
                    name, profession, email = None, None, None
    return persons_list
