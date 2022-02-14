list_1 = [1,2,3,5,7,8,10,12,13,14,15,16,21,22,23,24,26,30,31,32,33,43,44,46,47,]

#Opdracht-1 #Show how many numbers there are in a list.
print (len(list_1))

#Opdracht-2 # Show all even numbers in a list.

numbers_even = 0
for numbers in list_1:
    if numbers % 2==0:
        numbers_even+=1
print(numbers_even)

#Opdracht-3 # Show all even numbers in a list.

for numbers in list_1:
    if numbers % 2==0:
        print(numbers)

#Opdracht-4 # Show all uneven numbers in a list.

for numbers in list_1:
    if numbers % 2 != 0:
        print(numbers)

#Opdracht-5 #Show all boring numbers.

for index, value in enumerate(list_1):
    if index == list_1[index]:
        print(value)
#trying to work on it
