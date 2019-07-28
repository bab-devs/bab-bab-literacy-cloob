## Declare character beeps
init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/low_beep.mp3", channel=3, loop=True)
        elif event == "slow_done" or event == "end":
             renpy.music.stop(channel=3)
        
    def beep(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/beep.mp3", channel=3, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel=3)
            
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/high_beep.mp3", channel=3, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel=3)
            
## Declare characters used by this game
## Yourself
define h = Character(what_italic=True)
define u = Character("[name]", color="#ff0086")

## Characters
define who = Character("???", color="#ffffff", what_size=18)
define bab = Character("bab", color="#ffffff", callback=beep)
define keek = Character("keek", color="ff351f", callback=low_beep)

## Declare audio used by this game
define audio.move = "sfx/move.mp3"
define audio.hit = "sfx/hit.mp3"

## The game starts here
label start:

    stop music
    
    h "Oh god, oh heck. Where am I?"
    who "helo i m bab" (callback=beep)
    play sound hit
    h "What the hell was that?!" with hpunch 
    
    play sound move
    show bab wave with moveinbottom
    play music "music/ohayu_bab.ogg" fadeout 1
    
    bab "it be i, bab"
    
    play sound move
    show bab neutral at left with move
    play sound move
    show keek neutral at right with moveinright
    
    bab @ wave "and this be keek"   
    keek "owo what's this?"
    
    python: 
        u = renpy.input("what ur name be?")
        u = u.strip() or "u"
    
    u "im [u]"
    bab "hi [u]"
    u "hi bab & keek"
    bab "welcum to the bab bab literacy cloob!!" (multiple=2)
    keek "welcum to the bab bab literacy cloob!!" (multiple=2)
    who "wake up"
    
    scene bg home
    stop music
    
    u "what the hecc was that"
    h "I just had the strangest dream."

    return
