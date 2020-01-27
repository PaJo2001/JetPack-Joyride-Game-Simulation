import os
import time
import random
import signal
from colorama import Fore, Style, Back
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from mando import mando, boss
from objects import beams, coins, bullets, dragon_bullets, magnet
mando_board = mando()
boss_board = boss()


class boards:
	def __init__(self, rows, columns):
		self.__rows = rows
		self.__columns =columns
		self.matrix =[]
		self.__boardloc=0
		self.__coincount=0
		self.bulletloc=[]
		self.dragbulletloc=[]
		self.bullet=[]
		self.beam=[]
		self.magnetloc=[]
		self.__detectspeedup=0
		self.__shieldactivation=0
		self.shield=0
		self.magnet_det=0

	def board_creation(self):
		for i in range (self.__rows):
			self.matrix2d =[]
			for j in range(self.__columns):
				self.matrix2d.append(" ")
			self.matrix.append(self.matrix2d)
		for j in range(self.__columns):
			self.matrix[30][j]="="
		mando_board.mando_create()
		boss_board.mando_create()

	def ifspeedup(self):
		return self.__detectspeedup
	def ifshield(self):
		return self.__shieldactivation

	def get_boardloc(self):
		return self.__boardloc

	def coins_board(self):
		s=0
		e=100
		while(e<=400):
			for i in range(8):
				coinobj=coins()
				cly=random.randint(s,e)
				clx=random.randint(0,26	)
				for j in range (coinobj.size):
					if cly<=0:
						break
					self.matrix[clx][cly]=coinobj.design
					cly=cly+1
			s=s+100
			e=e+100
	def obstacle_board(self):
		s=0
		e=100
		while(e<=400):
			for i in range(8):
				beamobj=beams()
				cly=random.randint(s,e)
				clx=random.randint(0,25)
				type=random.randint(0,2)
				for j in range (beamobj.size):
					if cly<=0 or clx<=0:
						break
					self.matrix[clx][cly]=beamobj.design
					if type==0:
						cly=cly+1
					elif type==1:
						clx=clx-1
					else:
						clx=clx-1
						cly=cly+1
				self.beam.append(beamobj)
			s=s+100
			e=e+100
	def magnet_board(self):
		s=0
		e=175
		while(e<=350):
			magnet_obj=magnet()
			cly=random.randint(s,e)
			clx=random.randint(0,29)
			if cly<=0 or clx<=0:
				break
			magnet_obj.magnet_creation(clx,cly)
			self.matrix[clx][cly]=magnet_obj.design
			self.magnetloc.append(magnet_obj)
			s=s+175
			e=e+175

	def dragonshooter(self):
		mx,my=boss_board.mando_place_teller()
		bulletobj=dragon_bullets()
		k=random.randint(1,3)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(1,3)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(1,5)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(4,7)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(6,10)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(9,11)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(9,13)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(10,13)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		bulletobj=dragon_bullets()
		k=random.randint(13,14)
		bulletobj.bullet_creation(mx-k,my-2)
		self.dragbulletloc.append(bulletobj)
		
	def killdragon(self):
		
		k=0
		for obj in self.dragbulletloc:
			xb,yb=obj.get_location()
			xbc,ybc = mando_board.mando_place_teller()
			if yb>=400:
				self.matrix[xb][yb]=" "
				self.matrix[xb][yb-1]=obj.design
				obj.location_change(1)
			else :
				self.matrix[xb][yb]=" "
				del self.dragbulletloc[k]
				k=k-1
			k=k+1 	
		k=0
		for obj in self.bulletloc:
			xb,yb=obj.get_location()
			xbc,ybc = boss_board.mando_place_teller()
			if yb>=448 and xb<=xbc  and xb>=(xbc-14):
				boss_board.mando_decrease_live()
				self.matrix[xb][yb]=" "
				del self.bulletloc[k]
				k=k-1
			else:
				if yb+1 <500:
					self.matrix[xb][yb]=" "
					self.matrix[xb][yb+1]=obj.design
					obj.location_change(1)
				else:
					self.matrix[xb][yb]=" "
					del self.bulletloc[k]
					k=k-1
			k=k+1


	def printing_board(self):
		print("\033[0;0H")
		mx,my =  mando_board.mando_place_teller()
		if self.__boardloc>my:
			mando_board.change_ypos(self.__boardloc)
		mx,my =  mando_board.mando_place_teller()
		if self.shield==1:
			self.matrix[mx][my]= Fore.RED + mando_board.player[2][0]+Style.RESET_ALL
			self.matrix[mx-1][my]=Fore.RED +mando_board.player[1][0]+Style.RESET_ALL
			self.matrix[mx-2][my]=Fore.RED +mando_board.player[0][0]+Style.RESET_ALL
			self.matrix[mx][my+1]=Fore.RED +mando_board.player[2][1]+Style.RESET_ALL
			self.matrix[mx][my+2]=Fore.RED +mando_board.player[2][2]+Style.RESET_ALL
			self.matrix[mx-1][my+1]=Fore.RED +mando_board.player[1][1]+Style.RESET_ALL
			self.matrix[mx-1][my+2]=Fore.RED +mando_board.player[1][2]+Style.RESET_ALL
			self.matrix[mx-2][my+1]=Fore.RED +mando_board.player[0][1]+Style.RESET_ALL
			self.matrix[mx-2][my+2]=Fore.RED +mando_board.player[0][2]+Style.RESET_ALL
		else:
			self.matrix[mx][my]=mando_board.player[2][0]
			self.matrix[mx-1][my]=mando_board.player[1][0]
			self.matrix[mx-2][my]=mando_board.player[0][0]
			self.matrix[mx][my+1]=mando_board.player[2][1]
			self.matrix[mx][my+2]=mando_board.player[2][2]
			self.matrix[mx-1][my+1]=mando_board.player[1][1]
			self.matrix[mx-1][my+2]=mando_board.player[1][2]
			self.matrix[mx-2][my+1]=mando_board.player[0][1]
			self.matrix[mx-2][my+2]=mando_board.player[0][2]
		for obj in self.magnetloc:
				xc,yc= obj.get_loc()
				self.matrix[xc][yc]="M"		
		if self.__boardloc>=400:
			mbx,mby = boss_board.mando_place_teller()
			for i in range(14):
				for j in range(52):
					self.matrix[mbx+i-14][mby+j]=Fore.YELLOW +  boss_board.player[i][j] + Style.RESET_ALL
		print ("No. Of Coins - {}   Lives Left - {} Boss Lives - {} ".format((int(self.__coincount)) ,mando_board.mando_getlives(), boss_board.mando_getlives()))
		if mando_board.mando_getlives()<=0:
			print("YOU LOST")
			quit()
		if boss_board.mando_getlives()<=0:
			mbx,mby = boss_board.mando_place_teller()
			for i in range(14):
				for j in range(52):
					self.matrix[mbx+i-14][mby+j]=" "
			for i in range(self.__rows):
					for j in range(self.__boardloc,min(self.__boardloc+100,500)):
						self.matrix[i][j]=" "
			while (my<496):
				print("\033[0;0H")
				for i in range(self.__rows):
					for j in range(self.__boardloc,min(self.__boardloc+100,500)):
						print(self.matrix[i][j],end='')
					print()
				for i in range(self.__rows):
					for j in range(self.__boardloc,min(self.__boardloc+100,500)):
						self.matrix[i][j]=" "
				
				self.matrix[29][my]=mando_board.player[2][0]
				self.matrix[29-1][my]=mando_board.player[1][0]
				self.matrix[29-2][my]=mando_board.player[0][0]
				self.matrix[29][my+1]=mando_board.player[2][1]
				self.matrix[29][my+2]=mando_board.player[2][2]
				self.matrix[29-1][my+1]=mando_board.player[1][1]
				self.matrix[29-1][my+2]=mando_board.player[1][2]
				self.matrix[29-2][my+1]=mando_board.player[0][1]
				self.matrix[29-2][my+2]=mando_board.player[0][2]
				mx=29
				my=my+1
				time.sleep(0.05)
			print("YOU WON")
			quit()

		for i in range(self.__rows):
			for j in range(self.__boardloc,min(self.__boardloc+100,500)):
				print(self.matrix[i][j],end='')
			print()


	def activate_shield(self):
		mx,my =  mando_board.mando_place_teller()
		self.shield=1
		
	
	def deactivate_shield(self):
		self.shield=0

	def movemario(self):
		mx,my =  mando_board.mando_place_teller()
		
		def destroybeam(x,y):
			if self.matrix[x][y+1]==Fore.RED+'#'+Style.RESET_ALL or self.matrix[x][y-1]==Fore.RED+'#'+Style.RESET_ALL:
				i=0
				while self.matrix[x][y+i]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x][y+i]=" "
					i=i+1
				i=1
				while self.matrix[x][y-i]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x][y-i]=" "
					i=i+1
				i=0
			elif self.matrix[x-1][y]==Fore.RED+'#'+Style.RESET_ALL or self.matrix[x+1][y]==Fore.RED+'#'+Style.RESET_ALL:
				i=0
				while self.matrix[x-i][y]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x-i][y]=" "
					i=i+1
				i=1
				while self.matrix[x+i][y]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x+i][y]=" "
					i=i+1
				i=0
			elif self.matrix[x-1][y+1]==Fore.RED+'#'+Style.RESET_ALL or self.matrix[x+1][y-1]==Fore.RED+'#'+Style.RESET_ALL:
				i=0
				while self.matrix[x-i][y+i]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x-i][y+i]=" "
					i=i+1
				i=1
				while self.matrix[x+i][y-i]==Fore.RED+'#'+Style.RESET_ALL:
					self.matrix[x+i][y-i]=" "
					i=i+1
				i=0

		def obstacle_checker_w(coin_flag_count):
			mx,my =  mando_board.mando_place_teller()
			flag=0
			coin_added=0
			for i in range (3):
				if self.matrix[mx-3][my+i]==Fore.YELLOW+'$'+Style.RESET_ALL:
					coin_added=coin_added+1
				if self.matrix[mx-3][my+i]==Fore.RED+'#'+Style.RESET_ALL and flag==0:
					if self.shield!=1:
						mando_board.mando_decrease_live()
					destroybeam(mx-3,my+i)
					flag=1
			if coin_flag_count==1:
				self.__coincount=self.__coincount+coin_added/4
			elif coin_flag_count==2:
				self.__coincount=self.__coincount+coin_added/2
			else:
				self.__coincount=self.__coincount+coin_added
		def obstacle_checker_d(coin_flag_count):
			mx,my =  mando_board.mando_place_teller()
			flag=0
			coin_added=0
			for i in range (3):
				if self.matrix[mx-i][my+3]==Fore.YELLOW+'$'+Style.RESET_ALL:
					coin_added=coin_added+1
				if self.matrix[mx-i][my+3]==Fore.RED+Fore.RED+'#'+Style.RESET_ALL and flag==0:
					if self.shield!=1:
						mando_board.mando_decrease_live()
					destroybeam(mx-i,my+3)
					flag=1
			if coin_flag_count==1:
				self.__coincount=self.__coincount+coin_added/4
			elif coin_flag_count==2:
				self.__coincount=self.__coincount+coin_added/2
			else:
				self.__coincount=self.__coincount+coin_added
		def obstacle_checker_a():
			mx,my =  mando_board.mando_place_teller()
			flag=0
			for i in range (3):
				if self.matrix[mx-i][my-1]==Fore.YELLOW+'$'+Style.RESET_ALL:
					self.__coincount= self.__coincount+1
				if self.matrix[mx-i][my-1]==Fore.RED+'#'+Style.RESET_ALL and flag==0:
					if self.shield!=1:
						mando_board.mando_decrease_live()
					destroybeam(mx-i,my-1)
					flag=1
		def obstacle_checker_gravity():
			mx,my =  mando_board.mando_place_teller()
			flag=0
			for i in range (3):
				if self.matrix[mx+1][my+i]==Fore.YELLOW+'$'+Style.RESET_ALL:
					self.__coincount= self.__coincount+1	
				if self.matrix[mx+1][my+i]==Fore.RED+'#'+Style.RESET_ALL and flag==0:
					if self.shield!=1:
						mando_board.mando_decrease_live()
					destroybeam(mx+1,my+i)
					flag=1
		def bullet_check():
			k=0
			for obj in self.bulletloc:
				xb,yb=obj.get_location()
				self.matrix[xb][yb]=" "
				if yb>=self.__boardloc+99:
					del self.bulletloc[k]
					k=k-1
					self.matrix[xb][yb]=" "
				elif self.matrix[xb][yb+1]==Fore.RED+'#'+Style.RESET_ALL:
					destroybeam(xb,yb+1)
					self.matrix[xb][yb]=" "
					del self.bulletloc[k]
					k=k-1
				elif self.matrix[xb][yb+1]==Fore.YELLOW+'$'+Style.RESET_ALL:
					self.matrix[xb][yb]==" "
					i=2
					while self.matrix[xb][yb+i] == Fore.YELLOW+'$'+Style.RESET_ALL:
						i=i+1
					if yb+i < self.__boardloc+100:
						self.matrix[xb][yb-1]==" "
						self.matrix[xb][yb+i]=obj.design
						obj.location_change(i)
					else:
						del self.bulletloc[k]
						k=k-1
						self.matrix[xb][yb]=" "
				else:
					self.matrix[xb][yb]=" "
					self.matrix[xb][yb+1]=obj.design
					obj.location_change(1)
				k=k+1
		def magnet_check():
			for obj in self.magnetloc:
				xc,yc= obj.get_loc()				
				x1,y1 = mando_board.mando_place_teller()
				mx,my = mando_board.mando_place_teller()
				self.matrix[mx][my]=" "
				self.matrix[mx-1][my]=" "
				self.matrix[mx-2][my]=" "
				self.matrix[mx][my+1]=" "
				self.matrix[mx][my+2]=" "
				self.matrix[mx-1][my+1]=" "
				self.matrix[mx-1][my+2]=" "
				self.matrix[mx-2][my+1]=" "
				self.matrix[mx-2][my+2]=" "
				if abs(yc-y1)<=15 and abs(xc-x1)<=15:
					self.magnet_det=1
					if abs(yc-y1)>=abs(xc-x1):
						if (yc-y1)>=0:
							if(x1-2>0):
								obstacle_checker_d(0)
								mando_board.mando_move_forward()
						else:
							if mx<29:
								obstacle_checker_a()
								mando_board.mando_move_back()
					else:
						if (xc-x1)>=0:
							if my+3<min(self.__boardloc+100,500):
								obstacle_checker_gravity()
								mando_board.mando_gravity()
								mando_board.mando_gravity()
																
						else:
							if my>self.__boardloc:
								obstacle_checker_w(0)
								mando_board.mando_move_up()
								mando_board.mando_move_up()
				else:
					self.magnet_det=0

						


			
		def alarmhandler(signum, frame):
			raise AlarmException
		def user_input(timeout=0.03):
			signal.signal(signal.SIGALRM, alarmhandler)
			signal.setitimer(signal.ITIMER_REAL, timeout)
			try:
				text = getChar()()
				signal.alarm(0)
				return text
			except AlarmException:
				pass
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''
		
		self.matrix[mx][my]=" "
		self.matrix[mx-1][my]=" "
		self.matrix[mx-2][my]=" "
		self.matrix[mx][my+1]=" "
		self.matrix[mx][my+2]=" "
		self.matrix[mx-1][my+1]=" "
		self.matrix[mx-1][my+2]=" "
		self.matrix[mx-2][my+1]=" "
		self.matrix[mx-2][my+2]=" "
		if self.__boardloc>=400:
			mbx,mby = boss_board.mando_place_teller()
			for i in range(14):
				for j in range(52):
					self.matrix[mbx+i-14][mby+j]=" "

		char = user_input()
		magnet_check()
		bullet_check()
		if char == 'd':
			if my+3<min(self.__boardloc+100,500):
				obstacle_checker_d(0)
				mando_board.mando_move_forward()
				obstacle_checker_gravity()
				mando_board.mando_gravity()
				boss_board.mando_gravity()
				self.printing_board()
			
		elif char == 'w' and self.magnet_det==0:
			if mx-2>0 and my == self.__boardloc:
				obstacle_checker_w(0)
				obstacle_checker_d(0)
				mando_board.mando_move_up()
				boss_board.mando_move_up()
				self.printing_board()
			elif mx-2>0 :
				obstacle_checker_w(0)
				mando_board.mando_move_up()
				boss_board.mando_move_up()
				self.printing_board()
			elif mx-2==0 and my==self.__boardloc:
				coin_flag_count=1
				obstacle_checker_d(1)
				self.printing_board()
		elif char == 'a':
			if my>self.__boardloc:
				obstacle_checker_a()
				mando_board.mando_move_back()
				obstacle_checker_gravity()
				mando_board.mando_gravity()
				boss_board.mando_gravity()
				self.printing_board()
			elif my==self.__boardloc:
				obstacle_checker_d(0)
		elif char == 'q':
			quit()
		elif char == 'l':
			self.__detectspeedup=1
			bullet_check()
		elif char == 'j':
			self.__shieldactivation=1
		elif char =='k':
			bulletobj=bullets()
			bulletobj.bullet_creation(mx-1,my+3)
			self.bulletloc.append(bulletobj)
		else: 
			self.__detectspeedup=0
			self.__shieldactivation=0
			if my==self.__boardloc and mx<29:
				obstacle_checker_gravity()
				obstacle_checker_d(0)
				mando_board.mando_gravity()
				boss_board.mando_gravity()
				self.printing_board()
			elif mx<29:
				obstacle_checker_gravity()
				mando_board.mando_gravity()
				boss_board.mando_gravity()
				self.printing_board()
			elif mx==29 and my==self.__boardloc :
				coin_flag_count=2
				obstacle_checker_d(2)





	def shiftboard(self):
		if self.__boardloc<400 :
			self.__boardloc=self.__boardloc+1
			mx,my =  mando_board.mando_place_teller()
			if self.__boardloc>my:
				mando_board.change_ypos(self.__boardloc)
