import enum

# conditions of mtb quality
conditions = ["New - Dealer/Store", "New - Owner", "Excellent", "Good", "Poor"]

# mountain bike frame sizes
frame_sizes = ["XS", "S", "M", "L", "XL"]

# mountain bike wheel sizes
wheel_sizes = ["27.5", "29"]

# bike brands
brands = [
    "rocky mountain",
    "santa cruz",
    "yeti",
    "evil",
    "nukeproof",
    "commencal",
    "trek",
    "gt",
    "specialized",
    "cannondale",
    "giant",
    "juliana",
    "liv",
    "niner",
    "norco",
    "orbea",
    "pivot",
    "salsa",
    "kona",
    "scott",
    "ibis",
]


class BikeCategory(enum.Enum):
    """Bike categories offered by Pink Bike"""

    DOWNHILL = 1
    ENDURO = 2
    XC = 75
