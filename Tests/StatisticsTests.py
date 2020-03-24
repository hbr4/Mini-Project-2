import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.population_mean(self.column1), float(row['mean']))
        self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median_statistics(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column1), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
        self.assertEqual(self.statistics.result, float(row['mode']))

    def test_standard_deviation_statistics(self):
        for row in self.test_answer:
            pprint(row["stddev"])
        self.assertEqual(self.statistics.stddev(self.column1), float(row['stddev']))
        self.assertEqual(self.statistics.result, float(row['stddev']))

    def test_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['variance'])
        self.assertEqual(self.statistics.population_proportion_variance(self.column1), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))


    def test_correlation_statistics(self):
        for row in self.test_answer:
            pprint(row['correlation'])
        self.assertEqual(self.statistics.correlation_coefficient(self.column1, self.column2),
                         float(row['correlation']))
        self.assertEqual(self.statistics.result, float(row['correlation']))

    def test_zscore_statistics(self):
        self.assertEqual(self.statistics.zscore(self.column1), self.column_zscore)
        self.assertEqual(self.statistics.result, self.column_zscore)


    def test_confidence_interval(self):
        for row in self.test_answer:
            pprint(row['ci_top'])
            pprint(row['ci_bottom'])
        self.assertEqual(self.statistics.confidence_interval_top(self.column1), float(row['ci_top']))
        self.assertEqual(self.statistics.confidence_interval_bottom(self.column1), float(row['ci_bottom']))



if __name__ == '__main__':
    unittest.main()