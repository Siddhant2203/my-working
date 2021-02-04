#Exercise: Array DataStructure

'''QUESTION 1
Let us say your expense for every month are listed below,
January - 2200 February - 2350 March - 2600 April - 2130 May - 2190'''

# Create a list to store these monthly expenses and using that find out
# monthly expense of January,February,March,April,May respectively
expense = [2200,2350,2600,2130,2190]
print(expense)

#1. In Feb, how many dollars you spent extra compare to January?

extra_expense = expense[1] - expense[0]
print(extra_expense)

#2. Find out your total expense in first quarter (first three months) of the year.

quarter_expense = expense[0] + expense[1] + expense[2]
print(quarter_expense)

#3. Find out if you spent exactly 2000 dollars in any month

for i in expense:
    if i==2000:
        print(True)
    else:
        print(False)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print("After end of june,total expenses are",expense)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expense[3] = expense[3] - 200
print("New expense after returning 200$ in april:",expense)

'''QUESTION 2

You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

Using this find out'''

heros = ['spider man','thor','hulk','iron man','captain america']
print(heros)

# 1. Length of the list

print(len(heros))

# 2. Add 'black panther' at the end of this list

heros.append('black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.

heros[1:3] = ['doctor strange']
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

'''QUESTION 3

Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function'''

n = int(input("Enter a number till where you want to print odd numbers:"))

odd_numbers = []
for i in range(n):
    if i%2 ==1:
        odd_numbers.append(i)

print(odd_numbers)