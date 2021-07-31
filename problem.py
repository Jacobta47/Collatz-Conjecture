print("Collatz Conjecture")
amount = float(input('Principal Amount? '))

while amount > 1:

    if (amount % 2) != 0:
        amount = ((3 * amount) + 1)
        print(amount)

    elif (amount % 2) == 0:
        amount = (amount / 2)
        print(amount)

    else:
        print('Error')

