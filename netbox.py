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
    print(response)

if __name__ == "__main__":
    main()
