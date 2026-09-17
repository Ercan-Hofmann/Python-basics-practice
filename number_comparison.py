# Ask the user to enter their name
name = input("What is your name")
# remove extra space and capitalize the first letter of each word
name = name.strip( ).title( )

# ask the user to enter two number
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Compare the two number using if, elif, and else
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}. ")

elif first_number < second_number:
    print(f"{first_number} is less than {second_number}. ")

else:
    print("The two number are equal. ")

# Find the smaller and larger number
smal_number = min(first_number, second_number)
large_number = max(first_number, second_number)

# Use a for loop to print every number from the smallr to the larger number
print("Numbers in the range: ")

for i in range(smal_number, large_number + 1):
    print(i)

# Create a variable to store the total
total = 0
# Add each number in the range to the total
for i in range(smal_number, large_number + 1):
    total += i

#Display the final total
print(f"The total is: {total} ")
print(f"Thank you , {name} , for using the program! ")