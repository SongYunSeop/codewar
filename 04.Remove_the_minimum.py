def remove_smallest(numbers):
    return numbers[:numbers.index(min(numbers))]+numbers[numbers.index(min(numbers))+1:] if len(numbers) > 0 else []

