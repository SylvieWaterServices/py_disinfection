"""Console script for py_disinfection."""

import typer
from rich.console import Console

# from py_disinfection.estimation import conservative_ct, interpolate_ct, regression_ct
from py_disinfection.py_disinfection import (
    CTReqEstimator,
    DisinfectionSegment,
    DisinfectionSegmentOptions,
    DisinfectionTarget,
    DisinfectantAgent,
)

app = typer.Typer(
    name="disinfect",
    help="A command-line tool for drinking water disinfection analysis.",
)
console = Console()


def convert_temperature(temp: float, unit: str) -> float:
    """Convert Fahrenheit to Celsius if needed."""
    if unit.lower() == "f":
        return (temp - 32) * 5.0 / 9.0
    return temp


# @app.command()
# def estimate_ct(
#     temp: float = typer.Option(..., "-t", "--temp", help="Temperature value"),
#     temp_unit: str = typer.Option(
#         "C", "-u", "--temp-unit", help="Temperature unit: C or F"
#     ),
#     ph: float = typer.Option(..., "-p", "--ph", help="pH level"),
#     chlorine: float = typer.Option(
#         ..., "-c", "--concentration", help="Disinfectant concentration in mg/L"
#     ),
#     method: str = typer.Option(
#         ...,
#         "-m",
#         "--method",
#         help="Estimation method: conservative, interpolation, regression",
#     ),
# ):
#     """Estimate CT based on method (conservative, interpolation, regression)."""
#     temp_celsius = convert_temperature(temp, temp_unit)

#     if method == "conservative":
#         ct = conservative_ct(temp_celsius, ph, chlorine)
#     elif method == "interpolation":
#         ct = interpolate_ct(temp_celsius, ph, chlorine)
#     elif method == "regression":
#         ct = regression_ct(temp_celsius, ph, chlorine)
#     else:
#         console.print(
#             "[red]Invalid method. Use 'conservative', 'interpolation', or 'regression'.[/red]"
#         )
#         return

#     console.print(f"Estimated CT: [green]{ct} min-mg/L[/green]")


@app.command()
def analyze_segment(
    volume: float = typer.Option(..., "-v", "--volume", help="Volume in gallons"),
    temp: float = typer.Option(..., "-t", "--temp", help="Temperature value"),
    temp_unit: str = typer.Option(
        "C", "-u", "--temp-unit", help="Temperature unit: C or F"
    ),
    ph: float = typer.Option(..., "-p", "--ph", help="pH level"),
    chlorine: float = typer.Option(
        ..., "-c", "--concentration", help="Disinfectant concentration in mg/L"
    ),
    method: str = typer.Option(
        ...,
        "-m",
        "--method",
        help="Estimation method: conservative, interpolation, regression",
    ),
    target: str = typer.Option(
        ..., "-T", "--target", help="Disinfection target: giardia, viruses"
    ),
    agent: str = typer.Option(
        ...,
        "-a",
        "--agent",
        help="Disinfectant agent: free_chlorine, chlorine_dioxide, chloramines",
    ),
    baffling_factor: float = typer.Option(
        ..., "-b", "--baffling-factor", help="Baffling factor (0-1)"
    ),
    peak_flow: float = typer.Option(
        ..., "-f", "--peak-flow", help="Peak hourly flow in gallons per minute"
    ),
):
    """Analyze a disinfection segment and print results."""
    if method not in {"conservative", "interpolation", "regression"}:
        console.print(
            "[red]Invalid method. Use 'conservative', 'interpolation', or 'regression'.[/red]"
        )
        return

    if agent not in {"free_chlorine", "chlorine_dioxide", "chloramines"}:
        console.print(
            "[red]Invalid agent. Use 'free_chlorine', 'chlorine_dioxide', or 'chloramines'.[/red]"
        )
        return
    if method not in {"conservative", "interpolation", "regression"}:
        console.print(
            "[red]Invalid method. Use 'conservative', 'interpolation', or 'regression'.[/red]"
        )
        return

    agent_enum = DisinfectantAgent[agent.upper()]
    method_enum = CTReqEstimator[method.upper()]
    temp_celsius = convert_temperature(temp, temp_unit)

    options = DisinfectionSegmentOptions(
        volume_gallons=volume,
        agent=agent_enum,
        temperature_celsius=temp_celsius,
        ph=ph,
        concentration_mg_per_liter=chlorine,
        ctreq_estimator=method_enum,
        baffling_factor=baffling_factor,
        peak_hourly_flow_gallons_per_minute=peak_flow,
    )

    segment = DisinfectionSegment(options)
    results = segment.analyze()

    console.print("[bold yellow]Segment Parameters:[/bold yellow]")
    for key, value in options.__dict__.items():
        console.print(f"{key}: [cyan]{value}[/cyan]")

    console.print("\n[bold green]Disinfection Analysis Results:[/bold green]")
    for key, value in results.items():
        console.print(f"{key}: [cyan]{value}[/cyan]")


if __name__ == "__main__":
    app()
