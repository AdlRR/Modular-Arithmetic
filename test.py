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
  print(f"{xf} + {yf} = {xmod.getRemainder()} + {ymod.getRemainder()} =",
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
  print(f"{xf} * {yf} = {xmod.getRemainder()} * {ymod.getRemainder()} =",
        xmod * ymod)
  # Power with positive exponent:
  print("xmod ** abs(y) =", xmod ** abs(y))
  # Power with negative exponent:
  try:
    print("xmod ** -abs(y) =", end=' ')
    print(xmod ** -abs(y))
  except NotImplementedError as error:
    print(error)
  # Absolute value:
  print("abs(xmod) =", abs(xmod))
  print("abs(-xmod) =", abs(-xmod))


if __name__ == '__main__':
  main()
