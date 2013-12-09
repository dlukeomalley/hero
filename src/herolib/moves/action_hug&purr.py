from random import randint as r

level = 3
motors = ['RARM','LARM','PUR']
events = ['BELLY_RUB']

name = "interaction_1"

def run(parent):
	try:
		parent.move_to(PUR=100)
		parent.move_and_wait(LARM=100, RARM=100)
		parent.wait(10)
		parent.move_to(PUR=0)

	finally:
		parent.exit()

