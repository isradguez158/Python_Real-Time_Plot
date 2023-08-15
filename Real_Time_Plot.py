import datetime
import random
import matplotlib.pyplot as plt
import time
import math
import keyboard

# make up some data
#x = [time.time() + datetime.timedelta(hours=i) for i in range(12)]
begin=time.time()
prevtime=0
prevtime2=0
now=0
x2=[]
y2=[]
y3=[]
y4=[]

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
plt.ion()


while(True):

    now=time.time()-begin
    if now-prevtime2>0.005:
        prevtime2=now

        x = now
        y = math.sin(now*2)

        x2.append(x)
        y2.append(y)
        y3.append(-1*y)
        y4.append(2*y)
        print(x)
        #plt.show(block=False)

    if keyboard.is_pressed("a"):
        # plot
        #plt.plot(x2,y2)
        # beautify the x-labelsa
        axs[0].plot(x2,y2, color='blue')
        axs[0].plot(x2,y3, color='red')
        axs[1].plot(x2,y3, color='green', marker='o', linestyle='dashed')
        axs[1].plot(x2,y4, color='red', marker='o', linestyle='dashed')
        #plt.gcf().autofmt_xdate()
        plt.draw()
        plt.pause(0.0001)
        #prevtime=now

    if keyboard.is_pressed("b"):
         plt.close()