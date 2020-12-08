from tkinter import *
from tkinter import messagebox as msg

# TODO -> Initialize Window
root = Tk()
root.geometry("376x372")
root.resizable(width=False, height=False)
root.title("Intra Tic Tac Toe")


def restart():
    for j in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        j["text"] = ""


# TODO-> Function to End game
def finish(text):
    msg.showinfo("Finished", f"{text} Won!")
    restart()


# TODO -> Function to check if te1xt in vertical,horizontal or diagonal buttons are same
def check(lst):
    for j in range(0, 3):
        if lst[0][j]["text"] == lst[1][j]["text"] == lst[2][j]["text"] != "":  # Check Horizontal
            finish(lst[0][j]["text"])
            break

        elif lst[j][0]["text"] == lst[j][1]["text"] == lst[j][2]["text"] != "":  # Check Vertical
            finish(lst[j][0]["text"])
            break

        elif lst[0][0]["text"] == lst[1][1]["text"] == lst[2][2]["text"] != "":  # Check Diagonally(L-R)
            finish(lst[0][0]["text"])
            break

        elif lst[0][2]["text"] == lst[1][1]["text"] == lst[2][0]["text"] != "":  # Check Diagonally(R-L)
            finish(lst[0][2]["text"])
            break


count = 0


# TODO-> Function to insert "x" and "o" alternatively and check if all buttons are full
def press(btn):
    global count
    if btn["text"] == "":  # Check if button already has a Text
        count += 1
        if count % 2 == 0:
            btn.config(text="X", fg="red")
        else:
            btn.config(text="o", fg="blue")
        check(((b1, b2, b3), (b4, b5, b6), (b7, b8, b9)))
        for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9):  # Loop to check if all buttons are full
            if i["text"] == "":
                break
        else:
            msg.showerror("Finished", "Sorry game Draw!")
            restart()


men = Menu(root, font=(None, 20), fg="red")
root.config(menu=men)
sd = men.add_command(label="Restart", command=restart)

# TODO -> Initializing Buttons and Gridding Them
b1 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b1))
b2 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b2))
b3 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b3))
b4 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b4))
b5 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b5))
b6 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b6))
b7 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b7))
b8 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b8))
b9 = Button(root, height=2, width=5, font=(None, 30), relief=RAISED, command=lambda: press(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
