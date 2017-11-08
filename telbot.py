import telebot
from telebot import types
import time
import os

Token = "486136148:AAHWXUCSInnLhBLkow5XFXAdFIILBi7YKO4"

userStep = {}
knownUsers = []


#funcion que comprueba si el usuario
#a entrado antes o es nuevo

def get_user_step(uid):
	if uid in userStep: #si ha entradi antes, nos devuelve si id
		return userStep[uid]
	else:	#si es un nuevo usuario
		knownUsers.append(uid) #añade el id a la lista
		userStep[uid] = 0 # le asigna el numero de menu 0
		#imprime un mensaje por consola
		print(color.RED + " [i] NUEVO USUARIO" + color.ENDC)
#LISTENER
def listener(messages):
	for m in messages:
		if m.content_type == 'text'

class color:
	RED = '\033[91m'
	BLUE = '\033[94m'
	GREEN = '\033[32m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	
