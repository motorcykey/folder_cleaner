import unittest
from folder_cleaner.main import get_dir_by_file

class TestGetDirByFile(unittest.TestCase):
  def test_get_dir_by_file_images(self):
    input = 'wolf.jpg'
    expected = '/Users/michaelcarreiro/Documents/files/images'
    self.assertEqual(get_dir_by_file(input), expected)

  def test_get_dir_by_file_videos(self):
    input = 'movietrailer.mp4'
    expected = '/Users/michaelcarreiro/Documents/files/videos'
    self.assertEqual(get_dir_by_file(input), expected)

  def test_get_dir_by_file_docs(self):
    input = 'example.rtf'
    expected = '/Users/michaelcarreiro/Documents/files/notes'
    self.assertEqual(get_dir_by_file(input), expected)

  def test_get_dir_by_file_docs(self):
    input = 'styles.sass'
    expected = '/Users/michaelcarreiro/Documents/files/styles'
    self.assertEqual(get_dir_by_file(input), expected)
  
  def test_get_dir_by_file_unsupported_extension(self):
    input = 'other.exe'
    expected = None
    self.assertEqual(get_dir_by_file(input), expected)

  def test_get_dir_by_file_no_extension(self):
    input = 'filename'
    expected = None
    self.assertEqual(get_dir_by_file(input), expected)

  def test_get_dir_by_file_empty_string(self):
    input = ''
    expected = None
    self.assertEqual(get_dir_by_file(input), expected)

if __name__ == '__main__':
  unittest.main()