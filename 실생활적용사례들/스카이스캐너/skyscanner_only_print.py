# 이게 들어있는 폴더까지 cd해서 온 후
# source ../../venv/bin/activate 해서 venv 켠 뒤
# python skyscanner_only_print.py 해서 실행

from Dates.datesGenerator import dateGenerator
from savedUrls import urlFirst, urlLast
from cities import cities
import webbrowser

dateGenerator = dateGenerator()
datesCombinations = dateGenerator.datesCombinations

def writeURLsFile(cityName, numDates):
    stringToWrite = ""
    urlFirst2 = urlFirst[cityName]
    urlLast2 = urlLast[cityName]
    for i in range(numDates):
        stringToWrite += urlFirst2 + datesCombinations[i][0] + '/' + datesCombinations[i][1] + urlLast2 + "\n"
    f = open(f'./static/{cityName}URLs.txt', 'w')
    f.write(stringToWrite)
    f.close()

for city in cities:
    writeURLsFile(city, len(datesCombinations))

