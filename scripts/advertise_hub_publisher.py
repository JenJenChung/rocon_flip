#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway

def advertise(topic):
  rospy.init_node('advertise_hub_publisher')
  
  rospy.wait_for_service('/gateway/advertise')
  advertise_service=rospy.ServiceProxy('/gateway/advertise', gateway_srvs.Advertise)
  req = gateway_srvs.AdvertiseRequest()
  rule = gateway_msgs.Rule()
  rule.name = '/' + topic
  rule.type = gateway_msgs.ConnectionType.PUBLISHER
  rule.node = ""
  req.rules.append(rule)
  rospy.loginfo("Advertise : [%s,%s,%s,%s]."%(remote_gateway, rule.name, rule.type, rule.node))

  resp = advertise_service(req)
  if resp.result != 0:
      rospy.logerr("Advertise : %s"%resp.error_message)

  rospy.loginfo("Finished advertising connection.")

if __name__=='__main__':
  try:
    if len(sys.argv) < 2:
      print('Usage: advertise_hub_publisher.py topic')
    else:
      advertise(str(sys.argv[1]))
  except rospy.ROSInterruptException:
    pass
