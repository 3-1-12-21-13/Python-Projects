# CUSTOM TIMES TABLE

# The number you want to multiply goes here e.g - 7.
num = 21

# The amount of multiples you want goes here e.g - 10.
mult = 100

# A list which creates part of the statement which is printed.
filler = [f"multiplied by {i} is" for i in range(1,mult+1)]

# An empty list which stores the multiples for future use.
mult_num = []

# Another empty list which stores all the numbers which aren't multiples up to the last multiple.
not_mult_num = []

print("\nCustom Times Table\n")
# The loop starts by creating a range which counts between 1 and the last multiple.
for i in range(1,num*mult+1):
    if i in range(num,(num*mult+1),num): # It then checks if the number is the same as a multiple and prints it if it is. 
        print(f"{num} {filler.pop(0)} {i}.")
        mult_num.append(i)
    else: # If not, the number gets added to the not_mult_num list by exclusion.
        not_mult_num.append(i)
print("\n")