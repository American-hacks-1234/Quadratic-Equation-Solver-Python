import math

def quadraticsolver(a, b, c):
  a=int(a)
  b=int(b)
  c=int(c)
  print(f"ORIGINAL: X = (-{b}±√({b}^2-4•{a}•{c}))÷(2•{a})")
  B=b*-1
  b=b*b
  f=2*a
  y=(b-4*a*c)
  print("")
  print(f"STEP 1: X = ({B}±√({y}))÷{f}")
  result=math.sqrt(y)
  print("")
  print(f"STEP 2: X = ({B}±{result})÷{f}")
  Z=B+result
  z=B+-result
  print("")
  print(f"STEP 3: X = {Z}÷{f}, {z}÷{f}")
  x0=Z/f
  x1=z/f
  print("")
  print(f"ANS: X = {x0}, {x1}")

quadraticsolver(input("a: "), input("b: ") ,input("c: "))
