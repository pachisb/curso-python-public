#!/usr/bin/env python3
# -*- coding: utf-8 -*-

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
result = ""

for c in text:
    if c >= "a" and c <= "x":
        c = ord(c) + 2
        c = chr(c)
    elif c == "y":
        c = "a"
    elif c == "z":
        c = "b"
    # nota: otros caracteres (espacios, puntuación) no se han modificado
    result = result + c

print(result)
print()
print()


##################################################


# alternativa mucho más compleja, con listas y generadores y str.translate():
orig = [chr(i + ord("a")) for i in range(26)]
dest = [chr(i + ord("c")) for i in range(24)] + ["a", "b"]
orig = "".join(orig)
dest = "".join(dest)
print("CADENA 1 USADA PARA EL 'TRADUCTOR':", orig)
print("CADENA 2 USADA PARA EL 'TRADUCTOR':", dest)

transf = str.maketrans(orig, dest)
print("DICCIONARIO PREPARADO PARA EL 'TRADUCTOR':", transf)
print()

print(text.translate(transf))
# Una vez que hemos leido el texto, veremos que la solución final es "traducir" el texto "map"
# print("map".translate(transf))
