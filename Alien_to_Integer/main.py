def alien_to_integer(s):
    symbol_values = {
        'A': 1,
        'B': 5,
        'Z': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'R': 1000,
    }

    result = 0
    prev_value = 0

    for symbol in reversed(s):
        current_value = symbol_values[symbol]

        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value

        prev_value = current_value

    return result

# Test cases
print(alien_to_integer("AAA"))      # Output: 3
print(alien_to_integer("LBAAA"))    # Output: 58
print(alien_to_integer("RCRZCAB"))  # Output: 1994