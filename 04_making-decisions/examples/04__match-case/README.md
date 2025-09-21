We'll be exploring more graceful ways to write conditional logic in Python in-class on Wednesday.

A newer & awesome feature of Python (that many other languages have had forever!) is `match`-`case`.

```python
def say_hello(person):
    case "friend":
        print("Hey, wanna hang?")
    case "student":
        print("Hey, how's your term going?")
    case _:
        print("Howdy stranger!")
```
