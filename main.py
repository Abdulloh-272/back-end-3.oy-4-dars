def universal_func(numbers):
    def get_max():
        return max(numbers)

    def get_min():
        return min(numbers)

    def get_squares():
        return [x**2 for x in numbers]

    def get_average():
        return sum(numbers) / len(numbers)

    def get_multiples():
        result = 1
        for num in numbers:
            result *= num
        return result

    def get_length():
        return len(numbers)

    return {
        "min": get_min(),
        "max": get_max(),
        "squares": get_squares(),
        "average": get_average(),
        "multiples": get_multiples(),
        "length": get_length()
    }

result = universal_func([2, 6, 4, 3, 8, 5])
print(result)
