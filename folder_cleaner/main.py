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

print(f'PATH_TO_ORGANIZE: {PATH_TO_ORGANIZE}')
print(f'PATH_TO_PLACE_FILES: {PATH_TO_PLACE_FILES}')

def move_and_arrange(input_path: str) -> None:
  # change to input path
  os.chdir(input_path)
  # save list of files in directory to variable
  file_list = os.listdir()

  # iterate over file list
  for file in file_list:
    src_dest = get_file_category(file)
    
    if src_dest:
      # create the source directory if it doesn't exist yet
      if not os.path.exists(src_dest):
        os.makedirs(src_dest)

      desktop_file_path = os.path.join(input_path, file)
      shutil.move(desktop_file_path, src_dest)
      print(f'Moved {file} to directory: {src_dest}')
    
  print('All relevant files moved')

# returns directory the file should be moved to based off its extension
def get_file_category(file_name: str) -> Union[None, str]:
  image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
  video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
  document_extensions = ['.txt', '.docx', '.pdf', '.xlsx', '.csv', '.rtf']
  style_extensions = ['.css', '.sass', '.scss']

  ext = os.path.splitext(file_name)[1].lower()

  if ext in image_extensions:
    return IMAGE_FILE_PATH
  elif ext in video_extensions:
    return VIDEO_FILE_PATH
  elif ext in document_extensions:
    return TEXT_FILE_FOLDER
  elif ext in style_extensions:
    return CSS_FILE_FOLDER

  return None

move_and_arrange(PATH_TO_ORGANIZE)
