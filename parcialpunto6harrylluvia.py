def sistema_experto_harry():
    lluvia = input("¿Hoy llovió? (s/n): ").lower() == 's'
    visito_hagrid = input("¿Harry visitó a Hagrid hoy? (s/n): ").lower() == 's'
    visito_dumbledore = input("¿Harry visitó a Dumbledore hoy? (s/n): ").lower() == 's'

    # Evaluar la lógica
    if not lluvia:  # Si no llovió
        if visito_hagrid:  # Si visitó a Hagrid
            return "La proposición es verdadera: Harry visitó a Hagrid hoy."
        else:
            return "La proposición es falsa: Harry no visitó a Hagrid hoy."
    else:  # Si llovió
        if visito_dumbledore and not visito_hagrid:  # Visitó a Dumbledore y no a Hagrid
            return "La proposición es verdadera: Harry visitó a Dumbledore hoy y no a Hagrid."
        elif visito_hagrid:  # Si visitó a Hagrid
            return "La proposición es falsa: Harry no pudo haber visitado a Hagrid hoy porque llovió."
        else:  # Si no visitó a nadie
            return "La proposición es falsa: Harry no visitó ni a Hagrid ni a Dumbledore hoy."

# Ejecutar la función y mostrar el resultado
resultado = sistema_experto_harry()
print(resultado)
