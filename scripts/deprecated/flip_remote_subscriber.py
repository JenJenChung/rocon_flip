#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway

def flip(namespace, topic, node):
  rospy.init_node('flip_remote_subscriber')

  remote_gateway = "Hub_Gateway"
  flip_service = rospy.ServiceProxy('/gateway/flip', gateway_srvs.Remote)
  req = gateway_srvs.RemoteRequest()
  req.cancel = False
  req.remotes = []
  rule = gateway_msgs.Rule()
  rule.name = '/' + namespace + '/' + topic
  rule.type = gateway_msgs.ConnectionType.SUBSCRIBER
  rule.node = '/' + namespace + '/' + node
  req.remotes.append(gateway_msgs.RemoteRule(remote_gateway,rule))
  rospy.loginfo("Flip : [%s,%s,%s,%s]."%(remote_gateway, rule.name, rule.type, rule.node))

  resp = flip_service(req)
  if resp.result != 0:
      rospy.logerr("Flip : %s"%resp.error_message)

  rospy.loginfo("Finished flipping connection.")

if __name__=='__main__':
  try:
    if len(sys.argv) < 4:
      print('Usage: flip_remote_subscriber.py namespace topic node')
    else:
      flip(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
  except rospy.ROSInterruptException:
    pass
