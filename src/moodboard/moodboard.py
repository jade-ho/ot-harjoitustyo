# generoitu koodi alkaa
class Idea:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


class Moodboard:
    def __init__(self, name):
        self.name = name
        self.ideas = []

    def add_idea(self, idea):
        self.ideas.append(idea)

    def get_ideas(self):
        return self.ideas

    def get_completed_ideas(self):
        return [idea for idea in self.ideas if idea.completed]
# generoitu koodi päättyy