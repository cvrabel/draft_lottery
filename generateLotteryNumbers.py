from random import randint
import json


def generate_lottery_numbers():
    allChosenNumbersArray = []
    firstPickNumbersArray = []
    secondPickNumbersArray = []
    thirdPickNumbersArray = []
    fourthPickNumbersArray = []
    fifthPickNumbersArray = []

    allChosenNumbersArray, firstPickNumbersArray = fill_array_with_numbers(allChosenNumbersArray, 250)
    allChosenNumbersArray, secondPickNumbersArray = fill_array_with_numbers(allChosenNumbersArray, 250)
    allChosenNumbersArray, thirdPickNumbersArray = fill_array_with_numbers(allChosenNumbersArray, 160)
    allChosenNumbersArray, fourthPickNumbersArray = fill_array_with_numbers(allChosenNumbersArray, 190)
    allChosenNumbersArray, fifthPickNumbersArray = fill_array_with_numbers(allChosenNumbersArray, 150)

    write_to_json([firstPickNumbersArray, secondPickNumbersArray, thirdPickNumbersArray,
                 fourthPickNumbersArray, fifthPickNumbersArray])


def fill_array_with_numbers(allChosenNumbersArray, n):
    numbersArray = []
    while len(numbersArray) < n:
        randomNumber = randint(0, 999)
        if randomNumber not in allChosenNumbersArray:
            allChosenNumbersArray.append(randomNumber)
            numbersArray.append(randomNumber)
    numbersArray.sort()
    return allChosenNumbersArray, numbersArray


def write_to_json(arrayOfArrays):
    for i in range(5):
        fileName = "pickNumbersArray" + str(i + 1) + ".json"
        with open(fileName, 'w') as fp:
            json.dump(arrayOfArrays[i], fp)


if __name__ == "__main__":
    generate_lottery_numbers()
