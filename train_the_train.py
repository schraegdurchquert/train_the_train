import cv2
import numpy as np
from time import sleep

class SenseHat:

    board = np.zeros((8,8,3))

    def show_board():
        r = 20
        d = 50
        length = d*9
        img = np.zeros((length,length,3))
        for x in range(0,8):
            for y in range(0,8):
                img = cv2.circle(img,(d*x,d*y),r,board[x][y],-1)
        cv2.imshow("SenseHat",img)

    def set_pixel(self,x,y,r,g=None,b=None):
        if b == None:
            b = r[2]
            g = r[1]
            r = r[0]
        board[x][y] = (r,g,b)
        show_board()


    #col1 = (50,100,150)
    col1 = (0,200,0)
    #col2 = (0,200,150)
    col2 = (0,0,200)
    #col3 = (150,100,10)
    col3 = (200,0,0)

    set_pixel(2,3,255,255,0)

    #show_board()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
