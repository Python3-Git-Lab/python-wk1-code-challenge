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

```
Examples:
(2, 4, -3) == True

(-4, 6, 8) == True

(4, -6, 9) == True

(-4, 6, 0) == False

(4, 6, 10) == False

(-14, -3, -4) == False
```
## Challenge 3: Challenge 3: Consonant value

### `highest_consonant_value(word)`

This function takes a lowercase string with alphabetic characters only and no spaces. It returns the highest value of consonant substrings based on the given rules.

```
Examples;
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
```

## License

This project is licensed under MIT license standard

## Author

David Munuhe Muchoki

