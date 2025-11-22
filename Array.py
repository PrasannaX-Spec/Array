import sys

def process_scores():
    # If scores passed as command-line argument, use them
    if len(sys.argv) > 1:
        scores = list(map(int, sys.argv[1].split(",")))
    else:
        # Fallback only if running manually
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
