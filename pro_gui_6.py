from tkinter import *
import random as r

window = Tk()
window.title("Cows and Bulls")
window.geometry("1030x525")

bg = PhotoImage(file = "candb11.png")
bgpic1 = Label( window , image = bg) 
bgpic1.place(x = 0, y = 0) 



#function of START on first window
def game():
    sub1 = Tk()
    sub1.title("Cows and Bulls")
    sub1.configure(bg="#cfffee")

    lst_num = list(range(0, 10))
    not_zero = r.sample(lst_num[1:], 1)
    lst_num.remove(not_zero[0])
    n = not_zero + r.sample(lst_num, 3)
    n = list(map(str, n))
    

    lb_4=Label(sub1,text="RULES: ",bg="#cfffee",font=("Footlight MT Light",15))
    lb_4.grid(row=0,padx=350)
    lb_1=Label(sub1,text="1.REPETITIVE DIGITS ARE NOT ALLOWED. ",bg="#cfffee",font=("Footlight MT Light",15))
    lb_1.grid(row=1,padx=350)
    lb_2=Label(sub1,text="2.YOU CAN QUIT THE GAME ANYTIME BY CLICKING ON THE END BUTTON",bg="#cfffee",font=("Footlight MT Light",15))
    lb_2.grid(row=2)
    lb_3=Label(sub1,text="ENTER A FOUR DIGIT NUMBER",bg="#cfffee",font=("Footlight MT Light",15))
    lb_3.grid(row=3)

    digit = Entry(sub1 , width = 35)
    digit.grid(row = 4 , column = 0 , columnspan = 3 , padx = 10, pady = 10)

    c=0
    
    #function of SUBMIT on second window
    def game_func():
        number = digit.get()
        digit.delete(0,END)

        #main background function 
        def callme():
            cow = 0
            bull = 0
            for i in range(0,4):
                if (number[i] == n[i]):
                    cow += 1
                elif (number[i] in n):
                    bull += 1

            nonlocal c
            c += 1

            #function of CONGRATS on second window 
            def display_key2():
                name= e1.get()
                lb1=Label(window,text="CONGRATULATIONS"+name,bg="white",font=("Footlight MT Light",15))
                lb1.grid(pady=5)
                lb2=Label(window,text="You used "+str(c)+" turns",bg="white",font=("Footlight MT Light",15))
                lb2.grid()

            if (cow == 4):
                btn_1 = Button(sub1, text="CONGRATS", command=lambda:[sub1.destroy(),display_key2()])
                btn_1.grid()
                
            else:
                lbcow=Label(sub1,text=str(number)+"  "+"Cows= "+str(cow)+"   "+"Bulls= "+str(bull),bg="#cfffee")
                lbcow.grid()
            
        if (number.isdigit() and len(number) != 4) :
            lb1=Label(sub1,text='Enter a 4 digit number',bg="#cfffee")
            lb1.grid()

        elif (number.isdigit() and (len(set(number)) < len(number))):
            lb2=Label(sub1,text="Your number has repeating digits. Please enter your number again",bg="#cfffee")
            lb2.grid()
            
        elif all(list(map(lambda z: z.isdigit(), number))):
            callme()

        else:
            lb3=Label(sub1,text='Please enter only digits',bg="#cfffee")
            lb3.grid()
            
    btn_1 = Button(sub1, text="SUBMIT",command = game_func,bg="#c3fa64")
    btn_1.grid(row=5)

    #function of END on second window 
    def display_key():
        name= e1.get()
        lb1=Label(window,text="Better luck next time "+name,bg="white",font=("Footlight MT Light",15))
        lb1.grid(pady=5)
        lb2=Label(window,text="The correct number was "+''.join(n),bg="white",font=("Footlight MT Light",15))
        lb2.grid()

        
    btn_2 = Button(sub1, text="END", command=lambda:[sub1.destroy(),display_key()],bg="#ff4040")
    btn_2.grid()
    
lb1=Label(window,text="COWS AND BULLS",bg="white",font=("Broadway",30))
lb1.grid(row=0,padx=350)

lb1=Label(window,text="WELCOME TO THE GAME! HOPE YOU HAVE FUN!",bg="white",font=("Footlight MT Light",15))
lb1.grid(row=1,column=0)

lb3= Label(window,text="Enter your name",bg="white",font=("Footlight MT Light",15))
lb3.grid(row=2,column=0)
e1= Entry(window,width=25,borderwidth=2,font=("Footlight MT Light",15))
e1.grid(row=3,column=0)

#function of SUBMIT on first window    
def onClick():
    n= e1.get()
    e1.delete(0,END)
    lb1=Label(window,text="Welcome "+n+" click on START to begin playing",bg="white",font=("Footlight MT Light",15))
    lb1.grid(row=5)
    
    btn_start = Button(master=window, text="START", font=("Footlight MT Light",12),command=game,bg="#71f55f")
    btn_start.grid(row=8,column=0,pady=5)

bt1=Button(window,text="SUBMIT",font=("Footlight MT Light",12),command= onClick,bg="#71f55f" )
bt1.grid(row=4,pady=5)


window.mainloop()

