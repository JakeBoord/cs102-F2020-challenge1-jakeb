"""Define the command-line interface for the converter program."""

import typer

from converter import convert
from converter import units


def main(
    from_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.celsius,
    to_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.fahrenheit,
    temperature: float = typer.Option(98.6, min=-130, max=140),
):
    """Convert units.from Fahrenheit to Celsius or from Celsius to Fahrenheit."""
    # display the two input parameters provided on the command line
    typer.echo(f"Converting from {from_unit.value} to {to_unit.value}!")
    # perform the conversion of the temperature from one unit to another unit
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    # display the original temperature and then the converted temperature, always using units
    typer.echo(
        f"{temperature:.2f} degrees in {from_unit.value} is {converted_temperature:.2f} degrees in {to_unit.value}"
    )


if __name__ == "__main__":
    # indirectly call the main function through the typer.run function
    typer.run(main)
