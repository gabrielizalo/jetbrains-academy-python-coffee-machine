def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature = float(temperature)

    new_unit = ''
    new_temperature = 0

    if unit == 'C':
        new_temperature = celsius_to_fahrenheit(temperature)
        new_unit = 'F'
    else:
        new_temperature = fahrenheit_to_celsius(temperature)
        new_unit = 'C'

    print(new_temperature, new_unit)
