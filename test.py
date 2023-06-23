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
  print("-xmod =", -xmod)
  print("-ymod =", -ymod)
  print(f"{xf} * {yf} = {xmod.getRemainder()} * {ymod.getRemainder()} =",
        xmod * ymod)


if __name__ == '__main__':
  main()
