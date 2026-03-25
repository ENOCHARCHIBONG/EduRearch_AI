
def solve_linear_equation(equation):
    try:
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        if "x" in left:
            parts = left.split("x")
            a = int(parts[0]) if parts[0] not in ['', '+'] else 1
            b = int(parts[1].replace('+', '')) if '+' in parts[1] else int(parts[1]) if parts[1] else 0
        else:
            return 'Invalid equation format'
        c = int(right)
        x = (c - b) / a
        return f'Step 1: Subtract {b} from both sides\nStep 2: Divide by {a}\nAnswer: x = {x}'
    except:
        return 'Sorry, only simple equations like 2x + 3 = 7 can be solved'
