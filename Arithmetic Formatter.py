import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    for problem in problems:
        x, y, z = re.split(" ", problem)
        
        if y not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (x.isdigit() and z.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(x) > 4 or len(z) >4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(x), len(z)) + 2
        line1 += x.rjust(width) + "    "
        line2 += y + z.rjust(width - 1) + "    "
        line3 += "-" * width + "    "
        
        if show_answers:
            if y == '+':
                answer = str(int(x) + int(z))
            else:
                answer = str(int(x) - int(z))
            line4 += answer.rjust(width) + "    "
    
    arranged_problems += line1.rstrip() + "\n"
    arranged_problems += line2.rstrip() + "\n"
    arranged_problems += line3.rstrip()
    
    if show_answers:
        arranged_problems += "\n" + line4.rstrip()
    
    return arranged_problems