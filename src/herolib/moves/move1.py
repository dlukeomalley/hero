# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"LARM",
			"RARM",  ]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [ 	"BELLY_RUB"	]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 10

# Human readable name for debugging purposes.
name = "High Level Test - 1"

def run(parent):
	try:
		# YOUR CODE GOES HERE
		
		parent.move_and_wait(LARM=10, RARM=100)
		parent.play("sounds/happy_otters.mp3")

		# YOUR CODE ENDS HERE

	finally:
		# DO NOT MODIFY THIS CODE
		parent.exit()
