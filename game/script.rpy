# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character(what_italic=True)
define u = Character("[name]", color="#ff0086")
define who = Character("???", color="#ffffff", what_size=18)
define bab = Character("bab", color="#ffffff")
define keek = Character("keek", color="ff351f")

define audio.move = "sfx/move.mp3"


# The game starts here.

label start:

    h "oh god oh hecc where am i"
    
    who "helo i m bab"
    
    h "what the hecc was that"
    
    show bab wave with moveinbottom
    play sound move
    play music "music/ohayu_bab.mp3" fadeout 1
    
    bab "it be i, bab"
    bab "and this be keek"
    
    show bab neutral at left with move
    play sound move
    show keek neutral at right with moveinright
    play sound move
    
    keek "owo what's this?"
    
    python: 
        u = renpy.input("what ur name be?")
        u = u.strip() or "u"
    
    u "im [u]"
    bab "hi [u]"
    u "hi bab & keek"

    return
