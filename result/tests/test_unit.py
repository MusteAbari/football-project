from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_result(self):
        players = ["Rashford", "Rooney", "Beckham", "Cole"]
        teams = ["Liverpool", "Arsenal", "Chelsea", "Fulham"]
        result = [b"Rashford will score 4 goals", b"Rashford will score 4 goals", b"Rashford will score 4 goals", b"Rashford will score 4 goals",
                b"Rooney will not score", b"Rooney will score a hat-trick", b"Rooney will score a hat-trick", b"Rooney will score a hat-trick", 
                b"Beckham will not score", b"Beckham will score a freekick", b"Beckham will not score", b"Beckham will score a freekick", 
                b"Cole will not score", b"Cole will not score", b"Cole will not score", b"Cole will score a tap in"]
        i = 0
        for player in players:
            for team in teams:
                response=self.client.post(url_for("result"), json={"player" : player, "team" : team})
                self.assertEqual(response.data, result[i])
                i+=1
