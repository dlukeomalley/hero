# Otter moves right arm back and forth and makes happy sound

# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"RARM" ]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [ 	"RARM_GRAB"]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 4

# Human readable name for debugging purposes.
name = "Right Wave"

def run(parent):
	try:
		# YOUR CODE GOES HERE
		parent.move_and_wait(RARM=(70,90)
		parent.move_and_wait(RARM=(10,30)
		# YOUR CODE ENDS HERE

	finally:
		# DO NOT MODIFY THIS CODE
		parent.exit()