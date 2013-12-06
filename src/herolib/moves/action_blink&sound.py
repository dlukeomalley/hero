#;interaction 5                                                
#;Interaction_5: Otter blinks and makes soothing sound 
#;Level → 4
#;Motors → (‘BLINK’)
#;Event → ‘rub front of head’, ‘rub back of head’, ‘rub middle belly (lower chance)’ 
#;Code → 



from random import randint as r

# Use only the motors you need.
# Valid motors are BLINK, NECK, LARM, RARM, PUR.
motors = [  "BLINK" ]

# Associate this movement with events.
# Valid events are BELLY_RUB, LARM_GRAB, RARM_GRAB, HEAD_PAT
events = [  "BLINK"  ]# UPPER BELLY BELLY_RUB would have a lower chance 

# The lower the level, the more important this script is.
# Recommended to use 0, 10, 20, 30, 40...
level = 4

# Human readable name for debugging purposes.
name = "Blinking"

def run(parent):
	try:
        # YOUR CODE GOES HERE
        parent.move_and_wait(BLINK=100) ;# close
        parent.move_and_wait(BLINK=0) ; #open

        parent.stop_with_probability(.5)

        parent.move_and_wait(BLINK=100); #← chance for second blink
        parent.move_to(BLINK=0);
        # YOUR CODE ENDS HERE

    finally:
        # DO NOT MODIFY THIS CODE
        parent.exit()