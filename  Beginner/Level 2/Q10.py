def stone_piles(n):
    piles = []
    
    start = 2 if n % 2 == 0 else 1
    
    for i in range(start, n, 2):
        piles.append(i)
    
    return piles

n = int(input("Enter the number of stones in the first pile: "))

result = stone_piles(n)
print(f"Stones in a single pile: {result}")
