#!/usr/bin/env phthon

import sys
import rospy
from std_msgs.msg import UInt8MultiArray
#from std_msgs.msg import String
	
def talker(msg):
	
	
	
	
	pub = rospy.Publisher('JointsValue', UInt8MultiArray, queue_size = 10)
	rospy.init_node('Talker', anonymous = True)
	
	data
	
	pub.publish(int(msg))
	#pub.publish(String(msg))

if __name__ == '__main__':
		talker()
