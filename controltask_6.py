text = "книга без слов"
text_1 = text.replace(" ", "")
def find_izogramm (text_1):
    if len(text_1) == len(set(text_1)):
        return 'izogramm'
    else:
        return 'not izogramm'

print(find_izogramm(text_1))