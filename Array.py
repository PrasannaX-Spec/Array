def process_scores():
    # Accept scores from user input (comma-separated)
    scores = list(map(int, input("Enter scores separated by commas: ").split(",")))

    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Total Score:", total)
    print("Average Score:", round(average, 2))

if __name__ == "__main__":
    process_scores()