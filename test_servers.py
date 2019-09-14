import requests
import unittest

def generate_1000_nums(server):
    uniques = []
    for _ in range(1000):
        num = requests.get(server)
        if num not in uniques:
            uniques.append(num)
    return len(uniques) >= 750

class TestRandomness(unittest.TestCase):
    """
    Ensures 750/1000 numbers are unique 10 times
    """
    def test_randomness_python_cloud_server(self):
        print("Testing python cloud server:")
        for i in range(10):
            self.assertTrue(generate_1000_nums("http://cs4263-rngproject.appspot.com"))
            print("\tTest", i+1, "of 10 passed!")

    def test_randomness_java_cloud_server(self):
        print("Testing Java cloud server:")
        for i in range(10):
            self.assertTrue(generate_1000_nums("http://javaproject0-251917.appspot.com"))
            print("\tTest", i+1, "of 10 passed!")

    def test_randomness_python_VM_server(self):
        print("Testing python VM server:")
        for i in range(10):
            self.assertTrue(generate_1000_nums("http://34.67.84.130"))
            print("\tTest", i+1, "of 10 passed!")

    def test_randomness_java_VM_server(self):
        print("Testing Java VM server:")
        for i in range(10):
            self.assertTrue(generate_1000_nums("http://104.155.180.57:8080/RNG-page/rng"))
            print("\tTest ", i, " of 10 passed!")

if __name__ == '__main__':
    unittest.main()
