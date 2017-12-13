import reportPrinter
import unittest


class ReportPrinterTest(unittest.TestCase):

    def test_prints_all_characters_alphabetally_in_order(self):

        subject = reportPrinter.ReportPrinter()

        result = subject.printAllCharactersSortedAlphabetically()

        self.assertEqual(len(result), 1491)

        self.assertEqual(result[0][1], '3-D Man')

        self.assertEqual(result[len(result)-1][1], 'Zzzax')

    def test_prints_top_ten_characters(self):
        subject = reportPrinter.ReportPrinter()

        result = subject.printMostPopular(10)

        self.assertEqual(len(result), 10)

        self.assertEqual(result[0][1], 'Spider-Man')
        self.assertEqual(result[1][1], 'X-Men')
        self.assertEqual(result[2][1], 'Iron Man')
        self.assertEqual(result[3][1], 'Wolverine')

if __name__ == '__main__':
    unittest.main()