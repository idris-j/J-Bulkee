"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "NOV 2019 - till date."
"""
from tkinter import *
import time, subprocess as sp, os as gd, string as sg
from tkinter import messagebox as mb
def mainActivity():
    def abtF ():
        abtP = Tk()
        abtP.title("Bulkee@About-Us")
        abtP.geometry("610x350+340+200")
        titLab = Label (abtP, text = "About Us", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
        aboutUs = "Bulkee Software is yet another bulkee message sender but this particular one interfaces with an android device and uses the whatsapp messenger app to automatically send messages.\nThis project was written and is still managed by Jimoh Idris Olanshile, a computer programmer and a security & privacy advocate.\n\nThe first version of was simple a feature in TeLon but was later re-written to stand on it's own to in order to make room for additional features.\nHowever, using this app is solely your responsibility and telon and bulkee are not to be held liable for any accident that may occur in the process of using this software.\n\nUse Bulkee to make your life easier and not to span or committ any fraudulent act. We are not to be held responsible for how this software is utilized or used. We care about you and thus we've made this software free to use and free of charge.\nCONTACT US:\nEmail: bulkee@telon.com\nMobile Number: +233203450788\n"
        txt = Text(abtP, width = 70, height = 17, wrap = WORD)
        txt.insert(INSERT, aboutUs)
        txt.place(x=22, y=60)
        abtP.mainloop()
        
    def howtF ():
        howtP = Tk()
        howtP.title("Bulkee@How-To")
        howtP.geometry("610x350+340+200")
        titLab = Label (howtP, text = "How to Bulkee", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
        howText = """Hey, I heard you needed my help. This how-to should be simple and straightforward.\n\n1. Find Developer's Options on the device and Enable USB debugging.\nPS: If you can't find Developer's Options simply go to "About Phone" and Tap the text "Build Number" 3 times to enable it.\n\n2. Connect the PC to your phone's Hotspot or just make sure they're both on the same network.\n\n3. Visit www.TeLon.com/Bulkee/Download to register and download TeLon.\n\n4. Fire up and Login with your credentials.\n\n5. Attach your device with a USB cord and detach it once you've connected with your IP Address."""
        txt = Text(howtP, width = 70, height = 15, wrap = WORD)
        txt.insert(INSERT, howText)
        txt.place(x=25, y=60)
        howtP.mainloop()

    def dontF ():
        line = "-" * 70
        dontP = Tk()
        dontP.title("Bulkee@Assist-us")
        dontP.geometry("610x350+340+200")
        titLdon = Label (dontP, text = "Assist The Programmer", font = ("times new roman", 15, "bold")).place (x=0,y=25,relwidth=1)
        donText = "I truly appreciate your interest to make a donation as your donation would go a long way in the developnment and the continual improvement of TeLon no matter how little it may be, Thank you in advance.\n\n\n" + line + "\nBank Name: GtBank\nAccount Name: Jimoh Idris Olanshile\nAccount Number: 0202884092\nPhone Number: +2348159344489"
        txt = Text(dontP, width = 70, height = 10, wrap = WORD)
        txt.insert(INSERT, donText)
        txt.place(x=25, y=80)
        dontP.mainloop()

    def clearTerm(tt):
        time.sleep(tt)
        gd.system("cls")

    def bulkee():
        res = mb.askokcancel ("Warning", """Bulkee starts when you press "Ok".\nUpdate the nam.txt and numb.txt before proceeding.""")
        if res == True:
            ad = "zaglarh shell am force-stop com.gbwhatsapp3"
            ad0 = "zaglarh shell monkey -p com.gbwhatsapp3 1" #strt
            ad1 = "zaglarh shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0"
            ad2 = "zaglarh shell input keyevent KEYCODE_MENU" # option
            ad3 = "zaglarh shell input tap 965 270" # msg
            ad4 = "zaglarh shell input tap 842 813" # kk
            file1 = open ("bulkee_files\\num.txt", "r")
            file2 = open ("bulkee_files\\nam.txt", "r")
            msghd = "Hi%s"
            msgbdy = ",%sThanks%sfor%sbeing%sa%sgreat%scustomer%sall%sthe%swhile,%swe%sare%sdelighted%sto%sinform%syou%sthat%s*CFK%sRESTAURANT*%sis%sstill%shere%sfor%syou%swith%sour%sdelicious%smeals%sand%sthat%sa%snew%s*PROMO*%shas%sbeen%srolled%sout."
            msgbdy2 = "%sKindly%slog%sonto%sthe%s*OPay%s/%sOFood%sMobile%sApp%s/%sCFK%sRESTAURANT*%sto%smake%san%sorder%snow%sand%spay%sjust%s*#300*%sfor%sa%s*#600*%smeal%stwice%sdaily%s:Breakfast%sand%sLaunch."
            msgbdy3 = "%sThank%syou%sfor%schoosing%s*CFK%sRESTAURANT*."
            apol = "We%s*apologize*%sif%syou%shave%sgotten%sthis%smessage%smore%sthan%sonce."
            gd.system(ad)
            gd.system(ad0)
            gd.system(ad1)
            for i, n in zip(file1, file2): #using zip here to make the names wholly iterable
                gd.system(ad2)
                gd.system(ad3)
                gd.system("zaglarh shell input text " + i)
                gd.system(ad4)
                gd.system("zaglarh shell input text " + msghd + n)
                gd.system("zaglarh shell input text " + msgbdy)
                gd.system("zaglarh shell input text " + msgbdy2)
                gd.system("zaglarh shell input text " + msgbdy3)
                gd.system("zaglarh shell input keyevent KEYCODE_ENTER")
                gd.system("zaglarh shell input text " + apol)
                gd.system("zaglarh shell input keyevent KEYCODE_ENTER")
                gd.system("zaglarh shell input keyevent KEYCODE_BACK")
                gd.system("zaglarh shell input keyevent KEYCODE_BACK")
            file1.close()
            file2.close()
            mb.showinfo("Success", "Message has been sent to all numbers in the list.")
                ##Let something signify the process of sending msg (sending msg to number)and completion
        
        
    def connActivity():
        #++++++++++++++++++CREATE THE FUNCTION THAT CONNECTS THE DEVICE WITH THE PC using the IPAddress#++++++++++++++++++
        def connIP():
            ipa = ip.get() #get ip address from entry widget
            por = sp.check_output("zaglarh tcpip " + port)
            output = sp.check_output("zaglarh connect " + ipa + ":" + port)
            confOutput = "b'connected to " + str(ipa) + ":" + port + "\\r\\n'"
            if confOutput == str(output):
                time.sleep(5)
                clearTerm(0)
                mb.showinfo("Device Connected", "You can pull it out now (^~^)\n Press OK to continue.")
                conn.destroy()
                bulkee()
            else:
                mb.showerror("Not Connected", "Try again!!!\n\nPS: Check that the IP ADDRESS is correct.\nAnd also that you're on the same network")

        #++++++++++++++++++CREATE FUNCTION TO SKIP CONNECTION PAGE#++++++++++++++++++
        def skipConn():
            conn.destroy()
            bulkee()


        #++++++++++++++++++Destroy login window and create connection page#++++++++++++++++++
        login.destroy()
        conn = Tk()
        conn.title("Bulkee@Connection Page")
        conn.geometry("800x540+290+90")
        bgPic=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
        connLogo=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/cn.png")
        connBackground = Label(conn, image=bgPic)
        connBackground.place(x=0, y=0, relwidth=1, relheight=1)
        #++++++++++++++++++Set Display Name#++++++++++++++++++
        title = Label(conn, text = "CONNECT", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
        title.place (x=0,y=0,relwidth=1)
        #++++++++++++++++++Create Connection Frame#++++++++++++++++++
        connFrame = Frame (conn, bg="WHITE")
        connFrame.place(x=245, y=260)
        logoL = Label(connFrame, image = connLogo, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        #++++++++++++++++++Handle error that occurs if the device isnt attached with USB#++++++++++++++++++
        try:
            #++++++++++++++++++STRING MANIPULATION TO GET REAL IP ADDRESS FROM dumped IP Info#++++++++++++++++++s
            byteIP = sp.check_output("zaglarh shell ip route")
            stringIP = str(byteIP).rpartition("src")
            rIP = stringIP[2] #get the third item in the tuple
            rrIP = rIP.rpartition("\\r\\n")
            ipAdd = rrIP[0] #get the first item in the new partition
            devName = sp.check_output("zaglarh shell getprop transsion.device.name")
            #++++++++++++++++++Initialize a text class to insert texts in the current window#++++++++++++++++++
            text = Text(conn, width = 70, height = 10, wrap = WORD)
            text1 = sp.check_output("zaglarh devices")
            text2 = "PS: If you device isnt connected, kindly get your IP Address(" + ipAdd + ") below and place it in the to box connect. Or skip if your device is present.\n\n<-------------------------------------------------------------------->\n"
            text3 = sp.check_output("zaglarh shell ip route")
            text.insert(INSERT, text1)
            text.insert(INSERT, text2)
            text.insert(INSERT, text3)
            text.place(x=115, y=100)
            ip = StringVar() # Create StringVar variable to store the ip address.
            pType = StringVar() #Create variable to store the phone type
            ipEntry = Entry (connFrame, bg = "WHITE", width = 30, textvariable = ip).grid (rows = 2, columnspan = 2, pady = 20)
            spPhone = Spinbox (connFrame, state = "readonly", textvariable = pType, bg = "WHITE", wrap = True, width = 30, values = (devName, "HUAWEI Y7 Prime 2019", "Infinix Note 5 Stylus", "Samsung Galaxy S7 Edge", "Samsung Galaxy S8 Edge", "Nokia ")).grid(row = 3, columnspan = 2, padx = 10, pady = 1)
            btn = Button(connFrame, relief = GROOVE, command = connIP, text = "Connect & Start", bg = "#2896e0", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
            btn2 = Button(connFrame, relief = GROOVE, text = "Skip and Start", command = skipConn, bg = "RED", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 1)
            
        except sp.CalledProcessError:
            clearTerm(0)
            mb.showerror("Device Not Attached", "Hey, put it inside me (^~^)")
        conn.update_idletasks()
        conn.mainloop()

    def loginP():
        email_address = Email.get()
        phone_number = Numb.get()
        count = email_address.count("@")
        #Trust the process man, you deserve the best.
        if email_address == "" or phone_number == "":
            connActivity()
            #mb.showerror("Error", "All fields are required!!!")
            #++++++++++++++++++FOR CMD#++++++++++++++++++ print ("Error, all fields are required.")
        elif count > 0: #check if email address is present.
            #++++++++++++++++++Lets call this guy#++++++++++++++++++
            connActivity()
        else:
            mb.showwarning("Invalid Info", "Put in a valid email address!!!")
    login = Tk()
    ########create app menu
    menubar = Menu(login)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=login.quit)

    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Donate", command=dontF)
    helpmenu.add_command(label="About Us", command=abtF)
    helpmenu.add_command(label="How to use", command=howtF)

    login.config(menu=menubar)
    login.title("Bulkee: Powered by TeLon")
    abspath = gd.path.join ("C://", "virtualenvironment", "TeLon", "Scripts")
    gd.system("cd " + abspath)
    disC = sp.check_output("zaglarh disconnect")
    clearTerm(0)
    login.geometry("800x540+290+90")
    #++++++++++++++++++Save all Images to a variable#++++++++++++++++++
    bgPict=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
    logoIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/L.png")
    userIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/u.png")
    passIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/p.png")
    #++++++++++++++++++CREATE NECCESARY VARIABLES#++++++++++++++++++
    Email = StringVar()
    Numb = StringVar()
    port = "4204"
    #++++++++++++++++++Set Background Image#++++++++++++++++++
    background = Label(login, image=bgPict)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    #++++++++++++++++++Set Display Name#++++++++++++++++++
    title = Label(login, text = "LOGIN", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
    title.place (x=0,y=0,relwidth=1)
    #++++++++++++++++++Create Login Frame#++++++++++++++++++
    Login_Frame = Frame (login, bg="white")
    Login_Frame.place(x=165, y=95)
    #++++++++++++++++++Setup User Login Page#++++++++++++++++++
    logoLbl = Label(Login_Frame, image = logoIcon, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
    userLbl = Label(Login_Frame, text = "Email Address", image=userIcon, compound = LEFT, font=("times new roman", 20, "bold"), bg = "white").grid(rows=1, column=0, padx=20, pady=0)
    userTxt = Entry(Login_Frame, width = 13, bd =5, relief=GROOVE, textvariable = Email, font = ("", 15)).grid(row = 1, column = 1, padx = 20, pady = 0 )
    passLbl = Label(Login_Frame, text = "Phone Number", image=passIcon, compound = LEFT, font=("times new roman", 20, "bold"), bg = "white").grid(rows=1, column=0, padx=20, pady=0)
    passTxt = Entry(Login_Frame, width = 13, bd =5, relief=GROOVE, textvariable = Numb, font = ("", 15)).grid(row = 2, column = 1, padx = 20, pady = 0)
    loginButton = Button(Login_Frame, relief = GROOVE, command = loginP, text = "Login", bg = "#2896e0", width = 10, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 3, column = 1, pady = 10)
    login.mainloop()

mainActivity()
