"""
Kremlin unit tests
"""

import os
import kremlin
import unittest
import tempfile
import shutil

class KremlinTestCase(unittest.TestCase):
    """ Kremlin magical test cases and agile scrum buzzwords """

    def setUp(self):
        """ Setup blank database and temporary directories for tests """

        # Flip testing bit
        kremlin.app.config['TESTING'] = True

        # Disable CSRF during testing
        kremlin.app.config['CSRF_ENABLED'] = False

        # Obtain temporary files
        #self.db_fd = tempfile.mkstemp(prefix="kremlin-test_", suffix=".db")
        self.imgdir = tempfile.mkdtemp(prefix="kremlin-test_")
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
        return self.app.post('/login', data=dict(
            username=username,
            password=password,
        ), follow_redirects=True)

    def _logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def _register(self, username, email, password, confirm):
        return self.app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            confirm=confirm,
        ), follow_redirects=True)

    # Actual unit tests below

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

if __name__ == '__main__':
    unittest.main()
