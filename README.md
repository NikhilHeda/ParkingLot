# SquadStack Activity Round - Parking Lot (Python)

## Problem Statement
Design a Parking lot system which can hold `n` Cars. Every car been issued a ticket for a slot and the slot been assigned based on the nearest available slot to the entry. The system should also support the following queries:

- Vehicle Registration numbers of all cars which are parked by the driver of a certain age.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where cars of drivers of a particular age are parked.

## Solution Approach
### Model
1. A vehicle (used as a generic structure for car) consists of registration number and driver's age.
2. Parking Lot consist slots using python dictionary for storing cars on slots.

### Services
1. Parser is mainly used for processing input commands and using parking services to execute them.
2. Parking Service contains the core logic of the implementing the input command requirements.

## Requirements
1. Python version 3.7.2 - [Download Reference](https://www.python.org/downloads/release/python-372/)
2. Set the Path variable to point to the python executable
3. Install the coverage library ([link](https://coverage.readthedocs.io/en/coverage-5.4/install.html)) using pip - ```pip install converage``` or for Mac/Ubuntu use ```pip3 install coverage```

## Running Application
1. Check the python version is 3.7.2
```python
python3 --version
```
2. Executing the application
```python
python3 launcher.py -i input.txt
```
or
```python
python3 launcher.py --input_file input.txt
```

Sample:
```python
python3 launcher.py --input_file resources/input.txt
```

Note: Substitue python3 with python, if python3 executable is not present, <b>make sure that the python version is 3.7.2</b>

## Test Cases
- Total number of test cases - 28

<img src="/resources/testcases_snapshot.PNG" alt="Test Cases Snapshot" />

- Code coverage - 83%

<img src="/resources/coverage_snapshot.PNG" alt="Coverage Snapshot" />

#### Executing tests
```python
python3 -m unittest
```

#### Calculating code coverage
```python
coverage run -m unittest
coverage report -m --omit='tests/*,*/__init__.py'
```
