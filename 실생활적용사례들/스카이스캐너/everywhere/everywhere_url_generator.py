from Dates.datesGenerator import dateGenerator

first = 'https://www.skyscanner.co.kr/transport/flights-from/sela/'
last = '/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=1'

dateGenerator = dateGenerator()
datesCombinations = dateGenerator.datesCombinations

stringToWrite = ''
for dateComb in datesCombinations:
    stringToWrite += first + dateComb[0] + '/' + dateComb[1] + '\n'
f = open(f'./evetywhereURLs.txt', 'w')
f.write(stringToWrite)
f.close()