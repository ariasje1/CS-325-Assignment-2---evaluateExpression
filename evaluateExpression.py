def evaluateString(input):
    # Base case: empty string evaluates to 0
    if input == "":
        return 0

    # Find the next '+'
    i = 0
    while i < len(input) and input[i] != '+':
        i += 1

    # Get the current number
    number = int(input[0:i])

    # If end of string reached, return the number
    if i == len(input):
        return number

    # Otherwise, skip '+' and evaluate the rest
    rest_of_string = input[i + 1:]
    return number + evaluateString(rest_of_string)


# Example run
if __name__ == "__main__":
    expr = "12+13+15"
    result = evaluateString(expr)
    print(result)  # prints 40


