"""Handle main configuration for the Central server."""
from hydra import Resource
from rdflib import Namespace
from flock_controller.settings import CENTRAL_SERVER_NAMESPACE, DRONE1_NAMESPACE
from flock_controller.settings import DRONE1_URL, CENTRAL_SERVER_URL
from flock_controller.settings import IRI_CS, IRI_DRONE1


global CENTRAL_SERVER, DRONE1, DRONE_URL
CENTRAL_SERVER = Namespace(CENTRAL_SERVER_NAMESPACE)
print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_NAMESPACE)
# print(DRONE1)

global RES_CS, RES_DRONE
RES_CS = Resource.from_iri(IRI_CS)
RES_DRONE1 = Resource.from_iri(IRI_DRONE1)


# Methods related to Location
def gen_Location(coordinate_str):
    """Generate a Location object."""
    Area = {
        "@type": "Location",
        "Location": coordinate_str
    }
    return Area

# Methods related to Logs
def gen_Log(log_str):
    """Generate a Log object."""
    log = {
        "@type": "Log",
        "LogString": log_str
    }

    return log

# Methods related to Messages
def gen_Message(message):
    """Create a new Message."""
    message = {
        "@type": "Message",
        "MessageString": message,
    }
    return message


# Methods related to commands
def gen_State(drone_id, battery, direction, position, sensor_status, speed):
    """Generate a State objects."""
    state = {
        "@type": "State",
        "DroneID": drone_id,
        "Battery": battery,
        "Direction": direction,
        "Position": position,
        "Status": sensor_status,
        "Speed": speed,
    }
    return state
# state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
# print(state)


def gen_Command(state):
    """Generate a Command object."""
    command = {
        "@type": "Command",
        "State": state
    }
    return command


## Some general Functions
def ordered(obj):
    """Sort json dicts and lists within"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
