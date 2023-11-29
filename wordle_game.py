import tkinter as tk
import pandas as pd
import random

df = pd.read_excel("./단어장전처리.xlsx", sheet_name="vocList", header = None)
#print(df)
'''
window = tk.Tk()
window.title("< Wordle Game >")
window.geometry("500x500+500+150")
window.resizable(False, False)

def keyboardClicked():
    print(1)


button = [tk.Button(window, text="버튼 1", command=keyboardClicked) for i in range(26)]
for i in range(26):
    button[i].pack(side = tk.LEFT)
'''

difficulty = 0
difficultyArea = [[3, 4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]

lengthList = []
lengthSum = 0
for v in difficultyArea[difficulty]:
    lengthList.append(df[v - 1][0])
    lengthSum += df[v - 1][0]

randomNumber = random.randrange(0, lengthSum - 1)
print("randomNumber :", randomNumber)
for i in range(len(difficultyArea[difficulty])):
    if (randomNumber > lengthList[i]):
        randomNumber -= lengthList[i]
        continue
    else:
        keyword = df[v - 1][randomNumber + 1]
        break

print(keyword)

#keyword = "random"
wordLength = len(keyword)

#임의로 시작 단어를 "random"으로 지정함

inputWord = [[' ' for j in range(wordLength)] for i in range(wordLength + 1)]
wordStatus = [[0 for j in range(wordLength)] for i in range(wordLength + 1)]    # 0 - 미입력, 1 - 없음, 2 - 있지만 자리가 다름, 3 - 자리까지 같음

turn = 0
print("wordle game start!!!")
while(True):
    turn += 1
    
    #입력부
    correctAnswer = True
    while(correctAnswer):
        ans = input(">>")
        if (len(ans) > wordLength):
            correctAnswer = True
        else:
            correctAnswer = False
            for i in range(len(ans)):
                inputWord[turn - 1][i] = ans[i]
                if (ans[i] == keyword[i]):
                    wordStatus[turn - 1][i] = 3
                else:
                    count = 0
                    for j in range(wordLength):
                        #print(ans[i] == keyword[j])
                        if (ans[i] == keyword[j]):
                            wordStatus[turn - 1][i] = 2
                            count += 1
                    if (count == 0):
                        wordStatus[turn - 1][i] = 1
    
    #출력부
    print("turn :", turn)
    for i in range(wordLength + 1):
        for j in range(wordLength):
            if (wordStatus[i][j] == 0):
                print("___", end=' ')
            elif (wordStatus[i][j] == 1):
                print(' ', inputWord[i][j], ' ',sep='', end=' ')
            elif(wordStatus[i][j] == 2):
                print(' ', inputWord[i][j], '?',sep='', end=' ')
            elif(wordStatus[i][j] == 3):
                print(' ', inputWord[i][j], '!',sep='', end=' ')
        print()


