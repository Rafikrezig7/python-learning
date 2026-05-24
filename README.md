# 🐍 Python Learning Journey

Daily progress for AI Master's prep.

## Week 1

### Day 1 - Variables & Input/Output

**Topics:** Variables, input(), print(), string concatenation

**Project:** Band name generator

---

### Day 2 - Data Types & Operators

**Topics:**

- Subscripting `'Hello'[0]` → 'H'
- Slicing `'Hello'[0:3]` → 'Hel'
- `type()` function (str, int, float, bool, None)
- Type conversion: `int()`, `float()`, `str()`, `bool()`
- Arithmetic: `+`, `-`, `*`, `/`, `//` (floor), `%` (modulo), `**` (power)
- Assignment operators: `+=`, `-=`
- f-strings: `f"Score: {score}"`

**Key Example:**

```python
bmi = 84 / 1.65 ** 2
print(f"Your BMI is {round(bmi, 2)}")  # f-strings like backticks in JS
```

**Project:** Tip Calculator (input bill, tip%, people → calculate per person cost)

### Day 3 - Random Module & Lists

**Topics:**

- `import random` module
- `random.randint()`, `random.random()`, `random.uniform()`, `random.choice()`
- Lists: indexing, slicing, modifying, `.append()`
- Nested lists
- `if/elif/else` conditionals

**Key Example:**

```python
friends = ["Rafik", "Sami", "Yazid"]
random_friend = random.choice(friends)  # Pick random item from list
print(random_friend)
```
### Day 4 - Loops & Functions
**Topics:**
- `for` loops (iterate lists, ranges)
- Built-in functions: `sum()`, `max()`
- `while` loops
- Define functions with `def`
- `range(start, end)` for number sequences

**Key Examples:**
```python
# For loop
for fruit in fruits:
    print(fruit)

# Sum and max
total = sum([10, 14, 15, 9])  # 48
highest = max([10, 14, 15, 9])  # 15

# While loop
while cats > 0:
    print('cute cat')
    cats -= 1

# Functions
def my_function():
    print('hello')
my_function()
```

**Project:** Password Generator (combine letters/symbols/numbers, shuffle, display)

---

**Project:** Rock Paper Scissors game (user vs computer, logic with list indexing)

---
