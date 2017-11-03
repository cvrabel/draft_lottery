from random import randint
import json

def generateLotteryNumbers():
	allChosenNumbersArray = []
	firstPickNumbersArray = []
	secondPickNumbersArray = []
	thirdPickNumbersArray = []
	fourthPickNumbersArray = []
	fifthPickNumbersArray = []

	allChosenNumbersArray, firstPickNumbersArray = fillArrayWithNumbers(allChosenNumbersArray, 430)
	allChosenNumbersArray, secondPickNumbersArray = fillArrayWithNumbers(allChosenNumbersArray, 265)
	allChosenNumbersArray, thirdPickNumbersArray = fillArrayWithNumbers(allChosenNumbersArray, 165)
	allChosenNumbersArray, fourthPickNumbersArray = fillArrayWithNumbers(allChosenNumbersArray, 90)
	allChosenNumbersArray, fifthPickNumbersArray = fillArrayWithNumbers(allChosenNumbersArray, 50)

	dumpNumbers([firstPickNumbersArray, secondPickNumbersArray, thirdPickNumbersArray, fourthPickNumbersArray, fifthPickNumbersArray])



def fillArrayWithNumbers(allChosenNumbersArray, n):
	numbersArray = []
	while len(numbersArray) < n:
		randomNumber = randint(0,999)
		if randomNumber not in allChosenNumbersArray:
			allChosenNumbersArray.append(randomNumber)
			numbersArray.append(randomNumber)
	numbersArray.sort()
	return allChosenNumbersArray, numbersArray;

def dumpNumbers(arrayOfArrays):
	for i in range(5):
		fileName = "pickNumbersArray" + str(i+1) + ".json"
		with open(fileName, 'w') as fp:
			json.dump(arrayOfArrays[i], fp)


if __name__ == "__main__":
	generateLotteryNumbers()
