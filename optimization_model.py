# Import necessary libraries
from pulp import LpMaximize, LpProblem, LpVariable, value
# Create an LP Maximization problem
model = LpProblem("Maximize_Profit", LpMaximize)
# Define decision variables (units of P1 and P2)
x1 = LpVariable("P1", lowBound=0, cat='Continuous')  # Product P1
x2 = LpVariable("P2", lowBound=0, cat='Continuous')  # Product P2
# Objective function (Maximize profit)
model += 50 * x1 + 40 * x2, "Total_Profit"
# Constraints
model += 2 * x1 + 3 * x2 <= 100, "Labor_Hours"      # Labor constraint
model += 4 * x1 + 2 * x2 <= 120, "Raw_Materials"    # Raw material constraint
# Solve the optimization problem
model.solve()
# Display results
print("Optimal production of P1:", x1.varValue)
print("Optimal production of P2:", x2.varValue)
print("Maximum Profit:", value(model.objective))