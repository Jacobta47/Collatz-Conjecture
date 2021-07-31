print("Collatz Conjecture")
f = open('collatz-output.txt', 'a')
amount = float(input('Principal Amount? '))
fun = 

if (amount >= 1):
    f.write('\n' + str(amount) + ' ')

else: 
    f.write('\n' + 'UNKNOWN NUMBER')
    exit()

# If amount is set to '1' or more, perform Collatz Conjecture Equation
while amount > 1:

    if (amount % 2) != 0:
        amount = ((3 * amount) + 1)
        # print(amount)
        f.write(str(amount) + ' ')

    elif (amount % 2) == 0:
        amount = (amount / 2)
        # print(amount)
        f.write(str(amount) + ' ')

    else:
        print('Error')
        f.write(' ! Error !  ')

# When (amount) drops to '1', add '1'
if (amount == 1):
    amount += 1

# set limit for amount to reach
if (amount == 9999999999999999999999999999999999999999999):
    exit()

f.close