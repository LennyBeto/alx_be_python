# finance_calculator.py

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output Results
print(f"Your monthly savings are: {monthly_savings}.")
print(f"Your projected annual savings after including interest are: {projected_savings}.")
