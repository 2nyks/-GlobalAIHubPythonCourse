n = int(input("Please enter a single digit number: "))
list_of_even_numbers = []
for i in range(n):
    if (i%2) == 0:
        list_of_even_numbers.append(i)
        i+=1
    else:
        continue

print(list_of_even_numbers)

