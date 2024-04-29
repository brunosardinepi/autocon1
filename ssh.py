from netmiko import ConnectHandler

def main():
    """
    Send a command to a network device.

    Host: The IP or hostname of your network device. If using the hostname, make sure DNS on this server is working.
    Username: Your username to login to the device
    Password: Your password to login to the device
    Command: The command you want to run, e.g. "show run"
    """
    host = "10.0.0.100"
    username = "my_username"
    password = "my_password"
    command = "show run"

    """
    These parameters are required by NetMiko for logging into your device. 
    Note that the "device_type" variable has many options and you should use the one that is specific to your device.
    See all device types here: https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md#supported-ssh-device_type-values
    """
    parameters = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
    }

    """
    Establish an SSH connection to your device and send the specified command.
    Print the output so we can view it.
    """
    with ConnectHandler(**parameters) as conn:
        output = conn.send_command(command)
    print(output)

if __name__ == "__main__":
    main()
