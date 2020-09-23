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
    # TODO: display the two input parameters provided on the command line
    # TODO: perform the conversion of the temperature from one unit to another unit
    # TODO: display the original temperature and then the converted temperature, always using units


if __name__ == "__main__":
    # indirectly call the main function through the typer.run function
    typer.run(main)
