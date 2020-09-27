# Reflection by Jacob Boord

## Using a fenced code block, please display the correct output from running your program

```
Converting from Fahrenheit to Celsius!
32.00 degrees in Fahrenheit is 0.00 degrees in Celsius
```

## Using a fenced code block, give at least three lines of source code from `__main__.py` and explain them in a paragraph

```
    typer.echo(f"Converting from {from_unit.value} to {to_unit.value}!")
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    typer.echo(f"{temperature:.2f} degrees in {from_unit.value} is {converted_temperature:.2f} degrees in {to_unit.value}")
```

The above source code is responsible for running the converter and displaying the output correctly. Without this code, the converter itself would not run properly. In the first line of the code, the typer.echo produces a visual for the user. It uses the paramters of what conversion type the function is going to perform and adds text to produce a display for the user to view in the terminal window. The second line assigns a value to the variable converted_temperature. This value is taken from the convert.convert_temperature function using parameters that are inputed by the user. Finally, the last line of the code produces the output for the user by using typer.echo to display text along with the calculated conversion temperature.
