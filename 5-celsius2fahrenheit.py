def celsius2fahrenheit(nCelsius):
    return nCelsius * 1.8 + 32

#input
nCelsiusInput = int(input("what is the temperature in celsius?"))
#processing
nFahrenheit = celsius2fahrenheit(nCelsiusInput)
#output
print("The temperature in fahrenheit is", nFahrenheit)
