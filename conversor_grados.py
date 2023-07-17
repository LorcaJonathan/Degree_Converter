import signal

def handle_interrupt(signal, frame):
    print("\n¡ADIOS!")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

while True:

    pregunta = input("¿Quieres pasar los grados a Celsius o Fahrenheit? (C-F / F-C)")
    try:
        if (pregunta == "C-F"):

            pregunta_celsius = float(input("Introduce la temperatura en grados Celsius: "))
            fahrenheit = (pregunta_celsius * 9 / 5) + 32
            print(f"{pregunta_celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")

        elif (pregunta == "F-C"):
            pregunta_fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            celsius = (pregunta_fahrenheit -32) *5 / 9
            print(f"{pregunta_fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")

        else:
            print("Los valores introducidos no son válidos, introdúcelos de nuevo.")

        respuesta = (input("¿Quieres hacer otra conversión? (s/n):"))
        if respuesta == "s" or respuesta == "S":
            continue
        elif respuesta == "n" or respuesta == "N":
            print("¡ADIOS!")
            break
        else:
            print("No es una respuesta válida, por favor responde con: (s/n)")
            print("\nSiendo s para introducir otra frase y n para salir del script.")

    except KeyboardInterrupt:
        print("\n¡ADIOS!")
        break

