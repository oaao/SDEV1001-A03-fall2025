"""
Common debugger commands:

  n - run {n}ext line of code
  s - {s}tep into a function call (or run next line if there's no function call)
  c - continue running code (until EOF or next breakpoint)
  l - {l}ist surrounding lines of code
  p - {p}rint a specific variable, e.g. 'p x', 'p add', etc.
  q - {q}uit the debugger

  While at a breakpoint, you can also just type in the name of a variable:
    (Pdb) x
    10

  You can also *set* a variable to a different value:
    (Pdb) x = 20
    (Pdb) n       # run next line

"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


x = 10
y = 5

breakpoint()

result = add(x, y)
print(f"The result is: {result}")


