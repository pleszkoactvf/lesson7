print('-' * 65)
print('<100th Birthday Program> ')
print()
print('Description: This program asks you for your current age abd tells you the year that you will turn 100.')
print()

x = input('What is your age today? ')
x = int(x)

birthyear = 2018 - x

y = birthyear + 100

print('You will turn 100 in the year ' + str(y))