________________________________________________________________________________________________________________
            ________  _______   ________  _____ ______   _______  _________  ________  ___  ________     
           |\   ____\|\  ___ \ |\   __  \|\   _ \  _   \|\  ___ \|\___   ___\\   __  \|\  \|\   ____\    
           \ \  \___|\ \   __/|\ \  \|\  \ \  \\\__\ \  \ \   __/\|___ \  \_\ \  \|\  \ \  \ \  \___|    
            \ \  \  __\ \  \_|/_\ \  \\\  \ \  \\|__| \  \ \  \_|/__  \ \  \ \ \   _  _\ \  \ \  \       
             \ \  \|\  \ \  \_|\ \ \  \\\  \ \  \    \ \  \ \  \_|\ \  \ \  \ \ \  \\  \\ \  \ \  \____  
              \ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\  \ \__\ \ \__\\ _\\ \__\ \_______\
               \|_______|\|_______|\|_______|\|__|     \|__|\|_______|   \|__|  \|__|\|__|\|__|\|_______|
                                                                                                                                                                                           
                    _______   ________   ________  ___  ________   _______   ___              
                   |\  ___ \ |\   ___  \|\   ____\|\  \|\   ___  \|\  ___ \ |\  \             
                   \ \   __/|\ \  \\ \  \ \  \___|\ \  \ \  \\ \  \ \   __/|\ \  \            
                    \ \  \_|/_\ \  \\ \  \ \  \  __\ \  \ \  \\ \  \ \  \_|/_\ \  \           
                     \ \  \_|\ \ \  \\ \  \ \  \|\  \ \  \ \  \\ \  \ \  \_|\ \ \__\          
                      \ \_______\ \__\\ \__\ \_______\ \__\ \__\\ \__\ \_______\|__|          
                       \|_______|\|__| \|__|\|_______|\|__|\|__| \|__|\|_______|   ___        
                                                                                  |\__\       
                                                                                  \|__|       

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

**Hello! Welcome to the Geometric Engine!**

_This Tutorial will help you get an insight on getting started with a project in the Geometric Engine!_

**Chapter 1 : Camera Controller**

The base camera controller comes with 4 (user-allowed) functions:
            
            - Move
            - Rotate
            - Mouse_Controller
            - Reset

**Chapter 1.1 : The Move Function**

The `Move` function as the name states, is responsible for handling player-movement.

It takes in 4 parameters:

```
def Move(self, dt, key, flyCam=False):
```
Parameter Breakdown:

  dt - _DeltaTime_ (A Timer that is called every frame to calculate the positions of objects in a scene)
  
  key - _reference to `var_name = pygame.get_pressed()`_ ([Learn More](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed))
  
  flyCam - _Can the camera fly Up/Down?_ (E/Q - Up/Down)
__________________________________________
**Chapter 1.2 : The Rotate Function**

The `Rotate` function allows the player to rotate the Camera when pressing the Arrow Keys.
