import reportCache

reportApp = None


class ReportPrinter:

    def __init__(self):
        self.reportApp = reportCache.reportCache()

    def printAllCharactersSortedAlphabetically(self):
        list = self.reportApp.getAllCharactersList(True)

        sortedList = sorted(list, key=lambda character: character[1], reverse=True)  # sort by appearances

        return sortedList
