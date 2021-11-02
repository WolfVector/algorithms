#https://stackoverflow.com/questions/55187799/all-possible-combinations-of-operations-on-list-of-numbers-to-find-a-specific-nu

from itertools import permutations, combinations, combinations_with_replacement

number = ["1", "2", "3", "4"]
operations = ["+", "-", "*", "/"]
groups = ['X+X+X+X', 'X+X+(X+X)', 'X+(X+X)+X', '(X+X+X)+X', '(X+X)+X+X', 'X+(X+X+X)', '((X+X)+X)+X', 'X+(X+(X+X))', 'X+((X+X)+X)', '(X+X)+(X+X)', '(X+(X+X))+X']
seen = set()
target = 24

perm = permutations(number) #Get all the arragements

print("Operations")
for val_arr in perm: #iterate over the arragement of numbers
    for ope_arr in combinations_with_replacement(operations, 3): #iterate over the arragement of operations
        #Using the same arragement for the numbers, produce different operations
        for ope_perm in permutations(ope_arr, 3):
            #formula_key = "".join(ope_perm + val_arr)
            for pattern in groups:
                #Replace the '+' with the operations
                formula = "".join(l+r for l,r in zip([""] + list(ope_arr), pattern.split('+')))
                    
                #Replace 'X' with the numbers
                formula = "".join(l+r for l,r in zip([""] + list(val_arr), formula.split('X')))

                if formula not in seen and eval(formula) == target:
                    print(formula, '=', eval(formula))
                    seen.add(formula)
