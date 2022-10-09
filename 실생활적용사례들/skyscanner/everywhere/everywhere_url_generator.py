from Dates.datesGenerator import dateGenerator

first = 'https://www.skyscanner.co.kr/transport/flights-from/sela/'
last = '/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=1'

dateGenerator = dateGenerator()
datesCombinations = dateGenerator.datesCombinations
datesCombinationsOneMonth = dateGenerator.datesCombinationsOneMonth
datesCombinationsBetween14And45 = dateGenerator.datesCombinationsBetween14And45

# stringToWrite = ''
# for dateComb in datesCombinations:
#     stringToWrite += first + dateComb[0] + '/' + dateComb[1] + last + '\n'
# f = open(f'./evetywhereURLs.txt', 'w')
# f.write(stringToWrite)
# f.close()

# stringToWrite = ''
# for dateComb in datesCombinationsOneMonth:
#     stringToWrite += first + dateComb[0] + '/' + dateComb[1] + last + '\n'
# f = open(f'./evetywhereOneMonthURLs.txt', 'w')
# f.write(stringToWrite)
# f.close()

stringToWrite = ''
for dateComb in datesCombinationsBetween14And45:
    stringToWrite += first + dateComb[0] + '/' + dateComb[1] + last + '\n'
f = open(f'./evetywhereBetween14And45URLs.txt', 'w')
f.write(stringToWrite)
f.close()