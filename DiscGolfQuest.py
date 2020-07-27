import random

NumberOfPlayer = 0
Cards = [
'Throw your first drive with your bag on',
'Throw with your off hand',
'Another player chooses your disc',
'Putter only for the hole',
'Throw your Highest speed disc for every shot',
'Switch bags with a player for the hole',
'Sidearm only for the hole',
'Backhand only for the hole',
'Throw a thumber/tomahawk/scoober on the drive',
'Throw a roller for your drive',
'Choose disc at random from your bag',
'Choose disc at random from another players bag',
'Stand still drive',
'360 drive',
'Throw a mini for your drive',
'Switch lies with a player after the drive',
'Mulligan!',
'Putt while blindfolded',
'Another player caddies for you for the hole',
'Player must turbo putt',
'Throw midranges only for the hole',
'Target player must rethrow' ,
'Nope!(cancel out any card currently being played)',
'Test'
    ]

print("Here are your cards!\n", random.choice(Cards),"\n",random.choice(Cards),"\n",random.choice(Cards),"\n")
