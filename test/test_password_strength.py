import unittest
from python0924 import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_passwords(self):
        self.assertEqual(check_password_strength(""), "弱")
        self.assertEqual(check_password_strength("abc"), "弱")
        self.assertEqual(check_password_strength("1234567"), "弱")
        self.assertEqual(check_password_strength("ABCDEFG"), "弱")
        self.assertEqual(check_password_strength("abcdefg"), "弱")
        self.assertEqual(check_password_strength("@@@@@@@"), "弱")
        self.assertEqual(check_password_strength("A1"), "弱")
        self.assertEqual(check_password_strength("A@"), "弱")
        self.assertEqual(check_password_strength("a1"), "弱")

    def test_medium_passwords(self):
        self.assertEqual(check_password_strength("abcdefgh"), "中")
        self.assertEqual(check_password_strength("ABCDEFGH"), "中")
        self.assertEqual(check_password_strength("12345678"), "中")
        self.assertEqual(check_password_strength("abcd1234"), "中")
        self.assertEqual(check_password_strength("ABCD1234"), "中")
        self.assertEqual(check_password_strength("abcd@123"), "中")
        self.assertEqual(check_password_strength("Abcdefgh"), "中")
        self.assertEqual(check_password_strength("Abcd1234"), "中")

    def test_strong_passwords(self):
        self.assertEqual(check_password_strength("Abcd1234@"), "強")
        self.assertEqual(check_password_strength("A1b2c3d4!"), "強")
        self.assertEqual(check_password_strength("Qwerty1@"), "強")
        self.assertEqual(check_password_strength("Zxcvbnm1!"), "強")

    def test_edge_cases(self):
        self.assertEqual(check_password_strength("A1@aaaaa"), "中")
        self.assertEqual(check_password_strength("A1@aaaaaa"), "強")
        self.assertEqual(check_password_strength("!@#$%^&*"), "中")
        self.assertEqual(check_password_strength("A1b2c3d4"), "中")
        self.assertEqual(check_password_strength("A1b2c3d4e5!"), "強")

if __name__ == "__main__":
    unittest.main()
