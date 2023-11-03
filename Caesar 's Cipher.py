alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #русский алфавит
simvolo= '".,!?:'
probel ='()*&^-'
message = input("Сообщение: ").upper()
k=1
itog = ''
metod = input('Выберите метод шифрование/расшифрование/взлом: ')#выбор режима работа
if metod == 'шифрование':
    smeshenie = int(input('Шаг шифровки: '))
    smeshenie = smeshenie % 33
    s_smeshenie=smeshenie%6
    for i in message:
        mesto = alfavit_RU.find(i) #проверка места буквы в алфавите
        new_mesto = mesto + smeshenie #определение позиции буквы
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto] #запись в итоговое слово
        elif i in simvolo:
            mesto = simvolo.find(i)
            new_smeshenie = (mesto + s_smeshenie)%6
            itog += simvolo[new_smeshenie]
        elif i==' ':
            itog += probel[(k+s_smeshenie)%6]
        else:
            itog += i
        k=k+1
    print(itog)
elif metod == 'расшифровка': #режим расшифровки
    smeshenie = int(input('Шаг шифровки: '))
    smeshenie = smeshenie % 33
    s_smeshenie=smeshenie%6
    for i in message:
        mesto = alfavit_RU.find(i) #проверка места буквы в алфавите
        new_mesto = mesto - smeshenie#определение позиции буквы
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        elif i in simvolo:
            mesto = simvolo.find(i)
            new_smeshenie = (mesto - s_smeshenie)%6
            itog += simvolo[new_smeshenie]
        elif i in probel:
            itog += ' '
        else:
            itog += i
        k=k+1
    print(itog)
else: #режим взлома
        s=1
        while s<33: #перебор вариантов на русском
            k=0
            itog = ''
            for i in message:
                mesto = alfavit_RU.find(i)
                new_mesto = mesto - s
                if i in alfavit_RU:
                    itog += alfavit_RU[new_mesto]
                elif i in simvolo:
                    mesto = simvolo.find(i)
                    new_smeshenie = (mesto - (s%6))%6
                    itog += simvolo[new_smeshenie]
                elif i in probel:
                    itog += ' '
                else:
                    itog += i
                k=k+1
            s = s + 1

            print(itog) #вывод итогов