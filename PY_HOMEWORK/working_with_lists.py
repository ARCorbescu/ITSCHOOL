import sys

def read_input():
    no_numbers = int(sys.argv[1])
    numbers = []
    
    for _ in range(no_numbers):
        number = int(input("Enter a number: "))
        numbers.append(number)
    return numbers

def sum_of_numbers(numbers):
    return sum(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    return format(sum_of_numbers(numbers) / len(numbers), '.3f')

if __name__ == "__main__":

    numbers = read_input()
    print("Sum:", sum_of_numbers(numbers))
    print("Average:", calculate_average(numbers))
