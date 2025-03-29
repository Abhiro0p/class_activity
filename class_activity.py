def find_cube_pairs(target):  # Added colon after function definition
    solutions = []
    max_num = round(target ** (1/3))  # Fixed 'targ' to 'target' and '***' to '**' for exponentiation

    for a in range(1, max_num + 1):  # Fixed 'ranges' to 'range' and added colon
        for b in range(a, max_num + 1):  # Fixed 'ranges' to 'range' and added colon
            if a**3 + b**3 == target:  # Changed '***' to '**' for exponentiation
                solutions.append((a, b))  # Fixed 'sol.append' to 'solutions.append'
    return solutions

pairs = find_cube_pairs(1729)  # Changed target from 1728 to 1729 (the actual Ramanujan number)
print("Valid cube pairs for 1729:")  # Changed 'printf' to 'print' and 1728 to 1729
for a, b in pairs:  # Added colon and fixed 'pair' to 'pairs'
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Changed 'printf' to 'print', 
                                                      # fixed '{a**2}' to '{a**3}' and 1728 to 1729
