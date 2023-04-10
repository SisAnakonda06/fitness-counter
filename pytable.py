import numpy as np

table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.set_printoptions(formatter={'float': lambda x: format(x, 'g')})
i = 0
j = 0
def load(type_t):
    global table
    loaded_table = np.loadtxt('Data/tabulka.txt', delimiter=' ')
    table = np.array(loaded_table)
    print(type(table))    
    if type_t == "sring":
        table = str(table)
        table = table.replace("[", "")
        table = table.replace("]", "")
        return table
    elif type_t == "numpy":
        return np.array(table)

def save(table):
    np.savetxt('Data/tabulka.txt', table, delimiter=' ', fmt='%i')

def transfer():
    global i
    global j
    result = ""
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            result += str(table[i][j]) + " "
        result += ","
    return result
        
    
print(transfer())