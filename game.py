from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC TAC TOE")
player = 'X'

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

messagebox.showinfo('Welcome', "Hi, Sunny Lets Start !!")

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("Arial", 60), width=4, height=2, highlightbackground='powder blue', command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)


def callback(r, c):
    global player

    if player == 'X' and states[r][c] == 0:
        b[r][c].config(text='X', fg='blue', highlightbackground='white')
        states[r][c] = 'X'
        player = 'O'

    elif player == 'O' and states[r][c] == 0:
        b[r][c].config(text='O', fg='orange', highlightbackground='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()


def check_for_winner():
    for k in range(3):
        if states[k][0] == states[k][1] == states[k][2] != 0:
            result()

    for k in range(3):
        if states[0][k] == states[1][k] == states[2][k] != 0:
            result()

    if states[0][0] == states[1][1] == states[2][2] != 0 or states[2][0] == states[1][1] == states[0][2] != 0:
        result()


def result():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    ans = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", ans)
    root.destroy()  # is used to close the program


root.mainloop()