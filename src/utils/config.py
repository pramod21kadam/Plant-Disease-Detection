from packages.packages import os
def config(filename):
    """
        Reads the config file and returns a dictionary object
    """
    filename = os.path.join(filename)
    d = {}
    try:
        with open(filename, mode="rb") as config_file:
            exec(compile(config_file.read(), filename, "exec"), d)
    except IOError as e:
        e.strerror = "Unable to load configuration file (%s)" % e.strerror
    return d