#int()
#the int() function can convert stings that represent whole counting numbers into integers and strip decimals to convert float numbers to integers

#int("1") = 1 the string representing the integer character "1", cast to a number
#int(5.1) = 5 the decimal (float), 5.1, truncated into a non-decimal (integer)
#int("5.1") = ValueError "5.1" isn't a string representation of integer, int() can cast only strings representing integer values

weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)


# cast to int at input
student_age = int(input('enter student age (integer): '))

age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)

calculation = 5 + 15 / 5 + 3 * 2 - 1
print(calculation)