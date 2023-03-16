from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.console import Console

#utils
from time import sleep
from pynput import keyboard
#display
from display_functions import build_layout, MainDisplay

console = Console(force_terminal=True)


if __name__ == "__main__": 
    layout = build_layout()
    main_display = MainDisplay() 
    layout["header"].update(main_display.Header())
    layout["containers"].update(main_display.Containers(main_display))
    layout["logs"].update(main_display.Logs(main_display))
    
    console.print(layout)
    data = None
    with Live(layout, refresh_per_second=60, screen=True):
        while True:
            sleep(0.1)
            
            with keyboard.Events() as events:
                event = events.get(1e6)
                if event.key == keyboard.Key.down:
                    if main_display.actual_num_container + 1 < main_display.len_containers:
                        main_display.actual_num_container += 1
    
                elif event.key == keyboard.Key.up:
                    if main_display.actual_num_container - 1 >= 0:
                        main_display.actual_num_container -= 1
    
                elif event.key == keyboard.KeyCode.from_char("q"):
                    break

    print(main_display.len_containers)
            
        
            
        