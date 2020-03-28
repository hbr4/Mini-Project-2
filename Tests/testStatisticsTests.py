import unittest
from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    test_data = CsvReader('Tests/CSVFiles/TestCaseData.csv').data
    test_answer = CsvReader('Tests/CSVFiles/TestAnswers.csv').data
    zscore_ans = CsvReader('Tests/CSVFiles/ZScores.csv').data
    zdata = [float(row['zscore']) for row in zscore_ans]
    column1 = [int(row['Value 1']) for row in test_data]
    column2 = [int(row['Value 2']) for row in test_data]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        global row
        for row in self.test_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.mean(self.column1), float(row['mean']))
        self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median_statistics(self):
        global row
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
        self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))

    def test_correlation_statistics(self):
        for row in self.test_answer:
            pprint(row['correlation'])
        self.assertEqual(self.statistics.correlation(self.column1, self.column2),
                         float(row['correlation']))
        self.assertEqual(self.statistics.result, float(row['correlation']))


if __name__ == '__main__':
    unittest.main()