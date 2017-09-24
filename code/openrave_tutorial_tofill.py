#!/usr/bin/env python

PACKAGE_NAME = 'hw0'

# Standard Python Imports
import os
import copy
import time
import numpy as np
import scipy

# OpenRAVE
import openravepy
#openravepy.RaveInitialize(True, openravepy.DebugLevel.Debug)


curr_path = os.getcwd()
relative_ordata = '/models'
ordata_path_thispack = curr_path + relative_ordata

#this sets up the OPENRAVE_DATA environment variable to include the files we're using
openrave_data_path = os.getenv('OPENRAVE_DATA', '')
openrave_data_paths = openrave_data_path.split(':')
if ordata_path_thispack not in openrave_data_paths:
  if openrave_data_path == '':
      os.putenv('OPENRAVE_DATA', ordata_path_thispack)
  else:
      os.putenv('OPENRAVE_DATA', '%s:%s'%(ordata_path_thispack, openrave_data_path))



class RoboHandler:
  def __init__(self):
    pass 
    

  #remove all the time.sleep(0) statements! Those are just there so the code can run before you fill in the functions

  # move in a straight line, depending on which direction the robot is facing
  def move_straight(self, dist):
    pass

  # rotate the robot about the z-axis by the specified angle (in radians)
  def rotate_by(self, ang):
    pass

  # go to each of the square corners, point towards the center, and snap a photo!
  def go_around_square(self):
    pass
    #TODO Fill in

    # set the robot back to the initialize position after


  # a function to help figure out which DOF indices correspond to which part of HERB
  def figure_out_DOFS(self):
    pass
    #TODO Fill in, remove sleep
    time.sleep(0)
  
  # put herb in self collision
  def put_in_self_collision(self):
    #TODO Fill in, remove sleep
    time.sleep(0)

  # saves an image from above, pointed straight down
  def save_viewer_image_topdown(self, imagename):
    TopDownTrans = np.array([ [0, -1.0, 0, 0], [-1.0, 0, 0, 0], [0, 0, -1.0, 5.0], [0, 0, 0, 1.0] ])
    #seems to work without this line...but its in the tutorial, so I'll keep it here in case
    self.env.GetViewer().SendCommand('SetFiguresInCamera 1') # also shows the figures in the image
    I = self.env.GetViewer().GetCameraImage(640,480,  TopDownTrans,[640,640,320,240])
    scipy.misc.imsave(imagename + '.jpg',I)

if __name__ == '__main__':
  robo = RoboHandler()

  # Uncomment the following to make the script initialize the RoboHandler
  #  and drop you into an IPython shell.
#  t = np.array([ [0, -1.0, 0, 0], [-1.0, 0, 0, 0], [0, 0, -1.0, 5.0], [0, 0, 0, 1.0] ])  
#  robo.env.GetViewer().SetCamera(t)

  import IPython
  IPython.embed()

  
