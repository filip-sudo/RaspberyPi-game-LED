##################################import RPi.GPIO as GPIO
import time

LED_ZELENA = 17
LED_CRVENA = 16

##################################GPIO.setmode(GPIO.BCM)
##################################GPIO.setup(LED_ZELENA, GPIO.OUT)
##################################GPIO.setup(LED_CRVENA, GPIO.OUT)

rooms = {'Great Hall': {'name': 'Great Hall', 'South': 'Bedroom', 'North': 'Dungeon', 'West': 'Library', 'East': 'Kitchen', 'North-West':'Gallery', 'North-East':'Dining Room','South-West':'Cellar','South-East':'Bathroom'},
     'Bedroom': {'name': 'Bedroom','North': 'Great Hall'},
     'Bathroom': {'name': 'Bathroom', 'North-West': 'Great Hall'},
     'Library': {'name': 'Library', 'East': 'Great Hall','North': 'Gallery'},
     'Kitchen': {'name': 'Kitchen', 'West': 'Great Hall', 'North': 'Dining Room', 'East':'Pantry'},
     'Dining Room': {'name': 'Dining Room', 'South': 'Kitchen','South-West':'Great Hall'},
     'Dungeon': {'name': 'Dungeon', 'South': 'Great Hall'},
     'Gallery': {'name': 'Gallery', 'South-East': 'Great Hall','South':'Library', 'Item': 'Dungeon Key'},
     'Cellar':{'name': 'Cellar', 'North-East': 'Great Hall'},
     'Pantry':{'name': 'Pantry','West':'Kitchen'}
     }

directions= ['North', 'South', 'East', 'West' ,'North-West', 'North-East', 'South-East', 'South-West']

Inventory=[]

current_room = rooms['Bedroom']
print("     __________| |____")
print("    /                 \\")
print("   /     Welcome to    \\")
print("  /                     \\")
print("  |   my Haunted House! |")
print("  |     ____     ___    |")
print("  |    |    |   |___|   |")
print("__|____|____|___________|__")
print("")
# game loop
time.sleep(3)
while True:
   # display current location
    print()
    print('-' * 50)
    print('You are in the {}.'.format(current_room['name']))
    if current_room == rooms['Great Hall']:                  
        print()
        print("you can go: North, East, South, West, North-West, North-East, South-East, South-West")
        time.sleep(2)
    if current_room == rooms['Bedroom']:
        print()
        print("you can go: North")
        time.sleep(2)
    if current_room == rooms['Bathroom']:
        print()
        print("you can go: North-West")
        time.sleep(2)
    if current_room == rooms['Library']:
        print()
        print("you can go: North or East")
        time.sleep(2)
    if current_room == rooms['Kitchen']:
        print()
        print("you can go: North or East and West")
        time.sleep(2)
    if current_room == rooms['Dining Room']:
        print()
        print("you can go: South or South-West")
        time.sleep(2)
    if current_room == rooms['Dungeon']:
        print()        
        print("you can go: South")
        time.sleep(2)
    if current_room == rooms['Gallery']:
        if ("Dungeon Key" not in Inventory):
            print()
            print("You found a key in gallery!")
            time.sleep(2)
        else:
            print()
            print("you can go: South or South-East")
            time.sleep(2)
    if current_room == rooms['Pantry']:
        print()
        print("you can go: West")
        time.sleep(2)
    if current_room == rooms['Cellar']:
        if ("Sword" not in Inventory):
            print()
            print("You found a sword in Cellar!")
            time.sleep(2)
        else:
            print()
            print("you can go: North-East")
            time.sleep(2)

  # get user input
    if("Dungeon Key" not in Inventory) and (current_room == rooms['Gallery']):
        command = input('\nDo you want to pick it up(y/n)? ').strip()
        if command.lower() == ('y'):
            Inventory.append("Dungeon Key")
            print("Item is collected!")
            print()
            print("you can go: South or South-East")
        elif command.lower() == ('n'):
            print("Item is not collected!")
            print()
            print("you can go: South or South-East")
        else:
            print()
            print("I don't understand that command.")
            print()
            print("Nothing happens")
            print()
            print("you can go: South or South-East")

    if("Sword" not in Inventory) and (current_room == rooms['Cellar']):
        command = input('\nDo you want to pick it up(y/n)? ').strip()
        if command.lower() == ('y'):
            Inventory.append("Sword")
            print("Item is collected!")
            print()
            print("you can go: North-East")
        elif command.lower() == ('n'):
            print("Item is not collected!")
            print()
            print("you can go: North-East")
        else:
            print()
            print("I don't understand that command.")
            print()
            print("Nothing happens")
            print()
            print("you can go: South or South-East")

    #Dungeon w/o key
    if (current_room == rooms['Dungeon']) and ("Dungeon Key" not in Inventory):
        current_room = rooms['Great Hall']
        print()
        print("There is locked door in front of you!")
        time.sleep(2)
        print("There is probably a key somewhere close!")
        time.sleep(2)

    # Dungeon w/o sword scenario
    if (current_room == rooms['Dungeon']) and ("Sword" not in Inventory):
        current_room = rooms['Bedroom']
        Inventory.clear()
        print()
        print("There is scarry monster in there!")
        time.sleep(2)
        print("You died!")
        time.sleep(2)
        print("Respawn in 10...")
        for i in range (10):
            ##################################GPIO.output(LED_CRVENA, GPIO.HIGH)
            time.sleep(1)
            ##################################GPIO.output(LED_CRVENA, GPIO.LOW)

    # Dungeon w/ sword scenario
    if (current_room == rooms['Dungeon']) and ("Sword" in Inventory):
        Inventory.clear()
        print()
        print("There is scarry monster in there!")
        time.sleep(2)
        print("You used sword and defeated monster!")
        time.sleep(2)
        print("House is haunted no more! VICTORY!")
        for i in range (10):
            ##################################GPIO.output(LED_ZELENA, GPIO.HIGH)
            time.sleep(1)
            ##################################GPIO.output(LED_ZELENA, GPIO.LOW)
        ##################################GPIO.cleanup()
        break

    else:
        command  = input('\nWhat direction do you want to go? ').strip()

            # movement
    if command in directions:
        if command in current_room:
                current_room = rooms[current_room[command]]
        else:
        # bad movement
            print("You can't go that way.")
    
  # Exit game
    elif command.lower() in ('q', 'quit'):
        print('Thanks for playing!')
        ##################################GPIO.cleanup()
        break
       
  # bad command
    else:
        if command not in directions:
            if command not in current_room:
                if command.lower() in ('q', 'quit'):
                    print("I don't understand that command.")

        

        

