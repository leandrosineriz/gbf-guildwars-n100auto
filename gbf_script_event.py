import pyautogui as py
import time
    
        
def quit_mision():
    try:
        x, y = py.locateCenterOnScreen("resources/button_menu.PNG" , confidence=0.9)
    except:
        x, y = -1, -1
        
    if x != -1 and y != -1:
        py.click(x, y)
        time.sleep(1)
        while True:        
            try:
                x, y = py.locateCenterOnScreen("resources/button_retreat1.PNG" , confidence=0.9)
                py.click(x, y)
                time.sleep(1)
                while True:
                    try:
                        x, y = py.locateCenterOnScreen("resources/button_retreat2.PNG" , confidence=0.9)
                        py.click(x, y)
                        time.sleep(1)
                        return True
                    except:
                        continue
            except:
                continue

def death_restart():
    steps = ['defeat1', 'defeat2', 'defeat3', 'heal1', 'heal2', 'heal3']
    i = 0
    length = len(steps)
    global k
    global x
    global y
    print('Death restart, i: '+str(i)+' len: '+str(length))
    try:
        x, y = py.locateCenterOnScreen("resources/"+steps[i]+".PNG" , confidence=0.9)
        while i < len(steps):
            print('Death restart, i: '+str(i)+' len: '+str(length))
            try:
                x, y = py.locateCenterOnScreen("resources/"+steps[i]+".PNG" , confidence=0.9)
                i += 1
                time.sleep(.5)
                if i == 3:
                    time.sleep(10)
                py.click(x, y)
                if i == length-1:
                    k = 6
            except:
                continue
    except:
        x, y = -1, -1

def show_time():
    global k
    global loop
    global running_start
    #Control print
    running_time = time.time() - running_start
    print("Loop:", loop, "- Stage:", k, "- Execution Time:", time.strftime("%H:%M:%S", time.gmtime(running_time)))
    loop += 1
    
    
'''
El script sigue el orden de la lista como pasos
'''
steps = ['granblue_bookmark', 'summon_hades', 'button_ok', 
         'personaje_fediel', 'habilidad_fediel', 'button_attack', 
         'button_full', 'button_attackCancel', 'button_ok2']
steps_refill = ['potion', 'button_ok_refill']

k = 0 #step counter
j = 0 #step refill counter
loop = 0 #loop
running_start = time.time() #start of script
time_inic = time.time() #counter
reload = "f5" #reload button
reload_count = 0 #reload counter
x, y = -1, -1 #position variables
length = len(steps)
length_refill = len(steps_refill)

while True:
    try:
        x, y = py.locateCenterOnScreen("resources/"+steps[k]+".PNG" , confidence=0.9)
    except:
        #condicionales segun steps
        if k == 1:
            #if summon not found scroll dawn
            time.sleep(.5)
            py.moveTo(100, 200)
            py.scroll(-50)
        if k == 3: 
            #tryes to refill potion
            try:
                x, y = py.locateCenterOnScreen("resources/"+steps_refill[j]+".PNG" , confidence=0.9)
                while True:
                    try:
                        x, y = py.locateCenterOnScreen("resources/"+steps_refill[j]+".PNG" , confidence=0.9)
                        #Modificadores segun los pasos
                        if j == 0:
                            y += 150
                        #clicks    
                        py.click(x, y+150)
                        j += 1
                        #condicional de salida
                        if length_refill == j:
                            j == 0
                            time_inic = time.time()
                            break
                    except:
                        continue
            except:
                pass
        if k == 8:
            show_time()
            death_restart() #tryes to revive team
            continue
        #end value for not found
        x, y = -1, -1
    
    show_time()
    
    #validates image found and does the click on position x, y
    if  x != -1 and y != -1:
        #Reload timer and reload count
        time_inic = time.time()
        reload_count = 0
        #Reload loop
        if k == (length-1):
            k = 0
            continue
        #delay before attack
        if k == 3:
            time.sleep(0)
        #Click
        py.click(x, y)
        #Press f5 to avoid stuck on f6
        k += 1
        
    #validates timer and reload the page based on step do other things
    elif time.time() - time_inic > 15:
        #Before entering battle restart from step 1
        if k == 1:
            k = 5
        elif k <= 4:
            k = 0
        elif k==7:
            k+=1
            continue
        
        #If reload more than 3 times without cliking start from step 1
        if reload_count >= 3:
            quit_mision()
            k = 0
        
        #Reloads
        #Search bookmark and clicks
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
            py.click(x, y)
            time.sleep(1)
        except:
            x, y = -1, -1
        py.press(reload)
        time.sleep(2)
        time_inic = time.time() #reload timer
        reload_count += 1 #Add to reload counter
'''
while True:
    if k == 1:
        #Granblue slimes bookmark
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 2:
        #summon Hades
        try:
            x, y = py.locateCenterOnScreen("resources/summon_hades.PNG" , confidence=0.9)
        except:
            time.sleep(.5)
            py.moveTo(100, 200)
            py.scroll(-50)
            x, y = -1, -1
    if k == 3:
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 4:
        #Search fediel icon
        try:
            x, y = py.locateCenterOnScreen("resources/personaje_fediel.png" , confidence=0.9)
            time.sleep(5)
        except:
            #Search Potion use button
            try:
                x, y = py.locateCenterOnScreen("resources/potion.PNG" , confidence=0.9)
                py.click(x, y+150)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
            #Search ok button for refill
            try:
                x, y = py.locateCenterOnScreen("resources/button_ok_refill.PNG" , confidence=0.9)
                py.click(x, y)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
    if k == 5:
        #fediel hability
        try:
            x, y = py.locateCenterOnScreen("resources/habilidad_fediel.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 6:
        #button attack
        try:
            x, y = py.locateCenterOnScreen("resources/button_attack.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 7:
        #button full
        try:
            x, y = py.locateCenterOnScreen("resources/button_full.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 8:
        #button-cancel
        try:
            x, y = py.locateCenterOnScreen("resources/button_attackCancel.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 9:
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok2.PNG" , confidence=0.9)
        except:
            show_time()
            #time.sleep(5)
            death_restart()
            continue
            
    show_time()
    
    #validates image found and does the click on position x, y
    if  x != -1 and y != -1:
        #Reload timer and reload count
        time_inic = time.time()
        reload_count = 0
        #Reload loop
        if k == 9:
            k = 1
            continue
        #delay before attack
        if k == 4:
            time.sleep(0)
        #Click
        py.click(x, y)
        #Press f5 to avoid stuck on f6
        k += 1
        
    #validates timer and reload the page based on step do other things
    if time.time() - time_inic > 15:
        #Before entering battle restart from step 1
        if k == 2:
            k = 6
        elif k <= 6:
            k = 1
        elif k==8:
            k+=1
            continue
        
        #If reload more than 3 times without cliking start from step 1
        if reload_count >= 3:
            quit_mision()
            k = 1
        
        #Reloads
        #Search bookmark and clicks
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
            py.click(x, y)
            time.sleep(1)
        except:
            x, y = -1, -1
        py.press(reload)
        time.sleep(2)
        time_inic = time.time() #reload timer
        reload_count += 1 #Add to reload counter
'''