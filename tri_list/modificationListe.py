def compression(tableau):
    result = []
    for i in range(len(tableau)-1):
        if tableau[i] != 0:
            result.append(tableau[i])
    return result    

print('Execution')
test = [0, 2, 5, 6, 9, 0, 0, 6, 0, 4, 8, 0, 1, 0, 0, 11, 0, 18, 19, 20]
compression(test)
print(test)
test = compression(test)
print(test)