"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from .views import temp
from .views import water
from django.test import TestCase
import pathlib as pl

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 0, 400)

    def test_file_cam(self):
        """Tests the temp of page."""
        path = pl.Path("app/static/app/images/Cam.png")
        self.assertTrue(path.is_file())

    def test_temp(self):
        """Tests the temp of page."""
        result = temp()
        self.assertTrue(14 <= result <= 24)

    def test_water(self):
        """Tests the temp of page."""
        result = water()
        self.assertTrue(10 <= result <= 60)


    


