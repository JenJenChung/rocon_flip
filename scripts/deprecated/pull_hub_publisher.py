#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway

def pull(topic):
  rospy.init_node('pull_hub_publisher')
  
  rospy.wait_for_service('/gateway/pull')
  remote_gateway = "Hub_Gateway"
  pull_service = rospy.ServiceProxy('/gateway/pull', gateway_srvs.Remote)
  req = gateway_srvs.RemoteRequest()
  req.cancel = False
  req.remotes = []
  rule = gateway_msgs.Rule()
  rule.name = '/' + topic
  rule.type = gateway_msgs.ConnectionType.PUBLISHER
  rule.node = ""
  req.remotes.append(gateway_msgs.RemoteRule(remote_gateway, rule))
  rospy.loginfo("Pull : [%s,%s,%s,%s]."%(remote_gateway, rule.name, rule.type, rule.node))

  resp = pull_service(req)
  if resp.result != 0:
      rospy.logerr("Pull : %s"%resp.error_message)

  rospy.loginfo("Finished pulling connection.")

if __name__=='__main__':
  try:
    if len(sys.argv) < 2:
      print('Usage: pull_hub_publisher.py topic')
    else:
      pull(str(sys.argv[1]))
  except rospy.ROSInterruptException:
    pass
