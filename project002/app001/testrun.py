from flask import json, url_for
import unittest2 as unittest
import os
import sys


class TestApp001(unittest.TestCase):

    """Simple test for app001

    """

    def setUp(self):
        """Setup the db tables

        """
        setupdb.refresh()
        self.test_client = app.test_client()

    def test_some_app001_functionality(self):
        """Test a GET/POST request functionality in app001

        """
        post_data = {'name': 'knight and day'}

        with app.test_request_context():
            resp1 = self.test_client.post(
                '/admin/movie/add',
                data=json.dumps(post_data),
                content_type='application/json')
            resp2 = self.test_client.get('/admin/movies')

        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp2.status_code, 200)

    def tearDown(self):
        """Clear the db

        """
        setupdb.drop_all_tables()


def main():
    unittest.main()


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, BASE_DIR)
    from app001.utils import setupdb
    from app001.web.app import app
    main()
