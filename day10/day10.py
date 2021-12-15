def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip())

    bracket_map = {
        '<' : '>',
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }

    score_map = {
        '>' : 25137,
        '}' : 1197,
        ']' : 57,
        ')' : 3
    }

    score = 0
    for chunk in input_array:
        stack = []
        for bracket in chunk:
            if bracket in bracket_map:
                stack.append(bracket)
            else:
                if bracket != bracket_map.get(stack[-1]):
                    score += score_map.get(bracket)
                    break
                else:
                    stack.pop()

    return score

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip())

    bracket_map = {
    '<' : '>',
    '{' : '}',
    '[' : ']',
    '(' : ')'
    }

    score_map = {
    '>' : 4,
    '}' : 3,
    ']' : 2,
    ')' : 1
    }

    score_array = []
    incomplete_array = input_array.copy()
    
    # remove corrupted lines
    for chunk in input_array:
        stack = []
        for bracket in chunk:
            if bracket in bracket_map:
                stack.append(bracket)
            else:
                if bracket != bracket_map.get(stack[-1]):
                    incomplete_array.remove(chunk)
                    break
                else:
                    stack.pop()

    # incomplete lines only
    for chunk in incomplete_array:
        stack = []
        for bracket in chunk:
            if len(stack) == 0:
                stack.append(bracket)
            else:
                if bracket == bracket_map.get(stack[-1]):
                    stack.pop()
                else:
                    stack.append(bracket)
        score = 0
        for bracket in reversed(stack):
            close_bracket = bracket_map.get(bracket)
            score = (score * 5) + score_map.get(close_bracket)
        score_array.append(score)
    
    return sorted(score_array)[(len(score_array) - 1) // 2]