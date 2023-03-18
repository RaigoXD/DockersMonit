from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.console import Console

#utils
from time import sleep
from pynput import keyboard
#display
from display_functions import build_layout, MainDisplay, Dockers

if __name__ == "__main__": 
    layout = build_layout()
    dockersito = Dockers()
    main_display = MainDisplay() 
    layout["header"].update(main_display.Header())
    layout["containers"].update(main_display.Containers(main_display))
    layout["logs"].update(main_display.Logs(main_display))
    layout["commands"].update(main_display.Commands())
    layout["containers_info"].update(main_display.ContainersInfo(main_display))

    data = None
    with Live(layout, refresh_per_second=10, screen=False, vertical_overflow="fold"):
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
                elif event.key == keyboard.Key.f9:
                    dockersito.change_status_container(main_display.actual_id_container, 1)
                elif event.key == keyboard.Key.f1:
                    dockersito.change_status_container(main_display.actual_id_container, 2)
                elif event.key == keyboard.Key.f5:
                    dockersito.change_status_container(main_display.actual_id_container, 3)
    
                elif event.key == keyboard.KeyCode.from_char("q"):
                    break
            
        
            
        