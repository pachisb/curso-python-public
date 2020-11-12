#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    f = open('examples/runtime.txt')
    s = f.readline()
    r = float(s.split("-")[-1])
    print(f"Value: {r}")
# para capturar un tipo de excepción concreto
except OSError as err:
    print(f"OS error: {err}")
# lo mismo pero sin recoger/usar la info del error
except ValueError:
    print("Could not convert data to an integer.")
# para capturar cualquier excepción (tras las concretas). NO RECOMENDABLE!
except:
    print("Unexpected error!")
    # opcional: volverla a lanzar tras el print (como no gestionarla)
    raise
# parte opcional (siempre tras except) para continuar si NO hubo error
else:
    print("Finished OK")
    f.close()
# parte opcional (siempre la última) que se ejecuta EN CUALQUIER CASO (al fina)
finally:
    print("End")
