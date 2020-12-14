#Lior Ohana - 206101891
#Talia Amsalem - 2070746918 
def bisection_method(func, low, up, e, max_iterations, real_root=None):
    if func(low) * func(up) > 0:
        print("Bisection method will fail.")
    else:
        mid = (low + up) / 2.0
        iterations = 0
        while (up - low) / 2.0 > e and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0},".format(iterations)
            if func(mid) == 0:
                return c
            elif func(low) * func(mid) < 0:
                up = mid
            else:
                lower = mid
            mid = (low + up) / 2.0
            current_iteration_print += " Current root approximation: {0},".format(mid)
            if real_root != None:
                current_iteration_print += " Difference from the real root: {0}".format(abs(real_root - mid))
            print(current_iteration_print)
            iterations = iterations + 1
        if real_root != None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(mid, abs(real_root - mid)))
        else:
            print("Final approximation: {0}".format(mid))
        return mid


def fun(x):
    return x * x * x - x * x + 2


bisection_method(fun, -2.6, -0.1, 0.01, 30, 0)