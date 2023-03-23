from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.console import Console

#utils
from time import sleep
from pynput import keyboard
#display
from display_functions import build_layout, MainDisplay, Dockers
from display_functions import Commands,Containers, ContainersInfo,  Header, Logs 

if __name__ == "__main__": 
    layout = build_layout()
    dockersito = Dockers()
    main_display = MainDisplay() 
    layout["header"].update(Header())
    layout["containers"].update(Containers(main_display))
    layout["logs"].update(Logs(main_display))
    layout["commands"].update(Commands())
    layout["containers_info"].update(ContainersInfo(main_display))

    data = None
    with Live(layout, refresh_per_second=10, screen=False, vertical_overflow="fold"):
        while True:
            try:
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
            except KeyboardInterrupt:
                break
            
        
            
        