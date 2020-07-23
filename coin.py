import random
import time

def displayIntro():
	print('''Из за того, что у вас есть тяга к маленьким мальчикам,
вас посадили на зону.''')
	print()

def chooseChear():
	chear = ''
	while chear != '1' and chear != '2':
		print('''В хате вас встречает пахан.
			Он медленно встает с нар...
			И говорит
			-Есть два стула.
			На одном пики точеные.
			На другом хуи дроченые.
			На какой сам сядешь, на какой мать посадишь?
			(нажмите 1 или 2)''')
		chear = input()

	return chear

def checkChear(choosenChear):
	print('Вы приближаетесь ко стулу...')
	time.sleep(2)
	print('Ваше очко дрожит от страха...')
	time.sleep(2)
	print('Пахан достает заточку и спускает штаны...')
	print()
	time.sleep(2)

	friendlyChear = random.randint(1, 2)

	if choosenChear == str(friendlyChear):
		print('Хм... Сам на пики, а мать на колени? Ну ты ровный фраер!')
	else:
		print('Ага! Хуи выбрал! Пацаны держи его...')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
	displayIntro()
	chearNumber = chooseChear()
	checkChear(chearNumber)

	print('Сыграешь на очко еще раз? (да или нет)')
	playAgain = input()