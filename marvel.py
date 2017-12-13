import reportPrinter



if __name__ == '__main__':
    rp = reportPrinter.ReportPrinter()

    print('All Characters in Alphabetic order')

    inOrder = rp.GetAllCharactersSortedAlphabetically()

    for character in inOrder:
        print(character[1])

    topTen = rp.GetMostPopular(10)

    print('Most popular characters:')
    for character in topTen:
        print('{}, appears in {} comics'.format(character[1], character[2]))
