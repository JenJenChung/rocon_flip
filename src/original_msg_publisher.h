#include <ros/ros.h>
#include <ros/console.h>
#include <string>
#include "std_msgs/String.h"
#include "std_msgs/Bool.h"

class Sender{
  public:
    Sender(ros::NodeHandle) ;
    ~Sender(){}
  private:
    ros::Subscriber subHandshake ; // handshake flip published from remote gateway
    ros::Publisher pubHelloString ; // original flip publish message
    ros::Publisher pubAckHandshake ; // acknowledge flip publish handshake received
    
    ros::Subscriber subRemoteString ; // flip subscribe from remote gateway
    ros::Publisher pubRemoteReceived ; // acknowledge flip subscribe message received
    
    std::string gate_name ;
    
    void handshakeCallback(const std_msgs::String&) ; // testing flip publishing capabilities
    void remoteStringCallback(const std_msgs::String&) ; // testing flip publishing capabilities
} ;

Sender::Sender(ros::NodeHandle nh){
  subHandshake = nh.subscribe("/receiver/handshake", 10, &Sender::handshakeCallback, this) ;
  pubHelloString = nh.advertise<std_msgs::String>("original_message", 10, true) ;
  pubAckHandshake = nh.advertise<std_msgs::Bool>("msg_ack", 10, true) ;
  
  subRemoteString = nh.subscribe("/receiver/machine_name", 10, &Sender::remoteStringCallback, this) ;
  pubRemoteReceived = nh.advertise<std_msgs::Bool>("flip_sub_ack", 10, true) ;
  
  std_msgs::String s ;
  ros::param::get("/gateway/name",gate_name) ;
  s.data = "Hello from " + gate_name + "!" ;
  pubHelloString.publish(s) ;
}

void Sender::handshakeCallback(const std_msgs::String& msg){
  ROS_INFO("Handshake received from remote gateway!") ;
  ROS_INFO_STREAM("Message reads: " << msg.data ) ;
  
  std_msgs::Bool b ;
  b.data = true ;
  pubAckHandshake.publish(b) ;
}

void Sender::remoteStringCallback(const std_msgs::String& msg){
  ROS_INFO("Flip subscribe remote message received!") ;
  ROS_INFO_STREAM("Remote machine name: " << msg.data) ;
  
  std_msgs::Bool b ;
  b.data = true ;
  pubRemoteReceived.publish(b) ;
}
