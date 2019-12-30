# Bubble sort
# Douglas

def bubble_sort(numbers):
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i] #swap numbers
                swapped = True
    return numbers

numbers = [2,5,7,2,567,2435,6]

print(bubble_sort(numbers))
