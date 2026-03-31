from moodboard.moodboard import Moodboard, Idea

# generoitu koodi alkaa
class MoodboardService:
    def __init__(self):
        self.moodboards = []

    def create_moodboard(self, name):
        moodboard = Moodboard(name)
        self.moodboards.append(moodboard)
        return moodboard

    def add_idea_to_moodboard(self, moodboard, title, description):
        idea = Idea(title, description)
        moodboard.add_idea(idea)
        return idea

    def mark_idea_done(self, idea):
        idea.mark_completed()

    def list_moodboards(self):
        return self.moodboards
# generoitu koodi päättyy