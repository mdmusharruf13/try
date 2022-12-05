import cv2
import numpy as np
print("package is imported")

# # images in cv
# img = cv2.imread('images/first.jpg')
# down_points = (400, 600)
# resize_down = cv2.resize(img,down_points)
# cv2.imshow("output", resize_down)
# cv2.waitKey(0)

# # # videos in cv
# cap = cv2.VideoCapture("videos/attendance-porject.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# # use of web cam
# camera = cv2.VideoCapture(0)

# while True:
#     success, img1 = camera.read()
#     cv2.imshow("Video",img1)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# # how to gray am image
# img = cv2.imread("images/first.jpg")
# grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# size = (400,600)
# resized = cv2.resize(grayimg,size)
# cv2.imshow("gray image",resized)
# cv2.waitKey(0)

# # blur image
# img = cv2.imread("images/first.jpg")
# kernal = np.ones((5,5),np.uint8)

# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray,(7,7),0)
# imgcanny = cv2.Canny(img,100,100)
# imgdialation = cv2.dilate(imgcanny,kernal,iterations=2)
# imgerode = cv2.erode(imgdialation,kernal,iterations=2)
# size = (400,600)
# sized1 = cv2.resize(imggray,size)
# sized2 = cv2.resize(imgblur,size)
# sized3 = cv2.resize(imgcanny,size)
# sized4 = cv2.resize(imgdialation,size)
# sized5 = cv2.resize(imgerode,size)

# cv2.imshow("grey",sized1)
# cv2.imshow("blur",sized2)
# cv2.imshow("canny",sized3)
# cv2.imshow("dialation",sized4)
# cv2.imshow("erode",sized5)
# cv2.waitKey(0)

# # ch-3 resizing and cropping
# img = cv2.imread("images/first.jpg")
# print(img.shape)
# resized = cv2.resize(img,(400,600))
# imgcrop = resized[0:350,60:310]
# cv2.imshow("cropped",imgcrop)
# print(resized.shape)
# cv2.waitKey(0)

# # shapes and text
# img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:] = 255,0,255  # this color is arrplied to total window
# img[50:300,150:300] = 0,255,255 # particular part is colored
# cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),5)
# cv2.rectangle(img,(50,50),(400,300),(0,255,255),3)
# cv2.circle(img, (200,400),70,(0,255,255),3)
# cv2.putText(img,"Musharruf",(400,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),5)
# cv2.imshow("imgage",img)
# cv2.waitKey(0)

# # WARP PRESPECTIVE
# img = cv2.imread("images/first.jpg")
# size = (300,300)
# width, height = 250,350
# resized = cv2.resize(img,size)
# pt1 = np.float32([[109,489],[1637,505],[89,2509],[1637,2509]])
# pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pt1,pt2)
# imgop = cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow("image",resized)
# cv2.imshow("wrap img",imgop)
# cv2.waitKey(0)

# # JOINING IMAGES
# img = cv2.imread("images/first.jpg")
# size = (300,400)
# imgs = cv2.resize(img,size)
# imghor = np.hstack((imgs,imgs))
# imgver = np.vstack((imgs,imgs))
# cv2.imshow("hstack",imghor)
# cv2.imshow("vstack",imgver)
# cv2.waitKey(0)
 
# # COLOR DETECTION
def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("hue Max","TrackBars",137,179,empty)
cv2.createTrackbar("sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("val Min","TrackBars",145,255,empty)
cv2.createTrackbar("val Max","TrackBars",255,255,empty)

while True:
    # img0 = cv2.imread('images/first.jpg')
    cap = cv2.VideoCapture(0)
    img = cap.read()
    # img = cv2.resize(img0,(200,200))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("val Min","TrackBars")
    v_max = cv2.getTrackbarPos("val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("original",img)
    cv2.imshow("hsv image",imgHSV)
    cv2.imshow("new image",mask)
    cv2.imshow("only color image",imgResult)
    
    cv2.waitKey(1)

# # COUNTER / SHAPE DETECTION

# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area>500:
#             cv2.drawContours(imgContour,cnt,-1,(255,0,0),3) 
#             peri = cv2.arcLength(cnt,True)
#             print(peri)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             # print(approx)
#             print(len(approx))
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#             if objCor == 3: ObjType = "Tri"
#             elif objCor == 4: 
#                 aspRatio = w/float(h)
#                 if aspRatio >0.95 and aspRatio <1.05: ObjType = "Sqr"
#                 else: ObjType = "Rec"
#             elif objCor>4: ObjType="Cir"
#             else: ObjType = "None"

#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),1)
#             cv2.putText(imgContour,ObjType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1 )

# img0 = cv2.imread('images/shapess.png')
# img = cv2.resize(img0,(300,300))
# imgContour = img.copy()
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny = cv2.Canny(imgGray,50,50)
# # imgBlank = np.zeros_like(img)  # similar black window is created
# getContours(imgCanny)
# cv2.imshow("original",img)
# cv2.imshow("gray",imgGray)
# # cv2.imshow("blur",imgBlur)
# cv2.imshow("canny window",imgCanny)
# cv2.imshow("contours",imgContour)
# # cv2.imshow("black window",imgBlank)


cv2.waitKey(0)

