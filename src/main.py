from services.moodboard_service import MoodboardService

# generoitu koodi alkaa
def main():
    service = MoodboardService()

    mb = service.create_moodboard("Piirrosideat")

    idea1 = service.add_idea_to_moodboard(mb, "Piirrä maisema", "Vuoret ja järvi")
    idea2 = service.add_idea_to_moodboard(mb, "Hahmosuunnittelu", "Fantasia-hahmo")

    service.mark_idea_done(idea1)

    print("Moodboard:", mb.name)
    for idea in mb.get_ideas():
        status = "x" if idea.completed else " "
        print(f"[{status}] {idea.title} - {idea.description}")

if __name__ == "__main__":
    main()
# generoitu koodi loppuu