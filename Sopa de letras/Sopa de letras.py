#SOPA
with open('sopa de letras.txt', 'r') as f:
    letras_matrix = f.readlines()
    for i in range(len(letras_matrix)):
        letras_matrix[i] = letras_matrix[i].rstrip('\n')
        letras_matrix[i] = letras_matrix[i].replace(' ', '')
    print(letras_matrix)
#PALABRAS
with open('palabras.txt', 'r') as f:
    palabras = f.readlines()
    for i in range(len(palabras)):
        palabras[i] = palabras[i].replace('\n', '')
        palabras[i] = palabras[i].replace(' ', '')
    print(palabras)
ady = [[-1, -1], [-1, 0], [-1, 1],
       [ 0, -1],          [ 0, 1],
       [ 1, -1], [ 1, 0],[ 1, 1]]

def busqueda_inicial(current_palabra, pos):
    letra = current_palabra[0]
    for i in range(len(letras_matrix)):
        for j in range(len(letras_matrix[i])):
            if letra == letras_matrix[i][j]:
                pos.append([i, j])
    return

def busqueda_vec(current_palabra, pos_busq, l_pyv):
    letra = current_palabra[1]
    for j in pos_busq:
        for a in ady:
            x = j[0] + a[0]
            y = j[1] + a[1]
            len_mat = len(letras_matrix[1])
            if y < len_mat and x < len_mat and y >= 0 and x > 0:
                if letra == letras_matrix[x][y]:
                    l_pyv.append([j, a])
    return

def busqueda_resto(curr_palabra, l_pyv):
    for j in l_pyv:
        i = 0
        breaker = True
        while breaker:
            x = j[0][0] + j[1][0] * (i)
            y = j[0][1] + j[1][1] * (i)
            len_mat = len(letras_matrix[1])
            len_pal = len(curr_palabra)
            if i == len_pal:
                return
            elif y >= len_mat or x >= len_mat or y < 0 or x < 0:
                pos_palabra.clear()
                breaker = False
                continue
            else:
                if curr_palabra[i] == letras_matrix[x][y]:
                    pos_palabra.append([letras_matrix[x][y], x, y])
                else:
                    pos_palabra.clear()
                    breaker = False
            i += 1

def limpieza(lista):
    copy_list = lista
    for l in range(len(lista)-1, -1, -1):
        if len(lista[l]) < 2:
            del copy_list[l]
    return copy_list

current_pos = []
palabra_y_vector = []
pos_palabra = []
for p in palabras:
    busqueda_inicial(p, current_pos)
    busqueda_vec(p, current_pos, palabra_y_vector)
    palabra_y_vector = limpieza(palabra_y_vector)
    busqueda_resto(p, palabra_y_vector)
    print(pos_palabra)
    current_pos.clear()
    palabra_y_vector.clear()
    pos_palabra.clear()

