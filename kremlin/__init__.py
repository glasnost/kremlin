"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""

from flask import Flask
from flask_uploads import configure_uploads, UploadSet, IMAGES
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load default configuration values, override with whatever is specified
# in configuration file. This is, I think, the sanest approach.
app.config.from_object('kremlin.config_defaults')
app.config.from_envvar('KREMLIN_CONFIGURATION')

# Set database from configuration values
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
db = SQLAlchemy(app)

# Create upload set
# and configure like a motherfucker.
uploaded_images = UploadSet("images", IMAGES)
configure_uploads(app, uploaded_images)

# Import relevant modules
# this is done last to avoid touchy situations
import kremlin.dbmodel
import kremlin.core
import kremlin.forms

def db_init():
    """ Initialize database for use """
    db.create_all()

