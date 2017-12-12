import reportPrinter
import unittest


class ReportPrinterTest(unittest.TestCase):

    def test_prints_top_ten_characters(self):

        subject = reportPrinter.ReportPrinter()

        result = subject.printAllCharactersSortedAlphabetically()

        self.assertEqual(len(result), 1491)

if __name__ == '__main__':
    unittest.main()