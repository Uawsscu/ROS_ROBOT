#!/usr/bin/env phthon
import numpy as np
import sqlite3
import rospy
import numpy as np
#from std_msgs.msg import String
from std_msgs.msg import UInt8
from std_msgs.msg import String
#from sensor_msgs.msg import JointState

#>>>>>>>>>>> ROS STEP1 <<<<<<<<<<<<<<<<<<<
def callback(data):
    A= data.data
    print "This is a data.data >>> ",A
    B = A.split(', ')
    #B = B.split(' ')
    D = []
    for i in B:

        print "index :",i
        C = int(i)
        print "C:",C
        D.append(C)
    print "List >>> ",D
    return D

def listener():
	rospy.init_node('Listener', anonymous=True)
	#rospy.Subscriber("ArduinoMsg", UInt8, callback)
	rospy.Subscriber("JointsValue", String, callback)
	#rospy.Subscriber("ArduinoMsg", UInt16, callback)
	rospy.spin()

#>>>>>>>>>>>>>>>>>> ADD DATA
def callback_Talk(data): #insert ActionName
	name = int(data.data)
	with sqlite3.connect("Test_PJ1.db") as con:
		cur = con.cursor()
		cur.execute('SELECT * FROM ActionName')
		rows = cur.fetchall()
		lenR = len(rows)
		cur.execute('insert into ActionName (ID,Name) values (?,?)', (lenR ,name ,))
	print(lenR,name)
	return name


listener()