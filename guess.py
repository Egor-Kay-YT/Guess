import random
#Выбрать уровень сложности 
otvet = input('Выберите уровень сложности\n1=Легкий\n2=Средний\n3=Сложный\n4=НЕВОЗМОЖНЫЙ\nВыбирайте:')
#Если ответ (пользователя) 1 то
if otvet == '1':
	#Лёгкий уровень сложности
	words = ['Крокодил', 'Корова', 'Кошка']
	choicewords = random.choice(words)
	text = choicewords
	if text == 'Крокодил':
		def RandomNumber():
			RandomNumber=random.randint(1, 24)
			return RandomNumber
	if text == 'Корова':
		def RandomNumber():
			RandomNumber=random.randint(1, 10)
			return RandomNumber
	if text == 'Кошка':
		def RandomNumber():
			RandomNumber=random.randint(1, 15)
			return RandomNumber
	new_text = ""
	for char in enumerate(text):
	    if char[0] % RandomNumber() == 0:
	        new_text += '_'
	    else:
	        new_text += char[1]
	print(new_text)
	
#Если ответ (пользователя) 2 то 
if otvet == '2':
	#Средний уровень сложности
	words = ['Крокодил', 'Корова', 'Кошка']
	choicewords = random.choice(words)
	text = choicewords
	if text == 'Крокодил':
		def RandomNumber():
			RandomNumber=random.randint(1, 16)
			return RandomNumber
	if text == 'Корова':
		def RandomNumber():
			RandomNumber=random.randint(1, 10)
			return RandomNumber
	if text == 'Кошка':
		def RandomNumber():
			RandomNumber=random.randint(1, 10)
			return RandomNumber
	new_text = ""
	for char in enumerate(text):
	    if char[0] % RandomNumber() == 0:
	        new_text += '_'
	    else:
	        new_text += char[1]
	print(new_text)
	
#Если ответ (пользователя) 3 то
if otvet == '3':
	#Сложный уровень сложности
	words = ['Крокодил', 'Корова', 'Кошка']
	choicewords = random.choice(words)
	text = choicewords
	if text == 'Крокодил':
		def RandomNumber():
			RandomNumber=random.randint(1, 8)
			return RandomNumber
	if text == 'Корова':
		def RandomNumber():
			RandomNumber=random.randint(1, 5)
			return RandomNumber
	if text == 'Кошка':
		def RandomNumber():
			RandomNumber=random.randint(1, 5)
			return RandomNumber
	new_text = ""
	for char in enumerate(text):
	    if char[0] % RandomNumber() == 0:
	        new_text += '_'
	    else:
	        new_text += char[1]
	print(new_text)
	
#Если ответ (пользователя) 4 то
if otvet == '4':
	#НЕВОЗМОЖНЫЙ УРОВЕНЬ СЛОЖНОСТИ
	words = ['Крокодил', 'Корова', 'Кошка']
	choicewords = random.choice(words)
	text = choicewords
	if text == 'Крокодил':
		def RandomNumber():
			RandomNumber=random.randint(1, 1)
			return RandomNumber
	if text == 'Корова':
		def RandomNumber():
			RandomNumber=random.randint(1, 1)
			return RandomNumber
	if text == 'Кошка':
		def RandomNumber():
			RandomNumber=random.randint(1, 1)
			return RandomNumber
	new_text = ""
	for char in enumerate(text):
	    if char[0] % RandomNumber() == 0:
	        new_text += '_'
	    else:
	        new_text += char[1]
	print(new_text)
	
#КОНЕЦ