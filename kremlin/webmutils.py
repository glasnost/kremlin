"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import os, subprocess

from PIL import Image


def checkwebm(fp):
  """
  Check the file using ffprobe to confirm that the file is a WebM. If not,
  destroy the file and return a 403.
  """
  runtime = ['ffprobe']
  runtime.append(fp)
  proc = subprocess.Popen(runtime, stdout=subprocess.PIPE)
  out = proc.communicate()
  # Check for -1, if it exists return True
  searchres = out.find("vp8");
  if searchres == -1:
    return True
  else:
    return False


def checkforaudio(fp):
  """
  Using ffprobe, determine if the video file has audio and by default, reject
  it.
  """
  runtime = ['ffprobe']
  runtime.append(fp)
  proc = subprocess.Popen(runtime, stdout=subprocess.PIPE)
  out = proc.communicate()
  # Check for -1, if it exists return True
  searchres = out.find("Audio:");
  if searchres == -1:
    return True
  else:
    return False

def mkthumbfromwebm(fp,  h=128, w=128):
  """
  Create the image from a webm at a random second within the first 30 percent
  of its runtime (the Wadsworth constant)

  fp  filesystem path to the full size image
  h   height (default is 128)
  w   width  (default is 128)

  The thumbnail will be unceremoniously dumped in the same
  directory with 'thumbnail' between the file name and extension.

  ffmpeg with libvpx is required for this to work
  """


def destroyfile(fp):
  """
  WATCH THIS RARE PEPE GET DESTROYED
  """
