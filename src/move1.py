# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [	"LARM",
			"RARM",  ]

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 10

# Human readable name for debugging purposes.
name = "High Level Test - 1"

def run(parent):
#	try:
		# YOUR CODE GOES HERE
		
	parent.move_and_wait(LARM=10, RARM=100)

		# YOUR CODE ENDS HERE

#	finally:
		# DO NOT MODIFY THIS CODE
#		parent.exit()
