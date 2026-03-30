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


def _constant_slopes(x_vals, y_vals, tol=1e-9):
    slopes = []
    for i in range(1, len(x_vals)):
        dx = x_vals[i] - x_vals[i - 1]
        if dx == 0:
            return False
        slopes.append((y_vals[i] - y_vals[i - 1]) / dx)
    first = slopes[0]
    return all(abs(s - first) <= tol for s in slopes)


def _ratio_pattern(y_vals, tol=1e-9):
    ratios = []
    for i in range(1, len(y_vals)):
        if y_vals[i - 1] == 0:
            return False
        ratios.append(y_vals[i] / y_vals[i - 1])
    first = ratios[0]
    return all(abs(r - first) <= tol for r in ratios)


def main():
    print("Decreasing Pattern Analysis")
    use_custom = input("Do you want to input your own data? (Y/N): ").strip().lower()

    if use_custom == "y":
        x, y = _collect_user_data()
    else:
        x = [0, 1, 2, 3, 4]
        y = [16, 8, 4, 2, 1]

    print("\nDataset")
    print(f"x = {x}")
    print(f"y = {y}")

    print("\nStatistics")
    print(f"Min y: {min(y)}")
    print(f"Max y: {max(y)}")
    print(f"Average y: {sum(y) / len(y):.4f}")

    is_linear = _constant_slopes(x, y)
    is_exponential_like = _ratio_pattern(y)
    decreasing = all(y[i] > y[i + 1] for i in range(len(y) - 1))

    print("\nInterpretation")
    print(f"1. Linear decrease: {'Yes' if is_linear else 'No'}")
    if is_exponential_like:
        print("2. Pattern: exponential-like decay (values drop by a constant ratio).")
    elif is_linear:
        print("2. Pattern: linear decrease (constant difference).")
    else:
        print("2. Pattern: decreasing but not strictly linear or exponential.")
    if is_linear:
        print("3. Rate of decrease: constant.")
    else:
        print("3. Rate of decrease: not constant.")
    if decreasing and is_exponential_like:
        print("4. As x increases, y would likely keep decreasing toward 0.")
    elif decreasing:
        print("4. As x increases, y would likely keep decreasing.")
    else:
        print("4. As x increases, the behavior may change or level off.")

    plt.plot(x, y, marker="o")
    plt.title("Decreasing Pattern")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
