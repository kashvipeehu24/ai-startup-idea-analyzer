class StartupIdea:
    def __init__(self, name, problem, audience):
        self.name = name
        self.problem = problem
        self.audience = audience

    def display(self):
        print("\n" + "=" * 40)
        print("IDEA SUMMARY")
        print("=" * 40)
        print(f"Idea Name      : {self.name}")
        print(f"Problem        : {self.problem}")
        print(f"Target Audience: {self.audience}")
        print("=" * 40)