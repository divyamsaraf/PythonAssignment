def count_customers(N, S):
    available_computers = N
    waiting_customers = set()
    walked_away_count = 0
    
    for char in S:
        if char in waiting_customers:
            waiting_customers.remove(char)
            available_computers += 1
        else:
            # Customers arrival
            if available_computers > 0:
                # Allocate
                # print('Arrival:', char)
                available_computers -= 1
            else:
                # No computer available, customer walks away
                walked_away_count += 1
                # print('Walked Away:', char)

            # Add customer to the waiting set
            waiting_customers.add(char)
            # print('Added to waiting list', char)
    
    return walked_away_count

N = int(input("Enter the number of computers: "))
S = input("Enter the sequence of events: ")

result = count_customers(N, S)
print("Number of customers who walked away:", result)
