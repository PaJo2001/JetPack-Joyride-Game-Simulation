import os
import time
import random
from colorama import Fore, Style, Back

class beams:
    def __init__(self):
        self.design=Fore.RED+'#'+Style.RESET_ALL
        self.size=random.randint(4,6)
    def destroybeam(self,x,y):
        if self.matrix[x][y+1]=="#":
            i=0
            while self.matrix[x][y+i]=="#":
                self.matrix[x][y+i]=" "
                i=i+1
            i=1
            while self.matrix[x][y-i]=="#":
                self.matrix[x][y-i]=" "
                i=i+1
            i=0
        elif self.matrix[x-1][y]=="#":
            i=0
            while self.matrix[x-i][y]=="#":
                self.matrix[x-i][y]=" "
                i=i+1
            i=1
            while self.matrix[x+i][y]=="#":
                self.matrix[x+i][y]=" "
                i=i+1
            i=0
        elif self.matrix[x-1][y+1]=="#":
            i=0
            while self.matrix[x-i][y+i]=="#":
                self.matrix[x-i][y+i]=" "
                i=i+1
            i=1
            while self.matrix[x+i][y-i]=="#":
                self.matrix[x+i][y-i]=" "
                i=i+1
            i=0

class coins:
    def __init__(self):
        self.design=Fore.YELLOW+'$'+Style.RESET_ALL
        self.size=random.randint(5,8)

class bullets:
    def __init__(self):
        self.design=Fore.MAGENTA + '>' +Style.RESET_ALL
        self.__speed=3
        self.__x=0
        self.__y=0
    def bullet_creation(self,xc,yc):
        self.__x=xc
        self.__y=yc
    def get_location(self):
        return self.__x,self.__y
    def location_change(self,i):
        self.__y=self.__y+i

class dragon_bullets(bullets):
    def __init__(self):
        self.design=Fore.RED+'#'+Style.RESET_ALL
        self.__speed=3
        self.__x=0
        self.__y=0
    def bullet_creation(self,xc,yc):
        self.__x=xc
        self.__y=yc
    def location_change(self,i):
        self.__y=self.__y-i
    def get_location(self):
        return self.__x,self.__y

class magnet:
    def __init__(self):
        self.design="M"
        self.__x=0
        self.__y=0
    def magnet_creation(self,xm,ym):
        self.__x=xm
        self.__y=ym
    def get_loc(self):
        return self.__x, self.__y
    
    