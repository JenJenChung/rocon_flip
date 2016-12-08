#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway
import argparse

def advertise(namespace,topic,node):
  rospy.init_node('generic_advertiser')
  
  rospy.wait_for_service('/gateway/advertise')
  advertise_service=rospy.ServiceProxy('/gateway/advertise', gateway_srvs.Advertise)
  req = gateway_srvs.AdvertiseRequest()
  rule = gateway_msgs.Rule()
  if topic[0][0] == '/':
    rule.name = topic[0]
  elif not namespace:
    rule.name = '/' + topic[0] ;
  else:
    rule.name = '/' + namespace[0] + '/' + topic[0]
  rule.type = gateway_msgs.ConnectionType.PUBLISHER
  if not node:
    rule.node = ''
  elif node[0][0] == '/':
    rule.node = node[0]
  elif not namespace:
    rule.node = '/' + node[0]
  else:
    rule.node = '/' + namespace[0] + '/' + node[0]
  req.rules.append(rule)
  rospy.loginfo("Advertise : [%s,%s,%s]."%(rule.name, rule.type, rule.node))

  resp = advertise_service(req)
  if resp.result != 0:
      rospy.logerr("Advertise : %s"%resp.error_message)

  rospy.loginfo("Finished advertising connection.")

if __name__=='__main__':
  try:
    parser = argparse.ArgumentParser(description='Create advertiser.')
    parser.add_argument('-t', dest='topic', metavar='topic', type=str, action='store', 
      nargs=1, help='topic name')
    parser.add_argument('-n', dest='node', metavar='node_name', type=str, action='store',
      nargs=1, default='', help='node name')
    parser.add_argument('-l', dest='local', metavar='local_namespace', type=str, action='store', 
      nargs=1, default='')
    args = parser.parse_args() ;
    advertise(args.local,args.topic,args.node)
  except rospy.ROSInterruptException:
    pass
