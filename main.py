import random


"""Generate two factors (x - m) and (x - n)"""
def generate_factors():
    m = random.randint(-10, 10)
    n = random.randint(-10, 10)
    return m, n

"""Create a quadratic equation from the factors (x - m) and (x - n)"""
def create_quadratic(m, n):
    a = 1  # Coefficient of x^2 is always 1 in this case
    b = -m - n
    c = m * n
    return a, b, c

"""Display the quadratic equation in a readable format"""
def display_equation(a, b, c):
    
    equation = f"{a}x^2 "
    equation += f"+ {b}x " if b >= 0 else f"- {-b}x "
    equation += f"+ {c} = 0" if c >= 0 else f"- {-c} = 0"
    return equation

# Generate random factors
m, n = generate_factors()

# Create a quadratic equation from these factors
a, b, c = create_quadratic(m, n)

# Display the equation
equation = display_equation(a, b, c)
print(equation)
