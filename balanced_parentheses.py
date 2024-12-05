# function that checks if a given string has balanced parentheses
def is_balanced_parentheses(input_str):
    # Check if the input is a string
    if not isinstance(input_str, str):
        return "Input must be a string"
    # Initialize an empty list to serve as the stack
    stack = []

    # Define the sets of opening and closing brackets
    opening_brackets = "({["
    closing_brackets = ")}]"

    # Iterate through each character in the input string
    for char in input_str:
        # If the character is an opening bracket, push it onto the stack
        if char in opening_brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in closing_brackets:
            # Check if the stack is empty (unmatched closing bracket)
            if not stack:
                return False
            # Pop the top character from the stack
            top_char = stack.pop()
            # Check if the opening and closing brackets match
            if opening_brackets.index(top_char) != closing_brackets.index(char):
                return False

    # Check if the stack is empty (all brackets matched)
    return not stack


# Example usage:
test_string = "{[()]}"
print(is_balanced_parentheses(test_string))

test_string2 = ""
print(is_balanced_parentheses(test_string2))

test_string3 = "{[(mytest]}"
print(is_balanced_parentheses(test_string3))

test_string4 = "{[(mytest]}"
print(is_balanced_parentheses(test_string4))

test_string5 = "Hello"
print(is_balanced_parentheses(test_string5))