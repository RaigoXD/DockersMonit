from rich.live import Live
from rich import print
from rich.panel import Panel
from time import sleep

#display
from display_functions import build_layout, Header


if __name__ == "__main__": 
    layout = build_layout() 
    layout["header"].update(Header())
    
    print(layout)
    
    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            sleep(5)
            
            layout["containers_info"].update(Panel("Panel bonito"))
            
        