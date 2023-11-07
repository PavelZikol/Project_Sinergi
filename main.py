from players import Player
from utils import load_random_word

user_name = input('Ведите имя игрока: ')
player = Player(user_name)
basic_word = load_random_word()
min_word = len(min(basic_word.valid_subwords, key=len))

# Привет от программы
print(f'''Привет, {user_name})
Составте {basic_word.counting_subwords()} слов из слова "{basic_word.basic_word}"
Слова должны быть не короче {min_word} букв
Чтобы закончить игру, угадайте все слова или напишите "stop". Чтобы получить подсказку, напишите "help".
Поехали, ваше первое слово?: ''', end='')


help = 0  # счетчик подсказок

# запуск цикла, пока количество угаданных слов не сравняется с количеством слов, которые можно составить
while player.get_words_used() < basic_word.counting_subwords():
    user_answer = input('').lower()  # ответ игрока
    if len(user_answer) < min_word:  # проверка на краткость
        print('слишком короткое слово')
    elif user_answer in {'стоп', 'stop'}:  # проверка на остановку игры
        break
    # помощь игроку, цикл проходит по всем словам, если игрок не отгадал, то выводится слово и добавляется в отгаданные
    elif user_answer == 'help' or user_answer == 'помощь':
        remaining_words = tuple(set(basic_word.valid_subwords) - set(player.words_used))
        word = remaining_words[0]
        help += 1
        player.word_to_used(word)
        print(f'{word}, осталось: {len(basic_word.valid_subwords) - len(player.words_used)}')
        continue
    elif not basic_word.checking_subwords(user_answer):  # проверка введенного слова в списке допустимых подслов
        print('неверно')
    elif player.checking_word_before(user_answer):  # проверка было ли введенное слово угадано
        print('уже использовано')
    # добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю
    else:
        player.word_to_used(user_answer)
        print(f'верно, осталось: {len(basic_word.valid_subwords) - len(player.words_used)}')

print(f'Игра завершена, вы угадали {player.get_words_used() - help} слов(а)')  # вывод результата
