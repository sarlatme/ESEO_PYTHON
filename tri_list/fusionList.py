import modificationListe as modif
import triListe as tri

def merge_sort(tableauA, tableauB):
    tri.bubble_sort(tableauA)
    tri.bubble_sort(tableauB)
    i = 0
    j = 0
    k = 0
    
    n = len(tableauA) + len(tableauB)
    tableau = [0 for a in range(n)]

    while i < len(tableauA) and j < len(tableauB):
        if tableauA[i] < tableauB[j]:
            tableau[k] = tableauA[i]
            i = i + 1
            k = k + 1
        else:
            tableau[k] = tableauB[j]
            j = j + 1
            k = k + 1
    
    while i < len(tableauA):
        tableau[k] = tableauA[i]
        i = i + 1
        k = k + 1
    
    while j < len(tableauB):
        tableau[k] = tableauB[j]
        j = j + 1
        k = k + 1
    
    print(tableau)

print('Execution')
testA = [1,5,96,2,14]
testB = [4,7,75,23,8,69,188]
merge_sort(testA, testB)