"""
ProjectManager

Description:
"""
import pygame,sys
pygame.init()

# Defining Image Width
get_width = int(input("Image Width: (px)"))
get_height = int(input("Image Height: (px)"))
get_name = str(input("Project Name: "))
win_size = (get_width,get_height)

# Creating Project Script
file = get_name + '.txt'
with open(file,'w') as f:
    f.write("class " + get_name + ":\n")
    f.write("    def __init__(self,bg_color,pos=(0,0)):\n")
    f.write("        self.pos = list(pos)\n")
    f.write("        self.img = pygame.Surface(" + str([win_size[0],win_size[1]]) + ")\n")
    f.write("        self.img.fill(bg_color)\n\n")
    f.write("        # Drawing Code Goes Here")

# Editing Current Shape
currentPolygon = False

# Window
w,h = (win_size[0],win_size[1])
win = pygame.display.set_mode([w,h])

# Variables
image_panel = []
pt_list = []
color_list = []

# Idea for Saving Data?
save_data = {
    "item1": "color_data"
}

# Color Tuples
BACKGROUND = (255,255,255)
color = (0,0,0)

# Shaping Functions
def update_polygons(point_list):
    global image_panel
    
    for i in range(len(point_list)):
        pygame.draw.circle(win,(255,0,0),(point_list[i][0],point_list[i][1]),4)
        
    pygame.draw.polygon(win, color,point_list)
    
def polygon_tool():
    global pt_list,currentPolygon
    
    if not currentPolygon:
        image_panel.append(pt_list)
        color_list.append(color)
        pt_list = []
        
        print("Current Tool: None")
    
    else:
        print("Current Tool: Polygon Shape Tool")

def undo_move():
    global image_panel,pt_list,color
    
    try: image_panel.pop(-1)
    except: pass

    win.fill(BACKGROUND)
    
    for i in range(len(image_panel)):
        pygame.draw.polygon(win, color,image_panel[i])

def save_image(image_panel):
    with open (file, 'a') as f:
        for i in range(len(image_panel)):
            f.write('\n        pygame.draw.polygon(self.img,' + str(color_list[i]) + "," + str(image_panel[i]) + ')')
    
    print("Image Saved! You can now close the application...")
            
# Window Loop
while True:
    x, y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
            
        if e.type == pygame.MOUSEBUTTONDOWN:
            if currentPolygon:
                pt_list += [(x,y)]
    
        if e.type == pygame.KEYUP:
            if key[pygame.K_p]:
                print("Current Tool: Pen Tool")
                
            if key[pygame.K_r]:
                currentPolygon = not currentPolygon
                polygon_tool()
            
            if key[pygame.K_f]:
                print("Current Tool: Bucket Fill Tool")
            
            if key[pygame.K_LEFT]: # Undo Move
                undo_move()
            
            if key[pygame.K_RIGHT]: # Redo Move
                pass
            
            if key[pygame.K_c]: # Change Color
                new_color = input("Enter New Color: (tuple) | ")
                color = tuple(eval(new_color))
            
            if key[pygame.K_s]: # Saving
                print("Saving Image...")
                save_image(image_panel)
    
    update_polygons(pt_list)
    pygame.display.flip()
