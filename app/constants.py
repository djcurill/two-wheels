import enum
import json

with open("bikes.json", "r") as f:
    data = f.read()
    # then load it using json.loads()
    bikes = json.loads(data)

# conditions of mtb quality
conditions = ["New - Dealer/Store", "New - Owner", "Excellent", "Good", "Poor"]

# mountain bike frame sizes
frame_sizes = ["XS", "S", "M", "L", "XL"]

# mountain bike wheel sizes
wheel_sizes = ["27.5", "29"]


class BikeCategory(enum.Enum):
    """Bike categories offered by Pink Bike"""

    DOWNHILL = 1
    ENDURO = 2
    XC = 75


class Region(enum.Enum):
    """Regions where PinkBike operates"""

    NORTH_AMERICA = 3
    EUROPE = 5
