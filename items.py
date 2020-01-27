import os
import time
import random
         

class objects:
    def __init__(self):
        self.coinno=0

    def coins_placer(self):
        s=0
        e=110
        while(e<9200):
            for i in range(8):
                cly=random.randint(s,e)
                clx=random.randint(0,29)
                for j in range (6):
                    if cly<=0:
                        break
                    board_obj.matrix[clx][cly]="$"
                    cly=cly+1
            s=s+110
            e=e+110





