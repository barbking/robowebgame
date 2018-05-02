# From Learn Python the Hard Way

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.count = 0
        self.paths = {}
        self.soundEffect = ""

    def go(self, action):
        # direction comes from action input
        print("Self", self)
        print("direction", action)
        print("name", self.name)

        if self.name == "Laser Weapon Armory":
            return check_code(self,action)

        return self.paths.get(action, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
'''
The Google AI robot army is taking over the world and destroying all humankind.
You are the only member left of the secret Duck Duck Go rebels with access to the
main server room that is controlling the Google AI army.  Your last mission is to 
get the neutron destruct bomb from the Weapons Armory, put it in the main server room, 
and blow it up after getting into your escape hovercraft.
            
You're running down the central corridor to the Weapons Armory when a robot
jumps out.  It's blocking the door to the Armory and about to blast you with its
ray gun.
            
You are options are (1) to shoot, (2) to dodge and (3) to ask Siri for help.
Enter 1, 2 or 3:
''')

laser_weapon_armory = Room('Laser Weapon Armory',
'''
Lucky for you were able to ask Siri on your iPhone for help on how to dodge robots.
Siri distracts the robot by insulting Google's AI, while Siri and the Google AI
robot exchange insults, you shot the robot in its glass eyes and jump through
the Amory door.

You do a dive roll into the Weapon Armory, crunch and scan the room for more robots
that might be hiding.  It's dead quiet, too quiet.  You stand up and run to the far
side of the room and find the neutron bomb in its container.  There's a keypad
lock on the box and you need the code to get the bomb out.  If you get the code wrong
10 times then the lock closes forever and you can't get the bomb.  The code is
3 digits.

Make your best attempt at guessing a 3 digit code.
[keypad]:
''')

the_server_room = Room('The Server Room',
'''
You burst into the server room with the neutron destruct bomb under your arm
and surprise five Google AI robots guarding the room.  They haven't pulled their
weapons out yet, as they see the active bomb under your arm and don't want to
set it off.

Do you (1) throw the bomb or (2) slowly place the bomb?

Enter 1 or 2:
''')

escape_hovercraft = Room("Escape Hovercraft",
'''
You rush outside desperately trying to make it to the escape Duck Duck Go hovercrafts 
before the whole building explodes.  It seem like hardly any robots are in the area,
so your run is clear of interference.  You get to the parking lot and need to
pick one.  Some have been damaged by robots but you don't have time to check
them all.  There are five hovercraft, pick one to take.

Enter a number between 1 and 5 to select a hovercraft:
''')

the_end_winner = Room('The End',
'''
You jump into the hovercraft 2 and hit the go button.  The hovercraft
easily takes off in the air.  As it flies into the sky, you see the server building
explode...taking out the Google Robot AI army control.  You won!
''')

the_end_loser = Room("The End",
'''
You jump into a random pod and hit go button.  The hovercraft takes off but
then implodes as the engine ruptures, blowing you up into a million pieces.
''')

the_end_loser_dodge = Room("The End",
'''
Lise a world class boxer you dodge, weave, slip and slide right as
the robot's blaster cranks a laser past your head.  In the middle of your
artful dodge your foot slips and you bang your head on the metal wall and
pass out.  You wake up shortly after only to die as the robot blasts you
with it's laser.
''')

the_end_shoot = Room("The End",
'''
Quick on the draw you yank out your blaster and fire at the robot.  You're
laser hits the robot's reflective shield and bounces back at you, striking you 
dead.  There is no beating the Google AI robots taking over the world.
''')

the_end_loser_throw_bomb = Room("The End",
'''
In a panic you throw the bomb at the group of robots and make a leap for the
door.  Right as you drop it, a robot shoots you in the back killing you.  As
you die you see another robot frantically try to disarm the bomb.  You die
knowing they will probably blow up along with the main server when the bomb goes off.
''')

the_end_code_failure = Room ("The End",
'''
The lock buzzes one last time and then you hear a sickening
melting sound as teh mechanism is fused together.  You decide to sit there,
where the Google AI robots find you and blow you up with their laser guns.
''')


escape_hovercraft.add_paths({
    '2': the_end_winner,
    ' ': the_end_loser
})

generic_death = Room("death", "You died.")

the_server_room.add_paths({
    '1': the_end_loser_throw_bomb,
    '2': escape_hovercraft
})

laser_weapon_armory.add_paths({
    '333': the_server_room,
    'tryagain': laser_weapon_armory,
    'end': the_end_code_failure

})

central_corridor.add_paths({
    '1' : the_end_shoot,
    '2' : the_end_loser_dodge,
    '3' : laser_weapon_armory
})

START = 'central_corridor'

def check_code(self, action):
    if action == "333":
        self.soundEffect = "CLICK!"
        return self.paths.get("333", None)
    elif self.count < 3:
        self.count += 1
        self.soundEffect = "BZZZEDDO!!!"
        print("count",self.count)
        return self.paths.get("tryagain", None)
    else:
        self.soundEffect = "EXPLOSION!!!"
        self.action = "end"
        return self.paths.get("end", None)


def load_room(name):
    '''
    There is a potential security problem here.
    Who gets to set name?  Cna that expose a variable?
    '''
    return globals().get(name)

def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key