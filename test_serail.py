import rospy
# from std_msgs.msg import UInt8
from std_msgs.msg import UInt8
from std_msgs.msg import Int16MultiArray

from os import path
import pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *


# from cuttext import *

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print(data.data)


def listener():
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber("ArduinoMsg", UInt8, callback)
    rospy.Subscriber("JointsValue", Int16MultiArray, callback)
    # rospy.Subscriber("ArduinoMsg", UInt16, callback)
    rospy.spin()


def speech():
    MODELDIR = "/home/mprang/Desktop/Project/Control-Robot-master/model"
    DATADIR = "/home/mprang/Desktop/Project/Control-Robot-master/data"

    config = Decoder.default_config()
    config.set_string('-logfn', '/dev/null')
    config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
    config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
    config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
    decoder = Decoder(config)

    # Switch to JSGF grammar
    jsgf = Jsgf(path.join(DATADIR, 'sentence.gram'))
    rule = jsgf.get_rule('sentence.move')  # >> public <move>
    fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
    fsg.writefile('sentence.fsg')

    decoder.set_fsg("sentence", fsg)
    decoder.set_search("sentence")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()

    in_speech_bf = False
    decoder.start_utt()
    while True:
        buf = stream.read(20)
        if buf:
            decoder.process_raw(buf, False, False)

            if decoder.get_in_speech() != in_speech_bf:
                in_speech_bf = decoder.get_in_speech()
                if not in_speech_bf:
                    decoder.end_utt()

                    try:
                        strDecode = decoder.hyp().hypstr

                        if strDecode != '':

                            if strDecode == 'torque on':
                                printResulf(strDecode)
                                # talker(1)
                            elif strDecode == 'torque off':
                                printResulf(strDecode)
                                # talker(2)
                            elif strDecode == 'turn left':
                                printResulf(strDecode)
                                # talker(3)
                            elif strDecode == 'turn right':
                                printResulf(strDecode)
                                # talker(4)
                            elif strDecode == 'turn center':
                                printResulf(strDecode)
                                # talker(5)

                    except AttributeError:
                        pass

                    decoder.start_utt()
        else:
            break
    decoder.end_utt()
    print('An Error occured :', decoder.hyp().hypstr)


def talker(msg):
    pub = rospy.Publisher('setMotor', UInt8, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    pub.publish(int(msg))


def printResulf(strDecode):
    print '--- START ---', strDecode


if __name__ == '__main__':
    speech()
