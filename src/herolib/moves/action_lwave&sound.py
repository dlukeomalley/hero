from random import randint as r

level = 4
motors = ['RARM']
events = ['RARM_GRAB']

name = "interaction_4"

def run(parent):
	try:
		play(‘happy_otter.mp3’)
  		move_and_wait(RARM=r(0, 10))	
  		move_and wait(RARM=r(90, 100))
  		move_to(RARM=r(0, 10))
	finally:
		parent.exit()