import reportCache

reportApp = None


class ReportPrinter:

    def __init__(self):
        self.reportApp = reportCache.reportCache()

    def printAllCharactersSortedAlphabetically(self):
        charList = self.reportApp.getAllCharactersList(True)

        sortedList = sorted(charList, key=lambda character: character[0], reverse=False)  # sort Alphabetically

        return sortedList

    def printMostPopular(self, limit):
        charList = self.reportApp.getAllCharactersList(True)

        sortedList = sorted(charList, key=lambda character: character[1], reverse=True)  # sort by appearances

        return sortedList[0 : limit]
