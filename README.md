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
1. Python version 3.7.2
2. coverage library - ```pip install converage```

## Running Application
```python
python launcher.py -i input.txt
```
or
```python
python launcher.py --input_file input.txt
```

## Test Cases
- Total number of test cases - 28
- Code coverage - 83%

#### Executing tests
```python
python -m unittest
```

#### Calculating code coverage
```python
coverage run -m unittest
coverage report -m --omit='tests/*'
```
