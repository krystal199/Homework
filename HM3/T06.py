def int_func(input_word: str):
    return "".join([
        input_word[0].upper(), input_word[1:]
    ])


user_words = input("Введите строку из нескольких слов >>> ").split()
