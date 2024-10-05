from django.test import TestCase
from django.urls import reverse
from .models import SeniorDesign

class ModelTests(TestCase):
    def setUp(self):
        SeniorDesign.objects.create(
            Team_abbreviation="TEST",
            Location="Test Location",
            Poster_tittle="Test Poster",
            Abstract="Test Abstract",
            num_team_members=4,
            team_member_names="John, Jane, Bob, Alice",
            Need_power=True,
            two_outlets=True,
            table=True,
            foamboard=False,
            clips=False,
            large_presentaion=False,
            sponsor_logos=True,
            picutures=True
        )

    def test_senior_design_creation(self):
        test_team = SeniorDesign.objects.get(Team_abbreviation="TEST")
        self.assertEqual(test_team.Location, "Test Location")
        self.assertEqual(test_team.num_team_members, 4)
        self.assertTrue(test_team.Need_power)
        self.assertFalse(test_team.foamboard)

    def test_senior_design_str_method(self):
        test_team = SeniorDesign.objects.get(Team_abbreviation="TEST")
        self.assertEqual(str(test_team), "TEST")

class ViewTests(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what your main view should contain

class UrlTests(TestCase):
    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not authenticated

        