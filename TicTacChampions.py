# Gra w kółko i krzyżyk

from tkinter import *
import random

def next_turn(row, column):

    global gracz

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if gracz == gracze[0]:

            buttons[row][column]['text'] = gracz

            if check_winner() is False:
                gracz = gracze[1]
                label.config(text=("Runda "+gracze[1]))

            elif check_winner() is True:
                label.config(text=("Wygrywa "+gracze[0]))

            elif check_winner() == "Draw":
                label.config(text="Remis !")

        else:

            buttons[row][column]['text'] = gracz

            if check_winner() is False:
                gracz = gracze[0]
                label.config(text=("Runda "+gracze[0]))

            elif check_winner() is True:
                label.config(text=("Wygrywa "+gracze[1]))

            elif check_winner() == "Draw":
                label.config(text="Remis !")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Draw"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global gracz

    gracz = random.choice(gracze)

    label.config(text=gracz+" runda")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Gra w kółko i krzyżyk")
gracze = ["x","o"]
gracz = random.choice(gracze)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text="runda "+ gracz, font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="Restartuj plansze", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
