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

---

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

**Project:** Rock Paper Scissors game (user vs computer, logic with list indexing)

---

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

### Day 5 - While Loops & Game Logic

**Topics:**

- `while` loops (condition-based repetition)
- Loop control: setting `Game_Over = True` to exit
- Building strings dynamically
- Tracking state with flags and lists
- String membership: `if letter in word`
- Rebuilding display each iteration

**Key Example:**

```python
Game_Over = False
while not Game_Over:
    Guess = input("Guess a letter: ").lower()

    if Guess in Chosen_word:
        Correct_Letters.append(Guess)

    # Rebuild display with correct guesses
    Display = ""
    for Letter in Chosen_word:
        if Letter in Correct_Letters:
            Display += Letter
        else:
            Display += "_"

    print(Display)

    # Exit condition
    if "_" not in Display:
        Game_Over = True
```

**Project:** Hangman game (guess letters, track correct guesses, display progress, win condition)

---
