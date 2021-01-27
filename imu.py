"""
Copyright Harry Sarkis Terkanian
MIT License
December 8, 2020

Update position, linear velocity and bearing vectors based on racecar IMU data.

Members:        pos position vector:    np.array((3), np.float32)
                vel linear velocity:    np.array((3), np.float32)
                head bearing vector:    np.array((3), np.float32)
                timer elapsed time:     float
                rc: racecar object

Public:         current position, linear velocity, heading vectors and timer.
"""

########################################################################################
# Imports
########################################################################################

import numpy as np

########################################################################################
# Class definition
########################################################################################

class Imu:


    def __init__(self, racecar_object):
        self.rc = racecar_object                # MITLL racecar-MN object
        self.pos = np.zeros((3), np.float32)    # position vector
        self.vel = np.zeros((3), np.float32)    # linear velocity vector
        self.head = np.zeros((3), np.float32)   # heading vector
        self.timer = 0.0                        # elapsed time


    def update(self):
        """ Update position, velocity and bearing."""
        linear_accel = self.rc.physics.get_linear_acceleration()
        angular_velocity = self.rc.physics.get_angular_velocity()
        delta_time = self.rc.get_delta_time()
        self.vel += linear_accel * delta_time
        self.pos += self.vel * delta_time
        self.head += angular_velocity * delta_time
        self.timer += self.rc.get_delta_time()


    def position(self):
        """ Return position vector."""
        return self.pos


    def velocity(self):
        """ Return velocity vector."""
        return self.vel


    def bearing(self):
        """ Return heading vector."""
        return self.head

    def elapsed(self):
        """ Return elapsed time."""
        return self.timer


########################################################################################
# Begin execution
########################################################################################

if __name__ == '__main__':
    print("imu.py should be imported, not executed.")    # We don't really want to do this.
    pass