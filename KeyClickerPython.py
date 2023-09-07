from playsound import playsound
import tkinter as tk
import keyboard
import webbrowser
import asyncio
import random
import time

url = "https://www.google.com/" #This is a fake link. Ignore it or change.

background = '#1878de'

win = tk.Tk()
h = 700
w = 1100
win.config(bg=background)
win.title('TypeSpeedTrainer by Rmgs')
win.geometry(f"{w}x{h}+410+160")
win.resizable(False,False)
icon = tk.PhotoImage(file="icon.png")
win.iconphoto(False,icon)

global mainlabel
mainlabel = tk.Label(win, text="TypeSpeedTrainer",bg=background,font=("Arial",30,"bold"),height=2,anchor="center")
mainlabel.pack()

global fixvar 
fixvar = tk.IntVar()

global timeset 
timeset = tk.DoubleVar()
timeset.set(1.2)

#####################################################################################


al = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

async def wrong(scorelabel,letterlabel,timerlabel):
    background = '#ad1d1d'
    win.config(bg=background)
    scorelabel["bg"] = background
    letterlabel["bg"] = background
    mainlabel["bg"] = background
    timerlabel["bg"] = background
    win.update()
    playsound("audiofail.mp3",block=False) 
    background = '#1878de'
    win.config(bg=background)
    scorelabel["bg"] = background
    letterlabel["bg"] = background
    mainlabel["bg"] = background
    timerlabel["bg"] = background
    win.update()

async def right(scorelabel,letterlabel,timerlabel):
    background = '#2bbd50'
    win.config(bg=background)
    scorelabel["bg"] = background
    letterlabel["bg"] = background
    mainlabel["bg"] = background
    timerlabel["bg"] = background
    win.update()
    playsound("audiopass.mp3",block=False) 
    await asyncio.sleep(0.15)
    background = '#1878de'
    win.config(bg=background)
    scorelabel["bg"] = background
    letterlabel["bg"] = background
    mainlabel["bg"] = background
    timerlabel["bg"] = background
    win.update()

async def game(max_score,fixedposition):
    print("Game...")

    primecountdown = pyvar(timeset)

    background = '#1878de'
    exists = False
    score = 0
    scorelabel = tk.Label(win,text=f"Score: {score}",bg=background,font=("Arial",25,"bold"),anchor="center")
    scorelabel.pack()
    scorelabel.place(x=470,y=100)
    btnclose1 = tk.Button(win,text="Finish",bg="#13a172",command=lambda:[scorelabel.destroy(),timerlabel.destroy(),letterlabel.destroy(),btnclose1.destroy(),to_menu(max_score,fixedposition)],font=("Arial",14,"bold"),width=6,padx=12,anchor="center")
    btnclose1.pack()
    btnclose1.place(x=494, y=640)
    timerlabel = tk.Label(win,text=f"...",bg=background,font=("Arial",22,"bold"),anchor="center")
    timerlabel.pack()
    timerlabel.place(x=120,y=80)

    while btnclose1.winfo_exists() == True:
        countdown = primecountdown

        while countdown > 0:
            timerlabel["text"] = round(countdown,3)
            await asyncio.sleep(0.01)
            countdown = round(countdown - 0.012,3)
            win.update()

            if exists == False:
                letter = random.choice(al)
                letterlabel = tk.Label(win,text=letter,bg=background,font=("Arial",60,"bold"))
                letterlabel.pack()
                if fixedposition == 0:
                    letterlabel.place(x=random.randint(10,1025),y=random.randint(120,530))
                else:
                    letterlabel.place(x=510,y=300)
                exists = True

                blocked = False

            if keyboard.is_pressed(letter):
                countdown = primecountdown
                first = True
                while keyboard.is_pressed(letter):
                    if first == True:
                        if blocked == False:
                            taskpass = asyncio.create_task(right(scorelabel,letterlabel,timerlabel))
                            await taskpass
                            blocked = True
                        letterlabel.destroy()
                        win.update()
                        score += 1
                        exists = False
                        first = False
                    else:
                        pass

            elif (keyboard.is_pressed("A") or keyboard.is_pressed("B") or keyboard.is_pressed("C") or keyboard.is_pressed("D") or keyboard.is_pressed("E") or keyboard.is_pressed("F") or keyboard.is_pressed("G") or keyboard.is_pressed("H") or keyboard.is_pressed("I") or keyboard.is_pressed("J") or keyboard.is_pressed("K") or keyboard.is_pressed("L") or keyboard.is_pressed("M") or keyboard.is_pressed("N") or keyboard.is_pressed("O") or keyboard.is_pressed("P") or keyboard.is_pressed("Q") or keyboard.is_pressed("R") or keyboard.is_pressed("S") or keyboard.is_pressed("T") or keyboard.is_pressed("U") or keyboard.is_pressed("V") or keyboard.is_pressed("W") or keyboard.is_pressed("X") or keyboard.is_pressed("Y") or keyboard.is_pressed("Z")):
                countdown = primecountdown
                first = True    
                while (keyboard.is_pressed("A") or keyboard.is_pressed("B") or keyboard.is_pressed("C") or keyboard.is_pressed("D") or keyboard.is_pressed("E") or keyboard.is_pressed("F") or keyboard.is_pressed("G") or keyboard.is_pressed("H") or keyboard.is_pressed("I") or keyboard.is_pressed("J") or keyboard.is_pressed("K") or keyboard.is_pressed("L") or keyboard.is_pressed("M") or keyboard.is_pressed("N") or keyboard.is_pressed("O") or keyboard.is_pressed("P") or keyboard.is_pressed("Q") or keyboard.is_pressed("R") or keyboard.is_pressed("S") or keyboard.is_pressed("T") or keyboard.is_pressed("U") or keyboard.is_pressed("V") or keyboard.is_pressed("W") or keyboard.is_pressed("X") or keyboard.is_pressed("Y") or keyboard.is_pressed("Z")):
                    if first == True:
                        if blocked == False:
                            taskfail = asyncio.create_task(wrong(scorelabel,letterlabel,timerlabel))
                            await taskfail
                        letterlabel.destroy()
                        win.update()
                        score -= 1
                        exists = False
                        first = False
                    else:
                        pass

            max_score = max(max_score,score)

            win.update()
            scorelabel["text"] = f"Score: {score}"

        print("Time's out!")
        taskfail = asyncio.create_task(wrong(scorelabel,letterlabel,timerlabel))
        await taskfail
        letterlabel.destroy()
        win.update()
        score -= 1
        max_score = max(max_score,score)
        if max_score > 0:
            max_score = max_score - 1
        first = False
        scorelabel.destroy()
        timerlabel.destroy()
        letterlabel.destroy()
        btnclose1.destroy()
        to_menu(max_score,fixedposition)


async def start(max_score,fixedposition):
    taskgame = asyncio.create_task(game(max_score,fixedposition))
    await taskgame
    #asyncio.run(game())
    #asyncio.ensure_future(game())

def to_menu(max_score,fixedposition):
    print("Menu...")

    background = '#1878de'
    highscorelabel = tk.Label(win,text=f"Max score: {max_score}",bg=background,font=("Arial",25,"bold"),anchor="center")
    highscorelabel.pack()
    highscorelabel.place(x=440,y=100)
    btnstart1 = tk.Button(win,text="Start",command=lambda:[btncredits.destroy(),btnexit.destroy(),highscorelabel.destroy(),btnstart1.destroy(),btnsettings.destroy(),asyncio.run(start(max_score,fixedposition))],bg="#13a172",font=("Arial",20,"bold"),width=6,padx=12,anchor="center")
    btnstart1.pack()
    btnstart1.place(x=480, y=200)

    btnsettings = tk.Button(win,text="Settings",command=lambda:[btncredits.destroy(),btnexit.destroy(),highscorelabel.destroy(),btnstart1.destroy(),btnsettings.destroy(),to_settings(max_score)],bg="#13a172",font=("Arial",20,"bold"),width=6,padx=12,anchor="center")
    btnsettings.pack()
    btnsettings.place(x=480, y=290)

    btncredits = tk.Button(win,text="Credits",command=lambda:[btncredits.destroy(),btnexit.destroy(),highscorelabel.destroy(),btnstart1.destroy(),btnsettings.destroy(),to_credits(max_score,fixedposition)],bg="#13a172",font=("Arial",20,"bold"),width=6,padx=12,anchor="center")
    btncredits.pack()
    btncredits.place(x=480, y=380)

    btnexit = tk.Button(win,text="Exit",command=lambda:[print("Quit"),win.quit()],bg="#13a172",font=("Arial",20,"bold"),width=6,padx=12,anchor="center")
    btnexit.pack()
    btnexit.place(x=480, y=470)

    win.config(bg=background)
    highscorelabel["bg"] = background
    mainlabel["bg"] = background
    win.update()

def to_credits(max_score,fixedposition):
    print("Credits...")

    creditslabel = tk.Label(win,text="Credits:",bg=background,font=("Arial",26,"bold"),anchor="center")
    creditslabel.pack()
    creditslabel.place(x=480,y=100)

    rmgslabel = tk.Label(win,text="Rmgs",bg=background,fg='#ffffff',font=("Arial",40,"bold"),anchor="center")
    rmgslabel.pack()
    rmgslabel.place(x=473,y=200)

    webinfolabel = tk.Label(win,text="Website is opened!",bg=background,fg='#ffffff',font=("Arial",20,"bold"),anchor="center")

    btndonate = tk.Button(win,text="Donate!",command=lambda:[webbrowser.open_new(url),webinfolabel.pack(),webinfolabel.place(x=425,y=340)],bg="#1bc4b9",font=("Arial",16,"bold"),width=6,padx=10,anchor="center")
    btndonate.pack()
    btndonate.place(x=495, y=280)

    btnclose3 = tk.Button(win,text="Return to menu",command=lambda:[webinfolabel.destroy(),rmgslabel.destroy(),btndonate.destroy(),btnclose3.destroy(),creditslabel.destroy(),to_menu(max_score,fixedposition)],bg="#13a172",font=("Arial",16,"bold"),width=12,padx=12,anchor="center")
    btnclose3.pack()
    btnclose3.place(x=455, y=635)

def pyvar(var):
    newvar = var.get()
    return newvar

def to_settings(max_score):
    print("Settings...")

    settingslabel = tk.Label(win,text="Settings",bg=background,font=("Arial",26,"bold"),anchor="center")
    settingslabel.pack()
    settingslabel.place(x=475,y=100)

    timesetlabel = tk.Label(win,text="Set countdown",bg=background,font=("Arial",22,"bold"),anchor="center")
    timesetlabel.pack()
    timesetlabel.place(x=430,y=300)

    fixcheckbutton = tk.Checkbutton(text="Enable fixed position",bg=background,variable=fixvar,font=("Arial",20,"bold"))
    fixcheckbutton.pack(padx=6, pady=6)
    fixcheckbutton.place(x=390,y=200)

    scala = tk.Scale(win, from_=0.5, to=5, resolution=0.1, variable=timeset, orient= "horizontal",bg=background)
    scala.pack(padx=5, pady=5)
    scala.place(x=490,y=355)

    btnclose2 = tk.Button(win,text="Return to menu",command=lambda:[timesetlabel.destroy(),scala.destroy(),fixcheckbutton.destroy(),btnclose2.destroy(),settingslabel.destroy(),to_menu(max_score,pyvar(fixvar))],bg="#13a172",font=("Arial",16,"bold"),width=12,padx=12,anchor="center")
    btnclose2.pack()
    btnclose2.place(x=450, y=635)

to_menu(0,False)

win.mainloop()