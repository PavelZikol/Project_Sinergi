class Player:

    def __init__(self, user_name):
        '''имя пользователя, использованные слова пользователя'''
        self.user_name = user_name
        self.words_used = []

    def get_words_used(self):
        '''получение количества использованных слов (возвращает int)'''
        return len(self.words_used)

    def word_to_used(self, user_answer):
        '''добавление слова в использованные слова (ничего не возвращает)'''
        self.words_used.append(user_answer)

    def checking_word_before(self, user_answer):
        '''проверка использования данного слова до этого (возвращает bool)'''
        return user_answer in self.words_used

    def __repr__(self):
        return f'{self.user_name} {self.words_used}'
