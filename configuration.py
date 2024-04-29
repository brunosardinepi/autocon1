from jinja2 import Environment, FileSystemLoader

def main():
    """
    Define a list of interfaces. This is a list of dictionaries, where each dictionary has the
    name and description of the interface.
    Change these as needed since this is only used as an example.
    """
    interfaces = [
        {
            "name": "Ethernet1/1",
            "description": "ISP #1",
        },
        {
            "name": "Ethernet1/2",
            "description": "ISP #2",
        },
        {
            "name": "Ethernet1/48",
            "description": "vPC peer link",
        },
    ]

    """
    Load the Jinja2 template and pass the list of interfaces to it as a variable.
    The template will create a configuration for each interface based on the
    "interfaces" list and the configuration in the Jinja2 template.

    Edit the "configuration.j2" file in the "templates/" directory to see the Jinja2 template structure.
    Variables are included in Jinja2 templates using double curly brackets.
    """
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("interfaces.j2")
    config = template.render(interfaces=interfaces)
    print(config)

if __name__ == "__main__":
    main()
