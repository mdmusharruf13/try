from tkinter import *
import tkinter as tk
window=Tk()
window.minsize(height=500,width=900)
# label1 = Label(window,text="WELCOME TO AUTOMATIC \n FACE RECOGNITION ATTENDANCE\n SYSTEM",font=("Times_New_Roman",25))
# label1.pack()
mainFrame = tk.Frame(window,bg='orange')
global homePage
def homePage():
    global camPage
    def camPage():
        p1_lb.destroy()
        p2_lb = tk.Label(mainFrame,text="Starting Face Recogniton", font=("Bold",30)).pack()
        p2_btn = tk.Button(mainFrame,text="Start Camera",font=('Bold',20),bg='green',fg="yellow").pack()
        
        global attendancePage
        def attendancePage():
            p3_lb = tk.Label(page3,text="attendanec", font=("Bold",30)).pack()
            bottomframe = Frame(window) 

            home = tk.Button(bottomframe,text="Home",font=('Bold',18),bg='red',fg="white",width=10,command=homePage)
            home.pack(side=tk.LEFT,padx=10)

            camera = tk.Button(bottomframe,text="Take Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=camPage)
            camera.pack(side=tk.LEFT,padx=10)

            attendance = tk.Button(bottomframe,text="Check Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=attendancePage)
            attendance.pack(side=tk.LEFT,padx=10)

            exit = tk.Button(bottomframe,text="Exit",font=('Bold',18),bg='red',fg="white",width=10,command=window.destroy)
            exit.pack(side=tk.RIGHT,padx=10)

            bottomframe.pack(side=tk.BOTTOM,pady=10)
        bottomframe = Frame(mainFrame) 

        home = tk.Button(bottomframe,text="Home",font=('Bold',18),bg='red',fg="white",width=10,command=homePage)
        home.pack(side=tk.LEFT,padx=10)

        camera = tk.Button(bottomframe,text="Take Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=camPage)
        camera.pack(side=tk.LEFT,padx=10)

        attendance = tk.Button(bottomframe,text="Check Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=attendancePage)
        attendance.pack(side=tk.LEFT,padx=10)

        exit = tk.Button(bottomframe,text="Exit",font=('Bold',18),bg='red',fg="white",width=10,command=window.destroy)
        exit.pack(side=tk.RIGHT,padx=10)

        bottomframe.pack(side=tk.BOTTOM,pady=10)


    p1_lb = tk.Label(mainFrame,text="WELCOME TO AUTOMATIC \n FACE RECOGNITION ATTENDANCE\n SYSTEM", font=("Bold",30)).pack()
    
    bottomframe = Frame(mainFrame) 

    home = tk.Button(bottomframe,text="Home",font=('Bold',18),bg='red',fg="white",width=10,command=homePage)
    home.pack(side=tk.LEFT,padx=10)

    camera = tk.Button(bottomframe,text="Take Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=camPage)
    camera.pack(side=tk.LEFT,padx=10)

    attendance = tk.Button(bottomframe,text="Check Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=attendancePage)
    attendance.pack(side=tk.LEFT,padx=10)

    exit = tk.Button(bottomframe,text="Exit",font=('Bold',18),bg='red',fg="white",width=10,command=window.destroy)
    exit.pack(side=tk.RIGHT,padx=10)

    bottomframe.pack(side=tk.BOTTOM,pady=10)
    


# def attendancePage():
    
#     page3 = tk.Frame(window)
#     p3_lb = tk.Label(page3,text="attendanec", font=("Bold",30)).pack()
#     page3.pack(pady=50)

mainFrame.pack(fill=tk.BOTH,expand=True)

homePage

bottomframe = Frame(window) 

home = tk.Button(bottomframe,text="Home",font=('Bold',18),bg='red',fg="white",width=10,command=homePage)
home.pack(side=tk.LEFT,padx=10)

camera = tk.Button(bottomframe,text="Take Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=camPage)
camera.pack(side=tk.LEFT,padx=10)

attendance = tk.Button(bottomframe,text="Check Attendance",font=('Bold',18),bg='red',fg="white",width=15,command=attendancePage)
attendance.pack(side=tk.LEFT,padx=10)

exit = tk.Button(bottomframe,text="Exit",font=('Bold',18),bg='red',fg="white",width=10,command=window.destroy)
exit.pack(side=tk.RIGHT,padx=10)

bottomframe.pack(side=tk.BOTTOM,pady=10)

window.mainloop()