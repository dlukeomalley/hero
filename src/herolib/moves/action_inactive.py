#Resting Awake - Ollie hasn’t moved in XX minutes

# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"LARM",
			"RARM",
			"NECK",	]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [ 	"INACTIVE"	]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 1001

# Human readable name for debugging purposes.
name = "Inactive State"

def run(parent):
	try:
		# YOUR CODE GOES HERE
		while True:
			parent.move_to(LARM=(20, 80), RARM=(20, 80), NECK=(40, 60))
			parent.wait((.5, 2))
		# YOUR CODE ENDS HERE

	finally:
		# DO NOT MODIFY THIS CODE
		parent.exit()