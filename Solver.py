import math
def In(z):
  global out
  out=input(z)
  return out
def text(z):
  print(z)
a=In("A: ")
b=In("B: ")
c=In("C: ")
def quadraticsolver(a, b, c):
  a=int(a)
  b=int(b)
  c=int(c)
  text(f"ORIGINAL: x=(-{b}±sqrt({b}^2-4*{a}*{c}))/(2*{a})")
  B=b*-1
  b=b*b
  f=2*a
  y=(b-4*a*c)
  text(f"STEP 1: x=({B}±sqrt({y}))/{f}")
  result=math.sqrt(y)
  text(f"STEP 2: ({B}±{result})/{f}")
  Z=B+result
  z=B+-result
  text(f"step 3: {Z}/{f} and {z}/{f}")
  x0=Z/f
  x1=z/f
  text(f"ans: {x0} and {x1}")
quadraticsolver(a, b ,c)
