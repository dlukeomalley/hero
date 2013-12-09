level = 5
motors = ['RARM','BLINK']
events = ['HEAD_PAT']

name = "head pat 1"

def run(parent):
	try:
		parent.move_and_wait(RARM=r(0,10),BLINK=0)
		parent.move_and_wait(RARM=r(40,50),BLINK=100)
		parent.move_and_wait(RARM=r(0,10),BLINK=0)
		parent.move_and_wait(RARM=r(40,50),BLINK=100)



	finally:
		parent.exit()