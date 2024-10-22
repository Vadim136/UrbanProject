import random


first_stone = random.randrange(3,20)

pairs_list = []
print(first_stone)
for i in range(1, first_stone):
    for j in range(2, first_stone):
        if first_stone % (i+j) == 0 and i != j:
            pairs_list.append((i,j))
            
        else:
            continue 


unique_pairs = sorted(set(tuple(sorted(pair)) for pair in pairs_list))

password = "".join(f"{i}{j}" for i, j in unique_pairs)

print(password)
