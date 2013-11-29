# Motors script needs to "own" to run
# Decides which scripts can prempt others
# Name w/ no spaces
motors = set(["LARM",
		   	  "RARM",
		   	  "NECK"])	
level = 5
name = "move5"

def run(parent):
	try:
		for x in range(5):
			parent.move_to()
	finally:
	 	parent.exit()

# move("LARM"=5, "RARM"=10)
# wait_until("LARM"=5, "RARM"=10)
# move_and_wait("LARM"=5, "RARM"=10)
