# "Jump! Or I'll Push You" code samples
These are code samples from the "Jump! Or I'll Push You" presentation at AutoCon1. When running these scripts, it's best to limit your blast radius in case there are any issues. To do so, I recommend using a lab device and having that device be the only one in NetBox while running code from this repository.

Prerequisites for running this project:
1. NetBox server
2. Run `pip install -r requirements.txt` in this directory to install the required packages like Jinja2, Netmiko, and Requests.


## netbox.py
This script will connect to your NetBox server via the NetBox API and return a list of your devices. It requires the following pieces of information:
1. The URL of your NetBox server
2. Your NetBox API key/token

Run the script with `python3 netbox.py` and it will return a list of your devices from NetBox.


## ssh.py
This script will SSH to a network device and send a "show run" command. It requires the following pieces of information:
1. The hostname or IP address of your network device
2. Your username and password for connecting to the network device
3. The command to run, which has been set to "show run" in the example

Run the script with `python3 ssh.py` and it will send the "show run" command to your device and return the output.


## configuration.py
This script will take a list of variables and use them to programmatically create a configuration for your network device. In this example, we're creating a configuration to set interface descriptions on our device. This script requires the following pieces of information:
1. The name and description of each interface (specific to this example)

Run the script with `python3 configuration.py` and it will generate the configuration for setting the interface descriptions on a device.


## complete.py
This script takes everything that was learned in the previous scripts and puts it all together. It will get a list of devices from NetBox, create a configuration for each of them, and then push the configuration to each device. In this example, we're setting the SNMP contact on each device so that we don't do anything disruptive in the environment.

The following pieces of information are required:
1. The URL of your NetBox server
2. Your NetBox API key/token
3. SNMP contact email

Run the script with `python3 complete.py` and it will get the list of devices from NetBox, generate a configuration for each of them, and push the configurations to each device.
