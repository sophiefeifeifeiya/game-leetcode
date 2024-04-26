def check_brackets(strings):
    results = []
    for s in strings:
        stack = []
        indexes_left_bracket = []
        indexes_right_bracket = []
        output = [' '] * len(s) 
        for index, c in enumerate(s):
            if c == '(':
                stack.append(c)
                indexes_left_bracket.append(index)
    
            elif c == ')':
                if len(stack) == 0:
                    output[index] = '?'
                else:
                    stack.pop()
                    indexes_left_bracket.pop()
        
        # end of string
        while stack:
            stack.pop()
            output[indexes_left_bracket.pop()] = 'x'
        
        results.append("".join(output))
    
    return results

# assume the input is a list of strings
test_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

print(check_brackets(test_strings))
