def show_title():
    print("\n" + "=" * 40)
    print("      AI STARTUP IDEA ANALYZER")
    print("=" * 40)


def collect_idea():
    idea_name = input("\nStartup Idea Name: ")
    problem = input("Problem Being Solved: ")
    audience = input("Target Audience: ")

    print("\n" + "=" * 40)
    print("IDEA SUMMARY")
    print("=" * 40)
    print(f"Idea Name      : {idea_name}")
    print(f"Problem        : {problem}")
    print(f"Target Audience: {audience}")
    print("=" * 40)


def main():
    show_title()
    collect_idea()


if __name__ == "__main__":
    main()