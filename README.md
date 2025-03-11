# folder_cleaner
A simple python cli to move & organize your media files

## Before Running

1. `git clone` this repo to your machine
2. Create a new file named `.env` in the source directory of the repo
3. Open `development.env` and copy its contents into `.env`
4. Fill in the environment variables as described below:

The environment variables in this file will be concatenated to construct the folders you are looking to organize and move your media to. So, you'll want to make sure these files correctly include any trailing slashes.

Here is an example of what a `.env` would look like:

```
BASE_USER_PATH=/Users/mymacbook
PATH_TO_ORGANIZE=/Desktop
PATH_TO_PLACE_FILES=/Documents/media
IMAGE_FILE_PATH_NAME=/images
VIDEO_FILE_PATH_NAME=/videos
TEXT_FILE_FOLDER_NAME=/notes
CSS_FILE_FOLDER_NAME=/styles
```

Note that it won't matter whether these paths have a trailing slash at the end or not.

The above setup would use the directory found at `/Users/mymacbook/Desktop` as an input folder to search for media files. Upon locating these files, it would move them to `/Users/mymacbook/Documents/media` and place them into individual subfolders based on their filetype. If you do not already have these directories on your machine, the script will create them.

## Creating & Activating a virtual environment

As a best practice, you'll want to create a virtual environment and activate it specifically for this project. This helps neatly manage dependencies without affecting other projects.

### macOS

```
python -m venv .venv
source .venv/bin/activate
```

### Windows

```
python -m venv .venv
source .venv\Scripts\Activate.ps1
```

_If you get a permission error, run:_

`Set-ExecutionPolicy Unrestricted -Scope Process`

To deactivate the virtual environment, use:

`deactivate`

## Installing dependencies

Before you can run, you must install the dependencies used by this script.

1. Open your terminal and navigate to the main folder
2. Install the dependencies to your virtual environment by running:

`pip install -r requirements.txt`

## How to run

Once your dependencies are installed and your environment variables set up, you can run the script.

1. Open your terminal and navigate to the main folder
2. Run the package as a module using the command below

### On macOS

`python3 -m folder_cleaner.main`

### On Windows

`python -m folder_cleaner.main`

## Testing

Unit tests are covered using `unittest` and can be run using the following commands:

### On macOS

`python3 -m unittest discover -s tests -p "test_*.py"`

### On Windows

`python -m unittest discover -s tests -p "test_*.py"`
