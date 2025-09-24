import math 
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
print(calculate_circle_area(5))  # Example usage

student = [
{'id': 1, 'name': 'Alice', 'major': 'Computer Science'},
{'id': 2, 'name': 'Bob', 'major': 'Mathematics'},
{'id': 3, 'name': 'Charlie', 'major': 'Physics'}    
]
print (student[1]['name'])  # Accessing Bob's name
print (student[2]['major'])  # Accessing Charlie's major
print (student[0]['id'])  # Accessing Alice's id

#寫一個函示，輸入一個數字串列，回傳該數字串列的最大值
def find_max(numbers):
    """Return the maximum value from a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Example usage
print("--------------------")

#寫一個程式，從1印到100
#如果數字是3的倍數，印出"Fizz"
#如果數字是5的倍數，印出"Buzz"
#如果數字同時是3和5的倍數，印出"FizzBuzz"
#其他則印出數字本身
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
