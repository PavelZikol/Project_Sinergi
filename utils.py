from random import choice
import requests
from basic_word import BasicWord
import json


def load_random_word():
    '''
    - получает список слов с внешнего ресурса,
    - выберает случайное слово,
    - создает экземпляр класса,
    - возвращает этот экземпляр.
    '''
    response = requests.get('https://www.jsonkeeper.com/b/58RR')
    data = response.json()
    base_word = choice(data)
    basic_word = BasicWord(base_word['word'], base_word['subwords'])
    return basic_word
