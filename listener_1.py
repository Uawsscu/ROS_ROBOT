#!/usr/bin/env phthon
import numpy as np
import sqlite3
import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import UInt8
#from std_msgs.msg import String
#from sensor_msgs.msg import JointState


def callback_List(data):
	motor = data.data
	list = []
	list_motor = motor.split(', ')
	for i in list_motor:
		int_motor = int(i)
		list.append(int_motor)
	list.append(1)


	with sqlite3.connect("DB_Project.db") as con:
		cur = con.cursor()
		cur.execute('insert into Buffer_Action (M1,M2,ID) values (?,?,?)', (list))



def listener():
	rospy.init_node('Listener', anonymous=True)
	#rospy.Subscriber("ArduinoMsg", UInt8, callback_List)
	rospy.Subscriber("JointsValue", String, callback_List)
	#rospy.Subscriber("ArduinoMsg", UInt16, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	#callback_List("49, 65")
