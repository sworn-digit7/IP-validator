````markdown
# NUMB3RS — IPv4 Address Validator

A Python program that validates IPv4 addresses using regular expressions and unit tests.

The program determines whether a given string represents a valid IPv4 address.

## Overview

An IPv4 address consists of four numerical sections, known as octets, separated by periods.

For example:

```text
192.168.1.1
````

Each octet must be an integer between `0` and `255`.

The program accepts an IPv4 address as input and determines whether it is valid.

### Examples

| Input             | Result  |
| ----------------- | ------- |
| `127.0.0.1`       | Valid   |
| `192.168.1.1`     | Valid   |
| `255.255.255.255` | Valid   |
| `275.3.6.28`      | Invalid |
| `192.168.1`       | Invalid |
| `192.168.1.256`   | Invalid |
| `1.2.3.4.5`       | Invalid |

## Features

* Validates IPv4 addresses
* Uses Python's `re` module and regular expressions
* Ensures exactly four octets are present
* Ensures each octet falls within the range `0–255`
* Handles invalid input safely
* Includes automated unit tests using `pytest`

## How It Works

The main validation logic is implemented in:

```text
numb3rs.py
```

The program contains a `validate()` function:

```python
def validate(ip):
    ...
```

This function receives an IPv4 address as a string and returns:

* `True` if the address is valid
* `False` if the address is invalid

The program uses a regular expression to check the overall structure of the input before validating the individual numerical components.

## Project Structure

```text
NUMB3RS/
│
├── numb3rs.py
├── test_numb3rs.py
└── README.md
```

### `numb3rs.py`

Contains the main program and the `validate()` function responsible for determining whether an IPv4 address is valid.

### `test_numb3rs.py`

Contains automated tests that verify the behaviour of `validate()` against a range of valid and invalid IPv4 addresses.

## Testing

The project uses `pytest` for automated testing.

Run the test suite with:

```bash
pytest test_numb3rs.py
```

A successful test run confirms that the validation function behaves correctly across the tested cases.

## What I Learned

Through this project, I strengthened my understanding of:

* Regular expressions in Python
* Input validation
* String manipulation
* Functions and Boolean return values
* Writing automated unit tests
* Using `pytest`
* Designing tests for both valid and invalid inputs
* Handling edge cases in software validation

## Technologies Used

* **Python 3**
* **Regular Expressions (`re`)**
* **pytest**

## Course

This project was completed as part of:

**CS50's Introduction to Programming with Python**

Harvard University — CS50P

## Author

**Gurleen Singh**

Computer Science / Physics student interested in software engineering, artificial intelligence, and computational problem solving.

