def ten_different_values():
    tableau = [0 for i in range(10)]
    print(tableau)
    for i in range(10):
        value = input('Value : ')
        tableau[i] = value
    print(tableau)

    if len(tableau) != len(set(tableau)):
        print('Double caracteres exist')
    else:
        print('No double caractere')

def bubble_sort(tableau):
    for i in range(len(tableau)-1):
        for j in range(len(tableau)-1):
            if(tableau[j+1] < tableau[j]):
                tableau[j+1], tableau[j] = tableau[j], tableau[j+1]

def insert_sort(tableau, n):
    for i in range(n-1):
        x = tableau[i]
        j = i
        while j > 0 and tableau[j-1] > x:
            tableau[j] = tableau[j-1]
            j = j - 1
        tableau[j] = x


print("Execution")

# ten_different_values()
test = [12, 10 , 4, 5, 6, 7, 8, 9, 10, 1]
bubble_sort(test)
print(test)
insert_sort(test, 5)
print(test)



