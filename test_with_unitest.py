import unittest


# La fonction à tester
def add_numbers(a, b):
    return a + b

# La classe de test
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)


class TestExecutionOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("1. setUpClass - Exécuté une fois avant tous les tests")

    @classmethod
    def tearDownClass(cls):
        print("6. tearDownClass - Exécuté une fois après tous les tests")

    def setUp(self):
        print("2. setUp - Exécuté avant chaque test")

    def tearDown(self):
        print("4. tearDown - Exécuté après chaque test")

    def test_1(self):
        print("3. Exécution du test_1")

    def test_2(self):
        print("5. Exécution du test_2")



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro n'est pas permise")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Chaque méthode de test a sa propre instance Calculator
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertNotEqual(self.calc.add(2, 2), 5)

    def test_subtract(self):
        self.assertTrue(self.calc.subtract(10, 5) == 5)
        self.assertFalse(self.calc.subtract(10, 5) == 6)

    def test_multiply(self):
        self.assertGreater(self.calc.multiply(3, 4), 10)
        self.assertLess(self.calc.multiply(2, 3), 10)


    def test_types(self):
        self.assertIsInstance(self.calc.add(1, 2), int)
        self.assertIsNotNone(self.calc.subtract(5, 5))

    def test_in_not_in(self):
        result = self.calc.multiply(2, 3)
        self.assertIn(result, [4, 5, 6])
        self.assertNotIn(result, [7, 8, 9])

    def test_assert_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
