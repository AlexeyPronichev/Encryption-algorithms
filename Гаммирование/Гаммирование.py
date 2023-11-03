#Гаммирование

alphabet_eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(text, gamma):
    text_len = len(text)
    out_str = []
    space = 0

    for index, char in enumerate(text):
        if char in alphabet_eng:
            current = text[index]
            current_key = gamma[(index - space) % len(gamma)]
            # print(alphabet_eng.index(current), alphabet_eng.index(current_key))
            out_str.append(alphabet_eng[(alphabet_eng.index(current) + alphabet_eng.index(current_key)) % 2])
        elif char == ' ':
            space += 1
            out_str.append(' ')
        else:
            out_str.append(char)

    #print(space)
    return ''.join(out_str)


def decrypt(text, gamma):
    text_len = len(text)
    out_str = []
    space = 0

    for index, char in enumerate(text):
        if char in alphabet_eng:
            current = text[index]
            current_key = gamma[(index - space) % len(gamma)]
            # print(alphabet_eng.index(current), alphabet_eng.index(current_key))
            out_str.append(alphabet_eng[(alphabet_eng.index(current) - alphabet_eng.index(current_key)) % 26])
        elif char == ' ':
            space += 1
            out_str.append(' ')
        else:
            out_str.append(char)

    #print(space)
    return ''.join(out_str)

if __name__ == "__main__":
    temp = int(input('Введите 1 - для шифрации, 2 - для дешифрации: '))
    if temp == 1:
        text = input('Введите исходный текст: ')
        gamma = input('Введите гамму: ')
        print(encrypt(text, gamma))
    if temp == 2:
        text = input('Введите зашифрованный текст: ')
        gamma = input('Введите гамму: ')
        print(decrypt(text, gamma))
