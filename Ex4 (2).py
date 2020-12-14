#Lior Ohana - 206101891
#Talia Amsalem - 2070746918

def func(x):
    return x * x * x - x * x + 2


def bisection_method(x0, x1, e):
    step = 1

    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, func(x2)))

        if func(x0) * func(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(func(x2)) > e

    return float(x2)


def find_roots(x0, x1, error):
    # find roots with the function
    roots = bisection_method(x0, x1, error)
    # find roots with the derivative
    roots_der = bisection_method(x0, x1, error)
    for i in roots_der:
        if func(i) == 0:
            roots.append(i)
    # Check x = 0
    if func(0) == 0:
        roots.append(0)
    print(roots)


x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

if func(x0) * func(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection_method(x0, x1, e)

#find_roots(x0, x1, e)
