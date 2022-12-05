import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import tkinter as tk
from tkinter import *

def startCamera():
    # pass
    path = 'images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cls in myList:
        crntImg = cv2.imread(f'{path}/{cls}')
        images.append(crntImg)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    encodeListKnown = findEncodings(images)
    print("Enocding Complete...")

    def markAttendance(name):
        with open('Attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')



    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
        faceCrntFrme = face_recognition.face_locations(imgS)
        encodeCrntFrme = face_recognition.face_encodings(imgS,faceCrntFrme)
        for encodeFace,faceLoc in zip(encodeCrntFrme,faceCrntFrme):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,225,0),3)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                markAttendance(name)
        cv2.imshow('webcam',img) 
        cv2.waitKey(0)


window = Tk()  
window.geometry("720x720")  
window.title("Home Page")
mainFrame = Frame(window,bg='orange')
# btn = tk.Button(mainFrame, text = 'Exit', command = window.destroy)
page1 = tk.Frame(mainFrame)
p1_lb = tk.Label(page1,text="FACE RECOGNITION ATTENDENCE \n SYSTEM", font=("Bold",30)).pack()
page1.pack(pady=100)

page2 = tk.Frame(mainFrame)
p2_lb = tk.Label(page2,text="starting face recogniton", font=("Bold",30)).pack(side=tk.TOP)
p2_btn = tk.Button(page2,text="start camera",font=('Bold',20),bg='green',fg="yellow",command=startCamera).pack(side=tk.BOTTOM)

page3 = tk.Frame(mainFrame)
p3_lb = tk.Label(page3,text="attendanec", font=("Bold",30)).pack()

mainFrame.pack(fill=tk.BOTH,expand=True)

pages = [page1,page2,page3]
count=0
def moveNextPage():
    global count
    if not count>len(pages)-2:
        for p in pages:
            p.pack_forget()
        count +=1
        page = pages[count]
        page.pack(pady=100)

def moveBackPage():
    global count
    if not count == 0:
        for p in pages:
            p.pack_forget()
        count -=1
        page = pages[count]
        page.pack(pady=100)

bottomframe = Frame(window) 

back_btn = tk.Button(bottomframe,text="Back",font=('Bold',18),bg='red',fg="white",width=8,command=moveBackPage)
back_btn.pack(side=tk.LEFT,padx=10)

next_btn = tk.Button(bottomframe,text="Next",font=('Bold',18),bg='red',fg="white",width=8, command=moveNextPage)
next_btn.pack(side=tk.RIGHT,padx=50)

bottomframe.pack(side=tk.BOTTOM,pady=10)

window.mainloop()


