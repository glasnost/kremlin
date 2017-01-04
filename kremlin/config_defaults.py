"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""

""" Configuration Defaults """

DEBUG = False # Debug mode
TESTING = False # Testing mode (unit testing)

SECRET_KEY = None # Session secret key

USE_X_SENDFILE = False # Enable web server sendfile support

LOGGER_NAME = "kremlin" # Main logger name

#SERVER_NAME = "localhost" # Default server name

MAX_CONTENT_LENGTH = 32 * 1024 * 1024 # 32 Megabytes

WTF_CSRF_ENABLED = True # WTForms Cross Site Request Forgery Prevention

UPLOADED_IMAGES_DEST = ""

SQLALCHEMY_TRACK_MODIFICATIONS = False # Disable for production

#UPLOAD_DEFAULT_URL="..."
