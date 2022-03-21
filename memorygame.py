import tkinter
import random

root = tkinter.Tk()
label1 = tkinter.Label(root, text = "Choose the Right Number Pattern", font = ('Helvetica', 20))
label1.pack(pady = 10)
scoreLabel = tkinter.Label(root, text = "Press Enter to Start", font = ('Helvetica', 20))
scoreLabel.pack(pady = 10)
label_expl = tkinter.Label(root, text = "(wait for the numbers to appear then click the buttons for the right number pattern)", font = ('Helvetica', 12))
label_expl.pack(pady = 10)
mframe = tkinter.Frame(root)
mframe.pack(pady = 30)
ans_list = []
new_list = []
btn_list = []
plc_list = []
list_click = []
lvl_list = []
score = 0
count = 0
count2 = 0
i = 0
j = 0
num = 0
initial = 4
lvl = 1

def click(b,place):
    global count, ans_list, i, count2, list_click, new_list, j, plc_list, lvl_list, initial, score, lvl
    if b["text"] == " " and count < initial:
        list_click.append(place)
        count += 1

    if (list_click[j] == new_list[i]) and count2 < initial:
        b["text"] = ans_list[i]
        count2 += 1
        i += 1
        j += 1
    else:
        b["text"] = random.randint(0,20)
        i += 1
        j += 1

    if count2 == initial:
        if initial == 9:
            score += 10
            scoreLabel.config(text = "Score: " + str(score))
            ans_list.clear()
            new_list.clear()
            list_click.clear()
            plc_list.clear()
            lvl_list.clear()
            i = 0
            j = 0
            count = 0
            count2 = 0
            score = 0
            lvl = 1
            initial = 4
            label7 = tkinter.Label(root, text = "Congratulations! You Reached the Last Level. Press Enter to Play Again. ", font = ('Helvetica', 14))
            label7.pack(pady = 21)
            label7.after(6000, label7.destroy)
        else:
            score += 10
            scoreLabel.config(text = "Score: " + str(score))
            label3 = tkinter.Label(root, text = "You Win!", font = ('Helvetica', 20))
            label3.pack(pady = 20)
            label3.after(3000,label3.destroy)
            label5 = tkinter.Label(root, text = "Press Enter to Keep Playing", font = ('Helvetica', 20))
            label5.pack(pady = 21)
            label5.after(3000, label5.destroy)
            ans_list.clear()
            new_list.clear()
            list_click.clear()
            plc_list.clear()
            lvl_list.clear()
            i = 0
            j = 0
            count = 0
            count2 = 0
            initial += 1
            lvl += 1

    if count == initial and count2 != initial:
        score = 0
        label4 = tkinter.Label(root, text = "You Lose!", font = ('Helvetica', 20))
        label4.pack(pady = 20)
        label4.after(3000,label4.destroy)
        label6 = tkinter.Label(root, text = "Press Enter to Play Again", font = ('Helvetica', 20))
        label6.pack(pady = 21)
        label6.after(3000,label6.destroy)
        ans_list.clear()
        new_list.clear()
        list_click.clear()
        plc_list.clear()
        lvl_list.clear()
        i = 0
        j = 0
        count = 0
        count2 = 0
        initial = 4
        lvl = 1



def app(b,place):
    global ans_list, new_list, lvl_list, btn_list
    b["text"] = random.randint(0,20)
    ans_list.append(b["text"])
    new_list.append(place)

def switch(b):
    b.config(state = 'normal')


def dis(b):
    b["text"] = " "

def start(event):
    global ans_list, new_list, list_click, i, j, btn_list, lvl_list, plc_list, num, lvl
    scoreLabel.config(text = "Score: " + str(score))
    label_expl.config(text = "Level " + str(lvl), font = ('Helvetica', 20))
    button = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button.grid(row = 0, column = 0)
    button2 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button2.grid(row = 0, column = 1)
    button3 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button3.grid(row = 0, column = 2)
    button4 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button4.grid(row = 1, column = 0)
    button5 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button5.grid(row = 1, column = 1)
    button6 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button6.grid(row = 1, column = 2)
    button7 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button7.grid(row = 2, column = 0)
    button8 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button8.grid(row = 2, column = 1)
    button9 = tkinter.Button(mframe, text = ' ', width = 10, height = 2, state = 'disabled')
    button9.grid(row = 2, column = 2)

    btn_list = [button,button2,button3,button4,button5,button6,button7,button8,button9]
    lvl_list = random.sample(btn_list,initial)

    for n in range(0,initial):
        if lvl_list[n] == button:
            num = 0
            plc_list.append(num)
        elif lvl_list[n] == button2:
            num = 1
            plc_list.append(num)
        elif lvl_list[n] == button3:
            num = 2
            plc_list.append(num)
        elif lvl_list[n] == button4:
            num = 3
            plc_list.append(num)
        elif lvl_list[n] == button5:
            num = 4
            plc_list.append(num)
        elif lvl_list[n] == button6:
            num = 5
            plc_list.append(num)
        elif lvl_list[n] == button7:
            num = 6
            plc_list.append(num)
        elif lvl_list[n] == button8:
            num = 7
            plc_list.append(num)
        elif lvl_list[n] == button9:
            num = 8
            plc_list.append(num)

    if initial == 4:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        button.after(5000, lambda: switch(button))
        button2.after(5000, lambda: switch(button2))
        button3.after(5000, lambda: switch(button3))
        button4.after(5000, lambda: switch(button4))
        button5.after(5000, lambda: switch(button5))
        button6.after(5000, lambda: switch(button6))
        button7.after(5000, lambda: switch(button7))
        button8.after(5000, lambda: switch(button8))
        button9.after(5000, lambda: switch(button9))

    elif initial == 5:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        lvl_list[4].after(5000,lambda: app(lvl_list[4],plc_list[4]))
        lvl_list[4].after(6000,lambda: dis(lvl_list[4]))
        button.after(6000, lambda: switch(button))
        button2.after(6000, lambda: switch(button2))
        button3.after(6000, lambda: switch(button3))
        button4.after(6000, lambda: switch(button4))
        button5.after(6000, lambda: switch(button5))
        button6.after(6000, lambda: switch(button6))
        button7.after(6000, lambda: switch(button7))
        button8.after(6000, lambda: switch(button8))
        button9.after(6000, lambda: switch(button9))

    elif initial == 6:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        lvl_list[4].after(5000,lambda: app(lvl_list[4],plc_list[4]))
        lvl_list[4].after(6000,lambda: dis(lvl_list[4]))
        lvl_list[5].after(6000,lambda: app(lvl_list[5],plc_list[5]))
        lvl_list[5].after(7000,lambda: dis(lvl_list[5]))
        button.after(7000, lambda: switch(button))
        button2.after(7000, lambda: switch(button2))
        button3.after(7000, lambda: switch(button3))
        button4.after(7000, lambda: switch(button4))
        button5.after(7000, lambda: switch(button5))
        button6.after(7000, lambda: switch(button6))
        button7.after(7000, lambda: switch(button7))
        button8.after(7000, lambda: switch(button8))
        button9.after(7000, lambda: switch(button9))

    elif initial == 7:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        lvl_list[4].after(5000,lambda: app(lvl_list[4],plc_list[4]))
        lvl_list[4].after(6000,lambda: dis(lvl_list[4]))
        lvl_list[5].after(6000,lambda: app(lvl_list[5],plc_list[5]))
        lvl_list[5].after(7000,lambda: dis(lvl_list[5]))
        lvl_list[6].after(7000,lambda: app(lvl_list[6],plc_list[6]))
        lvl_list[6].after(8000,lambda: dis(lvl_list[6]))
        button.after(8000, lambda: switch(button))
        button2.after(8000, lambda: switch(button2))
        button3.after(8000, lambda: switch(button3))
        button4.after(8000, lambda: switch(button4))
        button5.after(8000, lambda: switch(button5))
        button6.after(8000, lambda: switch(button6))
        button7.after(8000, lambda: switch(button7))
        button8.after(8000, lambda: switch(button8))
        button9.after(8000, lambda: switch(button9))

    elif initial == 8:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        lvl_list[4].after(5000,lambda: app(lvl_list[4],plc_list[4]))
        lvl_list[4].after(6000,lambda: dis(lvl_list[4]))
        lvl_list[5].after(6000,lambda: app(lvl_list[5],plc_list[5]))
        lvl_list[5].after(7000,lambda: dis(lvl_list[5]))
        lvl_list[6].after(7000,lambda: app(lvl_list[6],plc_list[6]))
        lvl_list[6].after(8000,lambda: dis(lvl_list[6]))
        lvl_list[7].after(8000,lambda: app(lvl_list[7],plc_list[7]))
        lvl_list[7].after(9000,lambda: dis(lvl_list[7]))
        button.after(9000, lambda: switch(button))
        button2.after(9000, lambda: switch(button2))
        button3.after(9000, lambda: switch(button3))
        button4.after(9000, lambda: switch(button4))
        button5.after(9000, lambda: switch(button5))
        button6.after(9000, lambda: switch(button6))
        button7.after(9000, lambda: switch(button7))
        button8.after(9000, lambda: switch(button8))
        button9.after(9000, lambda: switch(button9))

    elif initial == 9:
        lvl_list[0].after(1000,lambda: app(lvl_list[0],plc_list[0]))
        lvl_list[0].after(2000,lambda: dis(lvl_list[0]))
        lvl_list[1].after(2000,lambda: app(lvl_list[1],plc_list[1]))
        lvl_list[1].after(3000,lambda: dis(lvl_list[1]))
        lvl_list[2].after(3000,lambda: app(lvl_list[2],plc_list[2]))
        lvl_list[2].after(4000,lambda: dis(lvl_list[2]))
        lvl_list[3].after(4000,lambda: app(lvl_list[3],plc_list[3]))
        lvl_list[3].after(5000,lambda: dis(lvl_list[3]))
        lvl_list[4].after(5000,lambda: app(lvl_list[4],plc_list[4]))
        lvl_list[4].after(6000,lambda: dis(lvl_list[4]))
        lvl_list[5].after(6000,lambda: app(lvl_list[5],plc_list[5]))
        lvl_list[5].after(7000,lambda: dis(lvl_list[5]))
        lvl_list[6].after(7000,lambda: app(lvl_list[6],plc_list[6]))
        lvl_list[6].after(8000,lambda: dis(lvl_list[6]))
        lvl_list[7].after(8000,lambda: app(lvl_list[7],plc_list[7]))
        lvl_list[7].after(9000,lambda: dis(lvl_list[7]))
        lvl_list[8].after(9000,lambda: app(lvl_list[8],plc_list[8]))
        lvl_list[8].after(10000,lambda: dis(lvl_list[8]))
        button.after(10000, lambda: switch(button))
        button2.after(10000, lambda: switch(button2))
        button3.after(10000, lambda: switch(button3))
        button4.after(10000, lambda: switch(button4))
        button5.after(10000, lambda: switch(button5))
        button6.after(10000, lambda: switch(button6))
        button7.after(10000, lambda: switch(button7))
        button8.after(10000, lambda: switch(button8))
        button9.after(10000, lambda: switch(button9))

    button.config(command = lambda: click(button,0))
    button2.config(command = lambda: click(button2,1))
    button3.config(command = lambda: click(button3,2))
    button4.config(command = lambda: click(button4,3))
    button5.config(command = lambda: click(button5,4))
    button6.config(command = lambda: click(button6,5))
    button7.config(command = lambda: click(button7,6))
    button8.config(command = lambda: click(button8,7))
    button9.config(command = lambda: click(button9,8))




root.title("Memory Game")
root.geometry("500x475")
root.bind('<Return>', start)
root.mainloop()
