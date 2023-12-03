from Wordle import Wordle
from SaveData import saveData

s=saveData()
s.start_game()
w = Wordle()
ans = input("난이도를 입력하세요(쉬움 : 0, 보통 : 1, 어려움 : 2) : ")
w.setDifficulty(ans)
w.preSetting()
w.gamePlay()










