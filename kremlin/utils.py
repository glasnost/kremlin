"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import os

from PIL import Image

def mkthumb(fp, h=128, w=128):
    """ Create a thumbnail for an image

        fp  filesystem path to the full size image
        h   height (default is 128)
        w   width  (default is 128)

        The thumbnail will be unceremoniously dumped in the same
        directory with 'thumbnail' between the file name and extension.

     """

    size = (h, w)
    f, ext = os.path.splitext(fp)

    with Image.open(fp) as im:
        im.thumbnail(size, Image.ANTIALIAS)
        im.save('.thumbnail'.join([f, ext]))
