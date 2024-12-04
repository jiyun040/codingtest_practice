def solution(array):
    maxValue = max(array)
    maxIndex = array.index(maxValue)
    return [maxValue, maxIndex]