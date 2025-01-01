import os
import shutil
from dotenv import load_dotenv
from typing import Union

load_dotenv()

# setup environment variables & paths
BASE_USER_PATH = os.getenv('BASE_USER_PATH')
PATH_TO_ORGANIZE = BASE_USER_PATH + os.getenv('PATH_TO_ORGANIZE')
PATH_TO_PLACE_FILES = BASE_USER_PATH + os.getenv('PATH_TO_PLACE_FILES')
IMAGE_FILE_PATH = PATH_TO_PLACE_FILES + os.getenv('IMAGE_FILE_PATH_NAME')
VIDEO_FILE_PATH = PATH_TO_PLACE_FILES + os.getenv('VIDEO_FILE_PATH_NAME')
TEXT_FILE_FOLDER = PATH_TO_PLACE_FILES + os.getenv('TEXT_FILE_FOLDER_NAME')
CSS_FILE_FOLDER = PATH_TO_PLACE_FILES + os.getenv('CSS_FILE_FOLDER_NAME')

# setup supported file extensions lists
SUPPORTED_EXTENSIONS = {
  'IMAGE_EXTENSIONS': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
  'VIDEO_EXTENSIONS': ['.mp4', '.avi', '.mkv', '.mov'],
  'DOC_EXTENSIONS': ['.txt', '.docx', '.pdf', '.xlsx', '.csv', '.rtf'],
  'STYLE_EXTESNIONS': ['.css', '.sass', '.scss'],
}

def organize_input(input_path: str) -> None:
  # change to input path
  os.chdir(input_path)
  # save list of files in directory to variable
  file_list = os.listdir()

  # iterate over file list
  for file in file_list:
    src_dest = get_dir_by_file(file)
    
    if src_dest:
      # create the source directory if it doesn't exist yet
      if not os.path.exists(src_dest):
        os.makedirs(src_dest)

      desktop_file_path = os.path.join(input_path, file)
      shutil.move(desktop_file_path, src_dest)
      print(f'Moved {file} to directory: {src_dest}')
    
  print('All relevant files moved')

# returns directory the file should be moved to based off its extension
def get_dir_by_file(file_name: str) -> Union[None, str]:
  ext = os.path.splitext(file_name)[1].lower()

  if ext in SUPPORTED_EXTENSIONS['IMAGE_EXTENSIONS']:
    return IMAGE_FILE_PATH
  elif ext in SUPPORTED_EXTENSIONS['VIDEO_EXTENSIONS']:
    return VIDEO_FILE_PATH
  elif ext in SUPPORTED_EXTENSIONS['DOC_EXTENSIONS']:
    return TEXT_FILE_FOLDER
  elif ext in SUPPORTED_EXTENSIONS['STYLE_EXTESNIONS']:
    return CSS_FILE_FOLDER

  return None

organize_input(PATH_TO_ORGANIZE)
