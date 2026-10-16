# goit-pycore-hw-05

Homework assignment for the Python Core course.

Topic: **Functional Programming and Built-in Python Modules**

This repository contains solutions for four tasks covering closures, recursion, generators, regular expressions, log analysis, decorators, and exception handling.

---

## Task 1 — Caching Fibonacci

File: `homework5.py`

This task implements a closure for calculating Fibonacci numbers with caching.

The function `caching_fibonacci()` returns an inner function `fibonacci(n)`.

The solution uses:

- closures;
- recursion;
- caching with a dictionary;
- reuse of previously calculated values.

Example:

```python
fib = caching_fibonacci()

print(fib(10))
print(fib(15))

Expected result:
55
610

Task 2 — Generator of Numbers and Profit Calculation
File: homework5b.py
This task implements:
- generator_numbers(text) — extracts real numbers from a text and returns them using a generator;
- sum_profit(text, func) — calculates the total sum of numbers returned by the generator.
The solution uses:
- generators;
- yield;
- regular expressions;
- passing a function as an argument.
Example:
text = (    "Загальний дохід працівника складається з декількох частин: "    "1000.01 як основний дохід, доповнений додатковими "    "надходженнями 27.45 і 324.00 доларів.")total_income = sum_profit(text, generator_numbers)print(f"Загальний дохід: {total_income}")


Expected result:
Загальний дохід: 1351.46

Task 3 — Log File Analyzer
File: homework5c.py
Additional file: example.log
This optional task implements a command-line tool for analyzing log files.
The program:
- reads a log file;
- parses log entries;
- counts records by logging level;
- displays statistics;
- filters logs by a selected level;
- handles file-related errors.
Implemented functions include:
- parse_log_line()
- load_logs()
- filter_logs_by_level()
- count_logs_by_level()
- display_log_counts()
Supported log levels include:
- INFO
- DEBUG
- ERROR
- WARNING
Example:
python homework5c.py example.log

Example with filtering:
python homework5c.py example.log error

The program displays the total number of log entries for each level and, when a level is provided, shows the matching log records.
Task 4 — Console Assistant Bot with Error Handling
File: homework5d.py
This task extends the console assistant bot from the previous homework assignment.
Error handling is implemented using the input_error decorator.
The decorator handles:
- KeyError
- ValueError
- IndexError
Incorrect user input is handled without terminating the program.
Supported commands:
hello
add <name> <phone>
change <name> <phone>
phone <name>
all
close
exit

Examples:
Enter a command: hello
How can I help you?

Enter a command: add Bob 123456789
Contact added.

Enter a command: phone Bob
123456789

Enter a command: change Bob 987654321
Contact updated.

Enter a command: all
Bob: 987654321

Examples of error handling:
Enter a command: add
Give me name and phone please.

Enter a command: phone
Enter user name.

Enter a command: phone Alice
Contact not found.

The use of the decorator allows command handlers to process input errors while keeping the bot running.
Repository Structure
goit-pycore-hw-05/
│
├── homework5.py
├── homework5b.py
├── homework5c.py
├── homework5d.py
├── example.log
└── README.md

Running the Programs
Task 1:
python homework5.py

Task 2:
python homework5b.py

Task 3:
python homework5c.py example.log

or:
python homework5c.py example.log error

Task 4:
python homework5d.py

Technologies Used
- Python 3
- Closures
- Recursion
- Dictionaries
- Generators
- Regular expressions
- Functional programming techniques
- Command-line arguments
- File processing
- Decorators
- Exception handling

Author
Fedor Stoietskyi
```
