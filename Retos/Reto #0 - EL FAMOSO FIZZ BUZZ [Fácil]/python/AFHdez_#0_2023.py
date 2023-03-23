 '''CHALLENGE 1:  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".'''
 
 if numbers %3==0:
        print("fizz")
    if numbers %5==0:
        print("buzz")
    if numbers %3 %5==0:
        print("fizzbuzz")

    print(numbers, "\n" )
