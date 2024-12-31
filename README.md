# folder_cleaner
A simple python cli to move & organize your media files

## Before Running

1. `git clone` this repo to your machine
2. Create a new file named `.env` in the source directory of the repo
3. Open `development.env` and copy its contents into `.env`
4. Fill in the environment variables as described

## How to run

1. Open your terminal and navigate to the main folder
2. Run the package as a module using the command below

### On Mac OS

`python3 -m folder_cleaner.main`

### On Windows

`python -m folder_cleaner.main`

## Testing

Unit tests are covered using `unittest` and can be run using the following commands:

### On Mac OS

`python3 -m unittest discover -s tests -p "test_*.py"`

### On Windows

`python -m unittest discover -s tests -p "test_*.py"`
