#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 2 "tablero de 27 piezas" del Módulo 7

#############################################################################

# Para comparar y entenderlo mejor solamente...
# Versión sencilla SIN clases (NO es la solución a lo que se pide en el ejercicio)

def posic_ficha(tablero, ficha):
    """Devuelve una tupla con las coordenadas (x, y: 0..6, 0..4) de una "ficha" en el tablero,
    que se espera que sea una matriz bien formada (...)"""
    for y in (range(4)):
        if ficha in tablero[y]:
            x = tablero[y].index(ficha)  # posición del elemento
            return (x, y)
    return (-1, -1)  # no debería ocurrir, pero por si acaso

def movim_es_valido(tablero, t1, t2):
    """Devuelve True si el movimiento (coord. x, y: 0..6, 0..4, origen y destino) es válido
    en el tablero. Se espera que el tablero sea una matriz bien formada (...)"""
    x1, y1 = t1
    x2, y2 = t2
    if ( x1 < 0 or x2 < 0 or x1 >= 7 or x2 >= 7 or
            y1 < 0 or y2 < 0 or y1 >= 4 or y2 >= 4 ):
        return False
    elif x1 == x2 and y1 == y2 - 1:  # abajo
        print("Abajo")
        return posic_ficha(tablero, " ") == (x2, y2)  # será válido si el hueco está abajo
    elif x1 == x2 and y1 == y2 + 1:  # arriba
        print("Arriba")
        return posic_ficha(tablero, " ") == (x1, y1)
    elif y1 == y2 and x1 == x2 - 1:  # izda
        print("Izquierda")
        return posic_ficha(tablero, " ") == (x1, y1)
    elif y1 == y2 and x1 == x2 + 1:  # dcha
        print("Derecha")
        return posic_ficha(tablero, " ") == (x2, y2)
    else:
        print("Incorrecto")
        return False  # movimiento "ilegal"


# Forma de uso esperada en este caso:
# tabl_ini = [['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['H', 'I', 'J', 'K', ' ', 'M', 'N'],
#             ['Ñ', 'O', 'P', 'Q', 'L', 'S', 'T'], ['U', 'V', 'W', 'X', 'R', 'Y', 'Z']]
# print(movim_es_valido(tabl_ini, (4, 0), (4, 1)))

#############################################################################

# Solución a lo que se pide realmente en el ejercicio (CON clases)...

class Tablero:
    def __init__(self, matriz):
        """Inicializa el tablero con los datos recibidos en la matriz 4x7 (4 filas).
        Se espera recibir una matriz con el tamaño correcto, y cada posición será una
        cadena de un sólo carácter (letras mayúsculas o espacio). No pueden repetirse"""
        # self.fichas = matriz
        # Lo anterior valdría, pero por comodidad permito que lo recibido sea una lista de cadenas
        # (o cualquier cosa equivalente) además de una matriz, recorriendo explícitamente los elem.:
        self.fichas = []
        for i in matriz:
            temp_list = list(i)  # convierte los elementos recib. (cualquier tipo de secuencia!) en lista
            self.fichas.append(temp_list)
        # Una posible ventaja de las clases es que puedo guardar más información asociada / útil...
        if self.comprobar_estado_correcto():
            self.pos_hueco = self.posic_ficha(" ")
        else:
            self.pos_hueco = None  # usamos esto como forma de indicar el error

    def __str__(self):
        """Muestra el tablero por pantalla, simplemente para depuración o uso interno"""
        cad = "Las fichas están así:\n"
        for i in self.fichas:
            cad = cad + str(i)  # una lista ya "sabe" convertirse a cadena como nos interesa
            cad = cad + "\n"
        cad = cad + "El hueco está en las coordenadas:\n"
        cad = cad + str(self.pos_hueco)  # la tupla igual
        return cad

    def comprobar_estado_correcto(self):
        """Devuelve True si no hay letras repetidas ni faltan, son mayúsc. todas y hay un hueco"""
        s = set()
        if len(self.fichas) != 4:
            return False
        for y in (range(4)):
            if len(self.fichas[y]) != 7:
                return False
            for ficha in self.fichas[y]:
                s.add(ficha)
        # Comprobar propiamente
        for i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ":
            if not i in s:
                return False
        return True

    def posic_ficha(self, ficha):
        """Devuelve una tupla con las coordenadas (x, y: 0..6, 0..4) de una "ficha" en el tablero"""
        for y in (range(4)):
            if ficha in self.fichas[y]:
                x = self.fichas[y].index(ficha)  # posición del elemento
                return (x, y)
        return (-1, -1)  # no debería ocurrir, pero por si acaso

    def movim_es_valido(self, t1, t2):
        """Devuelve True si el movimiento (coord. x, y: 0..6, 0..4, origen y destino) es válido"""
        x1, y1 = t1
        x2, y2 = t2
        if ( x1 < 0 or x2 < 0 or x1 >= 7 or x2 >= 7 or
             y1 < 0 or y2 < 0 or y1 >= 4 or y2 >= 4 ):
            return False
        elif x1 == x2 and y1 == y2 - 1:  # abajo
            print("Abajo")
            return self.posic_ficha(" ") == (x2, y2)  # será válido si el hueco está abajo
        elif x1 == x2 and y1 == y2 + 1:  # arriba
            print("Arriba")
            return self.posic_ficha(" ") == (x1, y1)
        elif y1 == y2 and x1 == x2 - 1:  # izda
            print("Izquierda")
            return self.posic_ficha(" ") == (x1, y1)
        elif y1 == y2 and x1 == x2 + 1:  # dcha
            print("Derecha")
            return self.posic_ficha(" ") == (x2, y2)
        else:
            print("Incorrecto")
            return False  # movimiento "ilegal"


# Algunos datos de ejemplo para probar (para construir el tablero)

# NOTA: lo siguiente es equivalente (y lo que se genera / imprime), pero
# por comodidad se preferirá / usará la forma "lista con 4 cadenas"...!
ini = [ ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        ['H', 'I', 'J', 'K', ' ', 'M', 'N'],
        ['Ñ', 'O', 'P', 'Q', 'L', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'R', 'Y', 'Z']]
print(ini)
ini = ["ABCDEFG", "HIJK MN", "ÑOPQLST", "UVWXRYZ"]  # más breve y también lo permitimos
fin = ["ABCDEFG", "HIJKLMN", "ÑOPQRST", "UVWXYZ "]
mal = ["AAADEFG", "HIJK MN", "ÑOPQLST", "UVWXRYZ"]  # repetidas! también casos con núm != 28
t1 = Tablero(ini)
t2 = Tablero(fin)
t3 = Tablero(mal)
print(t1)

print("Estado correcto 1:", t1.comprobar_estado_correcto())
print("Estado correcto 2:", t2.comprobar_estado_correcto())
print("Estado correcto 3:", t3.comprobar_estado_correcto())

print(t1.movim_es_valido((4, 0), (4, 1)))
print(t1.movim_es_valido((5, 0), (5, 1)))  # no posible
print(t1.movim_es_valido((4, 0), (4, 2)))  # "ilegal"
