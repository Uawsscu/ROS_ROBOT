#!/usr/bin/env phthon

import rospy

from std_msgs.msg import UInt8MultiArray

def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	print(data.data)
	
def listener():
	rospy.init_node('Listener', anonymous=True)
	rospy.Subscriber("JointsValue", UInt8MultiArray, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
