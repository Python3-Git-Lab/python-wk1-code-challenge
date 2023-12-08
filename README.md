# Project Challenges

## Challenge 1: Converting 12-hour time to 24-hour time

### `convert_to_24_hour_time(hour, minute, period)`

This function takes three parameters: `hour` (an integer in the range of 1 to 12), `minute` (an integer in the range of 0 to 59), and `period` (a string either "am" or "pm"). It returns a four-digit string that represents the input time in 24-hour format.

```python
def convert_to_24_hour_time(hour, minute, period):
    # Adjust hour for 12-hour clock
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    # Format the hour and minute as a four-digit string
    return "{hour:02d}{minute:02d}"
```

## Challenge 2: Two numbers are positive

### `exactly_two_positive(a, b, c)`

This function takes three integers a, b, and c as arguments and returns True if exactly two of them are positive, and False otherwise.

```python
def exactly_two_positive(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2
```
## Challenge 3: Challenge 3: Consonant value

### `highest_consonant_value(word)`

This function takes a lowercase string with alphabetic characters only and no spaces. It returns the highest value of consonant substrings based on the given rules.

```python
def highest_consonant_value(word):
    vowels = "aeiou"
    consonant_values = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
    
    # Extract consonant substrings
    consonant_substrings = ["".join(char for char in substring if char not in vowels) for substring in word.split(vowels)]
    
    # Calculate the value for each consonant substring
    values = [sum(consonant_values[char] for char in substring) for substring in consonant_substrings]
    
    # Return the highest value
    return max(values)
```

## Licence

This project is licensed under MIT license standard

## Author

David Munuhe Muchoki

