import pandas as pd 
import cv2

df = pd.read_csv("Inception.csv")

namelist = df['n'].tolist()
reglist = df['r'].tolist()
worklist = df['a'].tolist()

for i in range(len(namelist)):
    image = cv2.imread("scam.png")
    cv2.putText(image,'PERMITS ONE',(650,60+45),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(image,str(namelist[i]),(630,100+35),cv2.FONT_HERSHEY_SIMPLEX ,0.5,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(image,str(reglist[i]),(630,120+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
    if str(worklist[i]) == "nan":pass
    elif len(str(worklist[i])) > 22: cv2.putText(image,str(worklist[i]),(600,140+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
    else: cv2.putText(image,str(worklist[i]),(630,140+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
    path = "images/"+str(namelist[i])+".png"
    cv2.imwrite(path, image)