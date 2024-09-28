result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be greater than or equal to b")
        if b > 100:
            raise IndexError("b cannot be greater than 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except IndexError as ie:
        print(f"IndexError: {ie}")
        return None

data = {10: 2, 2: 5, 123: 4, 18: 1, 800: 400, 90: 30, 12: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
