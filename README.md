# rocon_flip
python and bash scripts for streamlining rocon communications

USAGE:
The main tools are the generic_*.py files in the scripts folder.
These programs read in topic name(-t), gateway name (-g), local (-l) and remote (-r) namespaces, node name (-n) parameters to set up connections across a multimaster ROS rocon network.

REQUIRED INPUTS:
- Publisher:
  - gateway name
  - topic name
  - (no option for remote namespace)
- Subscriber:
  - gateway name
  - topic name
- Advertiser
  - topic name
  - (no option for gateway name or remote namespace)
- Puller
  - gateway name
  - topic name
All other inputs default to an empty string.

RECOMMENDED INTERFACE:
The python scripts are set up such that they can be called from the command line with the necessary inputs.
Alternatively, you can set up a bash script to loop through all the connections you want to create.
See test_sender, test_receiver, advertise_from_hub, pull_from_hub for examples on how to create publish, subscribe, advertise and pull connections.

VERSIONS:
This package currently contains old versions of the code in various python scripts.
These will be slowly phased over the following months. Please only use the generic_*.py scripts in future projects.

TESTING:
Two launch files, sender.launch and receiver.launch, can be used for testing network connection.
Sender.launch will run a bash script to set up flip publisher and subscriber connections and launch a node to publish a string.
Receiver.launch will run a bash script to set up flip publisher connections and launch a node to perform a handshake once the original string from the sender is received.
Both nodes will print out to the command window when the relevant messages have been successfully received.
