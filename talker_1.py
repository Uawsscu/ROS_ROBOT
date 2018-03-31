#!/usr/bin/env phthon

import sys
import rospy
import sqlite3
import time
from std_msgs.msg import UInt8


# from std_msgs.msg import String

# def callback_Talk(msg): #insert ActionName
#	with sqlite3.connect("Test_PJ1.db") as con:
#		cur = con.cursor()
#		cur.execute('SELECT * FROM ActionName')
#		rows = cur.fetchall()
#		lenR = len(rows)
#		cur.execute('insert into ActionName (ID,Name) values (?,?)', (lenR ,msg ,))
#	print(lenR,name)


def talker(msg):
    pub = rospy.Publisher('setMotor', UInt8, queue_size=10)
    rospy.init_node('Talker', anonymous=True)

    pub.publish(int(msg))


# pub.publish(String(msg))


if __name__ == '__main__':
    index = 0
    while (True):
        step = input("Enter you Step : ")
        talker(9)
        name = "move to the left"
        list = []
        with sqlite3.connect("DB_Project.db") as con:
            cur = con.cursor()
            cur.execute("Select ID from ActionName where Action = ?", (name,))
            row = cur.fetchone()
            for element in row:
                id = element
                list.append(id)
            list.append(index)

            time.sleep(5)
            cur.execute("Select Motor1,Motor2,Motor3,Motor4,Motor5,Motor6,Motor7,Motor8 from Buffer_Action where ID_Buff = ?", (1,))
            row = cur.fetchone()
            for element in row:
                Motor = element
                list.append(Motor)

            cur.execute('insert into Action_Robot (ID,Step,Motor1,Motor2,Motor3,Motor4,Motor5,Motor6,Motor7,Motor8) values (?,?,?,?,?,?,?,?,?,?)', (list))
            cur.execute("DELETE FROM Buffer_Action WHERE ID_Buff=?", (1,))
        print(list)
        if (step == 0):
            break
        elif(step == 1):
            talker(0)

        index += 1

