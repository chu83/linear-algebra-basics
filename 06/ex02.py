#수치미분(Numerical Differentiation) vs 해석미분(Analytic Differentiation)

def f(x):
    return 20*(x-2)**2+500

def analytic_diff(x):
    return 40 * x - 80

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) -  f(x) )/h

print(f'Nuemrical Differentiation Value : {numerical_diff(f, 5)}')
print(f'Analytic Differentiation Vlaue : {analytic_diff(5)}')