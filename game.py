import os
import time
from board import boards

flag=0
dragflag=0

ob_board = boards(31, 500)
ob_board.board_creation()
ob_board.coins_board()  
ob_board.obstacle_board()
ob_board.magnet_board()
time_shield=0
speed=0.15
time_speed=0
time_shoot_dragon=1.5
shield_ready=0
shield_flag=0
time_shield_ready=0

while(True):
    ob_board.printing_board()
    if flag == 0:
        start = time.time()
        flag=1
    if dragflag == 0:
        startdrag = time.time()
        dragflag=1
    ob_board.movemario()
    speeddetection=ob_board.ifspeedup()
    shieldetection=ob_board.ifshield()
    if shieldetection==1 and shield_ready==0:
        ob_board.activate_shield()
        time_shield=time.time()
        shield_flag=1
    if time.time()-time_shield>=10 and shield_flag==1:
        ob_board.deactivate_shield()
        shieldetection=0
        shield_ready=1
        time_shield_ready=time.time()   
        shield_flag=0
    if time.time() - time_shield_ready >=10 and shield_ready==1 and shield_flag==0:
        shield_ready=0

    if speeddetection==1:
        speed=0.04
        time_speed=time.time()
    if time.time()-time_speed>=5:
        speed = 0.2
        speeddetection=0
    if time.time()-start>speed :
        ob_board.shiftboard()
        flag=0
    z = ob_board.get_boardloc()
    if(z>=400):
        ob_board.killdragon()
    if (z>=400) and time.time()-startdrag>=time_shoot_dragon:    
        ob_board.dragonshooter()
        dragflag=0







