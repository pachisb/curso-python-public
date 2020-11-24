#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 2 bis "leer ficheros CSV" del Módulo 9 (COMPLETA, con mejoras)


# command line arguments are stored in sys.argv
import sys
import random


def read_flashcard_file(filename, enc="utf-8"):
    """Devuelve un diccionario clave-valor en el que las claves son las preguntas, y
    los valores las respuestas, tal como se han leído de un fichero .csv"""

    question_dict = {}
    try:
        with open(filename, "r", encoding=enc) as f:
            for line in f:
                entry = line.strip()  # quitar \n, espacios ini/fin, etc.
                entry = entry.split(",")  # devuelve una lista de n (2) elem.
                if len(entry) == 2:  # Opcional: ignorar líneas vacías o "malas" (menos o más de 2 campos)
                    question = entry[0]
                    answer = entry[1]
                    question_dict[question] = answer
    except FileNotFoundError:
        print(f"Error reading '{filename}'', file not found or can not be opened!")
    except PermissionError:
        print(f"Error reading '{filename}'', you are not allowed to read this file!")
    except:
        print(f"Error reading '{filename}'', unexpected error!")

    return question_dict


# Nombre del fichero que se usará, puede ser por defecto o recibirlo como argumento

# flashcard_filename = "examples/flashcards_capitales_latin-1.csv"  # alternativa!
flashcard_filename = "examples/flashcards_capitales.csv"  # default value

if len(sys.argv) < 2:
    print("Note: you can supply a flash card file as a program argument.")
else:
    flashcard_filename = sys.argv[1]


# Leer el fichero en cuestión
print("Flash card file to use:", flashcard_filename)
question_dict = read_flashcard_file(flashcard_filename)
questions = list(question_dict.keys())
# print(len(questions))
if len(questions) == 0:
    # Ocurrió un error al leer el fichero, y no hay ninguna pregunta disponible
    quit()


# Escribir las instrucciones de juego
print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' or 'QUIT' to quit.")
print()


total = 0
correct = 0
while True:
    question = random.choice(questions)
    print("Question: " + question)

    answer = question_dict[question]

    user_input = input("Your guess: ")
    user_input = user_input.upper()
    if user_input == "QUIT":
        if total > 0:
            print("Your final score:", round(correct * 100.0 / total), "% correct!")
        print("Thanks for playing! Goodbye.")
        break
    elif user_input == answer:
        print("Correct!!! 🏆")
        correct += 1
    else:
        print("Sorry, the answer was: " + answer)

    total += 1
