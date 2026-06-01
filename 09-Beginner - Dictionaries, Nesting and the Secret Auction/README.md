# Secret Auction Program 🔨

Welcome to the Secret Auction! This is a fun little project I built while learning Python (specifically Day 9 of the 100 Days of Code bootcamp).

## What does it do?
It's a blind auction simulator. It allows multiple people to enter their names and place a bid in secret. Once everyone has placed their bids, the program calculates and announces the highest bidder!

## Features
- **Secret Bidding:** The screen clears after every turn so the next person can't see the previous bids.
- **Input Validation:** It won't crash if you accidentally type a letter instead of a number for your bid, and it makes sure no two people use the exact same name.
- **Winner Calculation:** Uses Python Dictionaries to keep track of everyone's bids and automatically finds the highest number at the end.

## How to run it
1. Run `main.py` in your terminal.
2. Type in your name.
3. Type in your bid amount.
4. Tell the program if there are other bidders (type 'yes' or 'no').
5. If yes, the screen "clears" so you can pass the computer to the next person!

## What I learned
This project was great practice for learning **Dictionaries** in Python. I learned how to store related data in key-value pairs (connecting a person's name to their bid amount). I also got a lot of practice using `while` loops to control the flow of a program and making sure user inputs are valid.
