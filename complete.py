from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

import requests

def main():
    """
    Take a URL and token (provided by you) and connect to NetBox to retrieve a list of devices.

    URL: The URL to your NetBox instance. The API endpoint "/api/dcim/devices" needs to be added to the URL.
    Token: The NetBox API key/token that is used to authenticate your API requests.
    """
    url = "http://netbox.local/api/dcim/devices"
    token = ""

    """
    These headers tell NetBox what type of data we expect and passes our NetBox API key/token
    to NetBox for authentication.
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f"Token {token}",
    }

    """
    Use the "requests" library to send an API GET request to NetBox. It includes our previously-defined headers
    and tells the "requests" library to ignore failed SSL certificate checks using the "verify=False" arguments.
    The response is a list of devices pulled from your NetBox instance.
    """
    response = requests.get(url, headers=headers, verify=False)
    devices = response.json()['results']

    """
    This will define the email address that we want to use for setting the SNMP contact on our network devices.
    """
    snmp_contact = "me@myself.com"

    """
    Load the Jinja2 template and pass the SNMP contact variable to it.
    The template will create a configuration for each device using the SNMP contact that you defined.

    Edit the "snmp.j2" file in the "templates/" directory to see the Jinja2 template structure.
    Variables are included in Jinja2 templates using double curly brackets.
    """
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("snmp.j2")

    """
    Go through our list of devices and for each device, generate the configuration using our
    SNMP contact variable, and then push the configuration to the device. Even though each configuration
    is going to look the same in this example, we generate the "config" variable inside our device loop
    because most use cases will require a unique configuration for each device.
    """
    for device in devices:
        config = template.render(snmp_contact=snmp_contact)

        """
        These parameters are required by NetMiko for logging into your device. 
        Note that the "device_type" variable has many options and you should use the one that is specific to your device.
        See all device types here: https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md#supported-ssh-device_type-values

        The host is dynamic now and is using the device name for each device that was found in NetBox.

        The username and password are your login credentials for the device. Make sure you don't store
        them in this file when saving to a version control system or sharing the file with others.
        """
        parameters = {
            "device_type": "cisco_ios",
            "host": device['name'],
            "username": "my_username",
            "password": "my_password",
        }

        """
        Establish an SSH connection to your device and send the configuration that was generated from
        our Jinja2 template.
        Print the output so we can view it.
        """
        with ConnectHandler(**parameters) as conn:
            output = conn.send_config_set([config])
        print(output)

if __name__ == "__main__":
    main()
