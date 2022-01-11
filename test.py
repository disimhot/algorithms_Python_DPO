n, m = [int(x) for x in input().split()]
def Right(n):
    return n * 2

def Left(n):
    return n - 1

def calculate(n, m):
    visited = set()
    stepLayer = set()
    nextLayer = set()
    stepLayer.add(n)
    step = 0
    
    while True:
        while stepLayer:
            candidate = stepLayer.pop()
            if candidate not in visited:
                visited.add(candidate);
                if candidate == m:
                    return step
                l = Left(candidate)
                r = Right(candidate)
                if l > 0 and l not in visited:
                    nextLayer.add(l)
                if r < 10000 and r not in visited:
                    nextLayer.add(r)
        while nextLayer:
            stepLayer.add(nextLayer.pop())
        step+=1
        if not stepLayer:
            break
    return -1

print(calculate(n, m))