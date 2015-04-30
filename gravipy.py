__author__ = 'Andrea Gangemi'
__Version__ = '0.0.1'

# Reference site:
# http://www.braeunig.us/space/orbmech.htm

class Orbit():
    def __init__(self):
        self.orbit_parameters = {'major_semiaxis': 0, 'eccentricity': 0, 'inclination': 0, 'periapsis_arg': 0,
                                 'periapsis_passage': 0, 'ascending_node_longitude': 0}
        pass

class Satellite(Orbit):
    def __init__(self):
        pass
