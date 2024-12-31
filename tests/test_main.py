import unittest
from folder_cleaner.main import get_file_category

class TestFormatter(unittest.TestCase):
  def test_get_file_category(self):
    input = 'wolf.jpg'
    expected = '/Users/michaelcarreiro/Documents/files/images'
    self.assertEqual(get_file_category(input), expected)

if __name__ == '__main__':
  unittest.main()