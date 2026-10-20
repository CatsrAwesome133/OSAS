# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edward") # ed for short
define h = Character("Hailey") # just hailey
define o = Character("Odelyna") # ody for short
define k = Character("The King") # king for short
define s = Character("Sybili") # syb for short

define nemo = Character("__ _", voice_tag="Narrator")
define story = Character("_ ___", who_color="#000000", voice_tag="Storyteller", what_prefix="{i}", what_suffix="{/i}")
define unknown = Character("???")

screen voice_toggle:
    vbox:
        textbutton "Mute the Narrator" action ToggleVoiceMute("Narrator")
        textbutton "Mute the Storyteller" action ToggleVoiceMute("Storyteller")

# The game starts here.

label start:
    # show screen voice_toggle
    scene blank
    with fade

    voice "nemo/nemo_intro1-1.ogg"
    nemo "Once upon a time there was a great kingdom, by the name of Trecia, in the land three planets from the sun. "
    play music singing1_quiet fadein 1.0
    voice "nemo/nemo_intro1-1.1.ogg"
    extend "The kingdom ruled for many a millenium, bringing peace and prosperity upon its people."

    pause 2.0
    scene intro 1
    with fade
    
    voice "nemo/nemo_intro1-2.ogg"
    nemo "But every century…"
    
    scene intro 2
    with fade
    play sound thunder
    voice "nemo/nemo_intro1-3.ogg"
    nemo "A terrible plague would occur."
 
    voice "nemo/nemo_intro1-3.1.ogg"
    nemo "For a decade or more, demons would ravage the land and spread rot among the kingdom."
    stop music fadeout 3.0
    
    scene intro 3
    with dissolve
    voice "nemo/nemo_intro1-4.ogg"
    nemo "And every century, without fail, a mage of Light would rise to banish the rot."
    
    scene blank
    with dissolve
    voice "multiple/nemo-story_welcome.ogg"
    centered "Welcome. You're not meant to be here."

    pause 2.0
    scene room ed
    with fade
    play sound footstep2
    pause 2.0
    show ody lean
    with dissolve

    unknown "Hey, sleepyhead! You wouldn't miss your big day, now, would you?"

    h "Wh- What?"

    "You don't recognise this person, or what she's talking about. \nAt all."

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

    h "Actually… Don't answer that question. \nLets, uh, go… ?"

    "Looks like you've been, ugh, reincarnated. Because your family and friends don't matter at all, apparently, and you just died in your sleep."

    "…"

    "Did you even die?"

    jump intro1


label intro1:
    scene blank
    with fade
    
    voice "nemo/nemo_interlude1.ogg"
    nemo "Even as Hailey walked to the new, shining world before her, she knew she could never stay."

    scene balcony people
    with fade

    "The outside is beautiful. It looks like renaissance fair, if an entire city were there. There's a crowd, looking at you."
   
    "While you were walking, the girl you saw when you woke up told you some things about today. You're being officially crowned heir to the throne of some kingdom or another, because your “brother” tragically died in battle. "
    
    "She seems stupidly unsuspicious of your apparent amnesia. "

    voice "nemo/nemo_placeholder1.ogg"
    nemo "We need some new dialouge from the king, but I'll let the others take over."

    jump intro2


label intro2:
    scene blank
    with fade

    voice "nemo/nemo_intro2-1.ogg"
    nemo "She scoured the books like a wildfire, and yet she found so little. "
    voice "nemo/nemo_intro2-2.ogg"
    extend "Demons were a plague; magics were a blessing. And:"
    
    story "The stars gave us life. They gave us magic. "
    extend "From Life and Light, we rose. And, from Death and Dark, the demons did too."
    
    story "The stars guide us every day, every night. "
    extend "Did you know, child, that the Sun is a star too? "
    extend "Mighty Heila blesses us all with warmth and light, from the bean-stalk in the garden to the story-teller who hearkens."
    
    story "Did you know, that when you look up at night, there is a star that shows you the way North? "
    extend "Great Polaris guides us home, from the sailors at sea to the children playing hide-and-seek."
    
    voice "nemo/nemo_intro2-3.ogg"
    nemo "She looked at the stars, and found so many more than she'd ever seen before. "
    voice "nemo/nemo_intro2-4.ogg"
    extend "She looked at the stars, and-"

    scene demon arena
    with fade
    play sound ow_my_bones
    pause 1.0

    s "Oh, Stars! Stop, you monster!"

    jump end



label end:
    return