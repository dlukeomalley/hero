# Otter moves neck back and forth and then lets out soothing utter sound

# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"NECK" ]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [ 	"BELLY_RUB"]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 11

# Human readable name for debugging purposes.
name = "Interaction_2"

def run(parent):
	try:
		# YOUR CODE GOES HERE
		parent.move_to(BLINK=(50,75), PUR=80) 
		
		for x in range(random.randint(1, 4)):
			parent.move_and_wait(NECK=(0,10))
			parent.wait((.75, 1.5))
			parent.move_and_wait(NECK=(90,100))
			parent.wait((.75, 1.5))

		parent.move_to(NECK=50)
		# YOUR CODE ENDS HERE

	finally:
		# DO NOT MODIFY THIS CODE
		parent.exit()
