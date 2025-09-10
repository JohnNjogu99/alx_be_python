#Prompt the user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

#Prompt total monthly expenses
total_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Step 3: Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Step 4: Display the results
print(f"Your monthly savings are: ${int(monthly_savings)}")
print(f"Your projected savings after one year (with 5% interest) are: ${int(projected_savings)}")