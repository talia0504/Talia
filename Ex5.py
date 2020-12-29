# name: lior ohana Id:206101891
# name: talia amsalem Id:207074691


def Newton_Raphson(func, deriv, x, tolerence, max_iterations, real_root=None):
    if deriv(x) == 0:
        print("Newton-Raphson method will fail.")
        return None
    else:
        iterations = 1
        while abs(func(x) / deriv(x)) >= tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            if func(x) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(x))
                return x
            x = x - func(x) / deriv(x)
            if deriv(x) == 0:
                print("Newton-Raphson method will fail.")
                return None
            current_iteration_print += ", Current root approximation: {0}".format(x)
            if real_root is not None:
                current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - x))
            iterations = iterations + 1
            print(current_iteration_print)

        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(x, abs(real_root - x)))
        else:
            print("Final approximation: {0}".format(x))
        return x


def func(x):
    return x ** 3 - 1


def df1(x):
    return 3 * (x ** 2)


def secant_method(func, lower, upper, tolerance, max_iterations, real_root=None):
    if func(lower) * func(upper) >= 0:
        print("Secant method will fail.")
        return None
    else:
        iterations = 1
        while abs(upper - lower) > tolerance and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            next_point = upper - (func(upper) * (upper - lower)) / (func(upper) - func(lower))
            if func(next_point) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(next_point))
                return next_point
            lower = upper
            upper = next_point
            current_iteration_print += ", Current root approximation: {0}".format(next_point)
            if real_root is not None:
                current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - next_point))
            iterations = iterations + 1
            print(current_iteration_print)

        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(next_point,
                                                                                        abs(real_root - next_point)))
        else:
            print("Final approximation: {0}".format(next_point))
        return next_point


def f1(x):
    return x ** 2 - 20


def f2(x):
    return x ** 3 - x ** 2 - 1


print(Newton_Raphson(func, df1, 1.5, 0.001, 20, 1))

print(secant_method(f1, 3, 5, 0.001, 20, 20 ** 0.5))
print(secant_method(f2, 1, 2, 0.001, 20, 1.4655712318767682))
