firstList = [1, "one", 3.3]
for i in firstList:
    print(i)
# 1 one 3.3

nestedList = [1, 1,[1, 2]]
print(nestedList[2][1])
# 2

lst = ['a', 'b', 'c']
print(lst[1:])
# ['b', 'c']

#weekday dictionary with keys of the weekdays and values are the numerical value of the day
weekdayDict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

D = {'k1': [1, 2, 3]}
print(D['k1'][1])
# 2

secondList = [1, [1,3]]
firstTuple = tuple(secondList)
print(firstTuple)
# (1, [1, 3])

word = "Mississippi"
wordSet = set(word)
wordSet.add("X")
print(wordSet)
# {'s', 'X', 'M', 'p', 'i'}

print(set([1,1,2,3]))