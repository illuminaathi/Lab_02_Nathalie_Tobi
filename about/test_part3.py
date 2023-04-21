import os
import unittest

import part3


class TestPart3(unittest.TestCase):
    def testGet_md5(self):
        with open('test.txt', 'w') as file:
            file.write('')

        test_hash = 'd41d8cd98f00b204e9800998ecf8427e'
        actual_hash = part3.get_md5('test.txt')
        self.assertEqual(test_hash, actual_hash)
        os.remove('test.txt')


if __name__ == '__main__':
    unittest.main()
