import math
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
    count = _get_int("How many data points? ", minimum=2)
    x_vals = []
    y_vals = []
    for i in range(count):
        x_vals.append(_get_float(f"Enter x[{i + 1}]: "))
        y_vals.append(_get_float(f"Enter y[{i + 1}]: "))
    return x_vals, y_vals


def _compute_stats(x_vals, y_vals):
    n = len(x_vals)
    mean_x = sum(x_vals) / n
    mean_y = sum(y_vals) / n

    var_x = sum((x - mean_x) ** 2 for x in x_vals)
    var_y = sum((y - mean_y) ** 2 for y in y_vals)
    cov_xy = sum((x_vals[i] - mean_x) * (y_vals[i] - mean_y) for i in range(n))

    if var_x == 0:
        slope = None
        intercept = None
    else:
        slope = cov_xy / var_x
        intercept = mean_y - slope * mean_x

    if var_x == 0 or var_y == 0:
        corr = None
    else:
        corr = cov_xy / math.sqrt(var_x * var_y)

    constant_growth = False
    if n >= 2:
        slopes = []
        for i in range(1, n):
            dx = x_vals[i] - x_vals[i - 1]
            if dx == 0:
                slopes.append(None)
            else:
                slopes.append((y_vals[i] - y_vals[i - 1]) / dx)
        if all(s is not None for s in slopes):
            first = slopes[0]
            constant_growth = all(abs(s - first) <= 1e-9 for s in slopes)

    return {
        "mean_x": mean_x,
        "mean_y": mean_y,
        "min_x": min(x_vals),
        "max_x": max(x_vals),
        "min_y": min(y_vals),
        "max_y": max(y_vals),
        "slope": slope,
        "intercept": intercept,
        "corr": corr,
        "constant_growth": constant_growth,
    }


def _relationship_text(stats):
    slope = stats["slope"]
    corr = stats["corr"]
    if slope is None:
        return "No defined relationship (all x values are the same)."
    if corr is None:
        return "Relationship is unclear (insufficient variation in data)."
    if abs(corr) >= 0.95:
        return "Strong linear relationship."
    if abs(corr) >= 0.7:
        return "Moderate linear relationship."
    return "Weak or non-linear relationship."


def main():
    print("Linear Growth Visualization")
    use_custom = input("Do you want to input your own data? (Y/N): ").strip().lower()

    if use_custom == "y":
        x, y = _collect_user_data()
    else:
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

    print("\nDataset")
    print(f"x = {x}")
    print(f"y = {y}")

    stats = _compute_stats(x, y)

    print("\nStatistics")
    print(f"Mean x: {stats['mean_x']:.4f}")
    print(f"Mean y: {stats['mean_y']:.4f}")
    print(f"Min x: {stats['min_x']}")
    print(f"Max x: {stats['max_x']}")
    print(f"Min y: {stats['min_y']}")
    print(f"Max y: {stats['max_y']}")
    if stats["slope"] is None:
        print("Slope: undefined (all x values are the same)")
    else:
        print(f"Slope (best-fit): {stats['slope']:.4f}")

    print("\nInterpretation")
    print(f"1. Relationship: {_relationship_text(stats)}")
    if stats["constant_growth"]:
        print("2. Growth: constant (rate does not change).")
    else:
        print("2. Growth: not constant (rate changes).")
    if stats["slope"] is None:
        print("3. Slope: undefined (cannot compute with identical x values).")
        print("4. If x = 0: undefined (no valid line).")
    else:
        print(f"3. Slope represents the change in y per 1 unit increase in x: {stats['slope']:.4f}")
        print(f"4. If x = 0, y would be {stats['intercept']:.4f}")

    plt.plot(x, y, marker="o")
    plt.title("Linear Growth")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
