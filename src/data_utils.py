'''
Authors: Alex Wong <alexw@cs.ucla.edu>, Xiaohan Fei <feixh@cs.ucla.edu>
If you use this code, please cite the following paper:
A. Wong, X. Fei, S. Tsuei, and S. Soatto. Unsupervised Depth Completion from Visual Inertial Odometry.
https://arxiv.org/pdf/1905.08616.pdf
@article{wong2020unsupervised,
  title={Unsupervised Depth Completion From Visual Inertial Odometry},
  author={Wong, Alex and Fei, Xiaohan and Tsuei, Stephanie and Soatto, Stefano},
  journal={IEEE Robotics and Automation Letters},
  volume={5},
  number={2},
  pages={1899--1906},
  year={2020},
  publisher={IEEE}
}
'''
import os
import numpy as np
from PIL import Image


def read_paths(filepath):
  '''
  Reads a list of paths from a file

  Args:
    path : str
      path to file where data will be stored
  '''
  path_list = []
  with open(filepath) as f:
     while True:
      path = f.readline().rstrip('\n')
      # If there was nothing to read
      if path == '':
        break
      path_list.append(path)

  return path_list

def load_depth_with_validity_map(path):
  '''
  Loads a depth map and validity map from a 16-bit PNG file

  Args:
    path : str
      path to 16-bit PNG file

  Returns:
    numpy : depth map
    numpy : binary validity map for available depth measurement locations
  '''
  # Loads depth map from 16-bit PNG file
  z = np.array(Image.open(path), dtype=np.float32)
  # Assert 16-bit (not 8-bit) depth map
  z = z/256.0
  z[z <= 0] = 0.0
  v = z.astype(np.float32)
  v[z > 0]  = 1.0
  return z, v

def load_depth(path):
  '''
  Loads a depth map from a 16-bit PNG file

  Args:
    path : str
      path to 16-bit PNG file

  Returns:
    numpy : depth map
  '''
  # Loads depth map from 16-bit PNG file
  z = np.array(Image.open(path), dtype=np.float32)
  # Assert 16-bit (not 8-bit) depth map
  z = z/256.0
  z[z <= 0] = 0.0
  return z

def save_depth(z, path):
  '''
  Saves a depth map to a 16-bit PNG file

  Args:
    z : numpy
      depth map
    path : str
      path to store depth map
  '''
  z = np.uint32(z*256.0)
  z = Image.fromarray(z, mode='I')
  z.save(path)

def load_validity_map(path):
  '''
  Loads a validity map from a 16-bit PNG file

  Args:
    path : str
      path to 16-bit PNG file

  Returns:
    numpy : binary validity map for available depth measurement locations
  '''
  # Loads depth map from 16-bit PNG file
  v = np.array(Image.open(path), dtype=np.float32)
  assert(np.all(np.unique(v) == [0, 256]))
  v[v > 0] = 1
  return v

def save_validity_map(v, path):
  '''
  Saves a validity map to a 16-bit PNG file

  Args:
    v : numpy
      validity map
    path : str
      path to store validity map
  '''
  v[v <= 0] = 0.0
  v[v > 0] = 1.0
  v = np.uint32(v*256.0)
  v = Image.fromarray(v, mode='I')
  v.save(path)
