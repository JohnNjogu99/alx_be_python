#Prompt the user to input their current age
current_age = input("How old are you? ")

int(current_age)  #Convert the input to an integer
current_age = int(current_age)  #Reassign the converted value back to current_age

#Calculate the age in 2050
years_to_add = 2050 - 2023 # Assuming the current year is 2023
furture_age = current_age + years_to_add
#Print the result
print(f"In 2050, you will be {furture_age} years old.")
