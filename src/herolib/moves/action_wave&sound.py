from random import randint as r

level = 4
motors = ['LARM']
events = ['LARM_GRAB']

name = "interaction_3"

def run(parent):
	try:
		play(‘happy_otter.mp3’)
		move_and_wait(LARM=r(0, 10)); 
		move_and_wait(LARM=r(50, 60))
		move_to(LARM=r(0,10))

	finally:
		parent.exit()