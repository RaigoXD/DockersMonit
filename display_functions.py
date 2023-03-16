#Rich functions to create the console structure
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.syntax import Syntax

#utils
from time import sleep
from datetime import datetime

#Dockers functions
from dockers_functions import Dockers

class MainDisplay:
    
    len_containers = 0
    actual_num_container = 0
    actual_id_container:str
    
    class Header:
        """Display header with clock."""

        def __rich__(self,) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_column(justify="center", ratio=1)
            grid.add_column(justify="right")
            grid.add_row(
                "[b]DockersMonitor[/b] application",
                datetime.now().ctime().replace(":", "[blink]:[/]"),
            )
            return Panel(grid, style="white on blue")

    class Containers:
        def __init__(self, main_display):
            self.__main_display = main_display
            
        def __rich__(self) -> Panel:
            dockersito = Dockers()
            containers_info = dockersito.list_containers()
            self.__main_display.len_containers = len(containers_info)
            table = Table(expand=True, box= box.SIMPLE_HEAD)
            table.add_column("Id", justify="center")
            table.add_column("Name", justify="center")
            table.add_column("Status", justify="center")

            for index,container in enumerate(containers_info):
                if index == self.__main_display.actual_num_container:
                    self.__main_display.actual_id_container = container[0]
                    table.add_row(container[0][:5], container[1], container[2], style="u bold")
                else:
                    table.add_row(container[0][:5], container[1], container[2])
    
            return Panel(table,title=f"[b]Containers {self.__main_display.len_containers}", border_style="red")
        
    class Logs:
        def __init__(self, main_display):
            self.__main_display = main_display

        def __rich__(self) -> Panel:
            dockersito = Dockers()
            logs = dockersito.container_logs(self.__main_display.actual_id_container).decode("utf-8")
    
            logs = Syntax(logs[-800:-1], "python", line_numbers=True,start_line=1)
            return Panel(logs, title=f"[b]Logs {self.__main_display.actual_id_container}", border_style="blue")
            
            

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
