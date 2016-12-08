#!/usr/bin/python
import rospy
import sys
import gateway_msgs.msg as gateway_msgs
import gateway_msgs.srv as gateway_srvs
import rocon_gateway
import argparse

def pull(gate, remote, local, topic, node):
  rospy.init_node('generic_puller')
  
  rospy.wait_for_service('/gateway/pull')
  remote_gateway = gate[0]
  pull_service = rospy.ServiceProxy('/gateway/pull', gateway_srvs.Remote)
  req = gateway_srvs.RemoteRequest()
  req.cancel = False
  req.remotes = []
  rule = gateway_msgs.Rule()
  if topic[0][0] == '/':
    rule.name = topic[0]
  elif not remote:
    rule.name = '/' + topic[0] ;
  else:
    rule.name = '/' + remote[0] + '/' + topic[0]
  rule.type = gateway_msgs.ConnectionType.PUBLISHER
  if not node:
    rule.node = ''
  elif node[0][0] == '/':
    rule.node = node[0]
  elif not local:
    rule.node = '/' + node[0]
  else:
    rule.node = '/' + local[0] + '/' + node[0]
  req.remotes.append(gateway_msgs.RemoteRule(remote_gateway, rule))
  rospy.loginfo("Pull : [%s,%s,%s,%s]."%(remote_gateway, rule.name, rule.type, rule.node))

  resp = pull_service(req)
  if resp.result != 0:
      rospy.logerr("Pull : %s"%resp.error_message)

  rospy.loginfo("Finished pulling connection.")

if __name__=='__main__':
  try:
    parser = argparse.ArgumentParser(description='Create subscriber flip connection.')
    parser.add_argument('-g', dest='gate', metavar='gateway', type=str, action='store', 
      nargs=1, help='gateway name')
    parser.add_argument('-t', dest='topic', metavar='topic', type=str, action='store', 
      nargs=1, help='topic name')
    parser.add_argument('-n', dest='node', metavar='node_name', type=str, action='store',
      nargs=1, default='', help='node name')
    parser.add_argument('-r', dest='remote', metavar='remote_namespace', type=str, action='store', 
      nargs=1, default='', help='remote namespace')
    parser.add_argument('-l', dest='local', metavar='local_namespace', type=str, action='store', 
      nargs=1, default='')
    args = parser.parse_args() ;
    pull(args.gate,args.remote,args.local,args.topic,args.node)
  except rospy.ROSInterruptException:
    pass
