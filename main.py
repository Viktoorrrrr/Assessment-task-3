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
    with open('save_file.txt', 'w') as save_file: #needs fixing
        save_file.write(f'name: {name}' + '\nhealth: 100' + '\nposition: 0,0' + '\nattack: 10' + '\nhealthpotion: 1')
        player = {'name': name,'health': 100, 'position': [0, 0], 'attack': 100, 'healthpotion': 5, 'inventory': [], 'max_health': 100, 'karma': 0, 'clear': False}
    return player

def terminal(text, speed=0.05): # function was entirely AI
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print() # Prints a newline at the end
def menu(player):
    print('MENU')
    print('Type I for inventory access')
    print('Type H to use a health potion')
    print('Type P to view player stats')
    print('Type S to save game')     
    print('Type E to exit game (please save first!!)')       
    valid = False
    while not valid:
        p_input = input('Type the correspondent key: ').upper()
        if p_input == 'I':
            check_inventory(player)
            valid = True
        elif p_input == 'H':
            if player['healthpotion'] >= 1:
                terminal('You have used a health potion and restored +30 HP')
                player['healthpotion'] -= 1
                player['health'] += 30
                if player['health'] > player['max_health']:
                    player['health'] = player['max_health']
            else:
                terminal('You are out of health potions')
            valid = True
        elif p_input == 'P':
            print(f'Health: {player['health']}/{player['max_health']} Attack: {player['attack']} Potions: {player['healthpotion']}')
            time.sleep(1)
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
        [' ', 'trap', 'chest', 'monster', 'NPC'], 
        ['BOSS', 'trap', ' ', 'trap', ' '], 
        ['BOSS', 'NPC', ' ', 'monster', ' '], 
        ['trap', 'monster', ' ', 'NPC ', ' '], 
        ['monster', ' ', 'monster', 'chest', 'BOSS']]
    
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
                    x += 1
                valid_input = False
                while not valid_input:
                    try:
                        d_input = int(input('Select the corresponding numbered item you would like to remove: '))
                        if d_input <= len(player['inventory']) and d_input > 0:
                            print(f'{player['inventory'][d_input - 1]} has been removed')
                            if player['inventory'][d_input - 1] =='Iron sword':
                                player['attack'] -= 5
                            elif player['inventory'][d_input - 1] == 'Cursed blade':
                                player['attack'] -= 15
                                player['max_health'] += 10
                            elif player['inventory'][d_input - 1] == 'Paladin sword':
                                terminal('This item improves attack by 25')
                                player['attack'] -= 25
                            elif player['inventory'][d_input - 1] == 'Giants armour':
                                terminal('This item improves health by 20, permamently')
                                player['max_health'] -= 30
                                if player['health'] > player['max_health']:
                                    player['health'] = player['max_health']
                            elif player['inventory'][d_input - 1] == 'dryads cloak':
                                terminal('This item improves health by 30 but lowers attack by 10')
                                player['attack'] += 10
                                player['max_health'] -= 30
                                if player['health'] > player['max_health']:
                                    player['health'] = player['max_health']
                            player['inventory'].pop(d_input - 1)
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
        m_input = int(input('Enter the number corresponding to your desired direction: OR  5 to access menu: '))
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
def event_active(tile):
    if tile =='monster' or tile == 'trap' or tile =='NPC' or tile == 'chest' or tile == 'BOSS':
        return True
    else:
        return False
def event(player, tile, map_layout):
    if tile == 'monster':
        combat(player)
    elif tile == 'NPC':
        NPC(player)
    elif tile == 'chest':
        chest(player)
    elif tile == 'trap':
        terminal('A nasty dungeon trap crashes into you')
        terminal('You take 10 damage from the trap')
        player['health'] -= 10  
    elif tile == 'BOSS':
        player['clear'] == True
        combat(player)
    map_layout[player['position'][0]][player['position'][1]] = ' ' #reset the tile so its blank
    return terminal('The event has passed')

def NPC(player):
    encounters = ['Priest', 'Priest', 'Beggar', 'Beggar', 'Beggar', 'Cultist', 'Cultist','Legion commander']
    encounter = encounters[7]
    if encounter == 'Priest':
        priest_event(player)
    elif encounter == 'Beggar':
        beggar_event(player)
    elif encounter == 'Cultist':
        cultist_event(player)
    elif encounter == 'Legion commander':
        legion_commander(player)
def priest_event(player):
    terminal('Greetings adventurer, the world is filled with pain and misery.')
    terminal('Allow me to help you on your journey.')
    terminal('Would you care for a blessing from the goddess of light? (Y/N)')
    valid = False
    while not valid:
        p_input = input('(Y/N): ').lower()
        if p_input =='y' or p_input =='yes':
            terminal('You feel the priests hand lay on your forehead')
            terminal('A strange light surrounds you')
            terminal('The goddess of light is ecstatic')
            time.sleep(0.5)
            print('+ 10 maximum health gain')
            player['max_health'] += 10
            player['karma'] += 5
            valid = True
        elif p_input =='n' or p_input =='no':
            terminal('The priest looks dissapointed')
            terminal('Oh well thats a shame, either way i shall pray for your safe journey')
            terminal('May the goddess of light shine your path ahead')
            valid = True
        else:
            print('Invalid input try again')
def beggar_event(player):
    terminal('This place needs to go to hell')
    terminal('I cant stand this place anymore')
    terminal('It appears to be a beggar, likely a criminal sent to the dungeon')
    terminal('They sent me here... all cause i stole some bread to survive!!!')
    valid = False
    while not valid:
        p_input = input('Want to help him? (Y/N): ').lower()
        if p_input =='y' or p_input =='yes':
            terminal('You walk alongside the beggar throughout the dungeon')
            terminal('Walking around has made you tired')
            terminal('You agree to interchange guard duty around the fire for the night')
            time.sleep(1)
            terminal('The beggar is gone')
            terminal('No trace of him is left but you feel awfully sick')
            print('health has been reduced by 10')
            player['health'] -= 10
            valid = True
        elif p_input =='n' or p_input =='no':
            terminal('You continue walking ignoring his story')
            terminal('A few minutes later the sounds of screams and blades can be heard')
            terminal('You carry on')
            valid = True
        else:
            print('Invalid input try again')
def cultist_event(player):
    terminal('A man in a red and black shady coat appraoches you')
    terminal('Adventurer, the god of darkness seeks candidates to inherit his godlike powers')
    terminal('Would you care for a blessing from the god of darkness? (Y/N)')
    valid = False
    while not valid:
        p_input = input('(Y/N): ').lower()
        if p_input =='y' or p_input =='yes':
            terminal('The priest dips his hand into a jar holding red liquid')
            terminal('It looks like blood yet you do not question it')
            terminal('The priest draws a symbol on your chest')
            time.sleep(0.5)
            terminal('The god of darkness laughs and praises your courage')
            terminal('The goddess of light sheds tears')
            print('Attack increased by 20 but max health lowered by 10')
            player['attack'] += 20
            player['max_health'] -= 10
            if player['health'] > player['max_health']:
                player['health'] = player['max_health']
            player['karma'] -= 5
            valid = True
        elif p_input =='n' or p_input =='no':
            terminal('The cultist looks at you with dissapointment')
            terminal('The goddess of light is overjoyed')
            player['karma'] += 5
            terminal('Oh well had i known this i wouldve started off with this')
            terminal('He runs away but leaves a strange orb near you')
            terminal('You quickly hear the sounds of monsters running this way')
            terminal('A monster attacks and you prepare for combat')

            combat(player)
            valid = True
        else:
            print('Invalid input try again')
def legion_commander(player):
    terminal('You notice a man in shining silver paladin armour walking through the dungeon')
    terminal('He approaches you, sizing you up')
    terminal('The god of darkness continues to invade our lands, will you help us? (Y/N)')
    valid = False
    while not valid:
        p_input = input('(Y/N): ').lower()
        if p_input =='y' or p_input =='yes':
            terminal('Wonderful!')
            terminal('The paladin makes a prayer before handing you a talisman')
            terminal('This is a sign that you are apart of the paladin legion')
            terminal('It is bound to your soul through the goddess of light so the forces of darkness can not harm you')
            time.sleep(0.5)
            terminal('The god of darkness slams his fists on his table')
            if player['karma'] > 0:
                terminal('The goddess of light admires the purity of your soul')
            elif player['karma'] == 0:
                terminal('The goddess of light sees room for improvement')
            elif player['karma'] < 0:
                terminal('The goddess of light is disgusted at you')
            print('Attack increased by 15 , max health increased by 10')
            player['attack'] += 15
            player['max_health'] += 10
            if player['health'] > player['max_health']:
                player['health'] = player['max_health']
            player['karma'] += 10
            terminal('Take this aswell, you will need it')
            terminal('He hands you 3 health potions')
            player['healthpotion'] += 1
            valid = True
        elif p_input =='n' or p_input =='no':
            terminal('The paladin walks away')
            terminal('If you ever need help dont be afraid to find us!')
            valid = True
        else:
            print('Invalid input try again')
def chest(player):
    items = ['Iron sword', 'Iron sword', 'Iron sword', 'Iron sword', 'Cursed blade', 'Paladin sword', 
             'health potion', 'health potion', 'health potion', 'health potion', 'giants armour', 'dryads cloak',
             ]
    RNG_item = items[random.randint(0, 11)]
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
            if player['health'] > player['max_health']:
                player['health'] = player['max_health']
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
        if RNG_item != 'health potion':
            player['inventory'].append(RNG_item)
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
    if player['clear'] == True:
        terminal('A red scaled dragon looms over you, blocking the dungeon exit')
        terminal('A voice cackles in the distance')
        terminal('Foolish humans')
        terminal('Youve never heard this voice before yet you know this is the god of darkness')
        terminal('SLAY THE DRAGON')
        terminal('STOP THE GOD OF DARKNESSES ADVANCE')
        monster['damage'] == 30
        monster['health'] == 500
        encounter = 'dragon'
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
        terminal('The dragon approaches you what do you do')
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
                terminal('Escape. Is. Not. An. Option')
            print(f'player ❤️ {player['health']}/{player['max_health']}, player ⚔️ {player['attack'] * damage_bonus}, monster ❤️ {monster['health']}')
        if player['health'] <= 0:
            a = f'Game over {player['name']}, You have died to the {encounter}'
            terminal(a)
            #delete_save()
            sys.exit()
        elif monster['health'] <= 0 and player['health'] > 0:
            terminal('The dragon has been slain')
            terminal('You open the large stone doors and witness the outside world')
            if player['karma'] >= 15:
                terminal('Rich landscapes and bustling cities can be seen in the distance')
                terminal('You walk through the forest, lush greenery and animals are seen everywhere')
                terminal('The goddess of light has not yet abandoned this realm')
                terminal('The righteous ending')
                terminal('Thank you for playing survive the dungeon!')
            elif player['karma'] <= -15:
                terminal('Barren, dry fields of cracked earth lay the wasteland')
                terminal('You walk through the barren desert, corruption seeps into the soil')
                terminal('Poverty, famine and demons infect this world')
                terminal('You grow tired and collapse under the brutal sun')
                terminal('The goddess of light has  abandoned this realm')
                terminal('A voice laughs in your ear as your consciousness fades')
                terminal('The demonic ending')
                terminal('Thank you for playing survive the dungeon!')
            elif player['karma'] < 15 and player['karma'] > -15:
                terminal('The land is torn apart, signs of warfare can be seen throughout the forest')
                terminal('You hear the sounds of clashing, biting, slashing, spells and swords in the distance')
                terminal('Legions of monsters are being desperately held off by the paladins')
                terminal('The god of darknesses invasion continues onto this realm')
                terminal('You continue to fight, not to protect')
                terminal('Just to survive')
                terminal('The hopeless ending')
                terminal('Thank you for playing survive the dungeon!')
    elif player['attack'] < 20: #Should only draw from easy enemies until player has progressed enough to fight harder enemies
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
        if player['health'] <= 0:
            a = f'Game over {player['name']}, You have died to the {encounter}'
            terminal(a)
            #delete_save()
            sys.exit()
        elif player['health'] > 0 and monster['health'] <= 0:
            chest_RNG = random.randint(0, 100)
            if chest_RNG <= 10 and chest_RNG >= 0:
                terminal('The opponent has dropped something!!')
                terminal('rolling..........')
                chest(player)
        
        
            
            


def game(player):
    map_layout= map()
    while player['clear'] != True and player['health'] > 0: # Exit condition player finish game to escape the dungeon or if health reaches 0 game ends
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