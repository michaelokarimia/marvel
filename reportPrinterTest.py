import reportPrinter
import unittest


class ReportPrinterTest(unittest.TestCase):

    def test_prints_all_characters_alphabetally_in_order(self):

        subject = reportPrinter.ReportPrinter()

        result = subject.printAllCharactersSortedAlphabetically()

        self.assertEqual(len(result), 1491)

        self.assertEqual(result[0], ('3-D Man', 12))

        self.assertEqual(result[len(result)-1], ('Zzzax', 3))

    def test_prints_top_ten_characters(self):
        subject = reportPrinter.ReportPrinter()

        result = subject.printMostPopular(10)

        self.assertEqual(len(result), 10)

        self.assertEqual(result[0], ('Spider-Man', 3095))
        self.assertEqual(result[1], ('X-Men', 2911))
        self.assertEqual(result[2], ('Iron Man', 2316))
        self.assertEqual(result[3], ('Wolverine', 2134))

if __name__ == '__main__':
    unittest.main()