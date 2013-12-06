# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [  "BLINK" ]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [  "BLINK"  ]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 1000

# Human readable name for debugging purposes.
name = "Blinking"

def run(parent):
#	try:
		# YOUR CODE GOES HERE
	parent.move_and_wait(BLINK=95)
	parent.move_and_wait(BLINK=5)

	parent.stop_with_probability(.5)

	parent.move_and_wait(BLINK=95)
	parent.move_to(BLINK=5)
		# YOUR CODE ENDS HERE

#	finally:
		# DO NOT MODIFY THIS CODE
	parent.exit()
