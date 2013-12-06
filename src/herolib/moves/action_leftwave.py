# Otter moves arms, makes sound, and blinks

# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"LARM"	]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [ 	"LARM_GRAB" ]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 4

# Human readable name for debugging purposes.
name = "Left Wave"

def run(parent):
	try:
		# YOUR CODE GOES HERE
		parent.move_and_wait(LARM=(70,90)
		parent.move_and_wait(LARM=(10,30)
		# YOUR CODE ENDS HERE

	finally:
		# DO NOT MODIFY THIS CODE
		parent.exit()
