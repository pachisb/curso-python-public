#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ejemplo de decorador para "cronometrar" y además "depurar" una función (Módulo 7)

def my_timer(f):
    # permitir recibir cualquier nº y tipo de parámetros!
    def _timer(*args, **kwargs):
        import time
        start = time.time()  # anotar fecha/hora actual (segundos)
        log_date = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        print(f"{log_date} {f.__name__}() will be executed now")
        # invocar ahora a f() "normalmente" y guardar su resultado!
        result = f(*args, **kwargs)
        log_date = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        print(f"{log_date} {f.__name__}() execution time:", time.time() - start)
        print(f"{log_date} {f.__name__}() returned:", result)  # suponiendo que es "printable"
        return result  # devolver lo que había devuelto f!
    return _timer


@my_timer
def f(x):
    return x * 2


f(2)
