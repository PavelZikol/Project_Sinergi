class BasicWord:

    def __init__(self, basic_word: object, valid_subwords: object) -> str:
        '''исходное слово и набор допустимых слов, составленных из исходного'''
        self.basic_word = basic_word
        self.valid_subwords = valid_subwords

    def checking_subwords(self, user_answer):
        '''проверка введенного слова в списке допустимых подслов (вернет bool)'''
        return user_answer in self.valid_subwords

    def counting_subwords(self):
        '''подсчет количества подслов (вернет int)'''
        return len(self.valid_subwords)

    def __repr__(self):
        return f'{self.basic_word} {self.valid_subwords}'