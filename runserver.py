#!/usr/bin/env python
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
import sys

def usage():
    """ Display program usage """
    print """
    Kremlin startup helper program
    Mostly useful for development and testing purposes.
    -------------------------------
    usage: %s <configfile.cfg>

    Configuration file name or path is entirely optional, the default value of
    'kremlin.cfg' will be use should it be omitted. Useful for multiple
    configurations such as testing/development/production.

    You may also set the environment variable 'KREMLIN_CONFIGURATION' to
    obtain the same result, which also works when running the application by
    other means, such as fcgi, gunicorn or unsupported application servers.
    """ % (sys.argv[0])

def main():
    """ Program entry point when ran interactively """
    print "Kremlin Magical Everything System v 0.0.0-None"
    print "Copyright (c) Glasnost 2010-2011"
    print "-----------------------------------------------"

    # If no configuration is specified, use the default.
    if len(sys.argv) < 2:
        if not os.environ.has_key('KREMLIN_CONFIGURATION'):
            os.environ['KREMLIN_CONFIGURATION'] = \
                    os.path.abspath('kremlin.cfg')
    elif len(sys.argv) == 2:
        # TODO: Ugly as sin. In due time, add better argument parsing.
        if sys.argv[1].startswith('-'):
            usage()
            sys.exit(1)
        else:
            if os.environ.has_key('KREMLIN_CONFIGURATION'):
                print "Warning! Overriding environment value for config file!"

            os.environ['KREMLIN_CONFIGURATION'] = sys.argv[1]
    else:
        usage()
        sys.exit(1)

    # Quick sanity check to make sure the config file actually exists,
    # abort noisily if it isn't the case. Anyone bugging me about how I
    # should use open() and fail because the situation might lead to a
    # race condition should voice complaints to /dev/null, or submit a
    # patch if it is that important to them.
    if not os.path.isfile(os.environ['KREMLIN_CONFIGURATION']):
        print "Critical: Specified configuration file %s doesn't exist!" %\
                (os.environ['KREMLIN_CONFIGURATION'])
        sys.exit(1)

    print "INIT: Using configuration file %s" %\
            (os.environ["KREMLIN_CONFIGURATION"])

    print "Connect to http://127.0.0.1:5000 to access."
    print "Starting application..."

    # Application is imported at this point because kremlin/__init__.py
    # actually loads the configuration.
    from kremlin import app, db_init
    print "Setting up database..."
    db_init()
    app.run()

if __name__ == '__main__':
    main()
