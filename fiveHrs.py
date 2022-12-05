import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# if(cap.isOpened() == True):
#     print("camera could not found")

# frameWidth = int(cap.get(3))
# frameHeight = int(cap.get(4))

# # video coded - encoder and decoders

# video_cod = cv2.VideoWriter_fourcc(*'XVID')
# videoOutput = cv2.VideoWriter('capture.MP4',video_cod,30,(frameWidth, frameHeight))

# while True:
#     res, frame = cap.read()
#     if res == True:
#         videoOutput.write(frame)
#         cv2.imshow("frame",frame)
#         if cv2.waitKey(1) & 0xFF == ord('m'):
#             break
#     else:
#         break
# cap.release()
# videoOutput.release()
# cv2.destroyAllWindows()

# # RegionOfInterest - cropping image
# img0 = cv2.imread("images/first.jpg")
# img = cv2.resize(img0,(500,800))
# roi = cv2.selectROI(img)
# print(roi)

# # cropping selected ROI image
# roiCropped = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
# cv2.imshow("ROI image",roiCropped)
# cv2.imwrite("croppedImg.jpeg",roiCropped)
# cv2.waitKey(0)

# # joining the splitted image
# img0 = cv2.imread("images/first.jpg")
# img = cv2.resize(img0,(300,500))
# g,b,r = cv2.split(img)
# cv2.imshow("green",g)
# cv2.imshow("blue",b)
# cv2.imshow("red",r)
# mrg = cv2.merge((g,g,r,r))
# cv2.imshow("all",mrg)
# cv2.waitKey(0)

# # blending images
# src1=cv2.imread("images/first.jpg")
# src2=cv2.imread("images/shapess.png")
# img1 = cv2.resize(src1,(300,400))
# img2 = cv2.resize(src2,(300,400))
# imgBlend1 = cv2.addWeighted(img1,0,img2,1,1)
# imgBlend2 = cv2.addWeighted(img1,1,img2,0.5,1)
# cv2.imshow("blended image1",imgBlend1)
# cv2.imshow("blended image2",imgBlend2)
# cv2.waitKey(0)

# # Sharpening image
# img0 = cv2.imread("images/first.jpg")
# img = cv2.resize(img0,(300,500))
# Sharp = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
# imgSharp = cv2.filter2D(img,-1,Sharp)
# cv2.imshow("filtered image",imgSharp)
# cv2.waitKey(0)

# # finding different color of different shapes
# img0 = cv2.imread('images/shapess.png')
# img = cv2.resize(img0,(400,400))
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# lower_green = np.array([10,50,50])
# upper_green = np.array([90,255,200])
# lower_yellow = np.array([10,40,90])
# upper_yellow = np.array([50,255,255])
# lower = np.array([0,50,50])
# upper = np.array([130,255,255])

# mask_img = cv2.inRange(hsv,lower,upper)
# res = cv2.bitwise_and(img,img,mask=mask_img)
# cv2.imshow('res',res)
# cv2.waitKey(0)
