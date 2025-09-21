# Exercises - Math & Data Types

This time, you'll be writing the exercises from scratch!

Create a new file for each exercise. 

## Hints
- Anything provided to `input()` is returned as a string. What you do with that afterwards is up to you!
- Remember your math operators; check back in the slides if you need.
- Google is your friend; ChatGPT is not (unless you're COMPLETELY stuck after looking stuff up on your own, *and* you ask it to not give you the answer but instead help you puzzle through it).
- Python f-strings are your friend!

---

## Exercise 1 (easy)
Create a program that asks the user for a temperature in Celsius and converts it to Fahrenheit.

Terminal interaction should be similar to:

```
Temperature in Celsius:  32
Celsius: 32.0 => Fahrenheit: 89.6
```


## Exercise 2 (easy)
Get inputs from the user for a name, an adjective, a verb (past tense) and a place.

Use those inputs in a goofy sentence printed to the console (i.e. terminal output).

```
Name: Oliver
Adjective: suspicious
Verb (past tense): crawled
Place: Citadel Theatre upper garden

Oliver crawled to the Citadel Theatre upper garden with a suspicious grin.
```


## Exercise 3 (medium)
Ask the user for an integer number input. Add up the *digits* for the input and display the sum. 

For example, if the integer is 423, the sum of the digits is 9 (i.e. 4 + 2 + 3).

Stumped? The main problem you're solving here is, "how can I [use Python data types to] convert a number into individual digits"?

Remember, anything provided to `input()` starts off as a *string*.

```
Enter an integer: 423
Sum of digits: 9
```


## Exercise 4 (easy/medium)
Ask the user for a number of seconds. Print the number of minutes & seconds.
```
Total seconds: 125
2 minute(s) and 5 second(s)
```


## Exercise 5 (medium - extension of Ex. 4)
Ask the user for a small currency amount. Display a breakdown of how you'd pay out that amount in quarters, dimes, nickels, and pennies.

```
Enter an amount (e.g. 1.43): 1.43

Quarters: 5
Dimes: 1
Nickels: 1
Pennies: 3
```
