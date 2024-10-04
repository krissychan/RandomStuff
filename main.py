#Krissy Killion
import sys

rooms = {  ##dictionary titled Rooms, containing the rooms and directions
    'Foyer': {
        'East': 'Great Hall'
    },
    'Great Hall': {
        'South': 'Parlor',
        'North': 'Dining Room',
        'East': 'Library'
    },
    'Dining Room': {
        'South': 'Great Hall',
        'East': 'Tower'
    },
    'Tower': {
        'West': 'Dining Room'
    },
    'Parlor': {
        'North': 'Great Hall',
        'East': 'Master Bedroom'
    },
    'Master Bedroom': {
        'West': 'Parlor'
    },
    'Library': {
        'West': 'Great Hall',
        'North': 'Courtyard'
    },
    'Courtyard': {'South: Library'}
}

itemdict = {  ##dictionary titled itemdict, containing the rooms and items
    'Great Hall': {
        'Item': 'Torch'
    },
    'Dining Room': {
        'Item': 'Meal',
        'NPC': 'A Waiter'
    },
    'Tower': {
        'Item': 'Big Silver Key 1'
    },
    'Parlor': {
        'Item': 'Mysterious Vial'
    },
    'Master Bedroom': {
        'NPC': 'Monster Under the Bed',
        'Item': 'Big Silver Key 2'
    },
    'Library': {
        'Item': 'Book'
    },
    'Courtyard': {
        'Item': 'Two Silver Locks (locked)',
        'NPC': 'The Lich'
    }
}

details = {  ##dictionary titled details, containing room details made for the room loop. excludes dining room, master bedroom, and courtyard because they have extra steps
    'Foyer':
    '-------\nYou are currently in the Foyer. Behind you, you see the door you came in.\nAs you look around, the pervasive darkness weighs on you. The only furnishing is a rug lining the middle of the floor.\nThere\'s only one way forward: East, to the Great Hall.\n-------\n',
    'Great Hall':
    '-------\nYou are currently in the Great Hall. On the east wall is a big stained glass window, looking into the courtyard.\nTo the north is a door, along with a fireplace. The walls, now peeling, are a deep red, and the floor is a dark hardwood.\nPillars rise in regular intervals around you, and empty picture frames litter the walls.\nTo the West lays the Foyer, locked up tight.\nFrom here, you can go three direcitons:\nNorth, to the Dining Room, East, to the Library, or South, to the Parlor\n-------\n',
    'Dining Room': '',
    'Tower':
    '-------\nYou are currently in the Tower. Spiral stone stairs line the walls, leading up to a simply room with four windows.\nFrom two of these windows, you can see the expansive courtyard below. It has a maze, a graveyard, and a wrought iron fence containing it all, lined with huge dark trees.\nIn this room you is a simple oak table with two chairs, and various items on it.\nFrom here, you can only go back West, to the dining room.\n-------\n',
    'Parlor':
    '-------\nYou are currently in the Parlor. A small but comfortable room, it has a recliner set in front of a stone, unlit fireplace.\nThere are decaying hunting trophies high on the wall, while bookshelves filled with dusty books line the lower wall.\nBack to the North is the Great Hall, and to the East is the Master Bedroom\n-------\n',
    'Master Bedroom': '',
    'Library':
    '-------\nYou are currently in the Library, a moderately sized room filled wall-to-wall and floor-to-ceiling with bookshelves.\nThere\'s a ladder to help reach the top shelves, but you decide against climbing it.\nTo the North is the Courtyard, door locked by two big silver locks with windows to either side of it.\nTo the West is the Great Hall.\n-------\n',
    'Courtyard': ''
}

playerinv = []  ##empty list called playerinv
waiter = []  ##empty list called waiter
monster = []  ##empty list called monster
yeslist = ['Yea', 'Yes', 'Ya', 'Ye',
           'Y']  ##list populated with different ways to say yes
nolist = ['No', 'N', 'Nay',
          'Nope']  ##list populated with different ways to say no


def game():  ##def game. contains the entire game loop

    def exitgame():  ##def exitgame. called upon when player types exit
        input('Well, there\'s always next time... Farewell! \n')
        sys.exit()

    def instructions(
    ):  ##def instructions. called upon when player types help or says yes to instructions during the intro
        input('In order to play Dreadspawn, you must type all your commands.')
        input(
            'When you are in a room and ready to move, type in one of the available directions.'
        )
        input(
            'For example, in the Foyer, you can only go East. So, enter "go east" in the box!'
        )
        input('When it comes to items, you must enter "pick up (item name)"')
        input('Please note, you must type the item name exactly!')
        input(
            'For example, in the Great Hall, there is a Torch. So, you would enter in "pick up Torch"!'
        )
        input('To access these instructions again, simply enter "help"!')
        input('I hope you enjoy the game! \n')
        if 'Torch' in playerinv:  ##checks for torch in playerinv. if it has it, passes
            pass
        else:  ##if it doesn't have torch
            thing()  ##starts the game loop by calling thing

    def lich(
    ):  ##def lich. called upon when you reach the courtyard, i.e. the winning condition
        print('-------')
        input(
            'You insert both keys into the locks, the Big Silver Locks falling off and hitting the floor with a thud.'
        )
        input('A shiver wracks your body. You\'re unsure why.')
        input(
            'As you venture into the courtyard, your torch gets dimmer and your body temperature slowly drops.'
        )
        input(
            'The courtyard is huge, expanding well beyond the walls of the house.'
        )
        input('The sky is still cloudy, and fog still permeates the grounds.')
        input(
            'As you saw from the tower, there\'s a maze directly outside of the door.'
        )
        input(
            'You knew that, beyond the maze, lay a great amount of empty land and a graveyard, all lined with a wrought iron fence.'
        )
        print('-------')
        input(
            'Shivering (from the cold, or from fear?), you walked into the maze.'
        )
        input(
            'You\'ve never been very good at mazes, so you followed a basic strategy: Always follow the right wall.'
        )
        input(
            'As you reach the end of the maze, your torch sputters and dies, leaving you in total darkness.'
        )
        input(
            'For a moment, you panic -- then you realize you can still feel the wall of the maze, so you continue onwards.'
        )
        input(
            'Before long, the clouds break, revealing a full moon that helps light your way, only vaguely dimmed by the fog.'
        )
        input(
            'Looking up in surprise, you realize the moon is almost at its peak. That means it\'s almost 3 in the morning!'
        )
        input(
            'A few moments later, you find the exit to the maze. Beyond it lay the empty courtyard, and to the left, a graveyard.'
        )
        print('-------')
        input(
            'You go over to the graves and examine them. They spanned several generations, and most shared a common name: Hornsby'
        )
        input(
            'You figure the odd-ones out were either important family friends, or females who married and changed their surname)'
        )
        input(
            'You feel an inexplicable grief upon viewing the most recent headstones:'
        )
        input('Dahlia Hornsby | Loving Wife and Mother of Two | 1920-1951')
        input(
            'Henry Hornsby III | Loving Husband and Father of Two | 1915-1951')
        input('Clarissa Hornsby | Gone Too Soon | 1947-1951')
        input('Henry Hornsby IV | Gone Too Soon | 1951-1951')
        input('Your chest aches with grieving, and.. hate.')
        input('Who was this family? What took them before their time?')
        print('-------')
        input(
            'As if in response to your question, you hear a low, rumbling laugh behind you...'
        )
        input('You turn around to see a floating skeleton behind you!')
        input(
            'The skeleton is wearing simple black robes with a hood, a crown upon his head.'
        )
        input(
            'It was holding a scepter with a carved wooden shaft topped with a strange green fire.'
        )
        input(
            'You noticed his skull is also carved, engraved with elaborate symbols inlaid with gold and accenting jewels.'
        )
        input(
            '"Foolish mortal! Who art thee to tread upon mine own land? Land yond I spill\'d mine own foe\'s blood on?"'
        )
        input(
            'Oh great. Not only is he a magical talking skeleton, he also speaks like he\'s in a Shakespearian play.'
        )
        input(
            '"Cometh hither, mortal, and I shalt add thy soul to mine own, thus sustaining mine own life force."'
        )
        input(
            'So now he wants to eat you. Wonderful. As your mind formulates this thought, you feel a sudden ice-cold chill in your pocket..'
        )
        input(
            'At this point, all you have is your burned out torch and that Mysterious Vial you picked up earlier.'
        )
        input(
            'Upon thinking about the Mysterious Vial, sudden clarity flashes through your mind:'
        )
        input('This magic skeleton is a Lich.')
        input('The item in your pocket is its Phylactery.')
        input('To kill the Lich, you must smash its Phylactery.')
        input(
            'The Lich started to float towards you, taking its time towards seemingly unsuspecting prey.'
        )
        input(
            'You shove your hand in your pocket, grasping for the Phylactery.')
        input(
            'When the Lich notices your movement, he comes to a halt, not quite nervous, but unwilling to continue forward until he knows more.'
        )
        input(
            'When the Phylactery is in your hand, you brandish it in front of the Lich.'
        )
        input('"Nay! Foolish mortal! What doth thee --"')
        input(
            'He didn\'t get to finish his sentence. You threw the Phylactery at the ground, shattering it.'
        )
        input(
            'You\'ve seen enough movies to know better than to let anyone monolgue at you.'
        )
        input(
            'The Lich didn\'t scream or flail on its way out, but rather slowly dissolved into a misty substance.'
        )
        input('Once the Lich was completely gone, you felt another chill.')
        input(
            '"Thank you..." Whispered quietly, on the wind -- so quietly, you weren\'t even sure if you heard right.'
        )
        input(
            'As if to prove you wrong, four ghosts appeared: a man, a woman, holding a baby, and a small girl.'
        )
        input(
            'They wave to you as they, too, disappear, released from their struggles and suffering wrought by the Lich.'
        )
        print('-------')
        input(
            'You walk around the side of the house until you find a gate that lets you back out to the front of the house.'
        )
        input(
            'You glance wearily around, suddenly unsure of the world around you.'
        )
        input(
            'Ghosts? Liches? Where had the knowledge of the Lich suddenly come from?'
        )
        input(
            'Debating what to do next, you ended up continuing on down your original path, pondering the experience you just had.'
        )
        input('The End!')
        sys.exit()

    def thing():  ##the meat of the game loop

        diningroomcount = 0  ##to call upon later
        bedroomcount = 0  ##to call upon later
        courtyardcount = 0  ##to call upon later
        playerroom = 'Foyer'  ##sets players room to Foyer

        while playerroom == 'Foyer':  ##if the player is in the foyer
            #print('You are in {}'.format(playerroom)) ##old code i was gonna use before changing it
            #moves = list(rooms[playerroom].keys())
            #print('Directions you can move in: ', str(moves)[1:-1])
            print(details[playerroom])  ##calls upon
            user_input = input(
                'Which direction would you like to go in?: \n'
            ).strip().lower().title().strip(
                'Go '
            )  ##accepts a user input for user_input, strip() removes extra whitespace at beginnign and end,
            ##lower() makes it all lowercase, title() capitalizes the first letter of each word, and strip('Go ') strips go from input. makes it universally useful for further code.
            while user_input not in rooms[playerroom].keys(
            ):  ##while user_input not in the keys for the current room. this line checks if the direction put in is valid in the dictionary
                ##this makes a loop to constantly check userinput if it is not a valid move
                if user_input == 'Exit':  ##if user types exit
                    exitgame()  ##calls the exitgame def
                elif user_input == 'Help':  ##if user types help
                    instructions()  ##calls the instructions def
                else:  ##otherwise
                    user_input = input(
                        '\nThat is not a valid input! Please try again. From the Foyer, you may only go East to the Great Hall. \n'
                    ).strip().lower().title()  ##accepts new user input
            if user_input in rooms[playerroom].keys() or user_input in (
                    'Go {}'.format(
                        rooms[playerroom].keys())):  ##if direction is valid
                print('\nNow moving to the {}... \n'.format(
                    rooms[playerroom]
                    [user_input]))  ##prints now moving to [room]
                print(
                    'Entering the Great Hall, the Foyer door slams behind you. You jiggle the doorknob and realize it\'s locked. You\'re now trapped in the castle. \n'
                )  ##a one-time print to emphasize you can't go back into the foyer
                playerroom = rooms[playerroom][
                    user_input]  ##assigns playerroom with the room related to the direction in user_input

        while playerroom == 'Great Hall':  ##if player is in the foyer
            if 'Torch' in playerinv:  ##if player has the torch
                break  ##breaks this loop

            elif 'Torch' not in playerinv:  ##if torch not in player inv
                print(details[playerroom])  ##prints the related details dict
                print('In this room, there is a {}. \n'.format(
                    itemdict[playerroom]['Item'])
                      )  ##prints a message showing available item in this room
                greathallinput = input(
                    'You have not yet picked up the Torch, which will be necessary to continue, as the castle has no other light sources. \n'
                ).strip().lower().title(
                )  ##accepts input stripped, lowered, and titled
                while greathallinput not in 'Pick Up {}'.format(
                        itemdict[playerroom]
                    ['Item']):  ##if "Pick Up 'Item'" not in greathallinput
                    if greathallinput == 'Exit':  ##if it's exit
                        exitgame()  ##calls exit def
                    elif greathallinput == 'Help':  ##if it's help
                        instructions()  ##calls instructions def
                    else:  ##otherwise, continues the loop until a valid input
                        greathallinput = input(
                            '\nThat is not a valid input! Please try again. Try typing: "pick up Torch" \n'
                        ).strip().lower().title()
                if greathallinput == 'Pick Up {}'.format(
                        itemdict[playerroom]
                    ['Item']):  ##if input is "Pick Up 'Item'"
                    input(
                        '\n*~Congratulations!~* You picked up the {}.'.format(
                            itemdict[playerroom]['Item'])
                    )  ##an input so player has to hit enter to continue alerting them to the item they picked up
                    playerinv.append(
                        itemdict[playerroom]
                        ['Item'])  ##adds the item to the playerinv list
                    input(
                        'Your inventory now consists of: {} \n'.format(
                            str(playerinv)[1:-1])
                    )  ##an input so player has to hit enter to continue alerting them to their current inventory
                    del itemdict[
                        playerroom]  ##deletes the playerroom from itemdict so it can't be called on later

        while playerroom != 'Foyer':  ##if player is not in the Foyer
            #print('You are in the {}'.format(playerroom)) ##old code i was going to use before i wanted to add more detail
            #moves = list(rooms[playerroom])
            #print('Directions you can move in: ', moves)#str(moves)[1:-1])
            print(details[playerroom])  ##etc.
            if playerroom != 'Master Bedroom' and playerroom != 'Dining Room' and playerroom != 'Courtyard':  ##if playerroom isn't the special rooms master bed, dining, or courtyard
                if playerroom not in itemdict:  ##checks if the current room is in the item dict. if its not,
                    user_input = input(
                        'There are no items remaining in this room. Which direction would you like to go? \n'
                    ).strip().lower().title().strip(
                        'Go ')  ##accepts input for direction
                    while user_input not in rooms[playerroom].keys(
                    ):  ##same old error checker loop
                        if user_input == 'Exit':
                            exitgame()
                            break
                        elif user_input == 'Help':
                            instructions()
                            break
                        else:
                            user_input = input(
                                '\nThat is not a valid input! Try typing a direction. \n'
                            ).strip().lower().title().strip('Go ')
                    if user_input in rooms[playerroom].keys(
                    ):  ##if direction is valid, same old room move loop
                        print('\nNow moving to the {}... \n'.format(
                            rooms[playerroom][user_input]))
                        playerroom = rooms[playerroom][user_input]
                        continue  ##goes back to the while loop

                elif playerroom in itemdict:  ##if the current room IS in the item dict, i.e. the current room has an item
                    print('In this room, there is a {}. \n'.format(
                        itemdict[playerroom]
                        ['Item']))  ##prints room's curent item
                    user_input = input(
                        'You must pick up the item to continue.\n'
                    ).strip().lower().title(
                    )  ##alerts player they MUST pick up the item, and accepts input
                    while user_input != 'Pick Up {}'.format(
                            itemdict[playerroom]['Item']
                    ) and playerroom != 'Dining Room' and playerroom != 'Master Bedroom':  ##same old error checker loop
                        if user_input == 'Exit':
                            exitgame()
                            break
                        elif user_input == 'Help':
                            instructions()
                            break
                        elif user_input != 'Pick Up {}'.format(
                                itemdict[playerroom]['Item']
                        ) and playerroom != 'Dining Room' and playerroom != 'Master Bedroom':
                            user_input = input(
                                '\nPlease pick up the item before you continue! \n'
                            ).strip().lower().title()
                            pass
                    if user_input == 'Pick Up {}'.format(
                            itemdict[playerroom]['Item']
                    ) and playerroom != 'Dining Room' and playerroom != 'Master Bedroom':  ##same old item pickup loop
                        input('\n*~Congratulations!~* You picked up the {}.'.
                              format(itemdict[playerroom]['Item']))
                        playerinv.append(itemdict[playerroom]['Item'])
                        input('Your inventory now consists of: {} \n'.format(
                            str(playerinv)[1:-1]))
                        del itemdict[playerroom]

            while playerroom == 'Dining Room':  ##if player room is dining room, prints out some story
                print('-------')
                print(
                    'Welcome to the Dining Room. The room is large with a high roof and several windows facing the woods outside.'
                )
                print(
                    'There are three chandeliers hanging from the ceiling, and a long table with 10 chairs in the center of the room.'
                )
                print('In this room, you see a Waiter.')
                print('-------')
                if 'Book' not in waiter and diningroomcount < 1:  ##if list waiter doesn't have Book and diningroomcount is less than 1
                    input(
                        'The waiter is ominously hovering in the corner of the Dining Room.'
                    )
                    input(
                        'Lit only by your torch, donned in a classic tuxedo from the 1900s, in his hand a silver platter with a lid...'
                    )
                    input('He looks rather bored.')
                    input(
                        'As you approach the waiter, his eyes track your movements.'
                    )
                    input(
                        'Once you\'re close enough, you greet him and introduce yourself. He doesn\'t respond, instead just staring at you.'
                    )
                    input(
                        'You wave your hand in front of his face, and he scrunches it up in annoyance. So.. he can hear you, but he won\'t respond.'
                    )
                    input('You ask if he\'s okay, and he gives a slight nod.')
                    input(
                        'You heave a sigh and comment that he must be bored. He gives a nod to this, too.'
                    )
                    input(
                        'You ponder this for a moment, and offer a trade: an entertainment source for his mysterious silver platter.'
                    )
                    input(
                        'Yet again, he nods. Pondering this trade, you wonder where you might find entertainment in this dilapidated old castle.'
                    )
                    print('-------')
                    diningroomcount = 1  ##sets dining room count to 1. this is used so if players return to the room, they get different dialogue
                    if 'Book' in playerinv and 'Book' not in waiter:  ##if player already has the book and waiter doesn't contain Book
                        input(
                            'You suddenly remember the book you picked up from the library earlier. Would this suffice?'
                        )
                        input(
                            'You tentatively hand the book to the waiter, worried about his reaction..'
                        )
                        input(
                            'Upon seeing the book, the waiter lets out the vaguest smile.'
                        )
                        input(
                            'He then sets down his silver tray, takes the book from you, and proceeds to sit.'
                        )
                        input(
                            'You notice he is facing away from both you and the silver tray...'
                        )
                        input(
                            'You decide to take the lid off the silver tray and see what\'s inside.'
                        )
                        input(
                            'Surprisingly, or perhaps unsurprisingly, inside the tray is a Meal!'
                        )
                        input(
                            'You put the meal in your inventory and prepare to continue your journey.'
                        )
                        print('-------')
                        input('\n*~Congratulations!~* You picked up the {}.'.
                              format(itemdict[playerroom]
                                     ['Item']))  ##same old item pickup loop
                        playerinv.append(itemdict[playerroom]['Item'])
                        input('Your inventory now consists of: {} \n'.format(
                            str(playerinv)[1:-1]))
                        del itemdict[playerroom]
                        waiter.append(
                            'Book'
                        )  ##adds Book to list waiter for further loop iterations
                        playerinv.remove('Book')  ##removes book from inventory
                        diningroomdirection = input(
                            'From the Dining Room, you may move East to the Tower, or South, back to the Great Hall. Which direction would you like to go? \n'
                        ).strip().lower().title().strip(
                            'Go ')  ##same old input
                        while diningroomdirection not in rooms[
                                playerroom].keys(
                                ):  ##same old error checker loop
                            if diningroomdirection == 'Exit':
                                exitgame()
                                break
                            elif diningroomdirection == 'Help':
                                instructions()
                                break
                            else:
                                diningroomdirection = input(
                                    '\nThat is not a valid input! Please try again. You may go East, to the Tower, or South, back to the Great Hall. \n'
                                ).strip().lower().title().strip('Go ')
                        if diningroomdirection in rooms[playerroom].keys(
                        ):  ##same old movement loop
                            print('\nNow moving to the {}... \n'.format(
                                rooms[playerroom][diningroomdirection]))
                            playerroom = rooms[playerroom][diningroomdirection]
                            break
                    elif 'Book' not in playerinv and 'Book' not in waiter:  ##if playerinv doesn't have book and waiter doesn't have done
                        input(
                            'You feel the urge to leave the room until you satisfy his request.'
                        )
                        print('-------')
                        diningroomdirection = input(
                            'From the Dining Room, you may move East to the Tower, or South, back to the Great Hall. Which direction would you like to go? \n'
                        ).strip().lower().title().strip(
                            'Go ')  ##same old input
                        while diningroomdirection not in rooms[
                                playerroom].keys(
                                ):  ##same old error checker loop
                            if diningroomdirection == 'Exit':
                                exitgame()
                                break
                            elif diningroomdirection == 'Help':
                                instructions()
                                break
                            else:
                                diningroomdirection = input(
                                    '\nThat is not a valid input! Please try again. You may go East, to the Tower, or South, back to the Great Hall. \n'
                                ).strip().lower().title().strip('Go ')
                        if diningroomdirection in rooms[playerroom].keys(
                        ):  ##same old move loop
                            print('\nNow moving to the {}... \n'.format(
                                rooms[playerroom][diningroomdirection]))
                            playerroom = rooms[playerroom][diningroomdirection]
                            break

                elif 'Book' not in waiter and 'Book' not in playerinv and diningroomcount > 0:  ##if book not in waiter and book not in player inv and diningroomcount greater than 0
                    ##i.e. if it's a repeat visit and you still don't have the book
                    input(
                        'The waiter is still waiting for his entertainment...')
                    input(
                        'You feel the urge to leave the room until you satisfy his request.'
                    )
                    print('-------')
                    diningroomdirection = input(
                        'From the Dining Room, you may move East to the Tower, or South, back to the Great Hall. Which direction would you like to go? \n'
                    ).strip().lower().title().strip('Go ')  ##same old input
                    while diningroomdirection not in rooms[playerroom].keys(
                    ):  ##same old error checker loop
                        if diningroomdirection == 'Exit':
                            exitgame()
                            break
                        elif diningroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            diningroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may go East, to the Tower, or South, back to the Great Hall. \n'
                            ).strip().lower().title().strip('Go ')
                    if diningroomdirection in rooms[playerroom].keys(
                    ):  ##same old move loop
                        print('\nNow moving to the {}... \n'.format(
                            rooms[playerroom][diningroomdirection]))
                        playerroom = rooms[playerroom][diningroomdirection]
                        break

                elif 'Book' in playerinv and 'Book' not in waiter:  ##final check for book in playerinv
                    input(
                        'You tentatively hand the book to the waiter, worried about his reaction..'
                    )
                    input(
                        'Upon seeing the book, the waiter lets out the vaguest smile.'
                    )
                    input(
                        'He then sets down his silver tray, takes the book from you, and proceeds to sit.'
                    )
                    input(
                        'You notice he is facing away from both you and the silver tray...'
                    )
                    input(
                        'You decide to take the lid off the silver tray and see what\'s inside.'
                    )
                    input(
                        'Surprisingly, or perhaps unsurprisingly, inside the tray is a Meal!'
                    )
                    input(
                        'You put the meal in your inventory and prepare to continue your journey.'
                    )
                    print('-------')
                    input(
                        '\n*~Congratulations!~* You picked up the {}.'.format(
                            itemdict[playerroom]
                            ['Item']))  ##same old item loop
                    playerinv.append(itemdict[playerroom]['Item'])
                    input('Your inventory now consists of: {} \n'.format(
                        str(playerinv)[1:-1]))
                    del itemdict[playerroom]
                    waiter.append('Book')
                    playerinv.remove('Book')
                    diningroomdirection = input(
                        'From the Dining Room, you may move East to the Tower, or South, back to the Great Hall. Which direction would you like to go? \n'
                    ).strip().lower().title().strip('Go ')  ##same old input
                    while diningroomdirection not in rooms[playerroom].keys(
                    ):  ##same old error checker loop
                        if diningroomdirection == 'Exit':
                            exitgame()
                            break
                        elif diningroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            diningroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may go East, to the Tower, or South, back to the Great Hall. \n'
                            ).strip().lower().title().strip('Go ')
                    if diningroomdirection in rooms[playerroom].keys(
                    ):  ##same old move loop
                        print('\nNow moving to the {}...'.format(
                            rooms[playerroom][diningroomdirection]))
                        playerroom = rooms[playerroom][diningroomdirection]
                        break

                elif 'Book' in waiter:  ##otherwise if done in waiter
                    print(
                        'The waiter is still sitting there, reading the book. Must be a good one..\n'
                    )
                    print('-------')
                    diningroomdirection = input(
                        'From the Dining Room, you may move East to the Tower, or South, back to the Great Hall. Which direction would you like to go? \n'
                    ).strip().lower().title().strip('Go ')  ##etc
                    while diningroomdirection not in rooms[playerroom].keys():
                        if diningroomdirection == 'Exit':
                            exitgame()
                            break
                        elif diningroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            diningroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may go East, to the Tower, or South, back to the Great Hall. \n'
                            ).strip().lower().title().strip('Go ')
                    if diningroomdirection in rooms[playerroom].keys():
                        print('\nNow moving to the {}...'.format(
                            rooms[playerroom][diningroomdirection]))
                        playerroom = rooms[playerroom][diningroomdirection]
                        break

            while playerroom == 'Master Bedroom':  ##same loop was waiter and dining room but with a bedroom and a monster
                print('-------')
                print(
                    'You are now in the Master Bedroom, a moderately sized room furnished with rugs, a bed, and a desk.'
                )
                print(
                    'The rugs are stacked seemingly randomly and haphazardly, covering the entire floor in an uneven surface.'
                )
                print(
                    'The room has windows on the South and East walls. The bed centered on the East wall, right under the window.'
                )
                print(
                    'On the west wall, next to the door you came in, is the desk.'
                )
                print('-------')
                input(
                    'As you make these observations, you notice something fuzzy moving under the bed...'
                )
                input(
                    'Upon closer examination, you realize one of the rugs came to life! Wait, no, not a rug...'
                )
                input('In this room, you see a Monster Under the Bed!')
                print('-------')

                if 'Meal' not in monster and bedroomcount < 1:
                    input(
                        'At first, you\'re terrified. A monster. A real monster! However, nothing happens.'
                    )
                    input(
                        'The Monster Under the Bed doesn\'t seem to notice it\'s been spotted...'
                    )
                    input(
                        'You take small steps closer, scared, but also curious.'
                    )
                    input(
                        'When it notices you getting closer, it draws its hand back further under the bed.'
                    )
                    input(
                        'Unsure if it is trying to hide itself for a better ambush, or hide itself because it\'s scared...'
                    )
                    input('You decide to speak to it. "Hello?"')
                    input(
                        'From under the bed, you hear a grunting noise that sounds surprised.'
                    )
                    input(
                        '"It\'s okay, I\'m not here to hurt you. Honestly, I don\'t even know WHY I\'m here."'
                    )
                    input(
                        'The monster slowly slides out of the bed, glaring at you. Suddenly, you hear a growl..'
                    )
                    input(
                        'Petrified, you put your hands up in a surrendering gesture, unsure if monsters understood body language or not.'
                    )
                    input(
                        'However, you soon realize that it\'s not the monster growling, but rather, the monster\'s stomach.'
                    )
                    input(
                        'Now that the monster is out from under the bed, you see something shiny in your torchlight. A key?'
                    )
                    print('-------')
                    bedroomcount = 1
                    if 'Meal' in playerinv and 'Meal' not in monster:
                        input(
                            'As the monster\'s stomach begins to growl again, you decide to give it the Meal from your inventory.'
                        )
                        input(
                            'When the monster sees the meal, its stomach growls even louder. However, it eyes you with suspicion, unwilling to get close.'
                        )
                        input(
                            'Remembering the key under the bed, you slowly put the meal on the desk and move to the North wall, away from the desk and the bed.'
                        )
                        input(
                            'The monster, starving, decides you\'ve made it safe enough to come out and eat.'
                        )
                        input(
                            'While it eats, you grab the key from under the bed. Better get out of here while you can!'
                        )
                        print('-------')
                        input('\n*~Congratulations!~* You picked up the {}.'.
                              format(itemdict[playerroom]['Item']))
                        playerinv.append(itemdict[playerroom]['Item'])
                        input('Your inventory now consists of: {} \n'.format(
                            str(playerinv)[1:-1]))
                        del itemdict[playerroom]
                        monster.append('Meal')
                        bedroomdirection = input(
                            'From the Master Bedroom, you may return to the Parlor by going West. \n'
                        ).strip().lower().title().strip('Go ')
                        while bedroomdirection not in rooms[playerroom].keys():
                            if bedroomdirection == 'Exit':
                                exitgame()
                                break
                            elif bedroomdirection == 'Help':
                                instructions()
                                break
                            else:
                                bedroomdirection = input(
                                    '\nThat is not a valid input! Please try again. You may only go West back to the Parlor. \n'
                                ).strip().lower().title().strip('Go ')
                        if bedroomdirection in rooms[playerroom].keys():
                            print('\nNow moving to the {}...'.format(
                                rooms[playerroom][bedroomdirection]))
                            playerroom = rooms[playerroom][bedroomdirection]
                            break
                    elif 'Meal' not in playerinv and 'Meal' not in monster:
                        input(
                            'It won\'t be safe to be in the room until you find something to satisfy the monster\'s hunger. Best leave for now.'
                        )
                        print('-------')
                        bedroomdirection = input(
                            'From the Master Bedroom, you may return to the Parlor by going West. \n'
                        ).strip().lower().title().strip('Go ')
                        while bedroomdirection not in rooms[playerroom].keys():
                            if bedroomdirection == 'Exit':
                                exitgame()
                                break
                            elif bedroomdirection == 'Help':
                                instructions()
                                break
                            else:
                                bedroomdirection = input(
                                    '\nThat is not a valid input! Please try again. You may only go West back to the Parlor. \n'
                                ).strip().lower().title().strip('Go ')
                        if bedroomdirection in rooms[playerroom].keys():
                            print('\nNow moving to the {}...'.format(
                                rooms[playerroom][bedroomdirection]))
                            playerroom = rooms[playerroom][bedroomdirection]
                            break

                elif 'Meal' not in monster and 'Meal' not in playerinv and bedroomcount > 0:
                    input('The monster\'s stomach is still loudly growling...')
                    input(
                        'It won\'t be safe to be in the room until you find something to satisfy the monster\'s hunger. Best leave for now.'
                    )
                    print('-------')
                    bedroomdirection = input(
                        'From the Master Bedroom, you may return to the Parlor by going West. \n'
                    ).strip().lower().title().strip('Go ')
                    while bedroomdirection not in rooms[playerroom].keys():
                        if bedroomdirection == 'Exit':
                            exitgame()
                            break
                        elif bedroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            bedroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may only go West back to the Parlor. \n'
                            ).strip().lower().title().strip('Go ')
                    if bedroomdirection in rooms[playerroom].keys():
                        print('\nNow moving to the {}...'.format(
                            rooms[playerroom][bedroomdirection]))
                        playerroom = rooms[playerroom][bedroomdirection]
                        break

                elif 'Meal' in playerinv and 'Meal' not in monster:
                    input(
                        'As the monster\'s stomach begins to growl again, you decide to give it the Meal from your inventory.'
                    )
                    input(
                        'When the monster sees the meal, it\'s stomach growls even louder. However, it eyes you with suspicion, unwilling to get close.'
                    )
                    input(
                        'Remembering the key under the bed, you slowly put the meal on the desk and move to the North wall, away from the desk and the bed.'
                    )
                    input(
                        'The monster, starving, decides you\'ve made it safe enough to come out and eat.'
                    )
                    input(
                        'While it eats, you grab the key from under the bed. Better get out of here while you can!'
                    )
                    print('-------')
                    input(
                        '\n*~Congratulations!~* You picked up the {}.'.format(
                            itemdict[playerroom]['Item']))
                    playerinv.append(itemdict[playerroom]['Item'])
                    input('Your inventory now consists of: {} \n'.format(
                        str(playerinv)[1:-1]))
                    del itemdict[playerroom]
                    monster.append('Meal')
                    bedroomdirection = input(
                        'From the Master Bedroom, you may return to the Parlor by going West. \n'
                    ).strip().lower().title().strip('Go ')
                    while bedroomdirection not in rooms[playerroom].keys():
                        if bedroomdirection == 'Exit':
                            exitgame()
                            break
                        elif bedroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            bedroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may only go West back to the Parlor. \n'
                            ).strip().lower().title().strip('Go ')
                    if bedroomdirection in rooms[playerroom].keys():
                        print('\nNow moving to the {}...'.format(
                            rooms[playerroom][bedroomdirection]))
                        playerroom = rooms[playerroom][bedroomdirection]
                        break

                elif 'Meal' in monster:
                    print(
                        'The monster has finished its meal and gone back under the bed. You hear a gentle snoring noise. Better leave it alone...'
                    )
                    print('-------')
                    bedroomdirection = input(
                        'From the Master Bedroom, you may return to the Parlor by going West. \n'
                    ).strip().lower().title().strip('Go ')
                    while bedroomdirection not in rooms[playerroom].keys():
                        if bedroomdirection == 'Exit':
                            exitgame()
                            break
                        elif bedroomdirection == 'Help':
                            instructions()
                            break
                        else:
                            bedroomdirection = input(
                                '\nThat is not a valid input! Please try again. You may only go West back to the Parlor. \n'
                            ).strip().lower().title().strip('Go ')
                    if bedroomdirection in rooms[playerroom].keys():
                        print('\nNow moving to the {}...'.format(
                            rooms[playerroom][bedroomdirection]))
                        playerroom = rooms[playerroom][bedroomdirection]
                        break

            while playerroom == 'Courtyard':  ##while playerroom is courtyard
                print('-------')
                input(
                    'As you attempt to enter the Courtyard from the Library, you notice two Big Silver Locks on the door.'
                )
                input(
                    'Beyond the door, you can\'t see much looking out the windows -- it\'s misty and dark outside, severely limiting your vision.'
                )
                if courtyardcount < 1:  ##if courtyardcount less than 1
                    if 'Big Silver Key 1' not in playerinv and 'Big Silver Key 2' not in playerinv:  ##if keys not in inv
                        input(
                            'On the door, you notice two locks. You wonder if the keys are laying around the castle?'
                        )
                        input(
                            'Unsure of what else to do, you return to the Library to look for the keys.'
                        )
                        print('------- \n')
                        courtyardcount = 1  ##courtyard count 1
                        playerroom = 'Library'  ##sets player room to library with no input
                    elif ('Big Silver Key 1' not in playerinv
                          and 'Big Silver Key 2' in playerinv) or (
                              'Big Silver Key 1' in playerinv
                              and 'Big Silver Key 2'
                              not in playerinv):  ##if one key is in inventory
                        input(
                            'While you have one of the keys, you decide not to insert it yet.'
                        )
                        input('Wouldn\'t want to lose it, now would we?')
                        input(
                            'Better go back through the house for the final key, starting with returning to the Library!'
                        )
                        print('------- \n')
                        playerroom = 'Library'  ##sets player room to library
                    elif 'Big Silver Key 1' in playerinv and 'Big Silver Key 2' in playerinv:  ##if both keys are in playerinv
                        lich()
                elif courtyardcount > 0:  ##if courtyard count more than 0
                    if 'Big Silver Key 1' not in playerinv and 'Big Silver Key 2' not in playerinv:  ##as above, so below
                        input(
                            'Back at the door to the Courtyard, you still don\'t have either key you require to progress.'
                        )
                        input(
                            'Unsure of what else to do, you return to the Library to look for the keys.'
                        )
                        print('------- \n')
                        playerroom = 'Library'
                    elif ('Big Silver Key 1' not in playerinv
                          and 'Big Silver Key2' in playerinv) or (
                              'Big Silver Key 1' in playerinv
                              and 'Big Silver Key 2' not in playerinv):
                        input(
                            'Back at the door to the courtyard, you only have one key you need.'
                        )
                        input(
                            'You decide not to insert it. Wouldn\'t want to lose it, now would we?'
                        )
                        input(
                            'Better go back through the house for the final key, starting with returning to the Library!'
                        )
                        print('------- \n')
                        playerroom = 'Library'
                    elif 'Big Silver Key 1' in playerinv and 'Big Silver Key 2' in playerinv:
                        lich()

    def readydef():  ##used to check if player is ready
        ready = input('Are you ready to explore? Type \'Yes\' or \'No\' \n'
                      ).strip().lower().title()  ##same old input
        if ready in nolist:  ##if answer is no
            ready = input(
                '\nAre you sure you would like to leave? Type yes to leave, and no to stay... \n'
            ).strip().lower().title()  ##same old input
            while ready not in yeslist and ready not in nolist and ready != 'Exit':  ##same old error checker loop
                ready = input('\nTry again! Please enter yes, no, or exit! \n'
                              ).strip().lower().title()
            if ready in yeslist or ready == 'Exit':  ##if answer is yes or exit
                exitgame()  ##calls exitgame
            elif ready in nolist:  ##if answer is no
                return readydef()  ##returns to readydef
        elif ready in yeslist:  ##elif ready is in yeslist
            input('\nWell, if you\'re certain... ')
            pass  ##passes
        elif ready == 'Exit':  ##if ready is exit
            exitgame()  ##exitgame function
        else:  ##else
            print('\nTry again! Please enter yes, no, or exit! \n'
                  )  ##prints error
            return readydef()  ##returns to readydef

        instru = input('\nWould you like to see the instructions? \n').strip(
        ).lower().title()  ##same old input
        while instru not in yeslist and instru not in nolist and instru != 'Exit':  ##as above, so below
            instru = input(
                '\nThis is not a valid input! Please type Yes or No.\n').strip(
                ).lower().title()
        if instru in nolist:
            print(
                '\nVery well. Good luck! Type "help" later if you change your mind. \n'
            )
            thing()
        elif instru in yeslist:
            instructions()
        elif instru == 'Exit':
            exitgame()

    def intro():  ##defines intro which ends with calling readydef
        input('Welcome to Dreadspawn! Press enter to continue.')
        input('In this world, anything is possible...')
        input(
            'You\'re a lone traveler, wandering the roads on a cloudy, foggy evening...'
        )
        input('when you come across a dilapidated castle.')
        input('A strange compulsion pulls you into the castle foyer,')
        input(
            'where you notice the permeating chill and darkness in the castle...'
        )
        input('Without knowing why, you venture farther into the castle,')
        input('where the only light comes from a flickering torch.')
        input('As you proceed through the rooms, you must collect items,')
        input('solve puzzles, and defeat the final boss. \n')
        readydef()

    intro()  ##calls intro


game()  ##calls game
