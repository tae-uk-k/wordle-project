import tkinter as tk


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

from Wordle import Wordle

w = Wordle()
w.preSetting()
w.gamePlay()














