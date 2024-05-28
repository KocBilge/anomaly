import unittest
import numpy as np
from src.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        data = np.random.rand(100, 2)
        predictions = np.random.choice([-1, 1], size=100)
        report_generator = ReportGenerator(data, predictions)
        report_generator.generate_report()
        # This test is just to make sure the function works.
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()