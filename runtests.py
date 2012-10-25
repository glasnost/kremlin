#!/usr/bin/env python

"""
Kremlin unit tests
"""

import os
import unittest
import tempfile
import shutil
import sys


class KremlinTestCase(unittest.TestCase):
    """ Kremlin magical test cases and agile scrum buzzwords """

    def setUp(self):
        """ Setup blank database and temporary directories for tests """

        # The module must be imported late because the kremlin package
        # has some tricky code in __init__.py due to side-effects of the very
        # convenient decorators Flask provides.
        # At the very least Python will actually cache this, so it
        # doesn't have a very large impact in practice.
        #
        # FIXME: I'm so sorry
        import kremlin

        # Flip testing bit
        kremlin.app.config['TESTING'] = True

        # Disable CSRF during testing
        kremlin.app.config['CSRF_ENABLED'] = False

        try:
            self.imgdir = tempfile.mkdtemp(prefix="kremlin-test_")
        except IOError as e:
            print "I/O Error({0}) during mkdtemp: {1}".format(
                    e.errno, e.strerror
                )
            self.fail()


        kremlin.app.config['UPLOADED_IMAGES_DEST'] = self.imgdir

        # Generate unique secret key for the duration of the test
        kremlin.app.config['SECRET_KEY'] = os.urandom(24).encode('hex')

        # Setup in-memory sqlite3 database for testing
        kremlin.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

        kremlin.db_init()

        self.app = kremlin.app.test_client()


    def tearDown(self):
        """ Tear down test fixtures and delete everything """
        shutil.rmtree(self.imgdir)

    def _login(self, username, password):
        """ Perform login with test client """
        return self.app.post('/login', data=dict(
            username=username,
            password=password,
        ), follow_redirects=True)

    def _logout(self):
        """ Perform logout with test client """
        return self.app.get('/logout', follow_redirects=True)

    def _register(self, username, email, password, confirm):
        """ Perform user registration with test client """
        return self.app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            confirm=confirm,
        ), follow_redirects=True)


    def test_basic_auth(self):
        """ Test basic user authentication """

        rv = self._register(
            username="jsmith",
            email="jsmith@gmail.com",
            password="hunter2",
            confirm="hunter2",
            )
        assert 'Registration complete! Please login.' in rv.data

        rv = self._login(
            username="jsmith",
            password='hunter2',
        )
        assert 'Hello, jsmith, you have been logged in.' in rv.data

        rv = self._logout()
        assert 'Logged out of Kremlin.' in rv.data



def usage():
    """ Print interactive usage help """
    print "Usage: {0} <configuration file>".format(sys.argv[0], sys.argv[1])


def main():
    """ Program entry point when ran interactively """

    # If configuration is not specified, use sane-ish defaults.
    # Most settings are actually overriden by the test suite's setUp()
    # method.
    if len(sys.argv) < 2:
        if not os.environ.has_key('KREMLIN_CONFIGURATION'):
            os.environ['KREMLIN_CONFIGURATION'] = \
                    os.path.abspath('kremlin-example.cfg')
        elif len(sys.argv) == 2:
            if sys.argv[1].startswith("-"):
                sys.exit(1)
            else:
                if os.environ.has_key('KREMLIN_CONFIGURATION'):
                    print "Warning! Overriding config file environment value!"

                os.environ['KREMLIN_CONFIGURATION'] = sys.argv[1]
        else:
            usage()
            sys.exit(1)

    # Attempt to further heighten the test running experience with
    # a horrible ASCII banner. Feel free to be hit by a strong feeling
    # of elation.
    print """
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

                        ------------------------
                        - EXECUTING TEST SUITE -
                        ------------------------

          """

    # Build and run test suite for finer control
    suite = unittest.TestLoader().loadTestsFromTestCase(KremlinTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
