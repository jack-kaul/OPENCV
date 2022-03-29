import cv2
import numpy as np
import datetime

size=1000
width,height=size,size
canvas=np.zeros((width,height,3))
padding=20;
w,h=int(width/2),int(height/2)
center=(w,h)
r=(int(w/2)-15)

minute=0.7*r
hour=0.4*r
sec=0.9*r


cv2.circle(canvas,center,(int(w/2)-3),(100,100,100),-1)
cv2.circle(canvas,center,int(w/2),(225,0,0),5)

for i in range(60):
    if(i%5==0):
        cv2.circle(canvas,(w+int(r*np.cos(i*np.pi/6)),h+int(r*np.sin(i*np.pi/6))),7,(0,0,255),-1)
        
    else:
        cv2.circle(canvas,(w+int(r*np.cos(i*np.pi/30)),h+int(r*np.sin(i*np.pi/30))),3,(0,0,0),-1)

        
while(True):
    canvas2=canvas.copy()
    dt=datetime.datetime.now()
    t=dt.time()
    d=dt.date()
    year,month,date=str(d).split('-')
    year=str(int(year)%100)
    hr=int(str(t).split(':')[0])
    mi=int(str(t).split(':')[1])
    se=int((str(t).split(':')[2]).split('.')[0])
    date_str='|{}|{}|{}|'.format(date,month,year)
    #putting date inside the clock:
    cv2.putText(canvas,date_str,((int(w)-int(2/25*size)),int(h)+int(r/2*np.sin(np.pi/2))),cv2.FONT_HERSHEY_COMPLEX,size/1000,(255,0,0),1,cv2.LINE_AA)
    #code for needles
    cv2.line(canvas2,center,(w+int(hour*np.cos(((hr)*np.pi/6+mi*(np.pi/360))+3*np.pi/2)),h+int(hour*np.sin(((hr)*np.pi/6+mi*(np.pi/360))+3*np.pi/2))),(0,0,255),7,cv2.LINE_AA)
    cv2.line(canvas2,center,(w+int(minute*np.cos(mi*np.pi/30+3*np.pi/2)),h+int(minute*np.sin(mi*np.pi/30+3*np.pi/2))),(0,255,0),5)
    cv2.line(canvas2,center,(w+int(sec*np.cos(se*np.pi/30+3*np.pi/2)),h+int(sec*np.sin(se*np.pi/30+3*np.pi/2))),(255,196,0),3)
    cv2.circle(canvas2,center,10,(0,0,0),-1)
    cv2.imshow('Analog Clock',canvas2)
    # cv2.waitKey(1000)
    #cv2.destroyAllWindows()
    #del canvas2
    if(cv2.waitKey(1)==27):
                break
# cv2.circle(canvas,(w+int(r*np.cos(0*np.pi/6-np.pi/2)),h+int(r*np.sin(0*np.pi/6-np.pi/2))),7,(255,255,255),-1)

cv2.waitKey()
cv2.destroyAllWindows()