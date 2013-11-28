perms = [ "LARM",
		  "RARM",
		  "NECK"]

def run():
	for x in range(4):
		self.move_to()

	rospy.loginfo("Exiting from {}".format(threading.current_thread().name))

# move("LARM"=5, "RARM"=10)
# wait_until("LARM"=5, "RARM"=10)
# move_and_wait("LARM"=5, "RARM"=10)
