class StartupIdea:
    def __init__(
        self,
        name,
        problem,
        audience,
        market_size,
        competition,
        development_cost
    ):
        self.name = name
        self.problem = problem
        self.audience = audience
        self.market_size = market_size
        self.competition = competition
        self.development_cost = development_cost

    def calculate_risk(self):
        return self.competition + self.development_cost

    def calculate_profit(self):
        return self.market_size - self.competition

    def calculate_score(self):
        return (
            self.market_size * 2
            - self.competition
            - self.development_cost
        )

    def display(self):
        print("\n" + "=" * 40)
        print(f"Idea: {self.name}")
        print(f"Problem: {self.problem}")
        print(f"Audience: {self.audience}")
        print(f"Market Size: {self.market_size}")
        print(f"Competition: {self.competition}")
        print(f"Development Cost: {self.development_cost}")
        print(f"Risk Score: {self.calculate_risk()}")
        print(f"Profit Potential: {self.calculate_profit()}")
        print(f"Overall Score: {self.calculate_score()}")
        print("=" * 40)