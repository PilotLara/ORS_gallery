
######################     OUR      RED     STRING  ######################

## v0.1 ################################################################################################################################################################################################################################################
## v0.1 ################################################################################################################################################################################################################################################
## v0.1 ################################################################################################################################################################################################################################################


############# PROLOGUE ################################################################################################################# PROLOGUE ##############################################################################################################################


label start:
    $ _game_menu_screen = None
    $ save_name = "Ian: Prologue"
    $ quick_menu = False
    $ _game_menu_screen = "tutorialquit"
    show blackbg
    with long


    $temp = None
    call screen choose_game_mode with dissolve
    # easy mode
    label easymode_on:
        $ renpy.block_rollback()
        $temp = 'easymode'
        show screen choose_game_mode
        hide screen choose_game_mode with Dissolve(1.5)
        pause 1
        $ ian_wits = 2
        $ ian_charisma = 2
        $ ian_athletics = 2
        $ ian_lust = 2
        $ ian_will = 2
        $ ian_money = 3

        $ lena_wits = 3
        $ lena_charisma = 3
        $ lena_athletics = 3
        $ lena_lust = 3
        $ lena_will = 3
        $ lena_money = 2
        jump new_prologue

    # cheat mode
    label cheatmode_on:
        $ renpy.block_rollback()
        $temp = 'cheatmode'
        show screen choose_game_mode
        hide screen choose_game_mode with Dissolve(1.5)
        pause 0.3
        "Cheats activated! {image=icon_wits.webp}{image=icon_charisma.webp}{image=icon_athletics.webp}{image=icon_lust.webp}{image=icon_will.webp}{image=icon_money.webp}{w=1.2}{nw}"

        # Cheat mode master var
        $ cheat_mode = True

        # Ian stats increase
        $ ian_wits = 10
        $ ian_charisma = 10
        $ ian_athletics = 10
        $ ian_lust = 10

        $ ian_will = 99
        $ ian_money = 99

        # Lena stats increase
        $ lena_wits = 10
        $ lena_charisma = 10
        $ lena_athletics = 10
        $ lena_lust = 10

        $ lena_will = 99
        $ lena_money = 99

        "Your stats have been maxed, and you are incredibly wealthy..."

        pause (1)
        jump new_prologue

    # normal mode
    label storymode_on:
        $ renpy.block_rollback()
        $temp = 'storymode'
        show screen choose_game_mode
        hide screen choose_game_mode with Dissolve(1.5)
        pause 1
        jump new_prologue


label new_prologue:
    if not persistent.tutorial:
        $ _game_menu_screen = "phone"
        $ quick_menu = True
    $ day = "Saturday"
    $ week = 3
    $ month = "October"
    $ lena_necklace = "choker"

    stop music fadeout 2.0
    scene black with long
    if persistent.tutorial:
        call label_tutorial(['tutorial_1']) from _call_label_tutorial_6

# TESTS ##########################################

    #
    
    
    
##
    play music "music/club_outside.mp3" fadein 4.0 loop
    pause 3
    i "I think I'm calling it a night."
    j "What? Really?"
    i "Yeah... I should've stayed home. I'm really not in the mood tonight."
    j "Come on man, that's exactly why you need this. You have to cheer up, dude..."
    i "I know, I know... Some other night, maybe."
    i "Say goodbye to the others for me."
    scene blazer_outside with Dissolve (2.0)
    $ fian = "n"
    $ ian_look = "cool"
    $ flena = "cry"
    $ lena_look = "sexy1"
    $ lena_choker = True
    i "..."
    show ian at lef with long
    i "Fuck..."
    $ fian = "sad"
    i "It's definitely not my night."
    show ian at truecenter with move
    stop music fadeout 6.0
    "I walked past the people that flocked at the entrance of the club. I just wanted to get home."
    i "Perry and the girls will probably get mad at me for leaving like this... But I can't stand this anymore."
    "I thought alcohol, crowds, and loud music would make me feel better and forget."
    "Instead, they had buried me even deeper in that pit of despair I had been trying to crawl out of."
    "That miserable and loathsome hell so often visited by the broken-hearted."
    $ fian = "serious"
    i "This is pathetic..."
    "I wanted to just punch myself. Whatever it took to get over what happened."
    $ fian = "worried"
    "To get over Gillian..."
    scene street2night with long
    "As I turned the corner, wallowing in my self-pity, a quiet scene caught my eye."
    play music "music/calm.mp3" loop
    scene v1_prologue1 with long
    "A lone girl was sitting on the sidewalk, and she seemed to be in very low spirits."
    "Her shiny dark hair contrasted with her pale, long legs. She had her arms wrapped around them, and..."
    scene v1_prologue0 with long
    "Was she... crying?"
    $ fian = "sad"
    scene street2night
    show ian at rig
    with long
    show ian at rig3 with move
    "I couldn't take my eyes off her as I walked past."
    i "..."
    show ian at rig with move
    "I knew whatever was troubling her wasn't my business, but..."
    "Whatever the reason, I couldn't ignore her."
    $ fian = "worried"
    "Something had me frozen in place. A chance wanting to happen."
    $ fian = "n"
    show ian at truecenter with move
    "I don't know if it was the alcohol or a genuine feeling of empathy for another suffering soul, but I mustered up the courage to retrace my steps, determined to talk to her."
    $ flena = "worried"
    scene v1_prologue0a with long # lena crying
    pause 0.5
    menu:
        "Offer help":
            $ renpy.block_rollback()
            "I stood at a certain distance and tried to get her attention gently."
            i "Hey..."
            scene v1_prologue0b with short # lena looks up
            "Her eyes met mine for a brief moment that seemed suspended in time."
            scene street2night
            show ian at lef
            show lena at rig
            with long
            i "I don't want to disturb you, so if you want me to go away just say so and I'll leave you alone..."
            $ fian = "sad"
            i "But I was wondering if I could offer you some help. Do you need anything?"
            girl  "..."
            girl  "I... Thanks."
            stop music fadeout 3.0
            call xp_up('wits') from _call_xp_up_504

            if persistent.tutorial:
                $ quick_menu = False
                call label_tutorial(['tutorial_2', 'tutorial_3', 'tutorial_4']) from _call_label_tutorial_7

            $ fian = "n"
            i "Can I sit next to you?"
            $ flena = "sad"
            girl  "Sure..."

        "Cheer her up":
            $ renpy.block_rollback()
            i "Hey. Rough night?"
            scene v1_prologue0b with short # lena looks up
            "Her eyes met mine for a brief moment that seemed suspended in time. Then she wiped off her tears."
            scene street2night
            show ian at lef
            show lena at rig
            with long
            girl  "Yeah..."
            i "That makes two of us, then..."
            i "I don't mean to bother you, but I thought maybe you could use someone to talk to."
            i "It usually helps."
            $ flena = "sad"
            girl  "It does."
            stop music fadeout 3.0
            call xp_up('charisma') from _call_xp_up_505
            if persistent.tutorial:
                $ quick_menu = False
                call label_tutorial(['tutorial_2', 'tutorial_3', 'tutorial_4']) from _call_label_tutorial_8

        "She's so hot!":
            $ renpy.block_rollback()
            "Even though she was crying, I couldn't help but be amazed at how hot and beautiful she was..."
            "It was both intimidating and irresistibly alluring."
            stop music fadeout 4.0
            call xp_up('lust') from _call_xp_up_506
            if persistent.tutorial:
                $ quick_menu = False
                call label_tutorial(['tutorial_2', 'tutorial_3', 'tutorial_4']) from _call_label_tutorial_9
            $ fian = "n"
            i "Hey... Are you all alone?"
            scene street2night
            show ian at lef
            show lena at rig
            with long
            girl  "Huh?"
            "Her eyes met mine for a brief moment that seemed suspended in time. Then she wiped off her tears."
            $ fian = "sad"
            i "I know it's none of my business, but you seem to be having a rough time... Do you need any help?"
            girl  "No, it's okay..."
            $ fian = "blush"
            i "If you need anything, I'm here to help. Even if it's just to get something off your chest."
            i "That usually helps, too."
            $ flena = "sad"
            girl  "I guess it does..."

    scene v1_prologue2
    with Dissolve (1.0)
    play music "music/broken_dreams1.mp3"
    pause 1
    i "Did something bad happen?"
    girl  "No..."
    girl  "I mean, yes... But it's nothing really serious."
    i "It seems serious to you."
    girl  "It's just... I fought with my boyfriend. Again."
    if ian_wits > 0:
        i "I figured it was something of that sort... Was it bad?"
    elif ian_charisma > 0:
        i "I see... Was it bad?"
    else:
        i "Oh..."
        "So she had a boyfriend..."
        i "Was it bad?"
    girl  "No. Well, the usual bad."
    girl  "It's... so many small things piling one over the other. It gets unbearable sometimes..."
    if persistent.tutorial:
        call label_tutorial(['tutorial_5']) from _call_label_tutorial_10
    menu:
        "{image=icon_wits.webp}Relationships are complicated" if ian_wits > 0:
            $ renpy.block_rollback()
            i "Relationships are complicated. And sometimes... they're just not meant to be."
            i "I would know..."
            scene v1_prologue3 with long
            girl "..."
            girl "Are you having trouble with that, too?"
            i "No... Not anymore. We broke up some time ago."
            girl "I'm sorry."
            i "Don't be... Nothing could save that relationship."
            i "I guess sometimes that's the only way things can go. Making any other choice would mean disrespecting oneself..."
            girl "I wonder about that sometimes too..."

        "{image=icon_charisma.webp}Some people just don't work together" if ian_charisma > 0:
            $ renpy.block_rollback()
            i "Some people just don't work together, as hard as they might try..."
            i "Sometimes it's just not meant to be. I would know."
            scene v1_prologue3 with long
            with short
            girl "..."
            girl "Are you having trouble with that, too?"
            i "No... Not anymore. We broke up some time ago."
            girl "I'm sorry."
            i "Don't be... Besides, we're not talking about me."
            i "Do you think you can make things work with your boyfriend?"
            girl "I'm trying, that's for sure... But at times I wonder if that's enough."
            girl "Sometimes it's just... too complicated."

        "I'm sorry to hear that":
            $ renpy.block_rollback()
            i "I'm... sorry to hear that."
            label prologuetime:
                scene v1_prologue3 with long
            girl "Jeez. I'm sorry, I'm here telling you my stupid sob story..."
            i "No, don't be. It was me who asked."
            i "I don't mind listening, I just wish I could say something helpful."
            girl "Don't worry. It's... complicated."
            i "Yeah, I know too well..."
            girl "..."
            i "Anyway, as long as the good stuff outweighs the bad, I guess it's okay, isn't it?"
            girl "I hate to say it, but sometimes I doubt that..."

    i "Are you thinking about breaking up with him?"
    scene v1_prologue2 with long
    girl "..."
    girl "I don't know. I..."
    girl "I don't know if I can."
    i "..."
    i "What makes you so afraid?"
    girl "Honestly, I'm not really sure. Sometimes life gets... heavy."
    girl "I know I should be thankful for so many things but at the same time... It feels like a very big burden."
    girl "I don't know, it... It makes me feel so..."
    i "Overwhelmed."
    scene v1_prologue3 with long
    girl "That's right... It's like constantly trying to stay afloat while the tides of life smother you."
    girl "One after another... And they never stop coming, crashing down on you."
    "I smiled at her."
    i "What you just said was beautiful... Sad, but beautiful."
    scene v1_prologue0c with long # lena looks at ian
    pause 1
    girl "Thanks..."
    "For the first time, I saw the hint of a smile appear on her lips."
    "They were so beautiful. And those piercing, vibrant blue eyes..."
    $ fian = "worried"
    $ flena = "worried"
    stop music
    play sound "sfx/honk.mp3"
    scene street2night
    show ian at lef
    show lena at rig
    with vpunch
    "A car pulled over in the corner and honked, getting our attention."
    girl "That's him."
    $ fian = "sad"
    i "Your boyfriend?"
    $ flena = "sad"
    girl "Yeah... I have to go."
    if ian_wits > 0:
        i "Will you be okay?"
        $ flena = "n"
        girl "Yes, don't worry... I feel better now."
    elif ian_charisma > 0:
        i "But do you want to?"
        $ flena = "n"
        girl "Yes... I feel better now."
    else:
        i "Sure... Are you okay?"
        $ flena = "n"
        girl "Yes, I'm better now."
    girl "Thank you for taking the time to listen, um..."
    $ fian = "n"
    i "Ian."
    girl "I'm Lena."
    play sound "sfx/honk.mp3"
    $ flena = "worried"
    $ fian = "sad"
    with vpunch
    "Her boyfriend honked again, impatient."
    show lena at rig3 with move
    l "Gotta go."
    $ flena = "n"
    l "Have a good night, and... Thanks again."
    $ fian = "n"
    i "Don't mention it..."
    play sound "sfx/car.mp3"
    hide lena with short
    "I watched as she got into the car and they drove away."
    show ian at truecenter with move
    stop sound fadeout 2.0
    i "..."
    i "Lena..."
    play music "music/title_music.mp3" noloop
    hide ian with Dissolve (1.5)
    pause 0.5
    $ lena_necklace = 0

    call screen screen_game_title
    scene black
    pause 1
    jump chapter_one

## MODE SCREEN ################################################################################################################################################################################################################################################
## MODE SCREEN ################################################################################################################################################################################################################################################
## MODE SCREEN ################################################################################################################################################################################################################################################
screen choose_game_mode():
    modal True

    if persistent.tutorial:
        $img = 'tutorial_yes_%s.webp'
    else:
        $img = 'tutorial_no_%s.webp'

    if temp is None:
        imagebutton auto "mode_easy_%s.webp" pos (69, 82) action Play ("ch_one", "sfx/xp.mp3"), Jump('easymode_on')
        imagebutton auto "mode_story_%s.webp" pos (665, 82) action Play ("ch_one", "sfx/willdown.mp3"), Jump('storymode_on')
        imagebutton auto "mode_cheat_%s.webp" pos (1261, 82) action Play ("ch_one", "sfx/gggb.mp3"), Jump('cheatmode_on')
    else:
        if temp == 'easymode':
            add "mode_easy_hover.webp" pos (69, 82)
        elif temp == 'cheatmode':
            add "mode_cheat_hover.webp" pos (1261, 82)
        else:
            add "mode_story_hover.webp" pos (665, 82)

    imagebutton auto img pos (1589, 904) action SetField(persistent, "tutorial", not persistent.tutorial), Play ("ch_one", "sfx/paper_hover.mp3")

    key "game_menu" action NullAction()


## END ################################################################################################################################################################################################################################################
## END ################################################################################################################################################################################################################################################
## END ################################################################################################################################################################################################################################################
label end:
    $ _game_menu_screen = None
    $ quick_menu = False
    scene black with long
    call screen tobecontinuedscreen
    # findme loop bug
    $ renpy.set_return_stack([])
    return

label calendar(_day=None, _month=None, _week=None):
    $prev_day = day
    $prev_month = month
    $prev_week = week

    $anim_day_dir = 1
    $anim_month_dir = 1
    $anim_week_dir = 1

    if _month is not None and month != _month:
        $month = _month
        if calendar_months[prev_month] > calendar_months[_month] and calendar_months[prev_month] - calendar_months[_month] < 11:
            $anim_month_dir = -1
    if _week is not None and week != _week:
        $week = _week
        if anim_month_dir == -1 or (prev_week > _week and prev_week != 4 and _week != 1):
            $anim_week_dir = -1
    if _day is not None and day != _day:
        $day = _day
        if anim_month_dir == -1 or anim_week_dir == -1 or (calendar_days[prev_day] > calendar_days[_day] and calendar_days[prev_day] - calendar_days[_day] < 6):
            $anim_day_dir = -1

    $max_len_month = max(len(prev_month), len(month))

    $ quick_menu = False
    pause 0.3
    scene black with dissolve
    call screen screen_calendar with long_dissolve
    $prev_day = day
    $prev_month = month
    $prev_week = week
    show screen screen_calendar
    hide screen screen_calendar with long_dissolve
    pause 0.5
    $ quick_menu = True
    return

screen tobecontinuedscreen():
    modal True
    add "gui/tobecontinued_bg.webp"

    imagebutton:
        auto "gui/tobecontinued_patreon_%s.webp"
        focus_mask True
        action [ Play ("ch_one", "sfx/phone_click.mp3") ], OpenURL ("https://www.patreon.com/Evakiss")

    imagebutton:
        auto "gui/tobecontinued_exit_%s.webp"
        focus_mask True
        action [ Play ("ch_one", "sfx/paper_click.mp3") ], Return () at fade_in_skill


label show_book_screen(num):
    $quick_menu = False

    $renpy.show_screen("book_screen_%d" % num)
    $renpy.with_statement(dissolve)
    $renpy.call_screen("book_screen_%d" % num)
    $renpy.show_screen("book_screen_%d" % num)
    $renpy.with_statement(None)
    $renpy.hide_screen("book_screen_%d" % num)
    $renpy.with_statement(short)

    $renpy.show_screen("screen_book", num)
    $renpy.with_statement(short)
    $renpy.pause(2)
    $renpy.hide_screen("screen_book")
    $renpy.with_statement(short)

    $quick_menu = True
    return

label book_screen_correct:
    $quick_menu = False
    
    $temp = [];
    
    call screen v10correctbook with dissolve
    if _return != 'quit':
        show screen screen_book(temp) with short
        $renpy.pause(2)
        hide screen screen_book with short
    else:
        show screen v10correctbook
        hide screen v10correctbook with short

    $quick_menu = True
    
    call chapter_ten_book_points from _call_chapter_ten_book_points

    return