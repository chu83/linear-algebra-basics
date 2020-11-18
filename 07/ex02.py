#편미분(Partial Differentiation)

def f(x1):
    return 3.**2 + x1**2

def numerical_diff(f, x1):
    h = 1.0e-4
    return (f(x1 + h) - f(x1-h)) / (2*h)

def analytic_diff(x1):
    return 2*x1

#(x0, x1) = (3,4)
print(f'Numerical Partial Differentiation Value : {numerical_diff(f, 4)}')
print(f'Analytic Differentiation Value : {analytic_diff(4)}')

#(x0, x1) = (1,4)
print(f'Numerical Partial Differentiation Value : {numerical_diff(f, 1)}')
print(f'Analytic Differentiation Value : {analytic_diff(1)}')

#(x0, x1) = (2,4)
print(f'Numerical Partial Differentiation Value : {numerical_diff(f, 2)}')
print(f'Analytic Differentiation Value : {analytic_diff(2)}')
