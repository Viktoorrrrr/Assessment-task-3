# task-3-2026-assessment
How to play the game:
Edburt: if ur reading this read this file and lmk if there is any thing ur confused aboutthat isnt explained in here
Intro:
You will first be introduced with a menu upon running this program. Either start a new game or load a old one or exit. When clicking load a new game, 
ensure that you have a save file already before clicking, if not the game will immediately send you into a new game.

Main goal:
Goal of the user is to not die, navigating the dungeon to collect items, improve their stats, defeat monsters and survive. To clear the game the user must kill the boss monster
at [4,4]. Clearing the boss will also wipe the players save. Dying however ends the game, to continue users must run the application again and load back up a previous save file

Saving/loading:
Saving can be done whenever a player is given the option to move around the dungeon i.e. 1. 2. 3. 4. NESW. typing 5 however will pull up the menu and
players can type s to save their game. NOTE, saving your game will overwrite your previous save file since only 1 save file exists. There are not multiple save files so
once you save the game, you can only load back from that point unless you choose to save again later.

In game menu: click 5 when givenan option to move
You can either choose to save, inspect inventory, view stats or leave the game
Choosing iventory, as long as the player has items in it they can choose to remove items in it. Also duplicates are not allowed so picking up new items will first check
if it already exists in the players inventory and the player will not receive said item. Only exception is health potions

Combat:
Upon combat, players will be asked whether they wish to roll a die. If they do roll it the die rolls a numebr between 1-20
any number higher then 10 is a damage bonus whilst lower is a debuf. the math works as number/10 times by damage e.g. if roll 15 you get a 1.5x damage multiplier
This is a RNG based combat system so players can either choose to take the risk if they believe they stand little chance against monsters or ignore it and continue with combat

In combat players can choose to either attack, use a health potion or escape
Attacking will deduct health from both the player and monster simultaneously
Health potions restore 30 hp but do not overflow past max hp. Players cannot use HP potions if they have none
Escape: There is a 10% chance in escaping. Upon success, monster dissappears and player returns to an empty tile however, it is advised players fight every monster they can
as they have a chance to drop items that can benefit the player

NPC's:
NPC interactions are fairly simple, only requiring yes or no input by users. These interactions can have a variety of positive, neutral, or negative outcomes.
Certain outcomes can inflcit permanent changes to a players stats
Other outcomes can affect players karma 

Karma:
These can be changed by a players items or their decisions in interacting with NPC's. Karma only affects the ending of the game, purely for in game lore and doesnt affect gameplay or combat.

Events: 
Can either be a trap, monster, NPC, BOSS, 

Traps damage players
Monsters intiate combat
NPC have dialogue and options
BOSS is the end game goal and msut be defeated to clear the game