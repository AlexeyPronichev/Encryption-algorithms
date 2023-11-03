#### Created by IFIFZNEN. ArtikovTU (m3o-318bk-19). Laba 3: Shift Vijenera
def encryptDecrypt(mode, message, keys):
	for key in listKeys:
		final = ""
		key *= len(message) // len(key) + 1
		for index, symbol in enumerate(message):
			if mode == 'E':
				temp = ord(symbol) + ord(key[index])
			if mode == 'D':
				temp = ord(symbol) - ord(key[index])
			final += chr(temp % 26 + ord('A'))
		message = final
	return final

metod = input("Vvedite funkciyu ([E]ncrypt|[D]ecrypt): ").upper()
if metod not in ['E','D']:
	print("Oshibka: Funkciya ne naydena!"); raise SystemExit
	
text = input("Vvedite text: ").upper().replace(" ", "")
numberKeys = int(input("Kol-vo kluchey: "))

listKeys = []
for index in range(numberKeys):
	 listKeys.append(input("Vvedite kluch["+str(index)+"]: ").upper().replace(" ", ""))


print("Vash text:",encryptDecrypt(metod, text, listKeys))

