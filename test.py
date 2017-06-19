# IMPORTANT: core.py must be up and running (locally) for this test to work
# Test each function for correct http status codes (200=ok, 400=bad request, 405=incorrect method)

from core import *
import unittest
import requests


class TestStringMethods(unittest.TestCase):

    # test flip function
    def test_flip(self):
        print 'Test Flip function'
        print '------------------------'

        r = [0, 0, 0]

        r[0] = requests.get('http://127.0.0.1:5000/flip/vertical/blend.jpg')
        r[1] = requests.get('http://127.0.0.1:5000/flip/invalid/blend.jpg')
        r[2] = requests.put('http://127.0.0.1:5000/flip/vertical/blend.jpg')

        self.assertEqual(str(r), '[<Response [200]>, <Response [400]>, <Response [405]>]')

    # test rotate function
    def test_rotate(self):
        print 'Test Rotate function'
        print '------------------------'

        r = [0, 0, 0]

        r[0] = requests.get('http://127.0.0.1:5000/rotate/-34/blend.jpg')
        r[1] = requests.get('http://127.0.0.1:5000/flip/370/blend.jpg')
        r[2] = requests.put('http://127.0.0.1:5000/flip/60/blend.jpg')

        self.assertEqual(str(r), '[<Response [200]>, <Response [400]>, <Response [405]>]')

    # test crop function
    def test_crop(self):
        print 'Test Crop function'
        print '------------------------'

        r = [0, 0, 0]

        r[0] = requests.get('http://127.0.0.1:5000/crop/10/10/20/20/blend.jpg')
        r[1] = requests.get('http://127.0.0.1:5000/crop/30/10/20/20/blend.jpg')
        r[2] = requests.put('http://127.0.0.1:5000/crop/10/10/20/20/blend.jpg')

        self.assertEqual(str(r), '[<Response [200]>, <Response [400]>, <Response [405]>]')

    # test blend function
    def test_blend(self):
        print 'Test Blend function'
        print '------------------------'

        r = [0, 0, 0]

        r[0] = requests.get('http://127.0.0.1:5000/blend/50/blend.jpg/blend.jpg')
        r[1] = requests.get('http://127.0.0.1:5000/blend/120/blend.jpg/blend.jpg')
        r[2] = requests.put('http://127.0.0.1:5000/blend/30/blend.jpg/blend.jpg')

        self.assertEqual(str(r), '[<Response [200]>, <Response [400]>, <Response [405]>]')

if __name__ == '__main__':
    unittest.main()