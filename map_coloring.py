# Map Coloring using Backtracking

regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

result = {}

def is_safe(region, color):
    for n in neighbors[region]:
        if n in result and result[n] == color:
            return False
    return True

def solve(index):
    if index == len(regions):
        return True
    
    region = regions[index]
    
    for color in colors:
        if is_safe(region, color):
            result[region] = color
            
            if solve(index + 1):
                return True
            
            result.pop(region)
    
    return False

solve(0)

print("Solution:")
for r in result:
    print(r, "->", result[r])