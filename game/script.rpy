# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edward") # ed for short
define h = Character("Hailey") # just hailey
define o = Character("Odelyna") # ody for short
define k = Character("The King") # king for short
define s = Character("Sybili") # syb for short

define nemo = Character("__ _")
define unknown = Character("???")


# The game starts here.

label start:
    nemo "Once upon a time there was a great kingdom, by the name of -, in the land of -. The kingdom ruled for many a millenium, bringing peace and prosperity upon its people."
    pause 2.0
    scene intro 1
    with fade
    
    nemo ""
    
    nemo "But every century…"
    
    scene intro 2
    with fade
    play sound thunder
    nemo "A terrible plague would occur."

    nemo "For a decade or more, demons would ravage the land and spread rot among the kingdom."
    
    scene intro 3
    with dissolve
    nemo "And every century, without fail, a mage of Light would rise to banish the rot."
    pause 2.0
    
    scene room ed
    with fade
    show ody lean

    unknown "Hey, sleepyhead! You wouldn't miss your big day, now, would you?"

    h "Wh- What?"

    "You don't recognise this person, or what she's talking about. At all."

    h "Who are you? How are you in my- what is this place? Where am I?"

    show ody stare
    unknown "..."

    show ody whaa
    ""

    unknown "How could you have forgotten your fiancé?"

    unknown "And this is your room, silly!"

    show ody hehe
    pause 1.5

    h "Since when was I engaged???"

    h "Actually… Don't answer that question. Lets, uh, go… ?"

    "Looks like you've been, ugh, reincarnated. Because your family and friends don't matter at all, apparently, and you just died in your sleep."

    "…"

    "Did you even die?"

    jump intro1


label intro1:
    scene blank
    with fade
    nemo "Even as Hailey walked to the new, shining world before her, she knew she could never stay."

    scene balcony people
    with fade

    "The outside is beautiful. It looks like renaissance fair, if an entire city were there. There's a crowd, looking at you."
   
    "While you were walking, the girl you saw when you woke up told you some things about today. You're being officially crowned heir to the throne of some kingdom or another, because your “brother” tragically died in battle. "
    
    "She seems stupidly unsuspicious of your apparent amnesia. "
    jump end



label end:
    return