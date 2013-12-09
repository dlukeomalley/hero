from random import randint as r

level = 5
motors = ['NECK']
events = ['BOTH_ARM_GRAB']

name = "interaction_2"

def run(parent):
	try:
		move_to(PUR=100))
		move_and_wait(NECK=r(0,10))
		move_and_wait(NECK=r(50,60))
		move_and_wait(NECK=r(0,10))
		move_and_wait(NECK=r(50,60))
		move_to(NECK=50)
	finally:
		parent.exit()