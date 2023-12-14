def get_first_recurring_char(input_str: str) -> str:
    chars = {}
    # Convert to lower case and remove whitespaces.
    for c in input_str.lower().replace(" ", ""):
        if c in chars.keys():
            return c
        else:
            chars[c] = 1
    return None


assert get_first_recurring_char("racecar") == "c"
assert get_first_recurring_char("The answer") == "e"
assert get_first_recurring_char("I am happy") == "a"
assert get_first_recurring_char("I am in") == "i"
