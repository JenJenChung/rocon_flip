#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway
import argparse

def flip(gate, namespace, topic, node):
  rospy.init_node('generic_flip_publisher')

  remote_gateway = gate[0]
  flip_service = rospy.ServiceProxy('/gateway/flip', gateway_srvs.Remote)
  req = gateway_srvs.RemoteRequest()
  req.cancel = False
  req.remotes = []
  rule = gateway_msgs.Rule()
  if not namespace:
    rule.name = '/' + topic[0]
  else:
    rule.name = '/' + namespace[0] + '/' + topic[0]
  rule.type = gateway_msgs.ConnectionType.PUBLISHER
  if not node:
    rule.node = ''
  elif not namespace:
    rule.node = '/' + node[0]
  else:
    rule.node = '/' + namespace[0] + '/' + node[0]
  req.remotes.append(gateway_msgs.RemoteRule(remote_gateway,rule))
  rospy.loginfo("Flip : [%s,%s,%s,%s]."%(remote_gateway, rule.name, rule.type, rule.node))

  resp = flip_service(req)
  if resp.result != 0:
      rospy.logerr("Flip : %s"%resp.error_message)

  rospy.loginfo("Finished flipping connection.")

if __name__=='__main__':
  try:
    parser = argparse.ArgumentParser(description='Create subscriber flip connection.')
    parser.add_argument('-g', dest='gate', metavar='gateway', type=str, action='store', 
      nargs=1, help='gateway name')
    parser.add_argument('-t', dest='topic', metavar='topic', type=str, action='store', 
      nargs=1, help='topic name')
    parser.add_argument('-n', dest='node', metavar='node_name', type=str, action='store',
      nargs=1, default='', help='node name')
    parser.add_argument('-l', dest='local', metavar='local_namespace', type=str, action='store',
      nargs=1, default='')
    args = parser.parse_args() ;
    flip(args.gate,args.local,args.topic,args.node)
  except rospy.ROSInterruptException:
    pass
