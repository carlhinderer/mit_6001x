def exhaustive_cube_root():
    x = get_int_from_user()
    ans = 0

    while ans**3 < abs(x):
        ans += 1

    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print('Cube root of', x, 'is', ans)


def bisection_square_root():
    x = get_int_from_user()
    epsilon = 0.01
    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0

    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2

    print('num_guesses:', num_guesses)
    print(ans, 'is close to the square root of', x)


def newtons_method_square_root():
    epsilon = 0.01
    num_guesses = 0
    k = get_int_from_user()
    guess = k / 2.0

    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess**2) - k) / (2 * guess))
        num_guesses += 1

    print('num_guesses:', num_guesses)
    print('Square root of', k, 'is about', guess)


def get_int_from_user():
    return int(input('Enter an integer: '))
