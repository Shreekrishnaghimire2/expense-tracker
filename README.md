# Expense Tracker

A small command-line program that helps me keep track of what I spend. I built it in Python while learning to write, test, and organise real programs instead of only following tutorials.

## What it does

You type in an expense (name, amount, category) and the program saves it. You can see your total spending, or how much you spent in each category. Your data is stored in a file, so it is still there the next time you open the program.

## How to run it

You need Python 3 installed. In the project folder, run:

```
python expense_tracker.py
```

Then pick an option from the menu.

## How to run the tests

```
pip install pytest
python -m pytest
```

There are 9 tests. They check the main functions, including bad inputs like a zero amount, a negative amount, text instead of a number, and a blank name.

## Features

- Add an expense with a name, amount, and category
- Rejects bad input instead of crashing
- Shows total spending
- Shows spending per category ("Food" and "food" count as the same category)
- Saves to `expenses.json` after every new expense and loads it on start
- Handles a missing or damaged save file without crashing

## Known limitations

- You can't edit or delete an expense yet
- Expenses have no dates
- It only works in the terminal, there is no screen or web page
- If the save file gets damaged, the next new expense overwrites it
- Money is stored as decimal numbers, which is fine for practice but not for real accounting

## What I learned

- Splitting a program into small functions makes it much easier to test
- User input is always text, so it must be converted and checked
- A test that has never failed is hard to trust, so I broke my code on purpose to confirm the tests catch it
- Saving data in JSON and loading it back safely

I used an AI coach for hints and code reviews while building this. I ran and fixed the code myself, and some of the test code was provided to me, which I then ran and checked.