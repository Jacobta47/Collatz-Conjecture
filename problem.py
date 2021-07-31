print("Collatz Conjecture")
f = open('collatz-output.txt', 'a')
amount = float(input('Principal Amount? '))
f.write('\n' + str(amount) + ' ')

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

f.close