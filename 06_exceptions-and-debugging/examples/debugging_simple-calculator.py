"""
Common debugger commands:

  n - run {n}ext line of code
  s - {s}tep into a function call (or run next line if there's no function call)
  c - continue running code (until EOF or next breakpoint)
  l - {l}ist surrounding lines of code
  p - {p}rint a specific variable, e.g. 'p x', 'p add', etc.
  q - {q}uit the debugger

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


