import unittest
from moodboard.moodboard import Moodboard, Idea

class TestMoodboard(unittest.TestCase):
    def test_idea_can_be_marked_completed(self):
        idea = Idea("Testi", "Kuvaus")
        idea.mark_completed()
        self.assertTrue(idea.completed)