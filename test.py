import random
from Modulo12 import Modulo12


def withParentheses(n):
  if n < 0:
    return f"({n})"
  else:
    return f"{n}"


def main():
  x = random.randint(-100, 100)
  y = random.randint(-100, 100)
  xf = withParentheses(x)
  yf = withParentheses(y)
  xmod = Modulo12(x)
  ymod = Modulo12(y)
  print(f"{xf} + {yf} = {xmod.representative} + {ymod.representative} =",
        xmod + ymod)
  print("xmod + y =", xmod + y)
  print("x + ymod =", x + ymod)
  print("+xmod =", +xmod)
  print("+ymod =", +ymod)
  print("-xmod =", -xmod)
  print("-ymod =", -ymod)
  print("xmod - ymod =", xmod - ymod)
  print("xmod - y =", xmod - y)
  print("x - ymod =", x - ymod)
  # Product between instances:
  print("xmod * ymod =", xmod * ymod)
  # Product between instance and integer:
  print("xmod * y =", xmod * y)
  print("x * ymod =", x * ymod)
  # Invertible elements:
  print("Is xmod invertible?", xmod.is_invertible())
  print("inverse of xmod:", xmod.inverse())
  print("Is ymod invertible?", ymod.is_invertible())
  print("inverse of ymod:", ymod.inverse())
  # True division:
  print("xmod / ymod =", xmod / ymod)
  print("xmod / y =", xmod / ymod)
  print("x / ymod =", xmod / ymod)
  # Divides:
  print("Does xmod divide ymod?", xmod.divides(ymod))
  # Power:
  print("xmod ** y =", xmod ** y)
  # Absolute value:
  print("abs(xmod) =", abs(xmod))
  print("abs(-xmod) =", abs(-xmod))


if __name__ == '__main__':
  main()
