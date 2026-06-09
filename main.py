from model import StartupIdea

def show_title():
    print("\n" + "=" * 40)
    print("      AI STARTUP IDEA ANALYZER")
    print("=" * 40)

def collect_idea():
    idea_name = input("\nStartup Idea Name: ")
    problem = input("Problem Being Solved: ")
    audience = input("Target Audience: ")

    idea = StartupIdea(
        idea_name,
        problem,
        audience
    )

    idea.display()


def main():
    show_title()
    collect_idea()


if __name__ == "__main__":
    main()