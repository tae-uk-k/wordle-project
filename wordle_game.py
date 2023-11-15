keyword = "random"
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


