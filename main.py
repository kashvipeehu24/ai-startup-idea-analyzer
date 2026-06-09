from model import StartupIdea

from menu import show_menu

ideas = []


def show_title():
    print("\n" + "=" * 40)
    print("AI STARTUP IDEA ANALYZER")
    print("=" * 40)


def add_idea():
    name = input("Startup Idea Name: ")
    problem = input("Problem Being Solved: ")
    audience = input("Target Audience: ")

    market_size = int(
        input("Market Size (1-10): ")
    )

    competition = int(
        input("Competition Level (1-10): ")
    )

    development_cost = int(
        input("Development Cost (1-10): ")
    )

    idea = StartupIdea(
        name,
        problem,
        audience,
        market_size,
        competition,
        development_cost
    )

    ideas.append(idea)

    print("\nIdea added successfully!")


def view_ideas():
    if len(ideas) == 0:
        print("\nNo startup ideas found.")
        return

    for idea in ideas:
        idea.display()


def compare_ideas():
    if len(ideas) < 2:
        print("\nAdd at least 2 ideas first.")
        return

    best = max(
        ideas,
        key=lambda idea: idea.calculate_score()
    )

    print("\nBest Startup Idea:")
    best.display()


def menu():
    while True:
        print("\n1. Add Startup Idea")
        print("2. View Startup Ideas")
        print("3. Compare Ideas")
        print("4. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            add_idea()

        elif choice == "2":
            view_ideas()

        elif choice == "3":
            compare_ideas()

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")


def main():
    show_title()
    menu()


if __name__ == "__main__":
    main()



        