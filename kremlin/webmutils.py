"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

Provides a set of utilities to implement WebM posting support.
"""
import os, subprocess

from PIL import Image


def checkwebm(fp):
  """
  Check the file using ffprobe to confirm that the file is a WebM. If not,
  reject it
  """.
  runtime = ['ffprobe']
  runtime.append(fp)
  proc = subprocess.Popen(runtime, stdout=subprocess.PIPE)
  out = proc.communicate()
  # Check for -1, if it exists return True
  searchres = out.find("vp8");
  if searchres > -1:
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


def mkthumbfromwebm(fp, h=128, w=128):
  """
  Create the image from a webm at the first second of playback

  fp  filesystem path to the full size image
  h   height (default is 128)
  w   width  (default is 128)

  The thumbnail will be unceremoniously dumped in the same
  directory with 'thumbnail' between the file name and extension.

  ffmpeg with libvpx is required for this to work
  """
  runtime = ['ffmpeg', '-i']
  runtime.append(fp);
  runtime.append('-ss 00:00:01.01 -vframes 1 outputtemp.png')
  out = proc.communicate()
  # Confirm output successful if so return fp for outputtemp



def destroyfile(fp):
  """
  Destroys an file if it does not meet the criteria we expect. Only the blackest
  of metal should be played during the ritual.
  """
