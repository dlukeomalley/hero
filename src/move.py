perms = [ "LARM",
		  "RARM",
		  "NECK"]

priority = 5

def run(parent):
	try:
		for x in range(4):
			parent.move_to()

	finally:
		rospy.loginfo("Exiting from {}".format(threading.current_thread().name))

# move("LARM"=5, "RARM"=10)
# wait_until("LARM"=5, "RARM"=10)
# move_and_wait("LARM"=5, "RARM"=10)
