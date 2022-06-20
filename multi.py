import time 
import threading  
from threading import *  
def cal_sqre(num): 
    print(" Calculate the square root of the given number")  
    for n in num: 
        time.sleep(0.3)  
        print(' Square is : ', n * n)  
  
def cal_cube(num): 
    print(" Calculate the cube of  the given number")  
    for n in num: 
        time.sleep(0.3) 
        print(" Cube is : ", n * n *n)  
  
ar = [4, 5, 6, 7, 2] 
  
t = time.time() 
th1 = threading.Thread(target=cal_sqre, args=(ar, ))  
th2 = threading.Thread(target=cal_cube, args=(ar, ))  
th1.start()  
th2.start()  
th1.join()  
th2.join()  
print(" Total time taking by threads is :", time.time() - t) 
print(" Again executing the main thread")  
print(" Thread 1 and Thread 2 have finished their execution.")  