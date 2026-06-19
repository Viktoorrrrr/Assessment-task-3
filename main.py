import time
import sys
import random
def introduction():
    story_dialogue = ['You wake up, the only thing surrounding you is the dark dim lights of torches that faintly illuminate the room.', 
                      'Your body gradually rises as the stone cold for that was pressing against on your face feels a gradual alleviation of pressure.', 
                      'The dungeon does not forgive.', 
                      'There is only one way out.', 'SURVIVE.']
    terminal('What is your name, young adventurer? ')
    name = input('').strip()
    while name == "" or name.isspace():
        name = input('Please enter a valid name: ')
    #for line in story_dialogue:
        #terminal(line)
        #p_input = input(f'Enter a key to continue...(or type "skip" to skip): ').strip()
        #if p_input.lower() == "skip":
            #break
    d = f'Welcome, {name}! Your adventure begins now...'
    terminal(d)
    with open('save_file.txt', 'w') as save_file:
        save_file.write(f'name: {name}' + '\nhealth: 100' + '\nposition: 0,0' + '\nattack: 10' + '\nhealthpotion: 1')
        player = {'name': name,'health': 100, 'position': [0, 0], 'attack': 40, 'healthpotion': 5, 'inventory': [], 'max_health': 100}
    return player

def terminal(text, speed=0.0005): # function was entirely AI
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print() # Prints a newline at the end
def menu(player):
    print('MENU')
    print('Type I for inventory access')
    print('Type S to save game')     
    print('Type E to exit game (please save first!!)')       
    valid = False
    while not valid:
        p_input = input('Type the correspondent key: ').upper()
        if p_input == 'I':
            check_inventory(player)
            valid = True
        elif p_input == 'S':
            #save()
            valid = True
        elif p_input == 'E':
            terminal('Thank you for playing!')
            sys.exit()
        else:
            print('Invalid input try again please')
def map():
    map_layout = [
        [' ', 'chest', 'chest', 'monster', 'NPC'], 
        ['monster', 'trap', ' ', 'trap', ' '], 
        [' ', 'NPC', ' ', 'monster', ' '], 
        ['trap', 'monster', ' ', 'NPC ', ' '], 
        ['monster', ' ', 'monster', 'chest', 'monster']]
    
    return map_layout # Starting position of player is (0, 0)
def check_inventory(player):
    print(f'INVENTORY: {player['inventory']}')
    valid = False
    while not valid:
        if len(player['inventory']) != 0:
            p_input = input('Would you like to dipose of any items? (Y/N)').lower()
            if p_input =='y' or p_input =='yes':
                x = 1
                for item in player['inventory']:
                    print(f'{x}. {item}')
                valid_input = False
                while not valid_input:
                    try:
                        d_input = int(input('Select the corresponding numbered item you would like to remove: '))
                        if d_input <= len(player['inventory']) and d_input > 0:
                            player['inventory'].pop(d_input - 1)
                            print(f'{player['inventory']} has been removed')
                            print(f'INVENTORY: {player['inventory']}')
                            valid_input = True
                        else:
                            print('That item does not exist try again')
                    
                    except ValueError:
                        print('Wrong input try again')
                valid = True
            elif p_input =='n' or p_input =='no':
                valid = True
            else:
                print('Invalid input try again')
        elif len(player['inventory']) == 0:
            terminal('A few flies fly out of your empty inventory, perhaps you should start searching')
            valid = True

                            
def Movement_option(player):
    terminal('The paths ahead are shrouded in darkness, where will you go?')
    #check if player can move north, south, east or west based on current position and map boundaries
    p_position = player['position']
    if  p_position[0] > 0:
        print('1. Move North')
    if p_position[0] < 4:
        print('2. Move South')
    if p_position[1] < 4:
        print('3. Move East')
    if p_position[1] > 0:
        print('4. Move West')
    try:
        m_input = int(input('Enter the number corresponding to your desired direction: OR  5 to access menu'))
        if m_input == 1 and p_position[0] > 0:
            p_position[0] -= 1
        elif m_input == 2 and p_position[0] < 4:
            p_position[0] += 1
        elif m_input == 3 and p_position[1] < 4:
            p_position[1] += 1
        elif m_input == 4 and p_position[1] > 0:
            p_position[1] -= 1
        elif m_input == 5:
            menu(player)
        else:
            print("⚠️⚠️You cannot move in that direction, try again⚠️⚠️")
    except ValueError:
        print("⚠️⚠️That is not a valid direction, try again⚠️⚠️")
    player['position'] = p_position
def event_active(tile,):
    if tile =='monster' or tile == 'trap' or tile =='NPC' or tile == 'chest':
        return True
    else:
        return False
def event(player, tile, map_layout):
    map_layout[player['position'][0]][player['position'][1]] = ' ' #reset the tile so its blank
    if tile == 'monster':
        combat(player)
        pass
    elif tile == 'NPC':
        #NPC
        pass
    elif tile == 'chest':
        chest(player)
        pass
    elif tile == 'trap':
        #trap()
        pass
    return terminal('The event has passed')
def chest(player):
    items = ['Iron sword', 'Iron sword', 'Iron sword', 'Iron sword', 'Cursed blade', 'Paladin sword', 
             'health potion', 'health potion', 'health potion', 'health potion', 'giants armour', 'dryads cloak',
             ]
    RNG_item = items[4] 
    #items[random.randint(0, 11)]
    term = f'You have received a {RNG_item}!'
    terminal(term)
    tally = 0
    for i in player['inventory']: #check if duplicates exists
        if RNG_item == i:
            tally += 1
    if tally == 0:
        if RNG_item =='Iron sword':
            terminal('This item improves your attack by 5')
            player['attack'] += 5
        elif RNG_item == 'Cursed blade':
            terminal('This item improves attack by 15 but lowers HP by 10')
            player['attack'] += 15
            player['max_health'] -= 10
        elif RNG_item == 'Paladin sword':
            terminal('This item improves attack by 25')
            player['attack'] += 25
        elif RNG_item == 'health potion':
            terminal('This item improves health by 30 when used in combat ')
            player['healthpotion'] += 1
        elif RNG_item == 'Giants armour':
            terminal('This item improves health by 20, permamently')
            player['max_health'] += 30
        elif RNG_item == 'dryads cloak':
            terminal('This item improves health by 30 but lowers attack by 10')
            player['attack'] -= 10
            player['max_health'] += 30
        player['inventory'].append(RNG_item)
        check_inventory(player)
    else:
        terminal('You already have this item so you throw it away')
        debug_inventory(player) #need to remove duplicates

def debug_inventory(player):
    inventory_dict = {}
    for i in player['inventory']:
        inventory_dict[i] = 0
    for i in player['inventory']:
        if i in player['inventory']:
            inventory_dict[i] += 1
    for i in player['inventory']:
        if inventory_dict[i] > 1:
            player['inventory'].remove(i)
    print(player['inventory'])
            




def combat(player):
    e_enemies = ['goblin', 'Silver wolf', 'Troll', 'golem'] #Easy enemies
    h_enemies = ['Wyvern', 'Centaur', 'Hydra', 'Phoenix']
    monster = {'health': '', 'damage': ''}
    if player['attack'] < 20: #Should only draw from easy enemies until player has progressed enough to fight harder enemies
        encounter = e_enemies[random.randint(0, 3)]
        if encounter == 'goblin':
                monster['damage'] = 5
                monster['health'] = 15
        elif encounter == 'Silver wolf':
                monster['damage'] = 7
                monster['health'] = 20
        elif encounter == 'Troll':
                monster['damage'] = 10
                monster['health'] = 20
        elif encounter == 'golem':
            monster['damage'] = 6
            monster['health'] = 30
        d = f'Combat has initiated'
        terminal(d)
        valid_input = False
        while not valid_input:
            try:
                p_input = int(input('Would you like to roll the die? (1 for yes, 2 for no) '))
                if p_input == 1:
                    terminal('Rolling the die of fate...') #Roll a die 1-20 like dnd and if 11-20 multiply damage but less than is a debuff
                    damage_bonus = random.randint(1, 20)
                    dialogue = f'You rolled a {damage_bonus}'
                    terminal(dialogue)
                    if damage_bonus > 10:
                        terminal('The goddess of light has blessed your fight')
                    elif damage_bonus < 10:
                        terminal('The god of darkness curses your fight')
                    damage_bonus = damage_bonus / 10
                    valid_input = True
                elif p_input == 2: 
                    damage_bonus = 1
                    valid_input = True
            except ValueError:
                print('Wrong input try again')
        a = f'A wild {encounter} has attacked you what will you do?'
        terminal(a)
        while player['health'] > 0 and monster['health'] > 0:
            if player['health'] != player['max_health']:
                if player['health'] > player['max_health']:
                    player['health'] = player['max_health']
            valid_input = False
            while not valid_input:
                time.sleep(0.5)
                print('1. Attack')
                print('2. Use a health potion')
                print('3. Escape')
                try:
                    combat_option = int(input('Enter the number corresponding to your desired choice:'))
                    if combat_option == 1 or combat_option == 2 or combat_option == 3:
                        valid_input = True
                except:
                    print('Wrong input try again')
            if combat_option == 1:
                monster['health'] -= player['attack'] * damage_bonus
                print(f'{player['name']} has dealt {player['attack'] * damage_bonus} to {encounter}')
                time.sleep(1.5) # AI
                print(f'{encounter} fights back and has dealt {monster['damage']} damage to {player['name']}')
                player['health'] -= monster['damage']
            elif combat_option == 2:
                if player['healthpotion'] >= 1:
                    terminal('You have use a health potion and restored +30 HP')
                    player['healthpotion'] -= 1
                    player['health'] += 30
                    if player['health'] > player['max_health']:
                        player['health'] = player['max_health']
                else:
                    terminal('You are out of health potions')
            elif combat_option == 3:
                terminal(f'You run trying to escape the {encounter}')
                ran = random.randint(1, 100)
                if ran <= 10:
                    terminal(f'You succesfully escape and the {encounter} vanishes into the darkness')
                    terminal('The god of darkness mocks your cowardice')
                    terminal('The goddess of light sighs in relief at your safety')
                    break
                else:
                    terminal('Failed to escape combat will resume')

            print(f'player ❤️: {player['health']}/{player['max_health']}, player ⚔️ {player['attack'] * damage_bonus}, monster ❤️ {monster['health']}')
        if player['health'] <= 0:
            a = f'Game over {player['name']}, You have died to the {encounter}'
            terminal(a)
            #delete_save()
            sys.exit()
        elif player['health'] > 0 and monster['health'] <= 0:
            chest_RNG = random.randint(0, 100)
            if chest_RNG <= 80 and chest_RNG >= 0:
                terminal('The opponent has dropped something!!')
                terminal('rolling..........')
                chest(player)
    elif player['attack'] > 35:
        h_enemies = ['Wyvern', 'Centaur', 'Hydra', 'Phoenix']
        encounter = h_enemies[random.randint(0, 3)]
        if encounter == 'Wyvern':
                monster['damage'] = 20
                monster['health'] = 60
        elif encounter == 'Centaur':
                monster['damage'] = 15
                monster['health'] = 65
        elif encounter == 'Hydra':
                monster['damage'] = 30
                monster['health'] = 50
        elif encounter == 'Phoenix':
            monster['damage'] = 45
            monster['health'] = 35
        d = f'Combat has initiated'
        terminal(d)
        valid_input = False
        while not valid_input:
            if player['max_health'] != 100:
                if player['health'] > player['max_health']:
                    player['health'] = player['max_health']
            try:
                p_input = int(input('Would you like to roll the die? (1 for yes, 2 for no) '))
                if p_input == 1:
                    terminal('Rolling the die of fate...') #Roll a die 1-20 like dnd and if 11-20 multiply damage but less than is a debuff
                    damage_bonus = random.randint(1, 20)
                    dialogue = f'You rolled a {damage_bonus}'
                    terminal(dialogue)
                    if damage_bonus > 10:
                        terminal('The goddess of light has blessed your fight')
                    elif damage_bonus < 10:
                        terminal('The god of darkness curses your fight')
                    damage_bonus = damage_bonus / 10
                    valid_input = True
                elif p_input == 2: 
                    damage_bonus = 1
                    valid_input = True
            except ValueError:
                print('Wrong input try again')
        a = f'A wild {encounter} has attacked you what will you do?'
        terminal(a)
        while player['health'] > 0 and monster['health'] > 0:
            valid_input = False
            while not valid_input:
                time.sleep(0.5)
                print('1. Attack')
                print('2. Use a health potion')
                print('3. Escape')
                try:
                    combat_option = int(input('Enter the number corresponding to your desired choice:'))
                    if combat_option == 1 or combat_option == 2 or combat_option == 3:
                        valid_input = True
                except:
                    print('Wrong input try again')
            if combat_option == 1:
                monster['health'] -= round(player['attack'] * damage_bonus)
                print(f'{player['name']} has dealt {round(player['attack'] * damage_bonus, 2)} to {encounter}')
                time.sleep(1.5) # AI
                print(f'{encounter} fights back and has dealt {round(monster['damage'], 2)} damage to {player['name']}')
                player['health'] -= round(monster['damage'], 2)
            elif combat_option == 2:
                if player['healthpotion'] >= 1:
                    terminal('You have use a health potion and restored +30 HP')
                    player['healthpotion'] -= 1
                    player['health'] += 30
                    if player['health'] > player['max_health']:
                        player['health'] = player['max_health']
                else:
                    terminal('You are out of health potions')
            elif combat_option == 3:
                terminal(f'You run trying to escape the {encounter}')
                ran = random.randint(1, 100)
                if ran <= 10:
                    terminal(f'You succesfully escape and the {encounter} vanishes into the darkness')
                    terminal('The god of darkness mocks your cowardice')
                    terminal('The goddess of light sighs in relief at your safety')
                    break
                else:
                    terminal('Failed to escape combat will resume')

            print(f'player ❤️ {player['health']}/{player['max_health']}, player ⚔️ {player['attack'] * damage_bonus}, monster ❤️ {monster['health']}')
        if player['health'] < 0:
            a = f'Game over {player['name']}, You have died to the {encounter}'
            terminal(a)
            #delete_save()
            sys.exit()
        elif player['health'] > 0 and monster['health'] <= 0:
            chest_RNG = random.randint(0, 100)
            if chest_RNG <= 80 and chest_RNG >= 0:
                terminal('The opponent has dropped something!!')
                terminal('rolling..........')
                chest(player)
        
        
            
            


def game(player):
    map_layout= map()
    while player['position'] != [4,4] and player['health'] > 0: # Exit condition player must reach  (4, 4) to escape the dungeon or if health reaches 0 game ends
        Movement_option(player)
        print(f'Your current position is: {player["position"]}')
        current_tile = map_layout[player['position'][0]][player['position'][1]]
        if current_tile == ' ':
            terminal('Darkness is all you see')
        if event_active(current_tile):
            print(f'You have encountered a {current_tile}!')
            event(player, current_tile, map_layout)

def main():
    #if new_game(): check if a save file exists already if not create a new game
    player = introduction()
    #Gameplay loop, as long as exit conditions not met (Either player dies, escapes or quits), the game continues to run.
    #while exit condtion not met run game):
    game(player)
    #while exit(health, escaped, quit) == False:
    return None

main()