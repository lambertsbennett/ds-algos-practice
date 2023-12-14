def reverse(input_string: str) -> str:
    i = len(input_string) - 1
    result = []
    while i >= 0:
        result.append(input_string[i])
        i -= 1
    return "".join(result)


assert "olleh" == reverse("hello")
assert "racecar" == reverse("racecar")
assert "ereht olleh" == reverse("hello there")
