import numpy as np
import matplotlib.pyplot as plt


def _get_int(prompt, minimum=1):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        return value


def _get_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def _collect_user_data():
    count = _get_int("How many scores? ", minimum=2)
    scores = []
    for i in range(count):
        scores.append(_get_float(f"Enter score #{i + 1}: "))
    return np.array(scores, dtype=float)


def _skew_text(mean_val, median_val, tol=1e-9):
    if abs(mean_val - median_val) <= tol:
        return "approximately symmetric"
    if mean_val > median_val:
        return "right-skewed"
    return "left-skewed"


def main():
    print("Score Distribution Histogram")
    use_custom = input("Do you want to input your own data? (Y/N): ").strip().lower()

    if use_custom == "y":
        data = _collect_user_data()
    else:
        data = np.array([5, 6, 7, 7, 8, 9, 10, 10, 10, 11])

    print("\nDataset")
    print(f"Scores = {data.tolist()}")

    mean_val = float(np.mean(data))
    median_val = float(np.median(data))
    min_val = float(np.min(data))
    max_val = float(np.max(data))

    counts, edges = np.histogram(data, bins=5)
    max_bin_index = int(np.argmax(counts))
    bin_center = (edges[max_bin_index] + edges[max_bin_index + 1]) / 2

    print("\nStatistics")
    print(f"Mean score: {mean_val:.2f}")
    print(f"Median score: {median_val:.2f}")
    print(f"Min score: {min_val}")
    print(f"Max score: {max_val}")

    skew_text = _skew_text(mean_val, median_val)

    print("\nInterpretation")
    print(f"1. Most students are concentrated around scores near {bin_center:.2f}.")
    print(f"2. The distribution is {skew_text}.")
    print("3. The tallest bar represents the score range with the most students.")
    if mean_val >= 8:
        print("4. Overall performance looks strong, with scores clustered in the higher range.")
    elif mean_val >= 6:
        print("4. Overall performance looks average, with a mix of low and high scores.")
    else:
        print("4. Overall performance looks low, with many scores in the lower range.")

    plt.hist(data, bins=5, color="lightgreen", edgecolor="black")
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
