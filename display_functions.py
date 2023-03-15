#Rich functions to create the console structure
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

#utils
from time import sleep
from datetime import datetime


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]DockersMonitor[/b] application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


def build_layout() -> Layout:
    """Define the display form

    Returns:
        Layout: The layout object created
    """
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    
    layout["main"].split(
        Layout(name="upper"),
        Layout(name="lower")
    )

    layout["upper"].split_row(
        Layout(name="containers"),
        Layout(name="containers_info")
    )

    layout["lower"].split_row(
        Layout(name="logs", ratio=5),
        Layout(name="commands")
    )
    return layout
