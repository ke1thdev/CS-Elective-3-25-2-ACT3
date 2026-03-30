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
    count = _get_int("How many days/data points? ", minimum=2)
    day_labels = []
    sales_vals = []
    for i in range(count):
        label = input(f"Enter label for day {i + 1}: ").strip() or f"Day{i + 1}"
        sales = _get_float(f"Enter sales for {label}: ")
        day_labels.append(label)
        sales_vals.append(sales)
    return day_labels, sales_vals


def _trend_text(sales_vals):
    increasing = all(sales_vals[i] <= sales_vals[i + 1] for i in range(len(sales_vals) - 1))
    decreasing = all(sales_vals[i] >= sales_vals[i + 1] for i in range(len(sales_vals) - 1))
    if increasing:
        return "Consistent upward trend."
    if decreasing:
        return "Consistent downward trend."
    return "Fluctuating trend."


def main():
    print("Weekly Sales Bar Chart")
    use_custom = input("Do you want to input your own data? (Y/N): ").strip().lower()

    if use_custom == "y":
        days, sales = _collect_user_data()
    else:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        sales = [100, 150, 120, 180, 160]

    print("\nDataset")
    print(f"Days = {days}")
    print(f"Sales = {sales}")

    max_sales = max(sales)
    min_sales = min(sales)
    max_day = days[sales.index(max_sales)]
    min_day = days[sales.index(min_sales)]
    avg_sales = sum(sales) / len(sales)

    print("\nStatistics")
    print(f"Total sales: {sum(sales):.2f}")
    print(f"Average sales: {avg_sales:.2f}")
    print(f"Highest sales: {max_sales} on {max_day}")
    print(f"Lowest sales: {min_sales} on {min_day}")

    trend = _trend_text(sales)

    print("\nInterpretation")
    print(f"1. Highest sales day: {max_day}")
    print(f"2. Lowest sales day: {min_day}")
    print(f"3. Trend: {trend}")
    if trend == "Consistent upward trend.":
        print("4. If the increase continues, next week may exceed this week's highest sales.")
    else:
        print("4. If sales begin increasing steadily, next week could show higher overall sales.")

    rotation = 30 if any(len(label) > 3 for label in days) else 0

    plt.bar(days, sales, color="skyblue", edgecolor="black")
    plt.title("Weekly Sales")
    plt.xlabel("Day")
    plt.ylabel("Sales")
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
