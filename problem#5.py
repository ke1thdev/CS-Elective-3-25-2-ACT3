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
    start = _get_float("Enter x start: ")
    end = _get_float("Enter x end: ")
    if end <= start:
        print("End must be greater than start. Using default range 0 to 10.")
        return np.linspace(0, 10, 100)
    points = _get_int("How many points? ", minimum=2)
    return np.linspace(start, end, points)


def main():
    print("Function Comparison (Linear vs Quadratic)")
    use_custom = input("Do you want to input your own x-range? (Y/N): ").strip().lower()

    if use_custom == "y":
        x = _collect_user_data()
    else:
        x = np.linspace(0, 10, 100)

    y1 = x
    y2 = x ** 2

    print("\nDataset (sample)")
    print(f"x[0:5] = {x[:5].round(3).tolist()}")
    print(f"y1[0:5] = {y1[:5].round(3).tolist()}")
    print(f"y2[0:5] = {y2[:5].round(3).tolist()}")

    max_x = float(np.max(x))
    max_y1 = float(np.max(y1))
    max_y2 = float(np.max(y2))

    print("\nStatistics")
    print(f"Max x: {max_x:.2f}")
    print(f"Max y1 (linear): {max_y1:.2f}")
    print(f"Max y2 (quadratic): {max_y2:.2f}")

    intersections = []
    if np.min(x) <= 0 <= np.max(x):
        intersections.append(0.0)
    if np.min(x) <= 1 <= np.max(x):
        intersections.append(1.0)

    significant_x = None
    for value in x:
        if value != 0 and (value ** 2) >= 2 * value:
            significant_x = float(value)
            break

    print("\nInterpretation")
    print("1. The quadratic function grows faster than the linear function as x increases.")
    if intersections:
        points = ", ".join(f"x = {pt:.2f}" for pt in intersections)
        print(f"2. Yes, they intersect at {points}.")
    else:
        print("2. They do not intersect within the chosen x-range.")
    if significant_x is not None:
        print(f"3. Quadratic growth becomes noticeably larger around x ≈ {significant_x:.2f}.")
    else:
        print("3. Quadratic growth does not become significantly larger in this range.")
    print("4. Quadratic growth appears in real life with area growth or distance under constant acceleration.")

    plt.plot(x, y1, label="Linear (y = x)")
    plt.plot(x, y2, label="Quadratic (y = x^2)")
    plt.title("Linear vs Quadratic Growth")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
