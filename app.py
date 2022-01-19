import pyautogui
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

i=0
rgb_vec = np.array([178,100,40])
bgr_vec = np.array(rgb_vec[::-1])
lista = list()
while i<200:
    s = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    taskbar_s = s[int(1037/1080*s.shape[0]):,:int(s.shape[0]/4),:]
    time.sleep(0.1)
    i+=1
    dif=taskbar_s-bgr_vec
    orange_dif = np.sum(np.linalg.norm(dif,axis=2))
    print(orange_dif)
    lista.append(orange_dif)
    # cv2.imshow('image', taskbar_s)
    # cv2.waitKey(0)


plt.plot(lista)
plt.ylabel("red content")
plt.show()