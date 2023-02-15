```
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
```

**Hello! Welcome to the Geometric Engine!**

_This Tutorial will help you get an insight on getting started with a project in the Geometric Engine!_

**Chapter 0 : Base Vocabulary**

Before we get started on learning how everything works, it's important you know what each individual thing is used for
so you can increase your productivity throughout the Engine!

       ~ Delta Time - A Timer that is called every frame to calculate the pos/rot/scale of objects in a scene
       ~ Entities ~ Fancy way of saying an object

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

  dt - _DeltaTime_
  
  key - _reference to `var_name = pygame.get_pressed()`_ ([Learn More](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed))
  
  flyCam - _(boolean) Enables/Disables cam fly controller_

```
while (1):
    key = pygame.key.get_pressed()
    dt = clock.tick(30) / 1000
    
    # Player Movement
    cam.Move(dt, key, False)
```
__________________________________________
**Chapter 1.2 : The Rotate Function**

The `Rotate` function allows the player to rotate the Camera when pressing the Arrow Keys.

This function takes in 3 Parameters:

```
def Rotate(self, dt, key):
```

Parameter Breakdown:
   
   dt - _Delta Time_
   
   key - _reference to `var_name = pygame.get_pressed()`_ ([Learn More](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed))

```
while (1):
    key = pygame.key.get_pressed()
    dt = clock.tick(30) / 1000
    
    # Player Movement
    cam.Rotate(dt, key, False)
```
__________________________________________
**Chapter 1.3 : The Reset Function**

The `Rotate` function allows the player to rotate the Camera when pressing the Arrow Keys.

This function takes in 3 Parameters:

```
def Reset(self, key):
```

Parameter Breakdown:

   key - _reference to `var_name = pygame.get_pressed()`_ ([Learn More](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed))

```
while (1):
    key = pygame.key.get_pressed()
    
    # Reset Player Controller
    cam.Reset(key)
```
__________________________________________
**Chapter 2 : Scenes**

Scenes, like in a play. Are a blank canvas, you can create new scenes by calling the `CreateScene` function within the Camera Class.

```
def CreateScene((w,h)):
```

Parameter Breakdown:
       w - Scene Width
       h - Scene Height

Scenes are extremely useful for things like:
    - Switching between menus
    
    - Switching between levels
    
    - etc
__________________________________________
**Chapter 3 : 3D Models**

The Geometric Engine can currently support simple primitave objects such as Quads or Cubes.
But there are expirimental classes being worked on to allow users to import their own 3D Models.

A good example of this would be the `Imported_OBJ` class in _'Primitives.py'_.
To import a 3D model:

    - Create a '.txt' file in the TechSmart Project Hierarchy
    
    - Name it "Model_OBJ"
    
    - Find the OBJ model of your choice, and change the format from ".obj" to ".txt"
    
    - Drag the file, into a new chrome tab
    
    - Copy and Paste the Contents into the "Model_OBJ.txt" file in TechSmart
    
   **If your model was made in Blender**
    
    - Go to the very top of the pasted "Model_OBJ.txt" file in TechSmart
    
    - Delete the "_# Blender v2.92.0 OBJ File: 'your_blend_file_here'_"
    
    - You're now ready to import a 3D model!
