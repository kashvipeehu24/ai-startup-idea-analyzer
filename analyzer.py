def calculate_average_score(ideas):
    if len(ideas) == 0:
        return 0

    total = 0

    for idea in ideas:
        total += idea.calculate_score()

    return total / len(ideas)


def find_best_idea(ideas):
    if len(ideas) == 0:
        return None

    return max(
        ideas,
        key=lambda idea: idea.calculate_score()
    )