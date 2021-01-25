![Run Python Tests](https://github.com/Pythonen/wolt_summer2021/workflows/Run%20Python%20Tests/badge.svg)

# Wolt summer 2021 pre-assignment

**Wolt** once again had this pre-assignment for internship positions.
This is my take on the task that is given [here](https://github.com/woltapp/summer2021-internship).

## My assignment

One of the requirements were that the task must be done with one of the following languages: *Typescript*, *ReasonML*, *Python*, *Scala*, *Kotlin* or *Java* and hence I used Python and [Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Running it locally
To get the assignment running on your machine, you have to have Python 3.7 =< and pip installed to your machine.

On your command line type

`pip install -r requirements.txt`

or if you're on mac

`pip3 install -r requirements.txt`

To run the api, in the root folder depending on your machine type:

`python main.py`

or

`python3 main.py`

To run tests in the root folder depending on your machine type:

`python utils_test.py`

or

`python3 util_test.py`

The 'API' responds from `/discovery` and it responds with all the restaurants from [restaurants.json](https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json) if not given any query parameters.
If given query params as suggested in assingment `/discovery?lat=60.1709&lon=24.941` it responds with the restaurants near the location.
