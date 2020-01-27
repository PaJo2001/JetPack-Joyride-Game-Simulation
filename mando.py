import os
import time

class mando:
    def __init__(self):
        self.__xpos = 29
        self.__ypos = 0
        self._lives=10
        self.player = []
    def mando_create(self):
        self.player = [("@"," ","@"),(" ","|"," "),("/"," ","\\")]
    def mando_place_teller(self):
        return self.__xpos, self.__ypos
    def mando_move_up(self):
        if self.__xpos>0:
            self.__xpos = self.__xpos - 1
    def mando_move_forward(self):
        if self.__ypos>=0:
            self.__ypos = self.__ypos +1
    def mando_move_back(self):
        if self.__ypos>0:
            self.__ypos = self.__ypos - 1
    def mando_gravity(self):
        if self.__xpos<29:
            self.__xpos = self.__xpos + 1
    def change_xpos(self, newxpos):
        self.__xpos=newxpos
    def change_ypos(self, newypos):
        self.__ypos=newypos
    def mando_getlives(self):
        return self._lives
    def mando_decrease_live(self):
        self._lives=self._lives-1

class boss(mando) :
    def __init__(self):
        mando.__init__(self)
        self.__xpos = 29
        self.__ypos = 447    
        self.player =[]
        self.boss = []
    def mando_create(self):
        with open("./boss.txt") as obj:
            for line in obj:
                self.player.append(line.strip('\n'))
    def mando_place_teller(self):
        return self.__xpos, self.__ypos
    def mando_move_up(self):
        if self.__xpos-14>0:
            self.__xpos = self.__xpos - 1
    def mando_gravity(self):
        if self.__xpos<29:
            self.__xpos = self.__xpos + 1



