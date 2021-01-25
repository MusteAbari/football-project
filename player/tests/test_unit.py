from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_player(self):
        with patch("random.choice") as random:
            random.return_value = "Rashford"
            response = self.client.get(url_for('get_player'))
            self.assertEqual(b'Rashford', response.data)
