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
define narrator = Character(what_italic=True)
define u = Character("[name]", color="#ff0086")

## Characters
define who = Character("???", color="#ffffff", what_size=18)
define bab = Character("Bab", color="#ffffff", callback=beep)
define keek = Character("Keek", color="ff351f", callback=low_beep)

## Declare audio used by this game
define audio.move = "sfx/move.mp3"
define audio.hit = "sfx/hit.mp3"

## The game starts here
label start:

    stop music
    
    "..."
    "Where in the world am I?"
    who "Psst..." (callback=low_beep)
    "There's something... or someone... behind me."
    "But I'm having trouble turning around."
    who "I have a question for you." (callback=low_beep)
    
    python: 
        u = renpy.input("What is your name?")
        u = u.strip() or "u"
    
    who "[u], huh? That's a nice name.\nIt'd be a shame if something happened to it though..." (callback=low_beep)
    
    u "What does that even mean?"
    play sound hit
    u "What do you want?!" with hpunch 
    who "I just wanted your name,\nnow that I have it, you can wake up now." (callback=low_beep)
    
    scene bg home
    
    u "What was that about..."
    "I just had the strangest dream."
    u "Oh! Time to get ready for school!"
    
    bab "Heyyyyyyyy"
    "I see a fluffy human waving at me as she quickly skips toward me."
    show bab wave with moveinright
    play sound move
    play music "music/ohayu_bab.ogg" fadeout 1
    show bab neutral
    
    u "Good morning, Bab."
    "This is Bab, my friend since we were children."
    "...She does look a little odd for a human girl."
    bab "hows it goin, [u!l]"

    return
