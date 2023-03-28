def birthdayCakeCandles():
    size = int(input())
    candlevalues = list(map(int, input().split(' ')[:size]))
    print(candlevalues.count(max(candlevalues)))

birthdayCakeCandles()