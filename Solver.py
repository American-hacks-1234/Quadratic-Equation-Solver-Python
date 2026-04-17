import time
import math
def now_ts():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
LOGNAME="log"
def append_my_log(msg):
    try:
        with open(LOGNAME, "a", encoding="utf-8") as fh:
            fh.write(f"{now_ts()} - {msg}\n")
    except Exception:
        pass
msg="this is the log"
now_ts()
import math
def text(z):
  print(z)
a=input("A: ")
b=input("B: ")
c=input("C: ")
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
  text(f"STEP 3: {Z}/{f}, {z}/{f}")
  x0=Z/f
  x1=z/f
  text(f"ans: {x0}, {x1}")
  str(x0)
  str(x1)
  q=f"x=[{x0}, {x1}]"
  append_my_log(q)
quadraticsolver(a, b ,c)
