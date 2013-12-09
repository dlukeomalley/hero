from random import randint as r

level = 5
motors = ['BLINK']
events = ['HEAD_PAT', 'BLINK']

name = "interaction_5"

def run(parent):
	try:
		play(‘happy_otter2.mp3’)
  		move_and_wait(BLINK=100) #open
		move_and_wait(BLINK=0) # close
		move_and_wait(BLINK=100)
	    move_to(BLINK=0)

	finally:
		parent.exit()