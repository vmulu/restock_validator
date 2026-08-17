# Warehouse Restock Manifest Validator

## Set Up

First you should clone this repository into your workspace by running:
`git clone https://github.com/vmulu/restock_validator.git `

Once you have the project in your workspace, navigate into the project: `cd restock_validate`

Then you must create and activate your virtual environment by running:

Start virtual environment: `python -m venv .venv`

Activate virtual environment: `source .venv/bin/activate`

Now that your virtual environment is set up we can install the dependencies for this module using: `pip install -e ".[dev]"`

## Running Tests

To run the test suite use the command: `python -m pytest -v`

## Running the Loader

I also included a main.py that demonstrates loading the provided restock manifest.

`python -m src.main`

