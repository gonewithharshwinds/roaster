import random


def roaster(val,roast):
    roast=random.randint(0,20)
    switcher = {
        1: "If I throw a stick, will you leave?",
        2: "You are more disappointing than an unflavored nacho.",
        3: "It's not possible to underestimate you.",
        4: "Oh my god! It breathes!",
        5: "Well, the jerk store called. They’re running out of you.",
        6: "Being with you is like having period cramps.",
        7: "Wow, I bet you even a fart smells better than you!",
        8: "You’re so fake, Barbie is jealous.",
        9: "Light travels faster than sound, which is why you seemed bright until you spoke.",
        10: "When you start talking, I stop listening! Isn't it magical?",
        11: "Your face makes onions cry.",
        12: "My phone battery lasts longer than your relationships.",
        13: "My middle finger gets a boner every time I see you.",
        14: "Calm down. Take a deep breath and then hold it for about twenty minutes.",
        15: "The smartest thing that ever came out of your mouth was p3nis. ",
        16: "I am allergic to stupidity, so I break out in sarcasm.",
        17: "You’re the reason I prefer machines to people. ",
        18: "You’re a gray sprinkle on a rainbow cupcake.",
        19: "It’s scary to think people like you are allowed to vote.",
        20: "The last time I saw something like you I flushed."
    }
    if val == 'Y':
        return switcher.get(roast,"Not today you cute sadist f**k.")
    else :
        return ('F**k you Tony!', exit())
 
# Driver program
while 1:
    roast = 0
    val = input("Roast? Y/N :\n")
    print(roaster(val,roast))
    print("\n")

