""" Configuration file. Main configuration for the robot. DO NOT CHANGE.
"""

# head limits
HEAD = {'X_LIMIT': 185, 'Y_LIMIT': 595}
# image size for api use
IMAGE_SIZE = (1024, 768)

try:
    from local import *
except ImportError:
    pass
