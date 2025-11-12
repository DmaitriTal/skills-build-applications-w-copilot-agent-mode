from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.workout = Workout.objects.create(name='Hero Strength', description='Full body', suggested_for='strength')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300, date='2025-11-01')
        self.leaderboard = Leaderboard.objects.create(team=marvel, points=1000)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Hero Strength')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 1000)
