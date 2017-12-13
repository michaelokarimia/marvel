import reportCache

reportApp = None


class ReportPrinter:

    def __init__(self):
        self.reportApp = reportCache.reportCache()

    def GetAllCharactersSortedAlphabetically(self):
        charList = self.reportApp.getAllCharactersList(True)

        sortedList = sorted(charList, key=lambda character: character[1].lower(), reverse=False)  # sort Alphabetically

        return sortedList

    def GetMostPopular(self, limit):
        charList = self.reportApp.getAllCharactersList(True)

        sortedList = sorted(charList, key=lambda character: character[2], reverse=True)  # sort by appearances

        return sortedList[0 : limit]
