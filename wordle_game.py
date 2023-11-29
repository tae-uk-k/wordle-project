import tkinter as tk
import pandas as pd
import random

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

class Wordle:
    df = pd.read_excel("./단어장전처리.xlsx", sheet_name="vocList", header = None)
    difficulty = 0
    difficultyArea = [[3, 4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
    keyword = ""
    wordLength = 0
    
    def __init__(self):
        df = pd.read_excel("./단어장전처리.xlsx", sheet_name="vocList", header = None)
    
    def preSetting(self):
        lengthList = []
        lengthSum = 0
        for v in self.difficultyArea[self.difficulty]:
            lengthList.append(self.df[v - 1][0])
            lengthSum += self.df[v - 1][0]
            randomNumber = random.randrange(0, lengthSum - 1)
            print("randomNumber :", randomNumber) #for debuging
        for i in range(len(self.difficultyArea[self.difficulty])):
            if (randomNumber > lengthList[i]):
                randomNumber -= lengthList[i]
                continue
            else:
                self.keyword = self.df[v - 1][randomNumber + 1]
                break
        self.wordLength = len(self.keyword)
        #keyword를 임의화 시켰는데 범위가 맞는지 확신하지 못하겠음.....

    def gamePlay(self):
        inputWord = [[' ' for j in range(self.wordLength)] for i in range(self.wordLength + 1)]
        wordStatus = [[0 for j in range(self.wordLength)] for i in range(self.wordLength + 1)]    # 0 - 미입력, 1 - 없음, 2 - 있지만 자리가 다름, 3 - 자리까지 같음
        turn = 0
        print("wordle game start!!!")
        while(True):
            turn += 1
            
            #입력부
            correctAnswer = True
            while(correctAnswer):
                ans = input(">>")
                if (len(ans) > self.wordLength):
                    correctAnswer = True
                else:
                    correctAnswer = False
                    for i in range(len(ans)):
                        inputWord[turn - 1][i] = ans[i]
                        if (ans[i] == self.keyword[i]):
                            wordStatus[turn - 1][i] = 3
                        else:
                            count = 0
                            for j in range(self.wordLength):
                                #print(ans[i] == keyword[j])
                                if (ans[i] == self.keyword[j]):
                                    wordStatus[turn - 1][i] = 2
                                    count += 1
                            if (count == 0):
                                wordStatus[turn - 1][i] = 1
            
            #출력부
            print("turn :", turn)
            for i in range(self.wordLength + 1):
                for j in range(self.wordLength):
                    if (wordStatus[i][j] == 0):
                        print("___", end=' ')
                    elif (wordStatus[i][j] == 1):
                        print(' ', inputWord[i][j], ' ',sep='', end=' ')
                    elif(wordStatus[i][j] == 2):
                        print(' ', inputWord[i][j], '?',sep='', end=' ')
                    elif(wordStatus[i][j] == 3):
                        print(' ', inputWord[i][j], '!',sep='', end=' ')
                print()


w = Wordle()
w.preSetting()
w.gamePlay()














