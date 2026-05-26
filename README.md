# Using_LinearRegression_for_Sales_Prediction
A Python implementation of Linear Regression that calculates the regression equation manually, predicts future values, and visualizes the relationship between variables using graphs.
Sales Prediction Using Linear Regression

A Python implementation of Linear Regression from mathematical first principles without using machine learning libraries such as scikit-learn or statsmodels.

This project demonstrates how mathematics can be converted directly into working Python code to model relationships between variables and make predictions from historical data.

Project Overview

The program predicts Sales Revenue based on Advertising Budget using the Linear Regression equation:

y = mx + c

Where:

y = Predicted Sales Revenue
x = Advertising Budget
m = Slope of the regression line
c = Intercept

The project manually computes:

Σx
Σy
Σxy
Σx²
Slope (m)
Intercept (c)

using the Least Squares Method.

Features

Manual Linear Regression implementation
No machine learning libraries used
User input validation
Automatic summation table generation
Step-by-step mathematical calculations
Sales prediction for new advertising budgets
Graph plotting using Matplotlib
Modular function-based design
Saves regression graph as PNG image
Mathematical Formulas
Slope Formula

m=
n∑x
2
−(∑x)
2
n∑xy−(∑x)(∑y)
	​


Intercept Formula

c=
n
∑y−m∑x
	​


Prediction Formula

y=mx+c

Technologies Used
Python 3.x
Matplotlib
Project Structure
linear-regression-sales-prediction/
│
├── main.py
├── regression_graph.png
├── README.md

Installation

1. Clone the Repository
git clone https://github.com/your-username/linear-regression-sales-prediction.git
2. Navigate into the Project Folder
cd linear-regression-sales-prediction
3. Install Required Library
pip install matplotlib
Running the Program

Run the Python file:

python main.py
Example Dataset
Advertising Budget ($)	Sales Revenue ($)
100	1200
150	1500
200	1800
250	2100
300	2500
Example Output
LINEAR REGRESSION EQUATION:
y = 6.4000x + 540.0000

PREDICTED SALES REVENUE = $2780.00

For an advertising budget of $350, the predicted sales revenue is:

$2780.00
Graph Output

The program generates a graph showing:

Original data points
Regression line
Predicted point

The graph is automatically saved as:

regression_graph.png
Program Functions
Function	Purpose
get_data()	Collect user input
calculate_sums()	Compute Σ values
calculate_slope()	Compute slope (m)
calculate_intercept()	Compute intercept (c)
predict()	Predict new y value
display_summation_table()	Display working table
plot_graph()	Plot regression graph
