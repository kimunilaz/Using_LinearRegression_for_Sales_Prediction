

import matplotlib.pyplot as plt   # For plotting the regression graph



def get_data():
    print("\n" + "=" * 60)
    print("  SALES PREDICTION USING LINEAR REGRESSION")
    print("=" * 60)

    # --- Number of observations ---
    while True:
        try:
            n = int(input("\nEnter number of observations (data points): "))
            if n < 2:
                print(" At least 2 data points are required. Please try again.")
            else:
                break
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

    #  Collect x values (advertising budgets)
    print(f"\nEnter {n} Advertising Budget values (x), one per line:")
    x_values = []
    for i in range(n):
        while True:
            try:
                val = float(input(f"  x[{i + 1}]: $"))
                x_values.append(val)
                break
            except ValueError:
                print(" Invalid input. Please enter a numeric value.")

    # --- Collect y values (sales revenues) ---
    print(f"\nEnter {n} Sales Revenue values (y), one per line:")
    y_values = []
    for i in range(n):
        while True:
            try:
                val = float(input(f"  y[{i + 1}]: $"))
                y_values.append(val)
                break
            except ValueError:
                print(" Invalid input. Please enter a numeric value.")

    # --- New x value to predict ---
    print("\nEnter the Advertising Budget for which you want to predict Sales:")
    while True:
        try:
            x_predict = float(input("  Predict for x = $"))
            break
        except ValueError:
            print(" Invalid input. Please enter a numeric value.")

    return x_values, y_values, n, x_predict



def calculate_sums(x_values, y_values, n):
    sum_x  = 0   # Will accumulate Σx
    sum_y  = 0   # Will accumulate Σy
    sum_xy = 0   # Will accumulate Σxy
    sum_x2 = 0   # Will accumulate Σx²

    # Iterate through each data point and add contributions to each summation
    for i in range(n):
        x = x_values[i]   # Current x value
        y = y_values[i]   # Corresponding y value

        sum_x  += x          # Add x   to Σx
        sum_y  += y          # Add y   to Σy
        sum_xy += x * y      # Add x·y to Σxy
        sum_x2 += x * x      # Add x²  to Σx²

    return sum_x, sum_y, sum_xy, sum_x2



def calculate_slope(n, sum_x, sum_y, sum_xy, sum_x2):
    numerator   = (n * sum_xy) - (sum_x * sum_y)   # Top part of the formula
    denominator = (n * sum_x2) - (sum_x ** 2)       # Bottom part of the formula

    # Guard against division by zero (all x values identical → vertical line)
    if denominator == 0:
        raise ValueError("Cannot compute slope: all x values are identical.")

    m = numerator / denominator   # Final slope value
    return m



def calculate_intercept(n, sum_x, sum_y, m):
    c = (sum_y - (m * sum_x)) / n   # Apply the intercept formula
    return c



def predict(m, c, x_new):
    y_pred = m * x_new + c   # Straight-line equation: y = mx + c
    return y_pred



def display_summation_table(x_values, y_values, n):
    print("\n" + "-" * 58)
    print(f"  {'i':<4} {'x':>8} {'y':>10} {'xy':>12} {'x²':>12}")
    print("-" * 58)

    # Print each row of the table
    for i in range(n):
        x  = x_values[i]
        y  = y_values[i]
        xy = x * y          # Product of x and y
        x2 = x * x          # Square of x
        print(f"  {i+1:<4} {x:>8.2f} {y:>10.2f} {xy:>12.2f} {x2:>12.2f}")

    print("-" * 58)

    # Print column totals (the Σ row)
    sum_x  = sum(x_values)
    sum_y  = sum(y_values)
    sum_xy = sum(x_values[i] * y_values[i] for i in range(n))
    sum_x2 = sum(x * x for x in x_values)

    print(f"  {'Σ':<4} {sum_x:>8.2f} {sum_y:>10.2f} {sum_xy:>12.2f} {sum_x2:>12.2f}")
    print("-" * 58)



def plot_graph(x_values, y_values, m, c, x_predict, y_predict):
    # --- Build the regression line ---
    # We need two x values to draw a straight line; use slightly beyond
    # the data range so the line extends cleanly across the plot.
    x_min = min(x_values) - 20
    x_max = max(x_predict, max(x_values)) + 20

    # Generate evenly spaced x points for a smooth line
    line_x = [x_min + i * (x_max - x_min) / 200 for i in range(201)]
    line_y = [m * x + c for x in line_x]   # Compute y for each line x using y=mx+c

    # --- Create the figure and axes ---
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot 1: Original data points — blue filled circles with black edge
    ax.scatter(x_values, y_values,
               color='steelblue', edgecolors='navy', s=100, zorder=5,
               label='Observed Data Points')

    # Plot 2: Regression line — solid red line
    ax.plot(line_x, line_y,
            color='crimson', linewidth=2, linestyle='-',
            label=f'Regression Line:  y = {m:.4f}x + {c:.4f}')

    # Plot 3: Predicted point — green star, larger marker for visibility
    ax.scatter([x_predict], [y_predict],
               color='limegreen', edgecolors='darkgreen', s=250,
               marker='*', zorder=6,
               label=f'Predicted Point  ({x_predict:.0f}, {y_predict:.2f})')

    # Draw dashed reference lines from the predicted point to both axes
    ax.axvline(x=x_predict, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
    ax.axhline(y=y_predict, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)

    # Annotate the predicted point with its coordinates
    ax.annotate(f'  ({x_predict:.0f}, {y_predict:.2f})',
                xy=(x_predict, y_predict),
                fontsize=10, color='darkgreen',
                xytext=(x_predict + 5, y_predict + 30))

    # --- Labels, title, legend, grid ---
    ax.set_title('Linear Regression Analysis\nSales Prediction Based on Advertising Budget',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Advertising Budget ($)', fontsize=12)
    ax.set_ylabel('Sales Revenue ($)',       fontsize=12)
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()

    # Save graph as PNG (useful for the report / submission)
    plt.savefig('regression_graph.png', dpi=150, bbox_inches='tight')
    print("\n  Graph saved as 'regression_graph.png'")

    plt.show()   # Display interactive window



#  orchestrates all functions in order
def main():

    # --- Step 1: Collect user data ---
    x_values, y_values, n, x_predict = get_data()

    # --- Step 2: Compute summations ---
    sum_x, sum_y, sum_xy, sum_x2 = calculate_sums(x_values, y_values, n)

    # step 3: Show the working summation table
    print("\n\n  STEP 1 — SUMMATION TABLE")
    display_summation_table(x_values, y_values, n)

    #step 4: Echo the computed Σ values
    print(f"\n  Σx   = {sum_x:.2f}")
    print(f"  Σy   = {sum_y:.2f}")
    print(f"  Σxy  = {sum_xy:.2f}")
    print(f"  Σx²  = {sum_x2:.2f}")
    print(f"  n    = {n}")

    # Step 5: Calculate slope m
    m = calculate_slope(n, sum_x, sum_y, sum_xy, sum_x2)

    print(f"\n  STEP 2 — SLOPE (m)")
    print(f"  m = (n·Σxy − Σx·Σy) / (n·Σx² − (Σx)²)")
    print(f"  m = ({n}×{sum_xy:.2f} − {sum_x:.2f}×{sum_y:.2f})")
    print(f"      / ({n}×{sum_x2:.2f} − {sum_x:.2f}²)")
    print(f"  m = {m:.4f}")

    # Step 6: Calculate intercept c
    c = calculate_intercept(n, sum_x, sum_y, m)

    print(f"\n  STEP 3 — INTERCEPT (c)")
    print(f"  c = (Σy − m·Σx) / n")
    print(f"  c = ({sum_y:.2f} − {m:.4f}×{sum_x:.2f}) / {n}")
    print(f"  c = {c:.4f}")

    # Step 7: Display the regression equation
    sign = "+" if c >= 0 else "-"
    print(f"\n{'=' * 60}")
    print(f"  LINEAR REGRESSION EQUATION:")
    print(f"  y  =  {m:.4f}x  {sign}  {abs(c):.4f}")
    print(f"{'=' * 60}")

    # --- Step 8: Predict the new y value ---
    y_predict = predict(m, c, x_predict)

    print(f"\n  STEP 4 — PREDICTION")
    print(f"  For x = ${x_predict:.2f}:")
    print(f"  y = {m:.4f} × {x_predict:.2f} {sign} {abs(c):.4f}")
    print(f"\n{'=' * 60}")
    print(f"  PREDICTED SALES REVENUE  =  ${y_predict:.2f}")
    print(f"{'=' * 60}\n")

    # Step 9: Plot the graph
    plot_graph(x_values, y_values, m, c, x_predict, y_predict)


# Entry point — run main() only when this script is executed directly
if __name__ == "__main__":
    main()