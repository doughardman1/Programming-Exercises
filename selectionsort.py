# Selection sort

def selection_sort(numbers):
    for i in range(len(numbers)):
        lowest_value_index = i
        
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest_value_index]:
                lowest_value_index = j
                
        numbers[i], numbers[lowest_value_index] = numbers[lowest_value_index], numbers[i]

    return numbers

numbers = [2,5,7,2,567,2435,6]

print(selection_sort(numbers))