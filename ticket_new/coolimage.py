import cv2

image = cv2.imread("scam.png")
h,w = image.shape[0:2]
print(h,w)


#putting text on our image
cv2.putText(image,'PERMITS ONE',(650,60+45),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
cv2.putText(image,'Scam Bannerjee',(630,100+35),cv2.FONT_HERSHEY_SIMPLEX ,0.5,(0,0,0),1,cv2.LINE_AA)
cv2.putText(image,'RA1611003010758',(630,120+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
cv2.putText(image,'Starts At 9:00 AM',(630,140+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)

#show
cv2.imshow('image',image)

#writing image to memory
cv2.imwrite("images/scam1.png", image)

cv2.waitKey(0)