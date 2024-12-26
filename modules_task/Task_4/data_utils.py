from collections import Counter
def mean(numbers):
    sum_of_numbers=0
    for i in numbers:
        sum_of_numbers+=i
    return sum_of_numbers/len(numbers)

def median(numbers):

    data=list(numbers)
    data.sort()
    if len(data)%2==0:
        median_of_data=data[int(len(data) / 2)]
    else:
        median_of_data=data[int((len(data) / 2) + 1)]
    return median_of_data

def mode(numbers):
    d=dict(Counter(list(numbers)))
    values=list(d.values())
    values.sort()
    for i,j in d.items():
        if j==values[-1]:
            return i
    return 'Please give an iterable argument.'
