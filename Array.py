def process_scores():
    scores = list(map(int, input("Enter scores separated by commas: ").split(",")))
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)
    print("Scores:", scores)
    print("Total Score:", total)
    print("Average Score:", round(average, 2))
    print("Maximum Score:", maximum)
    print("Minimum Score:", minimum)
if __name__ == "__main__":
    process_scores()
