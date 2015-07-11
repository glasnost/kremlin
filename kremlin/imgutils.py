"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import os, datetime, time, math, json, cStringIO, StringIO

from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS


def mkthumb(fp, h=128, w=128):
    """docstring for mkthumb"""

    size = (h, w)
    f, ext = os.path.splitext(fp)

    im = Image.open(fp)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('.thumbnail'.join([f, ext]))


def process_metadata(file_str, imagepath):
    """Returns pertinent metadata to be stored in a database record"""
    metaimagedata = cStringIO.StringIO(file_str)
    metaimagedata = Image.open(metaimagedata)
    exif = None

    if metaimagedata.format == 'JPEG':
        if metaimagedata._getexif():
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in metaimagedata._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

    fileHeight = metaimagedata.height
    fileWidth = metaimagedata.width
    fileCreated = int(time.time())
    fileSize = os.stat(imagepath).st_size
    fileExif = json.dumps(exif)

    return (fileHeight, fileWidth, fileCreated, fileSize, fileExif)


def sizeof_fmt(num, suffix='B'):
    """Returns a filesize based on the amounts of bytes provided"""
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
