############################################################################################################################################################################
## GALLERY SCENES START SETUPS #############################################################################################################################################
############################################################################################################################################################################

## WIP SCENE ###################################################################

label gallery_WIP:
    if _in_replay:
        scene blackbg 
        with long
        play sound "sfx/cat_angry.mp3"
        pause (1)
        show lolamad
        with short
        gal "Uh oh, looks like this scene is still a work in progress."
        gal "This is a reminder that although endorsed by the creator, the gallery is not an official part of the game."
        gal "Check back in the next version, maybe PilotLara has had time to finish and include this scene by then."
    $ renpy.end_replay()

################################################################################
## CHAPTER 1 ###################################################################
################################################################################

label setup_CH01_S01:
    scene blackbg
    with long

    # no music

    $ fian = "n"
    $ ian_look = 1

    scene ianroomnight
    with long
    show ianunder
    with short
return

label setup_CH01_S02:
    scene blackbg
    with long

    # no music
return

label setup_CH01_S03:
    scene blackbg
    with long

    # no music

    $ lena_look = 1
return

label setup_CH01_S04:
    scene blackbg
    with long

    play music "music/normal_day.mp3" loop
    
    $ lena_look = 1
return

################################################################################
## CHAPTER 2 ###################################################################
################################################################################

label setup_CH02_S01:
    scene blackbg
    with long

    # no music
return

label setup_CH02_S02:
    scene blackbg
    with long

    # no music

    $ flena = "n"
    $ lena_look = 1
return

label setup_CH02_S03:
    scene blackbg
    with long

    scene streetnight
    with long

    $ lena_look = 1
    $ flena = "n"
    $ robert_look = 1
    $ robert_hurt = 1
    $ frobert = "smile"

    show lena at rig
    show robert at lef
    with short
    menu:
        gal "Did Lena offer Robert to go get some drinks?"
        "Yes, she did":
            $ v2_robert_invite = True
        "No, Robert asked Lena":
            menu:
                gal "Did Robert bait Lena with secret info to get drinks?"
                "Yes, he did":
                    $ v2_robert_spoiler = True
                "No, he didn't":
                    pass
    scene blackbg
    with long

    # no music
return

label setup_CH02_S04:
    scene blackbg
    with long

    # no music

    $ robert_hurt = 1
    $ frobert = "smile"
    $ lena_look = 1
    $ flena = "n"
return

label setup_CH02_S05:
    scene blackbg
    with long

    # no music

    $ ivy_look = 2
    $ fivy = "n"
return

label setup_CH02_S06:
    scene blackbg
    with long

    play music "music/alisons_theme.mp3" loop

    $ fian = "smile"
    $ ian_look = 1
    $ fcherry = "flirt"
    $ cherry_look = 1
return

label setup_CH02_S07:
    scene blackbg
    with long

    scene cocktailbar
    with long
    show v2_alison1
    with short
    menu:
        gal "Did Alison and Ian kiss at the bar?"
        "Yes, they did":
            $ v2_alison_home = True
            scene cocktailbar
            show v2_alison2b
            with long
            pause(2)
        "No, they didn't":
            $ alison_jeremy = True
    scene blackbg
    with long

    play music "music/alisons_theme.mp3" loop

    $ fian = "confident"
    $ ian_look = 1
    $ alison_look = 2
    $ falison = "flirt"

    scene cocktailbar
    with long

    show jeremy at left5
    show alison at lef5
    show ian at truecenter
    show cherry at rig5
    show perry2 at right5
    with short
return

################################################################################
## CHAPTER 3 ###################################################################
################################################################################

label setup_CH03_S01:
    scene blackbg
    with long

    # no music

    $ lena_look = 4
    $ frobert = "flirt"
    $ robert_look = 1
return

label setup_CH03_S02:
    scene blackbg
    with long

    $ flena = "sad"
    $ lena_look = 1

    # no music

    scene lenahomenight_dark
    with long
    show lena
    with short
return

label setup_CH03_S03:
    scene blackbg
    with long

    # no music

    scene ianroom
    with long
return

label setup_CH03_S04:
    scene blackbg
    with long

    scene cocktailbar
    with long
    show v2_alison1
    with short
    menu:
        gal "Did Alison go home with Ian after the bar?"
        "Yes, she did":
            $ v2_alison_home = True

            scene ianhomenight_dark
            with long

            $ fian = "smile"
            $ falison = "smile"
            $ alison_look = 2
            $ alison_sexy = 1

            show alison at rig
            show ian at lef
            with short

            scene ianroomnight
            show iannude at lef
            show alisonnude at rig
            with long
            menu:
                gal "What happened after they got home?"
                "{image=icon_sad.webp} Ian couldn't get it up":
                    hide iannude
                    show iannude2 at lef
                    with short
                    $ falison = "n"
                    $ fian = "depress"
                    pause (2)

                    $ v2_ian_limp = True
                "They had sex":
                    scene ianroomnight
                    show v2_alison5_animation
                    with long
                    pause (2)

                    $ ian_alison_sex = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music
return

label setup_CH03_S05:
    scene blackbg
    with long

    call gallVar_lena_bdick from _call_gallVar_lena_bdick

    scene recordstore
    with long
    show v2_ian_kiss1
    with short
    menu:
        gal "Did Lena and Ian kiss during their date?"
        "Yes, they did":
            scene recordstore
            show v2_ian_kiss3
            with long
            pause (2)
            $ v2_ian_kiss = True

        "No, they didn't":
            pass
    scene blackbg
    with long

    $ flena = "flirt"
    $ lena_look = 4
    $ frobert = "flirt"
    $ robert_look = 1

    scene street
    with long
    show robert at rig
    show lena at lef
    with short
    menu:
        gal "Did Lena and Robert have sex on Sunday?"
        "Yes, they did":
            scene v3_robert9
            with long
            pause (2)

            $ lena_robert_sex = True
            $ lena_robert_sex_early = True

        "No, Lena chose to wait":
            $ lena_robert_sex_late = True
            $ flena = "n"
            $ frobert = "n"
    scene blackbg
    with long

    $ lena_look = 1

    # no music

    scene lenaroomnight
    with long
return

label setup_CH03_S06:
    scene blackbg
    with long

    # no music

    $ lena_look = 1
return

label setup_CH03_S08:
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop

    $ lena_look = 1
return

################################################################################
## CHAPTER 4 ###################################################################
################################################################################

label setup_CH04_S01:
    scene blackbg
    with long

    # no music

    $ lena_look = 1
return

label setup_CH04_S02:
    scene blackbg
    with long
    menu:
        gal "Do you want to do a quick replay or a custom one?"
        "Quick replay (No Holly)":
            scene recordstore
            show v2_ian_kiss3
            with long
            "Lena and Ian kissed during their date."
            $ v2_ian_kiss = True

            scene lenaroom
            show v3_robert5
            show v3_robert5_slut
            with long
            "Lena and Robert had sex."
            $ lena_robert_sex_late = True
            $ lena_robert_sex = True

            scene v3_louise1
            show v3_louise_door2
            with long
            "Lena focused on Jeremy's big dick."
            $ lena_bdick = 1

            scene v3_solo4
            with long
            "Lena used her dildo whilst masturbating."
            $ v3_use_dildo = True

            scene lenaroom
            show lenabra_phone
            show phone_axel_sad at lef3
            with long
            "Lena agreed to meet Axel."
            $ v4_axel_date = True

        "Custom replay":
            scene recordstore
            with long
            show v2_ian_kiss1
            with short
            menu:
                gal "Did Lena and Ian kiss during their date?"
                "Yes, they did":
                    scene recordstore
                    show v2_ian_kiss3
                    with long
                    pause (2)
                    $ v2_ian_kiss = True
                "No, they didn't":
                    pass
            scene blackbg
            with long

            $ flena = "flirt"
            $ lena_look = 4
            $ frobert = "flirt"
            $ robert_look = 1

            scene street
            with long
            show robert at rig
            show lena at lef
            with short
            menu:
                gal "Did Lena and Robert have sex on Sunday on their first date?"
                "Yes, they did":
                    scene lenaroom
                    show v3_robert5
                    show v3_robert5_slut
                    with long
                    pause (2)

                    $ lena_robert_sex = True
                    $ lena_robert_sex_early = True

                "No, Lena chose to wait":
                    $ lena_robert_sex_late = True
            scene blackbg
            with long

            call gallVar_lena_bdick from _call_gallVar_lena_bdick_1

            scene lenaroomnight
            with long
            scene v3_solo3
            with long
            menu:
                gal "Did Lena use her dildo the last time whilst masturbating?"
                "Yes, she did":
                    scene v3_solo4
                    with long
                    pause (2)

                    $ v3_use_dildo = True
                "No, she didn't":
                    scene v3_solo2
                    with long
                    pause (2)
            scene blackbg
            with long

            $ flena = "worried"
            $ lena_look = 1

            scene lenaroom
            with long
            show lenabra_phone
            show phone_axel_sad at lef3
            with short
            menu:
                gal "Did Lena agree to meet Axel?"
                "Yes, she did":
                    $ flena = "n"
                    $ faxel = "smile"
                    $ axel_look = 1

                    scene cafe
                    with long
                    show lena at rig
                    show axel at lef
                    with short
                    pause (2)

                    $ v4_axel_date = True
                "No, she didn't":
                    pass
    scene blackbg
    with long

    # no music
return

label setup_CH04_S03:
    scene blackbg
    with long

    play music "music/flirty.mp3" loop

    $ flena = "n"
    $ lena_look = 2
    $ frobert = "n"
    $ robert_look = 2

    scene restaurant
    with long
    show lenawork at truecenter
    with short
return

label setup_CH04_S04:
    scene blackbg
    with long

    # no music
return

label setup_CH04_S06:
    scene blackbg
    with long

    $ flena = "smile"
    $ lena_look = 1
    $ fian = "smile"
    $ ian_look = 3
    $ fholly = "n"

    scene park
    with long
    show ian at lef3
    show holly3
    show lena2 at rig3
    with short
    menu:
        gal "Did Ian go on a date with Lena and Holly in the park?"
        "Yes, he did":
            $ v3_ian_date = True
        "No, he didn't":
            pass
    scene blackbg
    with long

    $ flena = "flirt"
    $ lena_look = 4
    $ frobert = "flirt"
    $ robert_look = 1

    scene street
    with long
    show robert at rig
    show lena at lef
    with short
    menu:
        gal "Did Lena and Robert have sex on Sunday?"
        "Yes, they did":
            scene v3_robert9
            with long
            pause (2)

            $ lena_robert_sex = True
        "No, Lena chose to wait":
            pass
    scene blackbg
    with long

    call gallVar_lena_bdick from _call_gallVar_lena_bdick_2

    # no music

    scene lenaroomnight
    with long

    $ lena_look = 2
    $ flena = "flirtshy"
    $ ian_look = 3

    show lenabra at rig
    show lolahappy at lef
    with short
return

################################################################################
## CHAPTER 5 ###################################################################
################################################################################

label setup_CH05_S01:
    scene blackbg
    with long

    $ cindy_look = 1
return

label setup_CH05_S02:
    scene blackbg
    with long

    play music "music/dumb.mp3" loop

    scene blazer
    with long

    $ fian = "smile"
    $ femma = "smile"
    $ falison = "n"
    $ ian_look = "cool"
    $ emma_look = 2
    $ alison_look = 2

    show emma at truecenter
    show ian at lef3
    show alison at rig3
    with short
return

label setup_CH05_S03:
    scene blackbg
    with long

    scene ianroomnight
    with long
    $ ian_look = 2
    $ fian = "n"
    show ian 
    with short
    gal "Which shirt did Ian decide to wear?"
    hide ian
    with short
    call screen v6_ian_clothing
    $ fian = "smile"
    if ian_look == "cool":
        $ v5_ian_cool = True
    else:
        $ ian_look = 3
    show ian 
    with long
    pause (1)

    scene blackbg
    with long

    play music "music/edm.mp3" loop

    $ emma_look = 2

    scene blazer
    if v5_ian_cool:
        scene v5_emma1
    else:
        scene v5_emma1b
    with long
return

label setup_CH05_S04:
    scene blackbg
    with long

    scene ianroomnight
    with long
    $ ian_look = 2
    $ fian = "n"
    show ian 
    with short
    gal "Which shirt did Ian decide to wear?"
    hide ian
    with short
    call screen v6_ian_clothing
    $ fian = "smile"
    if ian_look == "cool":
        $ v5_ian_cool = True
    else:
        $ ian_look = 3
    show ian 
    with long
    pause (1)

    scene blackbg
    with long

    play music "music/dumb.mp3" loop

    scene blazer
    with long

    $ emma_look = 2
    $ alison_look = 2
    $ falison = "flirt"
    $ fian = "n"

    show ian at lef
    show alison at rig
    with short
return

label setup_CH05_S05:
    scene blackbg
    with long

    $ lena_look = 4

    scene lenaroomnight
    with long
    show lenabra
    with short
    gal "Which outfit did Lena wear to the club?"
    show lenabra at left with move
    call screen v5cluboutfit
    if lena_look == "4":
        hide lenabra with long
        $ flena = "smile"
        show lena2 with long
        pause (2)
    elif lena_look == "sexy":
        hide lenabra with long
        $ flena = "flirt"
        $ lena_necklace = "choker"
        $ lena_makeup = 1
        show lena with long
        pause (2)
        $ v5_lena_sexy = True
    scene blackbg
    with long

    $ louise_look = 2
return

label setup_CH05_S06:
    scene blackbg
    with long

    # no music

    $ lena_look = "sexy"
    $ lena_makeup = 1
    $ lena_necklace = "choker"
    $ mike_look = 2
    $ mike_extras = "chain"
return

label setup_CH05_S07:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    show lenanude
    with short
    menu:
        gal "Did Lena decide to check out Stalkfap?"
        "Yes, she did":
            scene lenaroomnight
            show v3_stalkfap2b
            with long
            pause (2)
            $ stalkfap = True

            scene lenaroomnight
            with long
            show lenanude
            with short
            menu:
                gal "Did she decide to take it seriously and post naughtier content?"
                "Yes, she did":
                    scene lenaroomnight
                    show v5_stalkfap1
                    if lena_piercing1:
                        show v5_stalkfap1_p1
                    elif lena_piercing2:
                        show v5_stalkfap1_p2
                    with long
                    pause (2)
                    $ stalkfap_pro = 1
                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ stan_camera = True

    scene lenahome
    with long
    show stan at lef
    show danny at rig
    with short
    menu:
        gal "Who did Lena ask to be her photographer?"
        "Stan":
            hide danny
            with short
            show stan at center
            with move

        "Danny":
            hide stan
            with short
            show danny at center
            with move
            jump v5shootdanny
    scene blackbg
    with long

    $ fstan = "blush"
    $ flena = "n"
    $ lena_look = 1

    scene lenahome
    with long
    show lenabra at rig
    show stan at lef
    with short
    menu:
        gal "Had Lena already posed as a model for Stan?"
        "Yes, she had":
            scene v3_stan3
            with long
            menu:
                gal "How did the shoot go?"
                "{image=icon_lust.webp} Lena extended the shoot and teased Stan":
                    $ v3_stan_shoot = 3
                    scene v3_stan5
                    with long
                    pause (2)
                "{image=icon_friend.webp} Lena extended the shoot":
                    $ v3_stan_shoot = 2
                    scene v3_stan4
                    with long
                    pause (2)
                "Lena ended the shoot early":
                    $ v3_stan_shoot = 1
                    scene lenahome
                    with long
                    show lenaunder2 at rig
                    show stan at lef
                    with short
        "No, she hadn't":
            $ v3_stan_shoot = 0
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop
return

label setup_CH05_S09:
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop

    $ lena_look = 1
return

################################################################################
## CHAPTER 6 ###################################################################
################################################################################

label setup_CH06_S01:
    scene blackbg
    with long

    $ ian_look = "cool"
    $ alison_look = 2

    # no music
return

label setup_CH06_S02:
    scene blackbg
    with long

    scene ianroomnight
    with long
    $ ian_look = 2
    $ fian = "n"
    show ian 
    with short
    gal "Which shirt did Ian decide to wear?"
    hide ian
    with short
    call screen v6_ian_clothing
    $ fian = "smile"
    if ian_look == "cool":
        $ v5_ian_cool = True
    else:
        $ ian_look = 3
    show ian 
    with long
    pause (1)

    $ cherry_look = 1

    # no music

    scene blackbg
    with long
return

label setup_CH06_S03:
    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex

    scene lenaroom
    with long

    $ lena_look = "sexy"
    $ flena = "n"

    show lenabra at truecenter
    with short
    menu:
        gal "Did Lena decide to wear Ivy's top?"
        "Yes, she did":
            hide lenabra
            with short
            $ v5_lena_sexy = True
            $ lena_look = "sexy1"
            $ lena_necklace = "choker"
        "No, she didn't":
            hide lenabra
            with short
            $ lena_look = 4
    $ lena_makeup = 1
    $ flena = "happy"
    show lena
    with long
    pause (2)

    $ ian_look = 2
    $ fian = "smile"
    $ flena = "shy"

    scene blackbg
    with long

    play music "music/date.mp3" loop
return

label setup_CH06_S04:
    scene blackbg
    with long

    $ ian_look = 1
    $ fminerva = "sad"
    $ fian = "evil"

    play music "music/danger.mp3" loop

    scene magazine
    with long
    show ian at lef
    show minerva at rig
    with short
return

label setup_CH06_S05:
    scene blackbg
    with long

    # no music
return

label setup_CH06_S06:
    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym

    # no music

    $ lena_look = 1
    $ holly_look = 1
    $ holly_glasses = True

    if holly_gym:
        jump v6hollyivy2
    else:
        jump v6hollylouise2
return

label setup_CH06_S07:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v3_solo3
    with long
    menu:
        gal "Did Lena use her dildo?"
        "Yes, she did":
            $ v3_use_dildo = True
            scene v3_solo4
            with long
            pause (2)

        "No, she didn't":
            scene v3_solo2
            with long
            pause (2)
    scene blackbg
    with long

    # no music

    $ lena_look = 1
    $ flena = "worried"
    $ louise_look = 1
    $ flouise = "sad"
return

label setup_CH06_S08:
    scene blackbg
    with long
    menu:
        gal "Do you want to do a quick replay or a custom one?"
        "Quick replay (no Robert or Mike)":
            # Interested in BigD
            scene v3_louise1
            show v3_louise_door2
            with long
            "Lena focused on Jeremy's big dick."
            $ v3_spy = True
            $ lena_bdick = 10
            $ lena_bbc = True

            # Done Anal
            scene v4_solo2_animation
            with long
            "Lena experimented with the anal plug."
            $ lena_anal = 1

            # Interested in Axel
            scene v4_solo1
            if lena_piercing1:
                show v4_solo1_p1
            elif lena_piercing2:
                show v4_solo1_p2
            show v4_solo1_pics
            with long
            "Lena looked at the old pictures of her and Axel."
            $ v4_axel_date = True
            $ axel_pictures_watch = True

            # Had sex with Louise
            scene v5_louise7
            show v5_louise7_choker
            with long
            "Lena had sex with Louise."
            $ louise_jeremy = False
            $ v6_louise_sex = True
            $ v6_louise_dildo = True
            $ lena_louise_sex = True

            # Used her dildo
            scene v3_solo4
            with long
            "Lena used her dildo whilst masturbating."
            $ lena_dildo1 = True
            $ v3_use_dildo = True

            # Kissed Holly
            scene v6_holly2_lena1
            with long
            "Lena kissed Holly"
            $ v6_holly_kiss = "lena"

            # Dating Ian
            scene street2night
            show v5_ian_kiss
            with long
            "Lena is dating Ian"
            $ ian_lena_dating = True
            $ v6_ian_selfie = True
            $ ian_lena_sex = True
            $ v6_lena_sex = True
            $ v6_ian_date = True

            # No relationship with Robert (conflicts with Ian and Mike)
            $ v5_robert_sexting = False
            $ v6_robert_date = False

            # No relationship with Mike (conflicts with Robert)
            $ lena_mike_dating = False

        "Custom replay":
            # Kissed Holly
            $ v6_holly_kiss = "lena"

            call gallVar_lena_bdick from _call_gallVar_lena_bdick_3

            call gallVar_lena_anal1 from _call_gallVar_lena_anal1

            scene lenaroomnight
            with long
            $ lena_look = 1
            $ flena = "blush"
            show lenaunder at right
            show v4_polaroid4
            show v4_polaroid3
            show v4_polaroid2
            show v4_polaroid1
            with long
            menu:
                gal "Did Lena look at the old pictures of her and Axel?"
                "Yes, she did":
                    $ v4_axel_date = True
                    $ axel_pictures_watch = True
                    hide v4_polaroid4
                    hide v4_polaroid3
                    hide v4_polaroid2
                    hide v4_polaroid1
                    scene lenaroomnight
                    with long
                    scene v4_solo1
                    if lena_piercing1:
                        show v4_solo1_p1
                    elif lena_piercing2:
                        show v4_solo1_p2
                    show v4_solo1_pics
                    with short
                    pause (2)
                "{image=icon_will.webp} No, she didn't":
                    pass
            scene blackbg
            with long

            scene lenaroomnight
            with long
            scene v5_louise1
            if lena_piercing1:
                show v5_louise1_p1
            elif lena_piercing2:
                show v5_louise1_p2
            show v5_louise1_eyes1
            with long
            menu:
                gal "Did Lena and Louise have sex?"
                "Yes, they did":
                    scene v5_louise7
                    show v5_louise7_choker
                    with long
                    pause (2)
                    $ v6_louise_sex = True
                    $ lena_louise_sex = True
                "No, they didn't":
                    $ louise_jeremy = True
            scene blackbg
            with long

            scene lenaroomnight
            with long
            scene v3_solo3
            with long
            menu:
                gal "Did Lena use her dildo whilst masturbating?"
                "Yes, she did":
                    scene v3_solo4
                    with long
                    pause (2)

                    $ v3_use_dildo = True
                "No, she didn't":
                    scene v3_solo2
                    with long
                    pause (2)
            scene blackbg
            with long

            $ ian_look = 3
            $ robert_look = 1
            $ mike_look = 1
            $ fian = "smile"
            $ frobert = "smile"
            $ fmike = "flirt"
            scene street
            with long
            show ian at left
            show robert at truecenter
            show mike at right
            with short
            menu:
                gal "Which of the guys is Lena meeting tomorrow?"
                "Ian":
                    hide robert
                    hide mike
                    show ian at truecenter with move
                    with long
                    $ ian_lena_dating = True
                    $ v6_ian_selfie = True
                    $ ian_lena_sex = True
                    $ v6_lena_sex = True
                    $ v6_ian_date = True

                "Robert":
                    hide ian
                    hide mike
                    show robert at truecenter with move
                    with long

                    $ v5_robert_sexting = True
                    $ v6_robert_date = True


                "Mike":
                    hide ian
                    hide robert
                    show mike at truecenter with move
                    with long

                    $ lena_mike_dating = True

                "No one":
                    hide ian
                    hide robert
                    hide mike
                    with short

            scene blackbg
            with long

            scene v6_holly1_lena1a
            with long
            menu:
                gal "Did Lena kiss Holly?"
                "Yes, she did":
                    scene v6_holly2_lena1
                    with long
                    pause(2)

                    $ v6_holly_kiss = "lena"
                "No, she didn't":
                    pass

    scene blackbg
    with long

    # no music

    $ lena_look = 1
    $ flena = "smile"
    scene lenaroomnight
    with long
    show lena
    with short
return

label setup_CH06_S09:
    scene blackbg
    with long

    call gallVar_lena_anal1 from _call_gallVar_lena_anal1_1

    scene stanroom
    show stanroom_fap3
    with long
    $ fstan = "surprise"
    $ flena = "surprise"
    $ flouise = "surprise"
    $ stan_look = 1
    $ louise_look = 2
    $ lena_look = 2
    show lenabra at rig3
    show louisebra at lef3
    show stannude2
    with long
    menu:
        gal "How did Lena react when she caught Stan masturbating?"
        "{image=icon_mad.webp} She got mad":
            $ flena = "serious"
            $ fstan = "worried"
            $ flouise = "serious"
            pause (2)
            $ stan_simp = 1
        "She was understanding":
            $ flena = "blush"
            $ fstan = "sad"
            $ flouise = "sad"
            pause (2)
            $ stan_simp = 2
    scene blackbg
    with long

    $ mike_look = 1
    $ mike_extras = 0

    play music "music/normal_day2.mp3" loop
return

label setup_CH06_S10:
    scene blackbg
    with long

    call gallVar_lena_anal1 from _call_gallVar_lena_anal1_2

    scene stanroom
    show stanroom_fap3
    with long
    $ fstan = "surprise"
    $ flena = "surprise"
    $ flouise = "surprise"
    $ stan_look = 1
    $ louise_look = 2
    $ lena_look = 2
    show lenabra at rig3
    show louisebra at lef3
    show stannude2
    with long
    menu:
        gal "How did Lena react when she caught Stan masturbating?"
        "{image=icon_mad.webp} She got mad":
            $ flena = "serious"
            $ fstan = "worried"
            $ flouise = "serious"
            pause (2)
            $ stan_simp = 1
        "She was understanding":
            $ flena = "blush"
            $ fstan = "sad"
            $ flouise = "sad"
            pause (2)
            $ stan_simp = 2
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop
return

label setup_CH06_S11:
    scene blackbg
    with long

    call gallVar_lena_anal1 from _call_gallVar_lena_anal1_3

    scene stanroom
    show stanroom_fap3
    with long
    $ fstan = "surprise"
    $ flena = "surprise"
    $ flouise = "surprise"
    $ stan_look = 1
    $ louise_look = 2
    $ lena_look = 2
    show lenabra at rig3
    show louisebra at lef3
    show stannude2
    with long
    menu:
        gal "How did Lena react when she caught Stan masturbating?"
        "{image=icon_mad.webp} She got mad":
            $ flena = "serious"
            $ fstan = "worried"
            $ flouise = "serious"
            pause (2)
            $ stan_simp = 1
        "She was understanding":
            $ flena = "blush"
            $ fstan = "sad"
            $ flouise = "sad"
            pause (2)
            $ stan_simp = 2
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop
return

label setup_CH06_S12:
    scene blackbg
    with long

    # no music

    $ lena_look = 2
    $ flena = "smile"
    scene lenaroom
    with long
return

label setup_CH06_S13:
    scene blackbg
    with long

    $ lena_look = 1
    $ flena = "worried"

    scene lenaroom
    with long
    show lenabra_phone
    show phone_axel_sad at lef3
    with short
    menu:
        gal "Did Lena agree to meet Axel?"
        "Yes, she did":
            scene cafe
            with long
            $ axel_look = 1
            $ faxel = "sad"
            show lena at rig
            show axel at lef
            with short
            pause (2)
            $ v4_axel_date = True

            scene blackbg
            with long

            scene lenaroomnight
            with long
            $ flena = "blush"
            show lenaunder at right
            show v4_polaroid4
            show v4_polaroid3
            show v4_polaroid2
            show v4_polaroid1
            with long
            menu:
                gal "Did Lena look at all the old pictures of her and Axel?"
                "Yes, she did":
                    $ axel_pictures_watch = True
                    hide v4_polaroid4
                    hide v4_polaroid3
                    hide v4_polaroid2
                    hide v4_polaroid1
                    scene lenaroomnight
                    with long
                    scene v4_solo1
                    if lena_piercing1:
                        show v4_solo1_p1
                    elif lena_piercing2:
                        show v4_solo1_p2
                    show v4_solo1_pics
                    with short
                    pause (2)
                "{image=icon_will.webp} No, she didn't":
                    pass
        "No, she didn't":
            $ flena = "serious"
    scene blackbg
    with long

    scene studio_black
    with long
    show v6_seymour0
    with short
    menu:
        gal "Did Lena agree to work with Seymour?"
        "Yes, she did":
            pause(1)
            pass

        "No, she didn't":
            pause(1)

            scene blackbg
            with long

            jump gallery_CH06_S14

    scene blackbg
    with long

    # no music

    $ lena_makeup = 1
    $ lena_look = 3
return

label setup_CH06_S15:
    scene blackbg
    with long

    $ flena = "smile"
    $ fian = "smile"
    $ lena_look = 4
    $ ian_look = 3

    scene street2night
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Was Lena dating Ian?"
        "Yes, she was":
            $ ian_lena_dating = True
            $ ian_lena_sex = True
            scene street2night
            show v5_ian_kiss
            with long
            pause(2)
        "No, she wasn't":
            pass
    scene blackbg
    with long

    $ lena_look = "sexy"
    $ flena = "n"
    $ lena_necklace = "choker"
    $ lena_makeup = 1
    $ mike_look = 2
    $ mike_extras = "chain"
    $ fmike = "smile"
    scene lenaroomnight
    with long
    show mike at lef
    show lena2 at rig
    with short
    menu:
        gal "Did Lena sleep with Mike?"
        "Yes, she did":
            $ lena_mike_sex = True
            $ v5_mike_cum = True
            $ v5_mike_bj = True
            scene v5_mike5c
            with long
            pause(2)
        "No, she didn't":
            pass
    scene blackbg
    with long
    $ lena_necklace = 0
    $ lena_makeup = 0

    $ flena = "flirt"
    $ lena_look = 4
    $ frobert = "flirt"
    $ robert_look = 1

    scene street
    with long
    show robert at rig
    show lena at lef
    with short
    menu:
        gal "Did Lena sleep with Robert?"
        "Yes, she did":
            scene lenaroom
            show v3_robert5
            show v3_robert5_slut
            with long
            pause (2)

            $ lena_robert_sex = True
            $ v5_robert_sexting = True

            scene blackbg
            with long

            $ lena_look = 1
            $ robert_look = 1
            $ frobert = "smile"
            $ flena = "n"

            scene streetnight
            with long
            show lena at lef
            show robert at rig
            with short
            menu:
                gal "Did Lena break up with Robert?"
                "Yes, she did":
                    $ frobert = "sad"
                    $ lena_robert_over = True
                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    play music "music/flirty.mp3" loop

    $ flena = "n"
    $ lena_look = 2
    scene lenaroomnight
    with long

    if ian_lena_dating == False:
        show lenatopless
        with short
        jump gallery_CH06_S15B

    show lenatopless_phone
    show phone_ian_smile at lef3
    with short
return

################################################################################
## CHAPTER 7 ###################################################################
################################################################################

label setup_CH07_S01:
    scene blackbg
    with long

    $ temp_gallery = True

    menu:
        gal "Do you want to do a quick replay or a custom one?"
        "Quick replay":
            # Ian dating Lena
            scene street2night
            show v5_ian_kiss
            with long
            "Ian was dating Lena."
            $ ian_lena_dating = True
            $ ian_lena_sex = True
            $ v6_ian_selfie = True

            # Lena did spicy photo shoot for SF
            scene lenaroomnight
            show v5_stalkfap1
            if lena_piercing1:
                show v5_stalkfap1_p1
            elif lena_piercing2:
                show v5_stalkfap1_p2
            with long
            "Lena decided to take StalkFap seriously and post naughty content."
            $ stalkfap = True
            $ stalkfap_pro = 1

            # Spicy shoots
            scene v5_model4
            with long
            "Lena did sexier poses during her shoot with Danny."
            $ v4_stan_shoot = False
            $ v4_danny_shoot = True
            $ v5_shoot = 3

            # Ian dating Alison
            scene v6_alison4
            with long
            "Ian was also dating Alison"
            $ v1_encourage_alison = True
            $ ian_alison_dating = True
            $ ian_alison_sex = True
            $ v3_alison_boobjob = True
            $ v5_alison_boobjob = True
            $ ian_alison_like = 2
            $ v6_alison_extra_pic = True
            $ v6_alison_cum = True
            $ v2_alison_home = True

            # Jeremy still together with Louise
            $ louise_jeremy = True

            # Jeremy not dating Alison
            $ alison_voyeur = False
            $ v5_alison_jeremy = False

            # Ian dating Cherry
            scene ianroomnight
            show v6_cherry3
            with long
            "Ian was also dating Cherry."
            $ ian_cherry_dating = True
            $ ian_cherry_pics.append("v6_cherry_selfie.webp")
            $ v4_cherry_sexting = True
            $ v6_cherry_selfie = True

            # Ian not dating Cindy
            $ ian_cindy_model = False
            $ ian_go_cindy = 0
            $ v5_cindy_shoot = False
            $ wade_cindy = 2
            $ v5_cindy_nude = 0

        "Custom replay":
            $ flena = "smile"
            $ fian = "smile"
            $ lena_look = 4
            $ ian_look = 3

            scene street2night
            with long
            show ian at lef
            show lena at rig
            with short
            menu:
                gal "Was Lena dating Ian?"
                "Yes, she was":
                    $ ian_lena_dating = True
                    $ ian_lena_sex = True
                    $ v6_ian_selfie = True
                    scene street2night
                    show v5_ian_kiss
                    with long
                    pause(2)
                "No, she wasn't":
                    pass
            scene blackbg
            with long

            scene rockbar
            with long
            $ fperry = "n"
            $ fian = "smile"
            $ falison = "smile"
            $ fcherry = "smile"
            $ ian_look = "cool"
            $ alison_look = 2
            show ian at left
            show perry at right
            show alison at centerlef
            show cherry at rig
            with short

            $ config.menu_include_disabled = False
            $ greyed_out_disabled = True
            menu:
                gal "Were Ian and Cherry dating?"
                "Yes, they were":
                    scene ianroomnight
                    with long
                    show v6_cherry3
                    with long
                    pause(2)

                    $ ian_cherry_dating = True
                    $ ian_cherry_pics.append("v6_cherry_selfie.webp")
                    $ v4_cherry_sexting = True
                    $ v6_cherry_selfie = True

                "No, Ian was loyal to Lena" if ian_lena_dating:
                    pass

                "No, they weren't" if not ian_lena_dating:
                    pass
            scene blackbg
            with long

            if persistent.include_disabled:
                $ config.menu_include_disabled = True
            $ greyed_out_disabled = False

            $ flena = "n"
            $ lena_look = 1

            scene lenaroomnight
            with long
            show lenanude
            with short
            menu:
                gal "Did Lena decide to check out Stalkfap?"
                "Yes, she did":
                    scene lenaroomnight
                    show v3_stalkfap2b
                    with long
                    pause (2)
                    $ stalkfap = True

                    scene lenaroomnight
                    with long
                    show lenanude
                    with short
                    menu:
                        gal "Did she decide to take it seriously and post naughtier content?"
                        "Yes, she did":
                            scene lenaroomnight
                            show v5_stalkfap1
                            if lena_piercing1:
                                show v5_stalkfap1_p1
                            elif lena_piercing2:
                                show v5_stalkfap1_p2
                            with long
                            pause (2)
                            $ stalkfap_pro = 1

                        "No, she didn't":
                            pass
                "No, she didn't":
                    pass
            scene blackbg
            with long

            $ stan_camera = True

            scene lenahome
            with long
            show stan at lef
            show danny at rig
            with short
            menu:
                gal "Who did Lena ask to be her photographer?"
                "Stan":
                    hide danny
                    with short
                    show stan at center
                    with move
                    $ v4_stan_shoot = True

                "Danny":
                    hide stan
                    with short
                    show danny at center
                    with move
                    $ v4_danny_shoot = True
            scene blackbg
            with long

            if v4_stan_shoot:
                if stalkfap:
                    $ v5_shoot = 1
                    if stalkfap_pro:
                        $ v5_shoot = 3
                else:
                    scene lenaroom
                    with long
                    $ lena_look = "sexy1"
                    $ flena = "n"
                    $ fstan = "shy"
                    show stan at lef
                    show lenatopless2 at rig
                    with short
                    menu:
                        gal "Did Lena go for sexier poses?"
                        "{image=icon_lust.webp} Yes, she did":
                            $ v5_shoot = 1
                            scene v5_model4
                            show v5_model4_thong
                            with long
                            pause (2)
                        "No, she didn't":
                            scene v5_model3
                            with long
                            pause (2)
                    scene blackbg
                    with long
            elif v4_danny_shoot:
                if stalkfap:
                    $ v5_shoot = 1
                    if stalkfap_pro:
                        $ v5_shoot = 3
                else:
                    scene lenaroom
                    with long
                    $ lena_look = 1
                    $ flena = "n"
                    $ fdanny = "n"
                    show lenanude2 at rig
                    show danny2 at lef
                    with short
                    menu:
                        gal "Did Lena go for sexier poses?"
                        "{image=icon_lust.webp} Yes, she did":
                            $ v5_shoot = 1
                            scene v5_model4
                            with long
                            pause (2)
                        "No, she didn't":
                            scene v5_model2b
                            if lena_piercing1:
                                show v5_model2_p1
                            elif lena_piercing2:
                                show v5_model2_p2
                            with long
                            pause (2)
                    scene blackbg
                    with long

            # Ian dating Alison # Forced
            $ v1_encourage_alison = True
            $ ian_alison_dating = True
            $ ian_alison_sex = True
            $ v3_alison_boobjob = True
            $ v5_alison_boobjob = True
            $ ian_alison_like = 2
            $ v6_alison_extra_pic = True
            $ v6_alison_cum = True
            $ v2_alison_home = True

            # Alison not dating Jeremy
            $ louise_jeremy = True
            $ alison_voyeur = False
            $ v5_alison_jeremy = False
            
            # Ian not dating Cindy
            $ ian_cindy_model = False
            $ ian_go_cindy = 0
            $ v5_cindy_shoot = False
            $ wade_cindy = 2
            $ v5_cindy_nude = 0

    scene blackbg
    with long

    # no music

    $ ian_look = 1
return

label setup_CH07_S02:
    scene blackbg
    with long

    $ ian_look = 3
    $ fian = "n"
    $ fholly = "smile"

    play music "music/normal_day.mp3" loop

    scene magazine
    with long
    show ian at lef
    show holly2 at rig
    with short
return

label setup_CH07_S03:
    scene blackbg
    with long

    $ lena_look = 1

    scene cafe
    with long
    $ flena = "n"
    $ fmolly = "n"
    $ fed = "n"
    show lena
    show ed at rig3
    show molly at lef3
    with short
    menu:
        gal "Did Lena offer to help the cafe by hosting life drawing sessions?"
        "Yes, she did":
            $ cafe_nude = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music

    $ ian_look = 3
return

label setup_CH07_S04:
    scene blackbg
    with long

    scene studio_black
    with long
    show v6_seymour0
    with short
    menu:
        gal "Was Lena working with Seymour?"
        "Yes, she was":
            $ lena_job_seymour = True
            $ seymour_disposition = 2
        "No, she wasn't":
            pass
    scene blackbg
    with long

    # no music
return

label setup_CH07_S05:
    scene blackbg
    with long

    $ lena_look = 1

    scene cafe 
    with long
    $ flena = "n"
    $ fmolly = "n"
    $ fed = "n"
    show lena
    show ed at rig3
    show molly at lef3
    with short
    menu:
        gal "Did Lena offer to help the cafe by hosting life drawing sessions?"
        "Yes, she did":
            $ cafe_nude = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    scene lenaroom
    with long
    show v6_robert1
    if lena_piercing1:
        show v6_robert1_p1
    elif lena_piercing2:
        show v6_robert1_p2
    with long
    menu:
        gal "Did Lena meet Robert after his vacation?"
        "Yes, she did":
            scene lenaroom
            with long
            show v6_robert3
            show v6_robert3_bunny
            if lena_piercing1:
                show v6_robert3_p1
            elif lena_piercing2:
                show v6_robert3_p2
            with short
            pause (2)
            $ v6_robert_date = True
            $ lena_robert_sex = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ flena = "smile"
    $ fian = "smile"
    $ lena_look = 4
    $ ian_look = 3

    scene street2night
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Was Lena dating Ian?"
        "Yes, she was":
            $ ian_lena_dating = True
            $ ian_lena_sex = True
            $ v7_drawing_flirt = True
            scene street2night
            show v5_ian_kiss
            with long
            pause(2)
        "No, wasn't":
            pass
    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop
return

label setup_CH07_S06:
    scene blackbg
    with long

    # no music

    $ lena_look = 1
    $ flena = "n"
    $ robert_look = 1
    $ frobert = "n"
return

label setup_CH07_S07:
    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_1

    # no music

    $ lena_look = 1
    $ ian_look = 3
    $ fian = "smile"
    $ flena = "smile"
return

label setup_CH07_S08:
    scene blackbg
    with long

    scene studio_black
    with long
    scene v7_dream1
    with long
    menu:
        gal "Did Lena dream of Axel?"
        "Yes, she did":
            scene v7_dream2
            with long
            pause (2)
            $ lena_axel_desire = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music

    jump v7lenafriday
return

label setup_CH07_S09:
    scene blackbg
    with long

    $ flena = "n"
    $ lena_look = "sexy1"
    $ lena_makeup = 1

    scene lenaroomnight
    with long
    show lenabra2
    with short
    gal "Which outfit did Lena decide to wear to the club?"
    with long
    hide lenabra2
    call screen v7lenawardrobe
    if lena_look == "lust":
        $ flena = "flirtshy"
        $ lena_makeup = 2
        show lena2 with long
    elif lena_look == "charisma":
        $ lena_makeup = 2
        show lena2 with long
    else:
        show lena2 with long
    pause (2)
    menu:
        gal "Did she wear a necklace?"
        "{image=icon_lust.webp} The choker":
            hide lena2 with short
            $ lena_necklace = "choker"
            show lena2 with short

        "{image=icon_charisma.webp} Seymour's necklace" if lena_look != "athletics" and lena_look != 1:
            $ flena = "flirt"
            hide lena2 with short
            $ lena_necklace = "seymour"
            show lena2 with short

        "No, she didn't" if lena_look != "sexy" and lena_look != "lust":
            pass
    scene blackbg
    with long

    $ mike_look = 2
    $ mike_extras = "chain"
    $ fmike = "smile"
    $ flena = "flirtshy"

    play music "music/edm.mp3" loop
return

label setup_CH07_S10:
    scene blackbg
    with long

    $ flena = "n"
    $ lena_look = "sexy1"
    $ lena_makeup = 1

    scene lenaroomnight
    with long
    show lenabra2
    with short
    gal "Which outfit did Lena decide to wear to the club?"
    with long
    hide lenabra2
    call screen v7lenawardrobe
    if lena_look == "lust":
        $ flena = "flirtshy"
        $ lena_makeup = 2
        show lena2 with long
    elif lena_look == "charisma":
        $ lena_makeup = 2
        show lena2 with long
    else:
        show lena2 with long
    pause (2)
    menu:
        gal "Did she wear a necklace?"
        "{image=icon_lust.webp} The choker":
            hide lena2 with short
            $ lena_necklace = "choker"
            show lena2 with short

        "{image=icon_charisma.webp} Seymour's necklace" if lena_look != "athletics" and lena_look != 1:
            $ flena = "flirt"
            hide lena2 with short
            $ lena_necklace = "seymour"
            show lena2 with short

        "No, she didn't" if lena_look != "sexy" and lena_look != "lust":
            pass
    scene blackbg
    with long
return

label setup_CH07_S11:
    scene blackbg
    with long

    $ flena = "n"
    $ lena_look = "sexy1"
    $ lena_makeup = 1

    scene lenaroomnight
    with long
    show lenabra2
    with short
    gal "Which outfit did Lena decide to wear to the club?"
    with long
    hide lenabra2
    call screen v7lenawardrobe
    if lena_look == "lust":
        $ flena = "flirtshy"
        $ lena_makeup = 2
        show lena2 with long
    elif lena_look == "charisma":
        $ lena_makeup = 2
        show lena2 with long
    else:
        show lena2 with long
    pause (2)
    menu:
        gal "Did she wear a necklace?"
        "{image=icon_lust.webp} The choker":
            hide lena2 with short
            $ lena_necklace = "choker"
            show lena2 with short

        "{image=icon_charisma.webp} Seymour's necklace" if lena_look != "athletics" and lena_look != 1:
            $ flena = "flirt"
            hide lena2 with short
            $ lena_necklace = "seymour"
            show lena2 with short

        "No, she didn't" if lena_look != "sexy" and lena_look != "lust":
            pass
    scene blackbg
    with long

    $ ivy_look = "sexy"
    $ flena = "worried"
    $ fivy = "flirt"

    scene blazer
    with long
    show lena at right
    show ivy2 at lef
    with short
    menu:
        gal "Did Lena accept Ivy's drugs?"
        "Yes, she did":
            $ flena = "smile"
            pause (1)
            $ lena_drugs = True
        "No, she declined":
            pass
    scene blackbg
    with long

    $ louise_look = 2

    # no music
return

label setup_CH07_S12:
    scene blackbg
    with long

    $ flena = "n"
    $ lena_look = 1

    play music "music/normal_day2.mp3" loop

    scene lenahome
    with long
    show lena
    with short
return

label setup_CH07_S13:
    scene blackbg
    with long

    play music "music/normal_day.mp3" loop

    $ ian_look = 2
    $ fian = "n"
    $ emma_look = "cool"
return

label setup_CH07_S14:
    scene blackbg
    with long

    $ fian = "n"
    $ ian_look = 2
    $ alison_look = "cool"
    # $ alison_extras = 1

    play music "music/normal_day.mp3" loop

    scene ianroomnight
    with long
return

label setup_CH07_S15:
    scene blackbg
    with long

    $ ian_look = "cool"
    $ cindy_look = "party"

    # no music
return

label setup_CH07_S16:
    scene blackbg
    with long

    $ ian_look = 3
    $ holly_look = 2

    play music "music/normal_day2.mp3" loop

    scene villagenight
    with long
return

label setup_CH07_S17:
    scene blackbg
    with long

    $ lena_look = 1

    scene sexshop
    with long
    $ flena = "shy"
    show lena at right
    with short
    menu:
        gal "Did Lena have a dildo?"
        "Yes, the badboy":
            $ flena = "slut"
            show toy_badboy with long
            $ toy_badboy = True

        "Yes, a normal dildo": #ToDO recheck dildos
            $ flena = "slutshy"
            show toy_dildo1 with long
            $ toy_dildo = True

        "No":
            $ flena = "n"
            pass
    scene blackbg
    with long

    scene v3_solo1c
    if lena_piercing1:
        show v3_solo1c_p1
    elif lena_piercing2:
        show v3_solo1c_p2
    with long
    menu:
        gal "Did Lena masturbate to the pictures of Louise and Jeremy?"
        "Yes, she did":
            scene v6_solo3_animation
            if lena_piercing1:
                show v6_solo3_p1
            elif lena_piercing2:
                show v6_solo3_p2
            show v6_solo3_jeremy4
            with long
            pause (2)
            $ v6_spy = True
        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_look = "lust"
    $ ivy_look = "sexy"
    $ jeremy_look = 1
    $ louise_look = 2
    $ fivy = "flirt"
    $ flena = "slutshy"
    $ fjeremy = "surprise"
    $ flouise = "blush"
    scene ivyroomnight
    with long
    show lenabra2 at right
    show ivynude2 at rig
    show louisenude at lef
    show jeremynude at left
    with short
    menu:
        gal "Did Lena agree to make Jeremy cum during Ivy's game?"
        "Yes, she did":
            scene v7_jeremy4_animation1
            with long
            pause (2)
            $ v7_bbc = "lena"
            $ lena_fty_bbc = True

        "No, she didn't":
            scene v7_jeremy_ivy
            with long
            pause (2)
            $ v7_bbc = "ivy"
            $ lena_fty_bbc = False
    scene blackbg
    with long

    if lena_fty_bbc == False and v6_spy == False:
        gal "Uh oh. You need to select at least one of the two options concerning Jeremy, please try again."
        jump setup_CH07_S17

    $ lena_look = 1

    # no music

    play music "music/normal_day2.mp3" loop
    $ flena = "n"
    scene lenahome
    show lenabra
    with long
    "Today I had to take care of the rent and other stuff, but before that, I had some time to put it to use."
    l "What should I do with my morning?"
return

label setup_CH07_S18:
    scene blackbg
    with long

    scene studio_black
    with long
    scene v7_dream1
    with long
    menu:
        gal "Did Lena dream of Axel?"
        "Yes, she did":
            scene v7_dream2
            with long
            pause (2)
            $ lena_axel_desire = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music

    jump v7lenafriday
return

label setup_CH07_S19:
    scene blackbg
    with long

    call gallVar_toy_badboy

    # no music

    jump v7lenafriday
return

label setup_CH07_S20:
    scene blackbg
    with long

    $ ian_look = 1
    $ fian = "smile"

    play music "music/sensual.mp3"
return

label setup_CH07_S21:
    scene blackbg
    with long

    play music "music/sensual.mp3" loop
return

################################################################################
## CHAPTER 8 ###################################################################
################################################################################

label setup_CH08_S01:
    scene blackbg
    with long

    # no music
return

label setup_CH08_S02:
    scene blackbg
    with long

    # no music

    $ lena_look = 2
    $ flena = "slutshy"
    $ frobert = "n"
    $ robert_look = 2
    $ robert_hurt = 0

    scene restaurant
    with long
return

label setup_CH08_S03:
    scene blackbg
    with long

    scene v7_louise1
    with long
    menu:
        gal "Did Lena act dominant with Louise?"
        "Yes, she did":
            show v7_louise2
            with long
            pause (2)

            $ louise_dominant = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = 1

    scene sexshop
    with long
    $ flena = "shy"
    show lena at right
    with short
    $ config.menu_include_disabled = False
    $ greyed_out_disabled = True
    menu v8GalToys:
        gal "Which toys has Lena bought?"
        "{image=icon_pay.webp} The collar" if louise_dominant == True and toy_collar == False:
            $ flena = "slutshy"
            $ toy_collar = True
            show toy_collar with long
            pause (1)
            hide toy_collar
            if toy_badboy == False:
                jump v8GalToys

        "{image=icon_pay.webp} The badboy dildo" if toy_badboy == False:
            $ flena = "slut"
            $ toy_badboy = True
            show toy_badboy with long
            pause (1)
            hide toy_badboy
            if toy_collar == False:
                jump v8GalToys

        "That's all" if toy_badboy or toy_collar:
            pass

        "She hasn't bought any toys" if toy_badboy == False and toy_collar == False:
            pass

    if persistent.include_disabled:
        $ config.menu_include_disabled = True
    $ greyed_out_disabled = False

    scene blackbg
    with long

    # no music

    $ lena_look = 4
return

label setup_CH08_S04:
    scene blackbg
    with long

    $ lena_money = 3

    $ flena = "slutshy"
    $ lena_look = "lust"
    $ lena_makeup = 2
    $ lena_necklace = "choker"
    
    $ fivy = "flirt"
    $ ivy_look = "sexy"

    $ fjeremy = "surprise"
    $ jeremy_look = 1

    $ flouise = "blush"
    $ louise_look = 2

    scene ivyroomnight
    with long
    show lenabra2 at right
    show ivynude2 at rig
    show louisenude at lef
    show jeremynude at left
    with short
    menu:
        gal "Did Lena agree to make Jeremy cum during Ivy's game?"
        "Yes, she did":
            scene v7_jeremy4_animation1
            with long
            pause (2)
            $ v7_bbc = "lena"
            $ lena_fty_bbc = True
            $ v7_bbc_cum = True

        "No, she didn't":
            scene v7_jeremy_ivy
            with long
            pause (2)
            $ v7_bbc = "ivy"
    scene blackbg
    with long
    $ lena_makeup = 0
    $ lena_necklace = 0

    $ flena = "slutshy"
    $ lena_look = 2
    scene lenaroomnight
    with long
    show lenabra2 at truecenter
    with short
    menu:
        gal "Did Lena interact with her fans on Stalkfap?"
        "Yes, she did":
            $ v8_stalkfap_dm1 = 1
            $ v8_stalkfap_dm2 = 1
            $ v7_dance_provoke = 3

        "No, she didn't":
            $ v8_stalkfap_dm1 = 0
            $ v8_stalkfap_dm2 = 0
            $ v7_dance_provoke = 0
    scene blackbg
    with long

    $ ian_look = 3
    $ robert_look = 1
    $ mike_look = 1
    $ fian = "smile"
    $ frobert = "smile"
    $ fmike = "flirt"
    scene street
    with long
    show ian at left
    show robert at truecenter
    show mike at right
    with short
    menu:
        gal "Which of the guys was Lena dating?"
        "Ian":
            hide robert
            hide mike
            $ fian = "happy"
            show ian at truecenter with move
            $ ian_lena_dating = True
            $ ian_lena_love = True
            $ v7_holly_kiss = False
            $ v6_ian_selfie = True
            $ ian_lena_sex = True
            $ lena_ian_love = True

        "Robert":
            hide ian
            hide mike
            $ frobert = "flirt"
            show robert at truecenter with move
            $ lena_robert_dating = True
            $ v8_robert_public = True

        "Mike":
            hide ian
            hide robert
            show mike at truecenter with move
            $ lena_mike_dating = True
            $ v7_mike_bj = True

        "No one":
            pass
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v4_solo1
    if lena_piercing1:
        show v4_solo1_p1
    elif lena_piercing2:
        show v4_solo1_p2
    with long
    menu:
        gal "Did Lena experiment with the anal plug?"
        "Yes, she did":
            scene v4_solo2_animation
            with long
            pause (2)
            $ lena_anal = 1

            if ian_lena_dating or lena_robert_dating or lena_mike_dating:
                scene blackbg
                with long
                if ian_lena_dating:
                    scene v6_ian1
                    if lena_piercing1:
                        show v6_robert1_p1
                    elif lena_piercing2:
                        show v6_robert1_p2
                    with long
                elif lena_robert_dating:
                    scene v6_robert1
                    if lena_piercing1:
                        show v6_robert1_p1
                    elif lena_piercing2:
                        show v6_robert1_p2
                    with long
                elif lena_mike_dating:
                    scene v6_mike1
                    if lena_piercing1:
                        show v6_robert1_p1
                    elif lena_piercing2:
                        show v6_robert1_p2
                    with long
                menu:
                    gal "Did Lena lose her anal virginity?"
                    "Yes, she did":
                        $ lena_anal = 2

                        if ian_lena_dating:
                            $ lena_anal_first = "ian"
                            scene v6_ian4b
                            with long
                        elif lena_robert_dating:
                            $ lena_anal_first = "robert"
                            scene v6_robert5
                            show v6_robert5_bunny
                            if lena_piercing1:
                                show v6_robert5_p1
                            elif lena_piercing2:
                                show v6_robert5_p2
                            with long
                        elif lena_mike_dating:
                            $ lena_anal_first = "mike"
                            scene v6_mike6_animation
                            with long
                        pause (2)

                    "No, she didn't":
                        $ lena_anal_first = "n"

                        if ian_lena_dating:
                            scene v6_ian4
                            with long
                        elif lena_robert_dating:
                            scene v6_robert6
                            show v6_robert6_bunny
                            if lena_piercing1:
                                show v6_robert6_p1
                            elif lena_piercing2:
                                show v6_robert6_p2
                            with long
                        elif lena_mike_dating:
                            scene v6_mike6c
                            with long
                        pause (2)

        "No, she didn't":
            $ lena_anal = 0
            $ lena_anal_first = "n"
    scene blackbg
    with long

    # no music
return

################################################################################
## CHAPTER 8b ##################################################################
################################################################################

label setup_CH08_S05:
    scene blackbg
    with long

    play music "music/normal_day.mp3" loop

    $ ian_look = 3
return

label setup_CH08_S06:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v4_solo1
    if lena_piercing1:
        show v4_solo1_p1
    elif lena_piercing2:
        show v4_solo1_p2
    with long
    menu:
        gal "Did Lena experiment with the anal plug?"
        "Yes, she did":
            scene v4_solo2_animation
            with long
            pause (2)
            $ lena_anal = 1

            scene blackbg
            with long

            scene v6_ian1
            if lena_piercing1:
                show v6_robert1_p1
            elif lena_piercing2:
                show v6_robert1_p2
            with long
            menu:
                gal "Did Lena have anal sex with Ian?"
                "Yes, she did":
                    scene v6_ian4b
                    with long
                    pause(2)
                    $ lena_anal = 2
                    $ lena_anal_first == "ian"
                "No, but she did with someone else":
                    $ lena_anal = 2
                "Not yet":
                    $ lena_anal_first = "n"
        "No, she didn't":
            $ lena_anal = 0
    scene blackbg
    with long

    scene lenaroom
    with long
    $ flena = "n"
    $ lena_look = "sexy1"
    show lenabra2 at left
    with short
    gal "Which outfit did Lena wear to the concert?"
    with long
    call screen v8lenawardrobe
    if lena_look == 4:
        hide lenabra2
        hide lena
        show lena at left
        with long
    elif lena_look == 3:
        hide lenabra2
        show lena at left
        with long
    elif lena_look == "wits":
        hide lenabra2
        hide lena
        show lena at left
        with long
    elif lena_look == "sexy1":
        hide lenabra2
        hide lena
        show lena at left
        with long
    show lena at truecenter with move
    menu:
        "{image=icon_lust.webp} Wear the choker":
            hide lena with short
            $ lena_necklace = "choker"
            $ flena = "smile"
            $ v8_choker = True
            $ v8_sy = False
            show lena with short

        "{image=icon_charisma.webp} Wear the onyx necklace":
            hide lena with short
            $ lena_necklace = "seymour"
            $ flena = "happy"
            $ v8_sy = True
            $ v8_choker = False
            show lena with short

        "No necklace":
            pass
    $ lena_makeup = 1
    pause (1)

    scene blackbg
    with long

    # no music

    $ fian = "smile"
    $ flena = "shy"
    $ ian_look = 3
return

label setup_CH08_S08:
    scene blackbg
    with long

    $ fian = "worried"
    $ ian_look = 3

    # no music

    scene ianhomenight_dark
    with long
return

################################################################################
## CHAPTER 8c ##################################################################
################################################################################

label setup_CH08_S09:
    scene blackbg
    with long

    $ louise_look = 1

    $ flena = "smile"
    $ lena_look = 1

    # no music

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
return

label setup_CH08_S10:
    scene blackbg
    with long

    $ flena = "smile"
    $ fian = "smile"
    $ lena_look = 4
    $ ian_look = 3

    scene street2night
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Was Lena dating Ian?"
        "{image=icon_love.webp} Yes, she was":
            $ ian_lena_dating = True
            $ ian_lena_love = True
            scene street2night
            show v5_ian_kiss
            with long
            pause(2)
        "No, she wasn't":
            pass
    scene blackbg
    with long

    scene v7_holly1
    show v7_holly1_eyes
    with long
    menu:
        gal "Did Holly kiss Ian after the book fair?"
        "Yes, she did":
            scene v7_holly2
            show v7_holly2_eyes
            with long
            pause (2)
            $ v7_holly_kiss = True

            if ian_lena_dating:
                $ ian_lena_over = True
            else:
                $ ian_lena_over = False

            menu:
                gal "Did Ian decide to reciprocate Holly's kiss?"
                "Yes, he did":
                    scene v7_holly2
                    with long
                    pause (2)

                    $ ian_holly_sex = True
                    $ v7_holly_lick = True
                    $ v7_holly_bj = True

                    scene blackbg
                    with long

                    scene v7_holly10
                    with long
                    menu:
                        gal "Did Ian decide to date Holly?"
                        "{image=icon_love.webp} Yes, he did":
                            scene v7_holly10
                            with long
                            pause (2)

                            $ ian_holly_dating = True
                        "No, he didn't":
                            pass

                "No, he didn't":
                    pass
        "No, he didn't":
            pass
    scene blackbg
    with long

    # no music

    $ lena_look = 4
    $ lena_makeup = 1
    $ holly_look = 1
    $ ivy_look = 1
return

label setup_CH08_S12:
    scene blackbg
    with long

    # no music

    $ lena_look = 4
    $ holly_look = 1
return

################################################################################
## CHAPTER 8d ##################################################################
################################################################################

label setup_CH08_S07:
    scene blackbg
    with long

    $ fian = "disgusted"
    $ ian_look = 2
    $ emma_look = 1

    # no music

    scene ianroomnight_dark 
    with vpunch
return

label setup_CH08_S11:
    scene blackbg
    with long

    $ lena_look = 2
    $ flena = "serious"
    $ mike_extras = 0
    $ mike_look = 1

    # no music

    scene lenaroomnight
    with long
    show lenabra
    with short
return

################################################################################
## CHAPTER 9 ###################################################################
################################################################################

label setup_CH09_S01:
    scene blackbg
    with long

    $ ian_look = 1
    $ holly_look = "1skirt"
    $ holly_glasses = True

    # no music
return

label setup_CH09_S02:
    scene blackbg
    with long

    scene ianroom
    with long
    $ ian_look = 3
    show ianunder with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    call screen v9ianclotheschoice2
    hide ianunder with short
    pause 0.5
    show ian with long

    $ cherry_look = 1

    # no music

    scene blackbg
    with long
return

label setup_CH09_S04:
    scene blackbg
    with long

    #ToDO
    menu:
        gal "Does Lena have an exhibitionistic fantasy?"
        "Yes, she confessed it to Ivy":
            $ lena_fty_show = True
        "Yes, she asked Stan to help shoot a video for SF":
            $ lena_fty_show = True
        "No":
            pass

    scene blackbg
    with long

    scene lenaroom
    with long
    $ flena = "n"
    show lenaunder at left
    with short
    menu:
        gal "How high was Lena's lust?"
        "{image=icon_lust.webp} Higher than 6":
            hide lenaunder
            with short
            $ lena_look = "sexy"
            show lena at left
            with short
            $ flena = "slut"
            show lena at truecenter
            with move
            pause(1)

        "6 or lower":
            hide lenaunder
            with short
            $ lena_look = 4
            show lena at left
            with short
            $ flena = "smile"
            show lena at truecenter
            with move
            pause(1)

    scene blackbg
    with long

    $ flena = "shy"
    $ fian = "shy"
    $ ian_look = 2

    # no music

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    l "And I can't think of anyone who I'd like to try that better than you. So..."
    i "So is that a yes?"
    l "Yes. I want to be with you too."
    $ fian = "happy"
    i "That's...! Awesome."
return

label setup_CH09_S05:
    scene blackbg
    with long

    $ fian = "smile"
    $ ian_look = 2

    # no music
return

label setup_CH09_S13:
    scene blackbg
    with long

    $ fian = "n"
    $ fjeremy = "flirt"
    $ ian_look = 3
    $ jeremy_look = 1

    scene streetnight
    with long
    show ian at lef
    show jeremy at rig
    with short
    menu:
        gal "Did Emma have sex with Jeremy?"
        "Yes, she did":
            show ian at left
            show jeremy at right
            with move
            show v8_emma_jeremy 
            with short
            $ fjeremy = "happy"
            pause(1)

            $ emma_jeremy = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ wade_look = 1
    $ fwade = "happy"
    $ cindy_look = 1
    $ fcindy = "n"
    $ ian_look = 2
    $ fian = "n"
    $ perry_look = 1
    $ fperry = "meh"

    scene ianhomenight
    with long
    show ian at left
    show wade2 at centerlef
    show cindy at rig
    show perry2 at right
    with short
return

label setup_CH09_S14:
    scene blackbg
    with long

    $ ian_look = 2
    $ fian = "n"

    # no music

    scene ianroomnight
    with long
    show ian
    with short
return

################################################################################
## CHAPTER 9_alison ############################################################
################################################################################

label setup_CH09_S03:
    scene blackbg
    with long

    scene hotelnight
    with long
    $ ian_look = 3
    show ianunder with short
    gal "Which outfit did Ian wear to the restaurant?"
    show ianunder at left with move
    call screen v9ianclotheschoice
    hide ianunder with short
    pause 0.5
    show ian at left with long

    scene blackbg
    with long

    # no music

    $ alison_look = "dress"
    $ falison = "smile"
    $ alison_makeup = 1
    $ fian = "smile"

    scene villagenight
    with long
    show ian at lef
    show alison at rig
    with short
return

################################################################################
## CHAPTER 9_axel ##############################################################
################################################################################

label setup_CH09_S10:
    scene blackbg
    with long

    # no music

    $ faxel = "smile"
    $ flena = "sad"
    $ axel_look = 1
    $ lena_makeup = 1
    $ lena_look = "sexy"

    scene axelhome
    with long
    show axel at lef
    show lena2 at rig
    with short
return

label setup_CH09_S11:
    scene blackbg
    with long

    # no music

    $ axel_look = 1
    $ faxel = "happy"
    $ flena = "n"
    $ lena_makeup = 1
    $ lena_look = "underwear2"

    scene axelhomenight
    with long
    show axel at lef
    show lenabra2 at rig3
    with short
return

################################################################################
## CHAPTER 9_cindy #############################################################
################################################################################

label setup_CH09_S06:
    scene blackbg
    with long

    scene ianroom
    with long
    $ ian_look = 3
    show ianunder
    with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    call screen v9ianclotheschoice2
    hide ianunder with short
    pause 0.5
    show ian at left
    with long

    scene blackbg
    with long

    # no music

    $ cindy_look = 2
    $ axel_look = 1
return

label setup_CH09_S07:
    scene blackbg
    with long

    scene street2night with long
    scene v7_cindy4 with short
    menu:
        gal "Did Ian stop after kissing Cindy?"
        "Yes, he did":
            pass

        "No, they went further":
            $ ian_cindy_sex = True
            $ v7_cindy_lust = True

            scene v7_cindy11_animation with fps
            pause(2)

    scene blackbg
    with long

    scene ianroom
    with long
    $ ian_look = 3
    show ianunder with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    call screen v9ianclotheschoice2
    hide ianunder with short
    pause 0.5
    show ian at left with long

    scene blackbg
    with long

    play music "music/calm.mp3" loop

    $ cindy_look = 2

    scene street_afternoon with long
    show ian at lef
    show cindy at rig
    with short
return

################################################################################
## CHAPTER 9b ##################################################################
################################################################################

label setup_CH09_S08:
    scene blackbg
    with long

    $ frobert = "flirt"
    $ flena = "n"
    $ lena_look = 4
    $ robert_look = 1

    play music "music/normal_day2.mp3" loop

    scene lenahome
    with long
    show lena at rig3
    show robert at truecenter
    with short
    r "So, where were we...?"
return

label setup_CH09_S09:
    scene blackbg
    with long

    scene sexshop
    with long
    show sexshop_bunny
    with short
    menu:
        gal "Did Lena acquire the bunny costume?"
        "{image=icon_pay.webp} Yes, she bought it":
            $ lena_wardrobe_bunny = True
            $ v6_robert_date = False
        "Yes, she got it from Robert":
            $ lena_wardrobe_bunny = True
            $ v6_robert_date = True
            scene lenaroomnight
            with long
            show v6_robert6
            show v6_robert6_bunny
            with short
            pause(2)

        "No, she didn't":
            $ lena_wardrobe_bunny = False
            $ v6_robert_date = False
    scene blackbg
    with long

    $ fmike = "flirt"
    $ mike_extras = 0
    $ mike_look = 1
    $ flena = "n"
    $ lena_look = 4

    play music "music/normal_day2.mp3" loop

    scene lenaroom
    with long
    show mike at lef
    show lena at rig
    with short
return

label setup_CH09_S12:
    scene blackbg
    with long

    $ seymour_look = 1
    $ lena_look = "wits"
    $ lena_makeup = 1
    $ lena_necklace = "seymour"

    $ fseymour = "smile"
    $ flena = "smile"

    scene seymourofficenight
    with long

    # no music

    show seymour2 at lef
    show lena2 at rig
    with short
return

label setup_CH09_S15:
    scene blackbg
    with long

    $ lena_look = 2
    $ ivy_look = 2
    $ holly_look = 4
    $ holly_glasses = False

    $ fivy = "n"
    $ flena = "n"
    $ fholly = "smile"

    play music "music/jeremys_theme.mp3" loop

    scene polegym with long
    show lena at rig
    with short
return

################################################################################
## CHAPTER 10 ##################################################################
################################################################################

label setup_CH10_S01:
    scene blackbg
    with long

    $ fian = "n"
    $ ian_look = 2

    # no music
return

label setup_CH10_S02:
    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_2

    $ flena = "flirt"
    $ lena_look = 4
    $ frobert = "flirt"
    $ robert_look = 1

    scene street
    with long
    show robert at rig
    show lena at lef
    with short
    menu:
        gal "Did Lena sleep with Robert?"
        "Yes, she did":
            scene lenaroom
            show v3_robert5
            show v3_robert5_slut
            with long
            pause (2)

            $ lena_robert_sex = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    if ian_lena_sex:
        scene v8_lena6a
        if v8_sy:
            show v8_lena6_sy
        if v8_choker:
            show v8_lena6_choker
        with long
        menu:
            gal "Did Ian and Lena have anal sex?"
            "Yes, they did":
                scene v8_lena5
                if v8_sy:
                    show v8_lena5_sy
                if v8_choker:
                    show v8_lena5_choker
                with long
                pause (2)

                $ v8_lena_anal = True

            "No, they didn't":
                pass

        scene blackbg
        with long
    
    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

        "They were just friends" if ian_lena_sex == False:
            gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
            jump setup_CH10_S03

    scene blackbg
    with long

    scene v9_axel1
    with long
    menu:
        gal "Did Lena have sex with Axel after the photo shoot?"
        "Yes, she did":
            scene v9_axel5
            with long
            pause (2)

            $ v9_axel_sex = True
            if ian_lena_couple:
                $ lena_cheating = True
            $ lena_axel_desire - True

        "No, she didn't":
            pass

    scene blackbg
    with long

    call gallVar_ian_lena_love from _call_gallVar_ian_lena_love

    call gallVar_ian_lena_dom from _call_gallVar_ian_lena_dom

    $ ian_look = 3
    $ fian = "n"

    scene ianroom
    with long
    show ianunder
    with short
    gal "Which outfit did Ian wear to the park?"
    show ianunder at left with move
    hide ianunder with short
    call screen v10ianwardrobe1
    show ian with short
    if ian_look == "wits1":
        $ v10_ianlook = "wits"
    elif ian_look == "charisma1":
        $ v10_ianlook = "charisma"
    elif ian_look == "athletics1":
        $ v10_ianlook = "athletics"
    elif ian_look == "lust1":
        $ v10_ianlook = "lust"
    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "n"
    show lenanude at rig
    with short
    menu:
        gal "Did Lena buy the {image=icon_wits.webp} outfit?"
        "{image=icon_pay.webp} Yes, she did":
            if ian_lena_couple:
                $ lena_look = "wits"
                hide lenanude
                $ lena_makeup = 1
                show lena at rig with short
                show lena with move
            else:
                $ lena_look = "sexy1"
                hide lenanude
                show lena at rig with short
                show lena with move

        "No, she didn't":
            if ian_lena_couple:
                $ lena_look = 4
                hide lenanude
                show lena at rig with short
                show lena with move
            else:
                $ lena_look = "sexy1"
                hide lenanude
                show lena at rig with short
                show lena with move

    scene blackbg
    with long

    $ flena = "smile"
    $ fholly = "smile"
    $ fian = "smile"

    play music "music/date.mp3" loop

    scene park
    with long
return

label setup_CH10_S03:
    scene blackbg
    with long

    $ cindy_look = 2
    $ fcindy = "blush"
    $ ian_look = "charisma1"
    $ fian = "n"

    scene street_afternoon
    with long
    show ian at lef
    show cindy at rig
    with short
    menu:
        gal "Did Ian confess his feelings for Cindy?"
        "{image=icon_love.webp} Yes, he did":
            $ ian_cindy_love = True

        "No, he didn't":
            pass
    scene blackbg
    with long

    $ cindy_look = 1
    $ ian_look = 2

    play music "music/normal_day.mp3" loop

    scene ianroom
    with long
    show ian
    with short
return

label setup_CH10_S04:
    scene blackbg
    with long

    $ ian_look = 3
    $ fian = "n"

    scene ianroom
    with long
    show ianunder at left
    with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    hide ianunder with short
    call screen v10ianwardrobe1
    show ian with short
    if ian_look == "wits1":
        $ v10_ianlook = "wits"
    elif ian_look == "charisma1":
        $ v10_ianlook = "charisma"
    elif ian_look == "athletics1":
        $ v10_ianlook = "athletics"
    elif ian_look == "lust1":
        $ v10_ianlook = "lust"

    $ fian = "smile"
    $ fholly = "blush"
    $ holly_look = "1skirt"

    # no music

    scene blackbg
    with long
return

label setup_CH10_S05:
    scene blackbg
    with long

    play music "music/jeremys_theme.mp3" loop

    $ fian = "smile"
    $ ian_look = 8

    scene gym
    with long
    show ian at lef
    show wen at rig
    with short
return

label setup_CH10_S06:
    scene blackbg
    with long

    scene ianroom
    with long
    $ ian_look = 3
    $ fian = "n"
    show ianunder with short
    gal "Which outfit did Ian wear to the concert?"
    show ianunder at left with move
    call screen v10ianwardrobe2
    hide ianunder with short
    pause 0.5
    if ian_look == "wits1":
        $ v10_ianlook = "wits"
    elif ian_look == "charisma1":
        $ v10_ianlook = "charisma"
    elif ian_look == "athletics1":
        $ v10_ianlook = "athletics"
    elif ian_look == "lust1":
        $ v10_ianlook = "lust"
    else:
        $ v10_ianlook = "cool"
    show ian at left with long
    scene blackbg
    with long

    $ fian = "worried"
    $ fperry = "meh"
    $ fwade = "n"
    $ cindy_look = 1
    $ fcindy = "mad"
    $ femma = "smile"
    $ emma_look = 2

    play music "music/the_fortress.mp3" loop

    scene rockbar
    with long
    show ian at lef
    show perry2 at left
    show cindy2 at rig
    show wade at right
    with short
return

label setup_CH10_S07:
    scene blackbg
    with long

    scene rockbar
    with long
    $ falison = "smile"
    $ ian_look = "cool"
    $ alison_look = 2
    $ fian = "smile"
    show ian at lef
    show alison at rig
    with short
    menu:
        gal "Were Ian and Alison dating?"
        "Yes, they were":
            scene ianroomnight
            show v6_alison4
            with long
            pause(2)
            $ ian_alison_dating = True
            $ v10ianshoppedwine = True
            $ v10_wine = True
            $ v8_alison_sexting = True
            scene blackbg
            with long

            scene streetnight
            with long
            $ ian_look = 1
            $ jeremy_look = 3
            $ fian = "n"
            $ fjeremy = "smile"
            show jeremy at rig
            show ian_phone at lef
            show phone_alison at left
            with short
            menu:
                gal "Did Ian go with Alison on the trip?"
                "Yes, he did":
                    scene v9_alison4
                    with long
                    pause (2)
                    $ v9_alison_trip = True
                    $ v9_alison_creampie = True

                    scene blackbg
                    with long
                    scene v9_alison11
                    with long
                    menu:
                        gal "Does Ian love Alison?"
                        "{image=icon_love.webp} Yes, he does":
                            scene v9_alison11b
                            with long
                            $ ian_alison_love = True
                            $ alison_satisfaction = 5
                        "No, he doesn't":
                            pass
                "No, he didn't":
                    pass
        "No, he didn't":
            $ ian_alison_dating = False
            $ alison_jeremy = True

            scene blackbg
            with long

            $ ian_look = 1
            $ fian = "n"

            scene ianroomnight
            with long
            show ian
            with long
            menu:
                gal "Did Ian request to see more content of Alison from Jeremy?"
                "Yes, he did":
                    show ian at left
                    with move
                    show v4_alison_jeremy
                    with short
                    $ alison_voyeur = True
                    $ v9_alison_voyeur = True
                "No, he didn't":
                    pass
    scene blackbg
    with long

    call gallVar_ian_chad from _call_gallVar_ian_chad

    if ian_chad > 3:
        $ alison_satisfaction = 5 # shortcut

    $ fian = "n"

    # no music
return

label setup_CH10_S17:
    scene blackbg
    with long

    scene v6_alison6
    with long
    menu:
        gal "Did Ian creampie Alison after bringing her home from the bar?"
        "Yes, he did":
            $ v6_alison_cum = True
            scene v6_alison3b
            with long
            pause (2)
        "No, he came on her face":
            $ v6_alison_cum = False
            scene v6_alison7
            show v6_alison7_cum
            show v6_alison7_cock
            with long
            pause (2)
    scene blackbg
    with long

    scene v9_alison14
    with long
    menu:
        gal "Did Ian creampie Alison in the hotel?"
        "Yes, he did":
            $ v9_alison_creampie = True
            scene v9_alison16
            with long
            pause (2)
        "No, he came on her tits":
            $ v9_alison_creampie = False
            scene v9_alison15
            show v9_alison15_cum2
            with long
            pause (2)
    scene blackbg
    with long

    # no music

    $ fian = "n"
    $ ian_look = 1
    jump v10alisondate
return

label setup_CH10_S19:
    scene blackbg
    with long

    $ fian = "n"
    $ ian_look = 2

    play music "music/normal_day2.mp3" loop

    scene ianroomnight
    with long
    show ian at left
    with short
return

label setup_CH10_S20:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "n"
    show lenanude at rig
    with short
    menu:
        gal "Did Lena buy the {image=icon_wits.webp} outfit?"
        "{image=icon_pay.webp} Yes, she did":
            $ lena_look = "wits"
            hide lenanude
            $ lena_makeup = 1
            show lena at rig with short
            show lena with move
        "No, she didn't":
            menu:
                gal "Was Lena's {image=icon_lust.webp} or {image=icon_charisma.webp} higher than her {image=icon_wits.webp}"
                "Yes":
                    $ lena_look = "sexy1"

                "No, her {image=icon_wits.webp} was higher than both":
                    $ lena_look = 4
            hide lenanude
            $ lena_makeup = 1
            show lena at rig with short
            show lena with move
    menu:
        gal "Did she wear Seymour's necklace?"
        "Yes, she did":
            $ lena_necklace = "seymour"

        "No, she wore the choker":
            $ lena_necklace = "choker"

        "No, she wore nothing on her neck":
            pass

    scene blackbg
    with long

    scene ianroom
    with long
    $ ian_look = 3
    $ fian = "n"
    show ianunder with short
    gal "Which outfit did Ian wear to the concert?"
    show ianunder at left with move
    call screen v10ianwardrobe2
    hide ianunder with short
    pause 0.5
    if ian_look == "wits1":
        $ v10_ianlook = "wits"
    elif ian_look == "charisma1":
        $ v10_ianlook = "charisma"
    elif ian_look == "athletics1":
        $ v10_ianlook = "athletics"
    elif ian_look == "lust1":
        $ v10_ianlook = "lust"
    else:
        $ v10_ianlook = "cool"
    show ian at left with long

    scene blackbg
    with long

    # no music
return

label setup_CH10_S21:
    scene blackbg
    with long

    $ fian = "confident"
    $ fminerva = "flirt"
    $ ian_look = 2
    $ minerva_look = 3

    scene magazine
    with long
    show minerva at rig
    show ian at lef
    with short

    menu:
        gal "Did Ian ask Minerva to be nicer to him?"
        "Yes, he did":
            $ ian_minerva_dating = True
            $ fian = "smile"
            $ fminerva = "n"
            pause(1)

        "No, he didn't":
            $ ian_minerva_dating = False
            $ fian = "serious"
            pause(1)

    scene blackbg
    with long

    $ minerva_look = "hot"
    $ ian_look = "wits1"
    $ fminerva = "n"
    $ fian = "worried"

    scene magazine
    with long
    show minerva at rig
    show ian at lef
    with short
    menu:
        gal "Did Ian accept Minerva's dinner invitation?"
        "Yes, he did":
            $ fian = "smile"
            $ fminerva = "smile"
            $ v10_minerva_dinner = 2
            $ ian_minerva = 5
            pause(1)

        "No, he was just interested in the sex":
            $ fian = "serious"
            $ fminerva = "mad"
            $ ian_minerva_dating = False
            $ v10_minerva_dinner = 1
            $ ian_minerva = 3
            pause(1)

    scene blackbg
    with long

    play music "music/normal_day.mp3" loop
return

################################################################################
## CHAPTER 10b #################################################################
################################################################################

label setup_CH10_S08:
    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym_1

    $ fholly = "smile"
    $ flena = "smile"
    $ fivy = "n"
    $ lena_look = 4
    $ lena_makeup = 1
    $ holly_look = 1
    $ ivy_look = 1

    scene ivyroomnight
    with long
    show lena at rig3
    show holly at lef3
    show ivy
    with short
    menu:
        gal "Did Holly have sex with one of the girls?"
        "Yes, with Lena":
            $ lena_holly_sex = True
            $ v8_holly_sex = "lena"
            scene v8_holly3
            if lena_tattoo2:
                show v8_holly3_t2
            if lena_tattoo3:
                show v8_holly3_t3
            with long
            pause (2)
        "Yes, with Lena and Ivy":
            $ v8_holly_sex = "lenaivy"
            scene v8_ivy8
            if lena_tattoo1:
                show v8_ivy8_t1
            if lena_tattoo2:
                show v8_ivy8_t2
            if lena_tattoo3:
                show v8_ivy8_t3
            if lena_piercing1:
                show v8_ivy8_p1
            elif lena_piercing2:
                show v8_ivy8_p2
            with long
            with long
            pause (2)
        "Yes, with Ivy":
            $ v8_holly_sex = "ivy"
            scene v8_ivy4
            with long
            pause (2)
        "No, she didn't":
            pass

    scene blackbg
    with long

    $ fivy = "flirt"
    $ ivy_look = "sexy"
    $ lena_makeup = 0
    $ lena_look = 1
    if lena_holly_sex:
        $ flena = "shy"
    else:
        $ flena = "smile"
    $ fholly = "blush"
    $ holly_look = 2

    if v8_holly_sex == "ivy" or v8_holly_sex == "lenaivy":
        play music "music/flirty.mp3" loop
    else:
        play music "music/date.mp3" loop

    scene lenahome with long
    if v8_holly_sex == "ivy" or v8_holly_sex == "lenaivy":
        show holly3 at lef3
        show lenabra at rig3
        show ivy
    else:
        show holly3 at lef
        show lenabra at rig
    with short
return

label setup_CH10_S09:
    scene blackbg
    with long

    scene v4_lenadate2
    with long
    menu:
        gal "Were Ian and Lena dating?"
        "{image=icon_love.webp} Yes, they were":
            scene v4_lena8
            with long
            pause (2)
            $ ian_lena_dating = True

        "No, they weren't":
            pass
    scene blackbg
    with long

    scene lenaroomnight with long
    $ flena = "n"
    show lenanude with short
    gal "Which outfit did Lena wear to the party?"
    hide lenanude with short
    call screen v10lenawardrobe
    if lena_look == "black_dress":
        $ flena = "happy"
        $ lena_makeup = 2
        $ lena_extras = "black_dress"
    else:
        $ lena_makeup = 1
        $ flena = "smile"
    show lena with long
    l "And for the final touch..."
    menu:
        "{image=icon_lust.webp} Wear the choker":
            l "Let's try the choker on..."
            hide lena with short
            $ lena_necklace = "choker"
            show lena with short
            $ v8_choker = True
            $ v8_sy = False
            $ flena = "smile"
            l "Alright!"

        "{image=icon_charisma.webp} Wear the onyx necklace":
            l "My Addingworth necklace will complete the look..."
            hide lena with short
            $ lena_necklace = "seymour"
            show lena with short
            $ v8_choker = False
            $ v8_sy = True
            $ flena = "happy"
            l "Perfect!"

        "No necklace":
            $ v8_choker = False
            $ v8_sy = False
            l "Like this is okay."
    scene blackbg
    with long
    $ flena = "happy"

    scene ianroom
    with long
    $ ian_look = 3
    show ianunder with short
    gal "Which outfit did Ian wear to the party?"
    call screen v10ianwardrobegallery
    hide ianunder with short
    pause 0.5
    if ian_look == "charisma1":
        $ v10_ianlook = "charisma"
    elif ian_look == "lust1":
        $ v10_ianlook = "lust"
    else:
        $ v10_ianlook = "cool"
    show ian
    with short
    scene blackbg
    with long
    $ fian = "smile"

    $ fivy = "flirt"
    $ ivy_look = "dress"
    $ fmike = "smile"
    $ mike_look = 2
    $ mike_extras = "chain"
    $ fjeremy = "happy"
    $ jeremy_look = 1
    $ fmark = "flirt"
    $ mark_look = 1
    $ fbilly = "happy"
    $ billy_look = 1

    play music "music/edm.mp3" loop
return

label setup_CH10_S10:
    scene blackbg
    with long

    $ flena = "sad"
    $ fivy = "n"
    $ lena_necklace = 0
    $ lena_makeup = 0
    $ ivy_look = "sexy"
    $ lena_look = "underwear2"

    play music "music/calm.mp3" loop

    scene ivyroomnight with long
    show ivybra at lef
    show lenatopless at rig
    with short
return

label setup_CH10_S11:
    scene blackbg
    with long

    $ flena = "smile"
    $ lena_look = 1

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
    play sound "sfx/door.mp3"
    hide louise with short
    $ flena = "shy"
    show lenabra at truecenter with move
    menu:
        gal "Did Lena sneak into Louise's room to wake Jeremy?"
        "Yes, she did":
            scene v8_jeremy1b
            with long
            pause (2)
            menu:
                gal "How far did Lena go with him?"
                "She only blew him":
                    $ v8_jeremy_sex = True
                    scene v8_jeremy5
                    with long
                    pause (2)

                "{image=icon_lust.webp} She went all the way":
                    $ v8_jeremy_sex = True
                    $ lena_jeremy_sex = True
                    scene v8_jeremy6c
                    with long
                    pause (2)
        "No, she didn't":
            $ v8_jeremy_sex = False
            $ lena_jeremy_sex = False

    $ lena_look = "charisma"
    $ flena = "n"
    $ lena_makeup = 1

    # no music

    scene blackbg
    with long
return

label setup_CH10_S12:
    scene blackbg
    with long

    $ toytrack_collar = False

    scene v4_lenadate2
    with long
    menu:
        gal "Were Ian and Lena dating?"
        "{image=icon_love.webp} Yes, they were":
            scene v4_lena8
            with long
            pause (2)
            $ ian_lena_dating = True

        "No, they weren't":
            pass
    scene blackbg
    with long

    scene v7_louise1
    with long
    menu:
        gal "Did Lena act dominant with Louise?"
        "Yes, she did":
            show v7_louise2
            with long
            pause (2)
            $ louise_dominant = True

            scene sexshop
            with long
            show lena at right
            with short
            menu:
                gal "Did Lena buy the BDSM collar?"
                "{image=icon_pay.webp} Yes, she did":
                    $ toy_collar = True
                    show toy_collar with long
                    pause (1)
                    hide toy_collar

                    $ lena_look = 1
                    $ flena = "flirt"
                    $ louise_look = 1
                    $ flouise = "smile"
                    scene louiseroomnight
                    with long
                    show lenabra at rig
                    show louisenude at lef
                    show hand_collar2 at rig
                    with short
                    menu:
                        gal "Did she already use it on Louise?"
                        "Yes, she did":
                            $ lena_louise_collar = True
                            scene v8_louise4
                            show v8_louise4_collar
                            if lena_piercing1:
                                show v8_louise4_p1
                            elif lena_piercing2:
                                show v8_louise4_p2
                            with long
                            pause (2)

                        "No, she didn't":
                            $ toytrack_collar = True

                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music

    $ lena_look = "wits"
    $ lena_makeup = 1
    $ flena = "n"
return

label setup_CH10_S13:
    scene blackbg
    with long

    $ lena_look = 3

    scene lenaroom 
    with long
    show lenabra at left
    with short
    gal "Who did Lena invite to be her photographer?"
    menu:
        "Ian":
            $ v10_stalkfap = "ian"
            $ ian_stalkfap_on = 1

            gal "Which path was her relationship with Ian on?"
            menu:
                "{image=icon_ring.webp} Loyal Ian":
                    $ ian_look = 2

                    $ ian_lena_couple = True
                    $ ian_lena_dating = True
                    $ ian_chad = 5
                    $ ian_stalkfap_on = 2
                    $ lena_anal_first = "ian"
                    $ ian_lena_sex = True
                    $ ian_lena_dom = 1

                "{image=icon_sad.webp} Sexless Ian":
                    $ ian_look = "cool"

                    $ ian_lena_couple = False
                    $ ian_lena_dating = True

                    $ ian_lena_sex = True

                "{image=icon_provoke.webp} Cuck Ian":
                    $ ian_look = "cool"

                    $ ian_lena_couple = True
                    $ ian_lena_dating = True

                    $ lena_cheating = True
                    $ lena_robert_sex = True
                    $ v9_axel_sex = True

                    $ ian_lena_sex = True
                    $ ian_cuck = True

                "{image=icon_sad.webp} Sexless  + {image=icon_provoke.webp} Cuck Ian":
                    $ ian_look = "cool"

                    $ ian_lena_couple = False
                    $ ian_lena_dating = True

                    $ lena_cheating = True
                    $ lena_robert_sex = True
                    $ v9_axel_sex = True

                    $ ian_lena_sex = False
                    $ ian_cuck = True

        "Mike":
            $ v10_stalkfap = "mike"

            $ lena_mike_dating = True
            $ lena_mike_love = True
            $ lena_anal_first = "mike"
            $ v10_axel_fight = "mike"
            

        "Stan":
            $ v10_stalkfap = "stan"

            $ v5_shoot = 3

    scene blackbg
    with long

    call gallVar_toy_badboy

    call gallVar_lena_anal1 from _call_gallVar_lena_anal1_4

    # no music

    $ flena = "smile"
    $ lena_look = "underwear2"

    # no scene
return

label setup_CH10_S14:
    scene blackbg
    with long

    $ v10posingwits = False
    $ v10posingcharisma = False
    $ v10posingathletics = False
    $ v10posinglust = False

    call gallVar_lena_seymour_dating from _call_gallVar_lena_seymour_dating

    if not lena_seymour_dating:
        $ stalkfap_pro = True
    scene blackbg
    with long

    play music "music/flirty.mp3" loop

    $ lena_makeup = 0
    $ lena_necklace = 0

    if lena_seymour_dating:
        jump v10seymourshooting
    else:
        jump v10kentshooting
return

label setup_CH10_S15:
    scene blackbg
    with long

    call gallVar_toy_badboy

    $ lena_look = 1
    $ flena = "n"

    scene lenaroom
    with long
    show lena at rig
    show lolahappy at lef
    with short
    menu:
        gal "Did Lena already masturbate last Thursday?"
        "Yes, she did":
            scene v7_solo1
            if lena_tattoo2:
                show v7_solo1_t2
            with long
            pause (2)
            $ v10_lena_masturbate = True
        "No, she didn't":
            pass

    scene blackbg
    with long

    play music "music/normal_day2.mp3" loop

    scene lenaroom
    with long
    show lenabra at rig
    show lolahappy at lef
    with short
return

label setup_CH10_S18:
    scene blackbg
    with long

    $ mike_look = 1
    $ mike_extras = 0

    # no music
return

################################################################################
## CHAPTER 11_prologue #########################################################
################################################################################

label setup_CH11_S01:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v7_louise1c
    with long
    menu:
        gal "Did Lena act dominant with Louise?"
        "Yes, she did":
            scene v7_louise2
            with long
            pause (2)
            $ louise_dominant = True

        "No, she didn't":
            pass
    scene blackbg
    with long

    # no music

    $ lena_look = 1
    $ louise_look = 1
return

label setup_CH11_S02:
    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_3

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

        "They were just friends" if ian_lena_sex == False:
            gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
            jump setup_CH11_S02

    scene blackbg
    with long

    call gallVar_ian_lena_love from _call_gallVar_ian_lena_love_1
    if ian_lena_couple:
        $ lena_ian_love = True
    elif ian_lena_dating:
        scene ianroomnight_dark
        with long
        menu:
            gal "Did Lena lovingly cuddle up to Ian?" #CH7
            "Yes, she did":
                scene v7_lena7end
                with long
                pause (2)

                $ lena_ian_love = True

            "No, she didn't":
                pass

        scene blackbg
        with long
    
    call gallVar_ian_lena_dom from _call_gallVar_ian_lena_dom_1

    scene v9_axel1
    with long
    menu:
        gal "Did Lena have sex with Axel after the photo shoot?"
        "Yes, she did":
            scene v9_axel5
            with long
            pause (2)

            $ v9_axel_sex = True
            if ian_lena_couple:
                $ lena_cheating = True
            $ lena_axel_desire - True

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_look = "underwear2"
    $ ivy_look = "sexy"
    $ fivy = "flirt"
    $ flena = "blush"
    scene ivyroomnight
    with long
    show lenatopless at rig
    show ivybra at centerlef
    with short
    menu:
        gal "Did Lena have sex with Ivy after the birthday party?"
        "Yes, she did":
            $ v10_ivy_sex = 3
            if ian_lena_couple:
                $ lena_cheating = True
            scene v10_ivy1
            if lena_tattoo1:
                show v10_ivy1_t1
            if lena_tattoo2:
                show v10_ivy1_t2
            if lena_tattoo3:
                show v10_ivy1_t3
            if lena_piercing1:
                show v10_ivy1_p1
            elif lena_piercing2:
                show v10_ivy1_p2
            with long
            pause (2)

        "No, she didn't":
            $ flena = "sad"
            hide lenatopless
            show lenatopless2 at rig behind ivy
            $ fivy = "sad"
            with short
            show lenatopless2 at rig3 with move
    scene blackbg
    with long

    scene v10_ian6
    show v10_ian6_panties
    if lena_piercing1:
        show v10_ian6_p1
    elif lena_piercing2:
        show v10_ian6_p2
    if lena_tattoo1:
        show v10_ian6_t1
    with long
    menu:
        gal "Did Ian ask Lena what she meant when she said his cock was {i}one{/i} of the best she ever had?" #CH10
        "Yes, he did":
            pause (2)
            $ ian_cuck = True
            if ian_chad > 1:
                $ ian_chad = 1
            else:
                $ ian_chad = 0

        "No, he didn't":
            pass

    scene blackbg
    with long

    if ian_lena_sex == False: #ch10
        $ ian_chad = 0

    $ ian_look = "lust1"
    $ fian = "confident"

    scene ianroom
    with long
    show ian at lef2
    with short
    menu:
        gal "How high was Ian's lust?"
        "Level 7 or more":
            $ ian_lust = 10

        "Level 6":
            $ ian_lust = 6

        "Level 5 or lower":
            $ ian_lust = 5

    scene blackbg
    with long

    $ lena_look = "sexy"
    $ flena = "slut"

    scene lenaroom
    with long
    show lena at lef2
    with short
    menu:
        gal "How high was Lena's lust?"
        "Level 8 or more":
            $ lena_lust = 10

        "Level 7 or lower":
            $ lena_lust = 6

    scene blackbg
    with long

    if v9_axel_sex or ian_lena_sex == False:
        $ v10_lena_sex = 1
    elif ian_lena_dom > 0:
        $ v10_lena_sex = 4
    else:
        $ v10_lena_sex = 3

    scene streetnight
    with long

    # no music
return

################################################################################
## CHAPTER 11 ##################################################################
################################################################################

label setup_CH11_S03:
    scene blackbg
    with long

    $ gillian_look = 1
    $ gillian_extras = 0
    $ fgillian = "n"

    $ fian = "n"
    $ ian_look = "cool"

    # no music

    scene street2night
    with long
    show ian at lef3
    with short
return

label setup_CH11_S04:
    scene blackbg
    with long

    scene v10_cindy10
    with long
    menu:
        gal "Did Ian compliment Cindy after their last time?"
        "Yes, he did":
            $ cindy_satisfaction = 3
            $ v10_cindy_compliment = True
            pause (1)
        "No, he didn't":
            $ cindy_satisfaction = 2

    scene blackbg
    with long

    $ ian_look = 2
    $ fian = "confident"
    $ cindy_look = 1

    # no music
return

label setup_CH11_S05:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True

    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Does Holly want to be more like Lena?"
        "Yes, she has been slowly pushed by Ivy and Lena":
            hide holly3 with short
            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_change = 5
            $ v11_holly_change = True
            $ holly_glasses = 2
            show holly with short
        "No, she doesn't":
            hide holly3 with short
            $ holly_look = "summer"
            $ holly_change = 0
            show holly3 with short
    pause (1)
    scene blackbg
    with long

    # no music

    $ ian_look = 2
    $ fian = "smile"
    $ fholly = "happyshy"
return

label setup_CH11_S06:
    scene blackbg
    with long

    $ ian_look = "cool"
    $ alison_look = 2
    $ fian = "smile"
    $ falison = "n"

    scene ianroomnight
    show ian at lef
    show alison at rig
    with short
    menu:
        gal "Was Ian dating Alison?"
        "Yes, he was":
            scene v6_alison4
            with long
            pause (2)

            $ v5_alison_public = True
            $ v5_alison_sex = True
            $ ian_alison_dating = True
            $ v9_alison_trip = True

            scene blackbg
            with long

            $ alison_look = "dress"
            $ ian_look = "lust1"
            $ fian = "smile"
            $ falison = "n"

            scene villagenight
            with long
            show ian at lef
            show alison at rig
            with short
            menu:
                gal "Was Ian in it for the love or just to use Alison as a fuck buddy?"
                "{image=icon_love.webp} For love":
                    scene v9_alison1_bg2
                    show v9_alison2d
                    with long
                    pause(2)

                    $ ian_alison_love = True

                "Fuck buddy":
                    scene v9_alison12
                    with long
                    pause (2)

                    $ ian_alison_dom = True

            scene blackbg
            with long

            $ fian = "confident"
            $ falison = "n"
            $ fjeremy = "happy"
            $ ian_look = 2
            $ jeremy_look = 1

            scene alisonhome
            with long
            show alisonnude at rig3
            show ianunder
            show jeremy at lef3
            with short
            menu:
                gal "Did Ian and Alison have a threesome with Jeremy?"
                "Yes, they did":
                    scene v10_alison6b
                    show v10_alison6b_condom
                    with long
                    pause (2)
                    $ alison_jeremy_3some = 2

                "No, they didn't":
                    $ alison_jeremy_3some = 0
        "No, he was not":
            $ fian = "smile"
            $ ian_look = 1
            scene ianroomnight
            show ian at left
            with short
            show v4_alison_jeremy
            with long
            pause (1)

            $ v5_alison_jeremy = True

            scene blackbg
            with long

            $ fian = "surprise"
            $ falison = "blush"
            $ fjeremy = "happy"
            $ ian_look = 1

            scene alisonhome
            with long
            show ian at lef3
            show alisonnude
            show jeremynude at rig3
            with short
            menu:
                gal "Did Ian participate in a threesome with Alison and Jeremy?"
                "Yes, he did":
                    scene v10_alison2
                    with long
                    pause (2)

                    $ alison_jeremy_3some = 2

                "No, he didn't":
                    scene blackbg
                    with long
                    gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
                    jump setup_CH11_S06

    if alison_jeremy_3some == 2 or ian_alison_dom or ian_alison_dating == False:
        $ alison_blonde = 1

    scene blackbg
    with long

    $ fian = "n"

    scene ianroom
    with long
    show ianunder
    with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    hide ianunder with short
    call screen v10ianwardrobe1
    show ian with short
    scene blackbg
    with long

    play music "music/flirty.mp3" loop

    $ falison = "n"
    $ alison_look = "dress"
    $ alison_makeup = 1
    if alison_jeremy_3some < 2:
        $ fian = "smile"
    elif ian_alison_dating:
        $ fian = "n"
    else:
        $ fian = "smile"

    scene gallery
    with long
    show ian at lef
    show alison at rig
    with move
return

label setup_CH11_S07:
    scene blackbg
    with long

    scene ianroom
    with long
    show ianunder
    with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    hide ianunder with short
    call screen v10ianwardrobe1
    show ian with short
    scene blackbg
    with long

    $ fian = "n"
    $ cherry_look = 2
    $ fcherry = "smile"

    # no music

    scene street2night with long
    show cherry at rig
    show ian at lef
return

label setup_CH11_S08:
    scene blackbg
    with long

    $ ian_look = "cool"
    $ alison_look = 2
    $ fian = "smile"
    $ falison = "n"

    scene ianroomnight
    show ian at lef
    show alison at rig
    with short
    menu:
        gal "Was Ian dating Alison?"
        "Yes, he was":
            scene v6_alison4
            with long
            pause (2)

            $ ian_alison_dating = True

            scene blackbg
            with long

            $ alison_look = "dress"
            $ ian_look = "lust1"
            $ fian = "smile"
            $ falison = "n"

            scene villagenight
            with long
            show ian at lef
            show alison at rig
            with short
            menu:
                gal "Was Ian in it for the love or just to use Alison as a fuck buddy?"
                "{image=icon_love.webp} For love":
                    scene v9_alison1_bg2
                    show v9_alison2d
                    with long
                    pause(2)

                    $ ian_alison_love = True

                "Fuck buddy":
                    scene v9_alison12
                    with long
                    pause (2)

                    $ ian_alison_dom = True

            scene blackbg
            with long

            $ fian = "confident"
            $ falison = "n"
            $ fjeremy = "happy"
            $ ian_look = 2
            $ jeremy_look = 1

            scene alisonhome
            with long
            show alisonnude at rig3
            show ianunder
            show jeremy at lef3
            with short
            menu:
                gal "Did Ian and Alison have a threesome with Jeremy?"
                "Yes, they did":
                    scene v10_alison6b
                    show v10_alison6b_condom
                    with long
                    pause (2)

                    $ alison_jeremy_3some = 2
                    $ v10_alison_3some = "ian"

                "No, they didn't":
                    $ alison_jeremy_3some = 0

        "No, he was not":
            $ fian = "smile"
            $ ian_look = 1
            scene ianroomnight
            show ian at left
            with short
            show v4_alison_jeremy
            with long
            pause (1)

            $ v5_alison_jeremy = True
            $ alison_voyeur = True
            $ v9_alison_voyeur = True

            scene blackbg
            with long

            $ fian = "surprise"
            $ falison = "blush"
            $ fjeremy = "happy"
            $ ian_look = 1

            scene alisonhome
            with long
            show ian at lef3
            show alisonnude
            show jeremynude at rig3
            with short
            menu:
                gal "Did Ian participate in a threesome with Alison and Jeremy?"
                "Yes, he did":
                    scene v10_alison2
                    with long
                    pause (2)

                    $ alison_jeremy_3some = 2
                    $ v10_alison_3some = "duo"

                "No, he didn't":
                    scene blackbg
                    with long

    if alison_jeremy_3some == 2 or ian_alison_dom or ian_alison_dating == False:
        $ alison_blonde = 3

    scene blackbg
    with long

    $ fian = "n"

    scene ianroom
    with long
    show ianunder
    with short
    gal "Which outfit did Ian decide to wear?"
    show ianunder at left with move
    hide ianunder with short
    call screen v10ianwardrobe1
    show ian with short
    scene blackbg
    with long

    $ falison = "n"
    $ alison_look = "dress"
    $ alison_makeup = 1

    # no music

    if ian_alison_dating:
        $ fian = "smile"
        jump v11alisondate
    else:
        jump v11alisonrejectdate
return

label setup_CH11_S09:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True

    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Does Holly want to be more like Lena?"
        "Yes, she has been slowly pushed by Ivy and Lena":
            hide holly3 with short
            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_change = 5
            $ v11_holly_change = True
            $ holly_glasses = 2
            show holly with short
        "A little":
            hide holly3 with short
            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_change = 4
            $ v11_holly_change = True
            $ holly_glasses = 2
            show holly2 with short
        "No":
            hide holly3 with short
            $ holly_look = "summer"
            $ holly_change = 0
            show holly3 with short
    pause (1)
    scene blackbg
    with long

    $ fholly = "n"
    $ flena = "blush"
    $ lena_look = 4
    $ holly_look = 1
    $ holly_glasses = True

    scene lenaroomnight
    with long
    show holly2 at lef3
    show lolahappy
    show lena2 at rig3
    with short
    menu:
        gal "Is Lena also interested in Holly?"
        "Yes, she is":
            $ lena_go_holly = True
            scene v8_holly1
            if lena_tattoo2:
                show v8_holly1_t2
            show v8_holly1_clothes
            with long
            pause (2)
        "No, she isn't":
            $ lena_go_holly = False
    scene blackbg
    with long

    $ holly_look = "summer"
    if holly_change > 3:
        $ holly_glasses = 2

    $ ian_look = 2
    $ fian = "smile"
    $ fholly = "sad"

    play music "music/calm.mp3"

    scene ianhomenight with long
    show ian at lef
    show holly2 at rig
return

label setup_CH11_S10:
    scene blackbg
    with long

    $ ian_look = 2
    $ lena_look = 4

    show ian at left5
    show lena at right5
    with short
    gal "Which path were your Ian and Lena on?"
    menu:
        "{image=icon_ring.webp} Loyal Ian + Loyal Lena {image=icon_ring.webp}":
            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = True
            $ ian_lena_love = True

            # No cheating
            $ v3_gillian_stop = True

            # No Cuck
            $ ian_cuck = False
            $ ian_chad = 5

            $ ian_lena_dom = 2
            $ v10_wc_bj = "ian"
            $ cafe_perry = True
            $ v10_lena_sex = 4

        "Both seeing other people":
            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = False
            $ ian_lena_love = False
            $ ian_lena_dating = True

            $ v3_gillian_stop = True

            # No Cuck
            $ ian_cuck = False
            $ ian_chad = 5
            $ v10_tease_perry = True
            $ v9_axel_sex = True

            $ ian_lena_dom = 2
            $ v10_wc_bj = "ian"
            $ v10_lena_sex = 4
            $ cafe_perry = False


        "{image=icon_provoke.webp} Cuck Ian + Cheating Lena {image=icon_lust.webp}":
            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = True
            $ ian_lena_love = True

            # Lena Cheating
            $ lena_cheating = True
            $ v3_gillian_stop = True
            $ v9_axel_sex = True
            $ v10_tease_perry = True
            $ cafe_perry = True
            $ v10_wc_bj = "mike"

            # Cuck
            $ v3_gillian_stop = False
            $ v11_gillian_talk = 3
            $ ian_cuck = 2
            $ v10_lena_sex = 1
            $ v11_tell_dream = True
            $ ian_chad = 0

        "{image=icon_sad.webp} Sexless {image=icon_provoke.webp} Cuck Ian + Cheating Lena {image=icon_lust.webp}":
            # No sex
            $ ian_lena_sex = False

            # Relationship
            $ ian_lena_couple = True
            $ ian_lena_love = True

            # Lena Cheating
            $ lena_cheating = True
            $ v3_gillian_stop = True
            $ v9_axel_sex = True
            $ v10_tease_perry = True
            $ cafe_perry = True
            $ v10_wc_bj = "mike"

            # Cuck
            $ v3_gillian_stop = False
            $ v11_gillian_talk = 3
            $ ian_cuck = 2
            $ v10_lena_sex = 1
            $ v11_tell_dream = True
            $ ian_chad = 0

    scene blackbg
    with long

    call gallVar_toy_badboy

    # no music

    $ ian_look = 2
    $ lena_look = 4
    $ fian = "smile"
    $ flena = "n"
return

################################################################################
## CHAPTER 11b #################################################################
################################################################################

label setup_CH11_S11:
    scene blackbg
    with long

    if gallery_scene_unlocked('CH11_S11b') or persistent.gallery_force_unlock:
        $ stalkfap = True
        $ stalkfap_pro = 2
        $ v10_stalkfap = "ian"
        $ toy_badboy = True
        $ lena_anal = 2

        $ temp_gallery = True

    play music "music/calm.mp3" loop

    $ lena_look = 1
    $ flena = "flirtshy"

    scene lenaoldroomnight
    with long
    show lenabra2 
    with short
return

label setup_CH11_S11b:
    scene blackbg
    with long

    $ v11sms2_axel = False
    $ v11sms2_mike = False
    $ v11sms2_jeremy = False
    $ v11sms2_robert = False

    play music "music/calm.mp3" loop

    $ lena_look = 1
    $ flena = "flirtshy"

    scene lenaoldroomnight
    with long
    show lenabra2
    with short
return

label setup_CH11_S11c:
    scene blackbg
    with long

    $ v11sms2_axel = False
    $ v11sms2_mike = False
    $ v11sms2_jeremy = False
    $ v11sms2_robert = False

    $ lena_look = 1
    $ flena = "n"

    # no music

    scene lenaoldroomnight
    with long
    show lenabra2
    with short
return

label setup_CH11_S13:
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "shy"
    $ fmike = "n"
    $ mike_look = 1

    # no music
return

label setup_CH11_S14:
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "shy"
    $ frobert = "n"
    $ robert_look = 1

    # no music
return

label setup_CH11_S15:
    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym_2

    $ flena = "n"
    $ fivy = "n"
    $ fholly = "n"
    $ fminerva = "smile"

    $ lena_look = 2
    $ ivy_look = 2
    $ ivy_extras = 0
    $ holly_look = 4
    $ minerva_look = 2
    $ holly_glasses = False

    # no music

    scene polegym 
    with long
    show lena at right
    show ivy at lef
    show holly at left
    show minerva at rig
    with short
return

label setup_CH11_S16:
    scene blackbg
    with long

    $ fholly = "smile"
    $ flena = "smile"
    $ fivy = "n"
    $ lena_look = 4
    $ lena_makeup = 1
    $ holly_look = 1
    $ ivy_look = 1

    scene ivyroomnight
    with long
    show lena at rig3
    show holly at lef3
    show ivy
    with short
    menu:
        gal "Did Lena join Ivy and Holly?"
        "Yes, she did":
            $ v8_holly_sex = "lenaivy"
            scene v8_ivy8
            if lena_tattoo1:
                show v8_ivy8_t1
            if lena_tattoo2:
                show v8_ivy8_t2
            if lena_tattoo3:
                show v8_ivy8_t3
            if lena_piercing1:
                show v8_ivy8_p1
            elif lena_piercing2:
                show v8_ivy8_p2
            with long
            with long
            pause (2)
        "No, she didn't":
            $ v8_holly_sex = "ivy"
            scene v8_ivy4
            with long
            pause (2)
    scene blackbg
    with long

    $ lena_makeup = 0
    $ lena_look = "underwear2"
    $ ivy_look = "sexy"
    $ fivy = "flirt"
    $ flena = "blush"
    scene ivyroomnight
    with long
    show lenatopless at rig
    show ivybra at centerlef
    with short
    menu:
        gal "Did Lena have sex with Ivy after the birthday party?"
        "Yes, she did":
            $ v10_ivy_sex = 3
            scene v10_ivy1
            if lena_tattoo1:
                show v10_ivy1_t1
            if lena_tattoo2:
                show v10_ivy1_t2
            if lena_tattoo3:
                show v10_ivy1_t3
            if lena_piercing1:
                show v10_ivy1_p1
            elif lena_piercing2:
                show v10_ivy1_p2
            with long
            pause (2)
        "No, she didn't":
            $ flena = "sad"
            hide lenatopless
            show lenatopless2 at rig behind ivy
            $ fivy = "sad"
            with short
            show lenatopless2 at rig3 with move
    scene blackbg
    with long

    if lena_holly_sex or (v10_lena_holly_sex and v8_holly_sex != "ivy" and v8_holly_sex != "lenaivy"):
        $ lena_holly_dating = True

    $ flena = "n"
    $ fholly = "n"
    $ fminerva = "smile"
    $ lena_look = 2
    $ ivy_look = 2
    $ ivy_extras = 0
    $ holly_look = 4
    $ holly_glasses = False
    $ minerva_look = 2

    scene polegym
    show holly at lef3
    show lena at rig3
    show ivy2
    with long
    v "Alright, that'll be all for today! Class dismissed!"
return

label setup_CH11_S16b:
    scene blackbg
    with long

    scene v10_holly14
    show v10_holly14_abs
    with long
    menu:
        gal "Did Lena have sex with Holly after her photo shoot?"
        "Yes, she did":
            $ v10_lena_holly_sex = True
            scene v10_holly16
            with long
            pause(2)
        "No, she didn't":
            pass
    scene blackbg
    with long

    if lena_holly_sex or v10_lena_holly_sex:
        $ lena_holly_dating = True

    $ flena = "n"
    $ fholly = "n"
    $ fminerva = "smile"
    $ lena_look = 2
    $ ivy_look = 2
    $ ivy_extras = 0
    $ holly_look = 4
    $ holly_glasses = False
    $ minerva_look = 2

    scene polegym
    show holly at lef3
    show lena at rig3
    show ivy2
    with long
    v "Alright, that'll be all for today! Class dismissed!"
return

label setup_CH11_S17:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True

    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Does Holly want to be more like Lena?"
        "Yes, she has been slowly pushed by Ivy and Lena":
            hide holly3 
            with short
            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_change = 5
            $ v11_holly_change = True
            $ holly_glasses = 2
            show holly 
            with short

        "No, she doesn't":
            hide holly3 
            with short
            $ holly_look = "summer"
            $ holly_change = 0
            show holly3 
            with short
    pause (1)

    scene blackbg
    with long
    
    $ fholly = "smile"
    $ flena = "smile"
    $ fivy = "n"
    $ lena_look = 4
    $ lena_makeup = 1
    $ holly_look = 1
    $ ivy_look = 1

    scene ivyroomnight
    with long
    show lena at rig3
    show holly at lef3
    show ivy
    with short
    menu:
        gal "Did Holly have sex with one of the girls?"
        "Yes, with Lena":
            $ lena_holly_sex = True
            $ v8_holly_sex = "lena"
            scene v8_holly3
            if lena_tattoo2:
                show v8_holly3_t2
            if lena_tattoo3:
                show v8_holly3_t3
            with long
            pause (2)

        "Yes, with Lena and Ivy":
            $ v8_holly_sex = "lenaivy"
            scene v8_ivy8
            if lena_tattoo1:
                show v8_ivy8_t1
            if lena_tattoo2:
                show v8_ivy8_t2
            if lena_tattoo3:
                show v8_ivy8_t3
            if lena_piercing1:
                show v8_ivy8_p1
            elif lena_piercing2:
                show v8_ivy8_p2
            with long
            with long
            pause (2)

        "Yes, with Ivy":
            $ v8_holly_sex = "ivy"
            scene v8_ivy4
            with long
            pause (2)

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_makeup = 0

    scene v10_holly14
    show v10_holly14_abs
    with long
    menu:
        gal "Did Lena have sex with Holly after her photo shoot?"
        "Yes, she did":
            $ v10_lena_holly_sex = True
            $ lena_go_holly = 5
            scene v10_holly16
            with long
            pause(2)
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = "underwear2"
    $ ivy_look = "sexy"
    $ fivy = "flirt"
    $ flena = "blush"
    scene ivyroomnight
    with long
    show lenatopless at rig
    show ivybra at centerlef
    with short
    menu:
        gal "Did Lena have sex with Ivy after the birthday party?"
        "Yes, she did":
            $ v10_ivy_sex = 3
            if ian_lena_couple:
                $ lena_cheating = True
            scene v10_ivy1
            if lena_tattoo1:
                show v10_ivy1_t1
            if lena_tattoo2:
                show v10_ivy1_t2
            if lena_tattoo3:
                show v10_ivy1_t3
            if lena_piercing1:
                show v10_ivy1_p1
            elif lena_piercing2:
                show v10_ivy1_p2
            with long
            pause (2)

        "No, she didn't":
            $ flena = "sad"
            hide lenatopless
            show lenatopless2 at rig behind ivy
            $ fivy = "sad"
            with short
            show lenatopless2 at rig3 with move
    scene blackbg
    with long

    if lena_holly_sex or (v10_lena_holly_sex and v8_holly_sex != "ivy" and v8_holly_sex != "lenaivy"):
        $ lena_holly_dating = True

    if v8_holly_sex == "ivy" or v8_holly_sex == "lenaivy":
        $ holly_ivy = True

        scene v11_shower1
        with long
        menu:
            gal "Did Lena join the fun?"
            "Yes, she did":
                scene v11_shower2b
                if lena_tattoo1:
                    show v11_shower2_t1
                if lena_tattoo2:
                    show v11_shower2_t2b
                if lena_tattoo3:
                    show v11_shower2_t3
                if lena_piercing1:
                    show v11_shower2_p1
                elif lena_piercing2:
                    show v11_shower2_p2
                with long
                pause (2)

                $ v11_shower_sex = "3some"

            "No, she didn't":
                pass

    else:
        $ flena = "blush"
        $ fholly = "worried"
        $ fivy = "flirt"
        scene gymshowers
        show ivynude2
        show hollynude2 at lef3
        show holly_towel at lef3
        show lenanude2 at rig3
        with long
        menu:
            gal "Did Lena make Holly join her and Ivy in the shower?"
            "Yes, she did":
                play sound "sfx/shower.mp3"
                scene v11_shower4
                if lena_tattoo3:
                    show v11_shower4_t3
                with long
                pause (2)

                $ holly_ivy = True
                $ v11_shower_sex = "3some"

            "No, she didn't":
                pass

    scene blackbg
    with long

    play music "music/hollys_theme.mp3" loop

    $ lena_look = 4
    $ flena = "n"
    $ holly_look = "summer"
    if holly_change > 3:
        $ holly_glasses = 2
    else:
        $ holly_glasses = True
    $ fholly = "happyshy"

    scene lenaroom
    with long
    show lena at rig
    show holly2 at lef
    with short
return

label setup_CH11_S18:
    scene blackbg
    with long

    call gallVar_ian_chad from _call_gallVar_ian_chad_1

    $ fian = "n"

    scene v11_lena8 
    if lena_tattoo2:
        show v11_lena8_t2
    if lena_tattoo3:
        show v11_lena8_t3
    with long
    menu:
        gal "Did Ian manage to make Lena Squirt?"
        "Yes, he did":
            show v11_lena8c with flash
            play sound "sfx/orgasm3.mp3" fadeout 1.0
            $ v11_lena_squirt = True
            hide v11_lena8c
            show v11_lena8d
            with vpunch
            pause 0.5
            with vpunch
            pause 0.5
            with vpunch
            pause 1
        "No, he didn't":
            pass
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v5_louise1
    if lena_piercing1:
        show v5_louise1_p1
    elif lena_piercing2:
        show v5_louise1_p2
    show v5_louise1_eyes1
    with long
    menu:
        gal "Did Lena have sex with Louise?"
        "Yes, she did":
            scene v5_louise7
            show v5_louise7_choker
            with long
            pause (2)

            $ lena_louise_sex = True

            scene blackbg
            with long

            scene lenaroomnight
            with long
            scene v7_louise1c
            with long
            menu:
                gal "Did Lena act dominant with Louise?"
                "Yes, she did":
                    scene v7_louise2
                    with long
                    pause (2)
                    $ louise_dominant = True

                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = "underwear2"
    $ flena = "flirtshy"
    $ flouise = "blush"
    $ louise_look = 1

    # no music
return

label setup_CH11_S19:
    scene blackbg
    with long

    scene lenaroomnight
    with long
    scene v5_louise1
    if lena_piercing1:
        show v5_louise1_p1
    elif lena_piercing2:
        show v5_louise1_p2
    show v5_louise1_eyes1
    with long
    menu:
        gal "Did Lena have sex with Louise?"
        "Yes, she did":
            scene v5_louise7
            show v5_louise7_choker
            with long
            pause (2)

            $ lena_louise_sex = True

            scene blackbg
            with long

            scene lenaroomnight
            with long
            scene v7_louise1c
            with long
            menu:
                gal "Did Lena act dominant with Louise?"
                "Yes, she did":
                    scene v7_louise2
                    with long
                    pause (2)
                    $ louise_dominant = True

                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = "underwear2"
    $ flena = "flirtshy"
    $ louise_look = 1

    # no music
return

label setup_CH11_S20:
    scene blackbg
    with long

    $ flena = "smile"
    $ fseymour = "smile"
    $ lena_look = "wits"
    $ seymour_look = 1
    scene seymourofficenight
    with long
    show seymour2 at lef
    show lena2 at rig
    with short
    menu:
        gal "Does Lena like working for Seymour?"
        "She obeys him":
            $ seymour_disposition = 3
        "Yes, she does":
            $ seymour_disposition = 2
            $ fseymour = "n"
        "No, she doesn't":
            $ seymour_disposition = 0
            $ fseymour = "n"
            $ flena = "worried"
    scene blackbg
    with long

    scene v9_seymour5b
    if lena_tattoo2:
        show v9_seymour5_t2b
    if lena_tattoo3:
        show v9_seymour5_t3
    show v9_seymour5_sy
    with long
    menu:
        gal "Did Seymour use his toy on Lena?"
        "Yes, he did":
            $ v9_seymour_orgasm = True
            scene v9_seymour7b
            if lena_tattoo1:
                show v9_seymour7_t1
            if lena_tattoo2:
                show v9_seymour7_t2b
            if lena_piercing1:
                show v9_seymour7_p1
            elif lena_piercing2:
                show v9_seymour7_p2
            show v9_seymour7_sy
            with long
            pause (2)
        "No, he didn't":
            pass
    scene blackbg
    with long

    $ lena_makeup = 0
    $ lena_look = "underwear2"
    if seymour_disposition > 2:
        $ flena = "smile"
    elif seymour_disposition > 0.5:
        $ flena = "n"
    else:
        $ flena = "worried"

    scene lenaroomnight
    with long
    show lenabra2
    with short
    gal "Which outfit did Lena decide to wear?"
    hide lenabra2 with short
    $ lena_makeup = 1
    call screen v11seymourdress
    if lena_look == "black_dress":
        $ lena_makeup = 2
        $ flena = "smile"
        show lena2 with short
        l "This seems like the perfect opportunity to wear the dress I bought... I wonder what Seymour's reaction will be."
    elif lena_look == "charisma":
        $ flena = "smile"
        show lena2 with short
        l "This outfit seems appropriate. Classy and sexy!"
    else:
        $ flena = "n"
        show lena2 with short
        l "This outfit seems appropriate, I guess..."

    menu:
        gal "Did Lena sell Seymour's necklace?"
        "Yes, she did":
            $ v7_necklace_sell = 1
            $ seymour_necklace = True
            if seymour_disposition > 2:
                l "Last time he wanted me to wear the necklace he gifted me... I was gonna wear it anyway; I love that piece."
                l "I never imagined I would own something like it..."
            elif seymour_disposition > 0.5:    
                l "Last time he wanted me to wear the necklace he gifted me... That'll keep him happy." 
            else:
                l "Last time he wanted me to wear the necklace he gifted me... I suppose need to indulge him, don't I...?"
        "No, she still has it":
            $ seymour_necklace = True
            $ lena_necklace = "seymour"
        "She never got to take it home":
            $ seymour_necklace = False
    pause (1)

    scene blackbg
    with long

    # no music
return

################################################################################
## CHAPTER 11 Epilogue #########################################################
################################################################################

label setup_CH11_S21:
    scene blackbg
    with long

    play music "music/girls_day.mp3" loop

    $ lena_look = 4
    $ emma_look = 1
    $ femma = "n"
    $ flena = "n"

    scene mall
    with long
    show lena at rig3
    show emma at lef3
    with short
return

label setup_CH11_S22:
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    if v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS22dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS22dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS22dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS22dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    $ jeremy_look = 1
    $ fjeremy = "smile"

    # no music

    scene street2night
    with long
    "I followed Jeremy through a back door as he continued to explain the logistics of the club."
    show lena at rig
    show jeremy at lef
    with short
    j "If we start running low on beers, grab one of those boxes to restock the fridge. We pile up empty bottles in those crates over there..."
    j "This is also where we take breaks. If the bar's not too busy and you need a smoke or to get some air, you can take five or ten minutes."
    l "Got it..."
return

label setup_CH11_S23:
    scene blackbg
    with long

    scene v4_lenadate2
    with long
    menu:
        gal "Were Ian and Lena dating?"
        "{image=icon_love.webp} Yes, they were":
            scene v4_lena8
            with long
            pause (2)
            $ ian_lena_dating = True
            $ ian_lena_couple = True
            $ v10_wc_bj = "ian"

        "No, they weren't":
            $ v10_wc_bj = "mike"
    scene blackbg
    with long

    $ lena_look = "lust"
    $ ivy_look = "sexy"
    $ jeremy_look = 1
    $ louise_look = 2
    $ fivy = "flirt"
    $ flena = "slutshy"
    $ fjeremy = "surprise"
    $ flouise = "blush"
    scene ivyroomnight
    with long
    show lenabra2 at right
    show ivynude2 at rig
    show louisenude at lef
    show jeremynude at left
    with short
    menu:
        gal "Did Lena agree to make Jeremy cum during Ivy's game?"
        "Yes, she did":
            scene v7_jeremy4_animation1
            with long
            pause (2)
            $ v7_bbc = "lena"

            scene blackbg
            with long

            $ flena = "smile"
            $ lena_look = 1

            scene lenahome
            with long
            show lenabra at rig
            show louise at lef
            with short
            play sound "sfx/door.mp3"
            hide louise with short
            $ flena = "shy"
            show lenabra at truecenter with move
            menu:
                gal "Did Lena sneak into Louise's room to wake Jeremy?"
                "Yes, she did":
                    $ v8_jeremy_sex = True
                    scene v8_jeremy5
                    with long
                    pause (2)
                "No, she didn't":
                    pass

        "No, she didn't":
            scene v7_jeremy_ivy
            with long
            pause (2)
            $ v7_bbc = "ivy"
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS23dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS23dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS23dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS23dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    # no music

    $ flena = "flirtshy"
    $ fmarcel = "n"

    scene street2night
    with long
    show lena at rig
    with short
return

label setup_CH11_S24:
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS24dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS24dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS24dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS24dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    $ flena = "n"
    $ axel_look = 2

    # no music

    scene blazer
    with long
    show lena
    with short
return

label setup_CH11_S27:
    scene blackbg
    with long

    scene v4_lenadate2
    with long
    menu:
        gal "Were Ian and Lena a couple?"
        "{image=icon_love.webp} Yes, they were":
            scene v4_lena8
            with long
            pause (2)
            $ ian_lena_couple = True
            $ v11_ian_sex = True

        "No, they weren't":
            pass
    scene blackbg
    with long

    $ flena = "flirtshy"
    $ fian = "smile"
    $ ian_look = "charisma1"
    $ lena_makeup = 2
    $ lena_look = "black_dress"
    $ lena_necklace = "seymour"

    scene blazer
    with long
    show ian at lef
    show lena2 at rig
    with short
    menu:
        gal "Was Lena cheating on Ian?"
        "Yes, she was":
            scene v10_wc_animation_full
            with long
            pause 2
            $ lena_cheating = True
            $ lena_mike_dating = True
        "No, she wasn't":
            pass
    scene blackbg
    with long

    $ lena_look = 4
    $ lena_makeup = 0
    $ flena = "n"
    $ lena_necklace = 0

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS27dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS27dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS27dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS27dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    $ flena = "n"

    play music "music/edm.mp3" loop
    $ jk = "{color=#CC0000}Jack{/color}"

    scene blazer
    with long
    show lena
    with short
return

label setup_CH11_S25:
    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS25dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS25dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS25dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS25dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    play music "music/calm.mp3" loop
return

label setup_CH11_S26:
    scene blackbg
    with long

    $ ian_look = 2
    $ lena_look = 4

    show ian at left5
    show lena at right5
    with short
    gal "Which path were your Ian and Lena on?"
    menu:
        "{image=icon_ring.webp} Loyal Ian + Loyal Lena {image=icon_ring.webp}":
            # Stats
            $ ian_lust = 10
            $ ian_fit = 1

            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = True

            # Love
            $ ian_lena_love = True
            $ lena_ian_love = True
            $ v11_lena_openup = True

            # Ian cheating
            $ ian_cindy_sex = False

            # Lena cheating
            $ lena_cheating = False
            $ lena_mike_dating = False
            $ lena_jack = False
            $ v11_bbc = False
            $ v11_john_flirt = False
            $ lena_axel_desire = False
            $ v10_tease_perry = False
            $ v11_bar4 = False
            $ v10_wc_bj = "ian"
            $ v10_stalkfap = "ian"
            $ ian_stalkfap_on = 2

            # Cuck
            $ ian_cuck = False
            $ ian_chad = 5
            $ v11_tell_dream = False
            $ v11_lena_dom = False
            $ ian_lena_dom = 2
            $ v11_lena_squirt = True

            # Anal
            $ lena_anal = 2
            $ v11_lena_anal = True

        "{image=icon_love.webp} Loyal Ian + Cheating Lena {image=icon_lust.webp}":
            # Stats
            $ ian_lust = 10
            $ ian_fit = 1

            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = True

            # Love
            $ ian_lena_love = True
            $ lena_ian_love = True
            $ v11_lena_openup = True

            # Ian cheating
            $ ian_cindy_sex = False

            # Lena cheating
            $ lena_cheating = True
            $ lena_mike_dating = True
            $ lena_jack = 2
            $ v11_bbc = "marcel"
            $ v11_john_flirt = 3
            $ lena_axel_desire = True
            $ v10_tease_perry = True
            $ v11_bar4 = 3
            $ v10_wc_bj = "mike"
            $ v10_stalkfap = "mike"
            $ ian_stalkfap_on = 2

            # Cuck
            $ ian_cuck = False
            $ ian_chad = 5
            $ v11_tell_dream = False
            $ v11_lena_dom = False
            $ ian_lena_dom = 2
            $ v11_lena_squirt = True

            # Anal
            $ lena_anal = 2
            $ v11_lena_anal = True

        "{image=icon_provoke.webp} Cuck Ian + Cheating Lena {image=icon_lust.webp}":
            # Stats
            $ ian_lust = 5
            $ ian_fit = 0

            # Sex
            $ ian_lena_sex = True

            # Relationship
            $ ian_lena_couple = True

            # Love
            $ ian_lena_love = True
            $ lena_ian_love = True
            $ v11_lena_openup = False

            # Ian cheating
            $ ian_cindy_sex = False

            # Lena cheating
            $ lena_cheating = True
            $ lena_mike_dating = True
            $ lena_jack = 2
            $ v11_bbc = "marcel"
            $ v11_john_flirt = 3
            $ lena_axel_desire = True
            $ v10_tease_perry = True
            $ v11_bar4 = 3
            $ v10_wc_bj = "mike"
            $ v10_stalkfap = "mike"
            $ ian_stalkfap_on = 2

            # Cuck
            $ ian_cuck = 2
            $ ian_chad = 0
            $ v11_tell_dream = True
            $ v11_lena_dom = 1
            $ ian_lena_dom = 0
            $ v11_lena_squirt = False

            # Anal
            $ lena_anal = 2
            $ v11_lena_anal = True

        "{image=icon_sad.webp} Sexless {image=icon_provoke.webp} Cuck Ian + Cheating Lena {image=icon_lust.webp}":
            # Stats
            $ ian_lust = 3
            $ ian_fit = 0

            # Sex
            $ ian_lena_sex = False

            # Relationship
            $ ian_lena_couple = False

            # Love
            $ ian_lena_love = True
            $ lena_ian_love = True
            $ v11_lena_openup = False

            # Ian cheating
            $ ian_cindy_sex = False

            # Lena cheating
            $ lena_cheating = False
            $ lena_mike_dating = True
            $ lena_jack = 4
            $ v11_bbc = "jeremy"
            $ v11_john_flirt = 3
            $ lena_axel_desire = True
            $ v10_tease_perry = True
            $ v11_bar4 = 3
            $ v10_wc_bj = "mike"
            $ v10_stalkfap = "mike"
            $ ian_stalkfap_on = 2

            # Cuck
            $ ian_cuck = 2
            $ ian_chad = 0
            $ v11_tell_dream = True
            $ v11_lena_dom = 1
            $ ian_lena_dom = 0
            $ v11_lena_squirt = False

            # Anal
            $ lena_anal = 2
            $ v11_lena_anal = False

        "Custom replay":
            scene blackbg
            with long

            # Sex
            call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_4

            # Relationship
            $ ian_look = 2
            $ lena_look = "sexy"
            $ fian = "n"
            $ flena = "n"

            scene parknight
            with long
            show ian at lef
            show lena at rig
            with short
            menu:
                gal "How serious was the relationship between Ian and Lena?"
                "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
                    $ fian = "blush"
                    $ flena = "blush"

                    $ ian_lena_dating = True
                    $ ian_lena_couple = True

                "They were just seeing each other": #CH5
                    $ ian_lena_dating = True

                "They were just friends" if ian_lena_sex == False:
                    gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
                    jump setup_CH11_S26

            scene blackbg
            with long

            # Love
            call gallVar_ian_lena_love from _call_gallVar_ian_lena_love_2
            call gallVar_lena_ian_love from _call_gallVar_lena_ian_love
            if ian_lena_couple: # shortcut
                $ v11_lena_openup = True

            call gallVar_ian_lena_dom from _call_gallVar_ian_lena_dom_2

            # Lena cheating
            call gallVar_lena_cheating from _call_gallVar_lena_cheating

            if lena_cheating:
                $ v10_tease_perry = True
                $ v11_john_flirt = 3
                $ v11_bar4 = 3
            if lena_mike_dating:
                $ v10_stalkfap = "mike"

            # Cuck
            $ ian_chad = 5
            call gallVar_ian_cuck from _call_gallVar_ian_cuck
            if ian_cuck > 0:
                $ v11_tell_dream = True

            # Anal
            call gallVar_lena_anal2 from _call_gallVar_lena_anal2
            if lena_anal > 1:
                if v10_wc_bj == "mark": #shortcut
                    $ v11_lena_anal = True

            if ian_lena_dom > 1: #shortcut
                $ v11_lena_squirt = True

            # Stats
            if ian_cuck: #shortcut
                $ ian_lust = 5
                $ ian_fit = 0
            else:
                $ ian_fit = 1

    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galS26dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galS26dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galS26dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galS26dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    play music "music/calm.mp3" loop
return

################################################################################
## CHAPTER 12a #################################################################
################################################################################

label setup_CH12_S01:
    scene blackbg
    with long

    # no music
return

label setup_CH12_S02:
    scene blackbg
    with long

    scene restaurant
    with long
    $ fian = "n"
    $ fminerva = "n"
    $ ian_look = "charisma1"
    $ minerva_look = "dress"
    show ian at lef
    show minerva4 at rig
    with short
    menu:
        gal "What were Ian's feelings towards Minerva?"
        "{image=icon_love.webp}He was falling for her":
            scene v10_minerva5
            with long
            pause (2)

            $ ian_minerva_dating = 3
        "He liked her":
            scene v10_minerva4b
            with long
            pause (2)

            $ ian_minerva_dating = 2
        "He was in it for the sex":
            scene v10_minerva6b
            with long
            pause (2)

            $ ian_minerva_dating = 1
    scene blackbg
    with long

    $ ian_look = 2
    $ minerva_look = "hot"
    $ fian = "n"
    $ fminerva = "n"

    play music "music/normal_day5.mp3" loop

    scene magazine
    with long
    show ian
    with short
return

label setup_CH12_S03:
    scene blackbg
    with long

    $ cindy_look = 2
    $ fcindy = "blush"
    $ ian_look = "charisma1"
    $ fian = "n"

    scene street_afternoon
    with long
    show ian at lef
    show cindy at rig
    with short
    menu:
        gal "Did Ian confess his feelings for Cindy?"
        "{image=icon_love.webp} Yes, he did":
            $ ian_cindy_love = True

        "No, he didn't":
            pass
    scene blackbg
    with long

    scene v9_cindy3
    with long
    menu:
        gal "Did Ian manage to satisfy Cindy?"
        "Yes, he did":
            scene v9_cindy6
            with long
            pause (2)

            $ cindy_satisfaction = 3
        "No, he didn't":
            pass
    scene blackbg
    with long

    $ ian_look = 2
    if ian_cindy_love:
        $ fian = "smile"
    else:
        $ fian = "confident"

    # no music
return

label setup_CH12_S04:
    scene blackbg
    with long

    call gallVar_ian_chad from _call_gallVar_ian_chad_2

    $ ian_look = "cool"
    $ alison_look = 2
    $ fian = "smile"
    $ falison = "n"

    scene ianroomnight
    show ian at lef
    show alison at rig
    with short
    menu CH12_S04:
        gal "Was Ian dating Alison?"
        "Yes, he was":
            scene v6_alison4
            with long
            pause (2)

            $ ian_alison_dating = True
            $ v9_alison_trip = True
            $ alison_sexy = 2

            scene blackbg
            with long

            $ alison_look = "dress"
            $ ian_look = "lust1"
            $ fian = "smile"
            $ falison = "n"

            scene villagenight
            with long
            show ian at lef
            show alison at rig
            with short
            menu:
                gal "Was Ian in it for the love or just to use Alison as a fuck buddy?"
                "{image=icon_love.webp} For love":
                    scene v9_alison1_bg2
                    show v9_alison2d
                    with long
                    pause(2)

                    $ ian_alison_love = True

                "{image=icon_lust.webp} Fuck buddy":
                    scene v9_alison12
                    with long
                    pause (2)

                    $ ian_alison_dom = True

            scene blackbg
            with long

            scene v9_alison18:
            with long
            menu:
                gal "Did Ian ask for Anal sex?"
                "Yes, he did":
                    $ fian = "worried"
                    $ falison = "mad"
                    scene hotel
                    show iannude at lef
                    show alisonnude at rig
                    with long

                    $ v9askanalalison = True
                "No, he didn't":
                    scene v9_alison19
                    with long
                    pause 1

                    $ v9askanalalison = False
                    $ v8_alison_sext = 3

            scene blackbg
            with long

            $ fian = "confident"
            $ falison = "n"
            $ fjeremy = "happy"
            $ ian_look = 2
            $ jeremy_look = 1

            scene alisonhome
            with long
            show alisonnude at rig3
            show ianunder
            show jeremy at lef3
            with short
            menu:
                gal "Did Ian and Alison have a threesome with Jeremy?"
                "Yes, they did":
                    scene v10_alison6b
                    show v10_alison6b_condom
                    with long
                    pause (2)
                    $ alison_jeremy_3some = 2

                "No, they didn't":
                    $ alison_jeremy_3some = 0

            scene blackbg
            with long

            if alison_jeremy_3some == 2 or ian_alison_dom or ian_alison_dating == False:
                if ian_alison_dating:
                    $ alison_blonde = 3
                else:
                    $ alison_blonde = 2

            scene alisonhomenight
            with long
            show iannude at lef
            show alisonnude at rig
            with short
            menu:
                gal "Did Ian agree to wear a condom the last time they had sex?"
                "Yes, he did":
                    scene v11_alison1_animation 
                    show v11_alison1_animation_condom
                    play sound "sfx/oh1.mp3"
                    with long
                    pause 4

                    $ v11_alison_condom = True

                "No, he didn't":
                    scene v11_alison3_animation 
                    if alison_blonde:
                        show v11_alison2_blonde
                    with long
                    play sound "sfx/bj6.mp3"
                    pause 4

            scene blackbg
            with long

            if ian_alison_love:
                $ fian = "n"

                scene mall
                with long
                show ian
                with short
                menu:
                    gal "Did Ian buy a gift for Alison?"
                    "{image=icon_pay.webp} Yes, he did":
                        $ fian = "smile"
                        $ v12_gift = "alison"
                        pause(1)
                    "No, he didn't":
                        pass
                scene blackbg
                with long

        "No, he was not":
            $ fian = "smile"
            $ ian_look = 1
            scene ianroomnight
            show ian at left
            with short
            show v4_alison_jeremy
            with long
            pause (1)

            $ v5_alison_jeremy = True
            $ v9_alison_trip = False
            $ alison_voyeur = True
            $ v11_alison_voyeur = True

            scene blackbg
            with long

            $ fian = "surprise"
            $ falison = "blush"
            $ fjeremy = "happy"
            $ ian_look = 1

            scene alisonhome
            with long
            show ian at lef3
            show alisonnude
            show jeremynude at rig3
            with short
            menu:
                gal "Did Ian participate in a threesome with Alison and Jeremy?"
                "Yes, he did":
                    scene v10_alison2
                    with long
                    pause (2)

                    $ ian_alison_fuck = True
                    $ ian_alison_sex = True
                    $ alison_jeremy_3some = 2

                "No, he didn't":
                    scene blackbg
                    with long
                    gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
                    jump CH12_S04

            if alison_jeremy_3some == 2 or ian_alison_dom or ian_alison_dating == False:
                if ian_alison_dating:
                    $ alison_blonde = 3
                else:
                    $ alison_blonde = 2

    scene blackbg
    with long

    # no music

    $ fian = "n"
    $ ian_look = 2

    scene mall
    with long
    show ian
    with short
return

label setup_CH12_S05:
    scene blackbg
    with long
    menu:
        gal "Do you want to do a quick replay or a custom one?"
        "Quick replay":
            $ stalkfap_pro = 2

            $ ian_lena_dating = True
            $ ian_lena_love = True
            $ ian_lena_couple = True

            $ v10_stalkfap = "ian"
            $ v10_stalkfap_facial = True
            $ ian_stalkfap_on = 2

            $ v10_stalkfap_anal = 3

            $ v10_stalkfap_dildo = 2
            $ v10_stalkfap_dildo_action = True

            $ flena = "shy"

            scene lenaroom
            with long
            show lenanude2
            with short
            gal "Which outfit did Lena decide to wear for the shoot?"
            hide lenanude2
            with short
            call screen v10lingerie
            $ flena = "flirtshy"
            if lena_look == "udw2":
                $ v10_shoot_look = 0
            elif lena_look == "bunny":
                $ v10_shoot_look = "bunny"
            else:
                $ v10_shoot_look = "lingerie"
            show lenabra2
            with long
            pause(2)

            scene blackbg
            with long

        "Custom replay":
            $ flena = "flirtshy"

            scene lenaroom
            with long
            show lenanude at right
            show v5_stalkfap1_comp
            with short
            menu:
                gal "Was Lena putting in extra effort on Stalkfap?"
                "Yes, she was sending custom videos":
                    show v9_stalkfap5
                    with long
                    pause (2)

                    $ stalkfap_pro = 2

                "Yes, she was posting naughtier content":
                    show v9_stalkfap1
                    if lena_tattoo1:
                        show v9_stalkfap1_t1
                    if lena_tattoo2:
                        show v9_stalkfap1_t2
                    if lena_tattoo3:
                        show v9_stalkfap1_t3
                    if lena_piercing1:
                        show v9_stalkfap1_p1
                    elif lena_piercing2:
                        show v9_stalkfap1_p2
                    with long
                    pause (2)

                    $ stalkfap_pro = 1

                "No, she wasn't":
                    $ stalkfap_pro = 0

            scene blackbg
            with long

            $ flena = "n"
            $ fian = "n"
            $ ian_look = 2
            $ lena_look = 4

            scene parknight
            with long
            show ian at left
            show lena at right
            with short
            menu:
                gal "Describe the relationship between Ian and Lena"
                "{image=icon_ring.webp}They are a devoted couple":
                    $ ian_lena_dating = True
                    $ ian_lena_love = True
                    $ ian_lena_couple = True

                    $ v10_stalkfap = "ian"
                    $ v10_stalkfap_facial = True
                    $ ian_stalkfap_on = 2

                "{image=icon_love.webp}They love each other":
                    $ ian_lena_dating = True
                    $ ian_lena_love = True

                    $ ian_stalkfap_on = 2

                "{image=icon_lust.webp}They hook up occasionally":
                    $ ian_lena_dating = True

                "They are just friends":
                    pass

            scene blackbg
            with long

            $ flena = "shy"

            scene lenaroom
            with long
            show lenanude2
            with short
            gal "Which outfit did Lena decide to wear for the shoot?"
            hide lenanude2
            with short
            call screen v10lingerie
            $ flena = "flirtshy"
            if lena_look == "udw2":
                $ v10_shoot_look = 0
            elif lena_look == "bunny":
                $ v10_shoot_look = "bunny"
            else:
                $ v10_shoot_look = "lingerie"
            show lenabra2
            with long
            pause(2)

            scene blackbg
            with long

            if not v10_stalkfap == "ian":
                menu:
                    gal "Did Lena invite someone to help her shoot content?"
                    "Yes, she invited Ian":
                        $ v10_stalkfap = "ian"
                        $ v10_stalkfap_facial = True
                    "Yes, she invited Mike":
                        $ v10_stalkfap = "mike"
                    "Yes, she invited Stan":
                        $ v10_stalkfap = "stan"

                if v10_shoot_look == "bunny":
                    scene v10_shoot1b
                    show v10_shoot1_face
                    if lena_tattoo1:
                        show v10_shoot1_t1
                    if lena_tattoo3:
                        show v10_shoot1_t3
                elif v10_shoot_look == "lingerie":
                    scene v10_shoot1c
                    if lena_tattoo1:
                        show v10_shoot1c_t1
                    if lena_tattoo3:
                        show v10_shoot1c_t3
                else:
                    scene v10_shoot1a
                    if lena_tattoo1:
                        show v10_shoot1_t1
                    if lena_tattoo3:
                        show v10_shoot1_t3
                if lena_piercing1:
                    show v10_shoot1_p1
                elif lena_piercing2:
                    show v10_shoot1_p2
                if v10_stalkfap == "ian":
                    show v10_shoot1_ian2
                elif v10_stalkfap == "mike":
                    show v10_shoot1_mike
                elif v10_stalkfap == "stan":
                    show v10_shoot1_stan
                with long
                pause (2)

                scene blackbg
                with long

            $ flena = "slutshy"

            scene lenaroom
            with long
            show lenabra2 at right
            show toy_plug1
            with short
            menu:
                gal "Did Lena use the butt plug?"
                "Yes, she did":
                    $ v10_stalkfap_anal = 3

                    if lena_look == "black_lingerie":
                        scene v10_shoot3c
                    elif lena_look == "bunny":
                        scene v10_shoot3b
                    else:
                        scene v10_shoot3a
                    show v10_shoot3_plug
                    if lena_tattoo3:
                        show v10_shoot3_t3
                    with long
                    pause 2

                "No, she didn't":
                    pass

            scene blackbg
            with long

            if lena_look == "black_lingerie":
                scene v10_shoot6c
                if lena_tattoo3:
                    show v10_shoot5c_t3
            else:
                if lena_look == "bunny":
                    scene v10_shoot6b
                else:
                    scene v10_shoot6a
                if lena_tattoo3:
                    show v10_shoot5c_t3
            if lena_tattoo2:
                show v10_shoot5_t2
            if lena_piercing1:
                show v10_shoot5_p1
            elif lena_piercing2:
                show v10_shoot5_p2
            with long
            menu:
                gal "Which dildo did Lena use during her shoot?"
                "The badboy (large)":
                    $ v10_stalkfap_dildo = 2
                    $ v10_stalkfap_dildo_action = True

                    if lena_look == "black_lingerie":
                        scene v10_shoot7c
                        if lena_tattoo1:
                            show v10_shoot5c_t1
                        if lena_tattoo3:
                            show v10_shoot5c_t3
                    else:
                        if lena_look == "bunny":
                            scene v10_shoot7b
                        else:
                            scene v10_shoot7a
                        if lena_tattoo1:
                            show v10_shoot5_t1
                        if lena_tattoo3:
                            show v10_shoot5c_t3
                    if lena_tattoo2:
                        show v10_shoot5_t2
                    if lena_piercing1:
                        show v10_shoot5_p1
                    elif lena_piercing2:
                        show v10_shoot5_p2
                    show v10_shoot7_dildo2
                    with long
                    pause 1
                "The normal dildo":
                    $ v10_stalkfap_dildo = 1
                    $ v10_stalkfap_dildo_action = True

                    if lena_look == "black_lingerie":
                        scene v10_shoot7c
                        if lena_tattoo1:
                            show v10_shoot5c_t1
                        if lena_tattoo3:
                            show v10_shoot5c_t3
                    else:
                        if lena_look == "bunny":
                            scene v10_shoot7b
                        else:
                            scene v10_shoot7a
                        if lena_tattoo1:
                            show v10_shoot5_t1
                        if lena_tattoo3:
                            show v10_shoot5c_t3
                    if lena_tattoo2:
                        show v10_shoot5_t2
                    if lena_piercing1:
                        show v10_shoot5_p1
                    elif lena_piercing2:
                        show v10_shoot5_p2
                    show v10_shoot7_dildo1
                    with long
                    pause 1
                "She didn't use any":
                    $ v10_stalkfap_dildo = 0
            scene blackbg
            with long

    play music "music/calm.mp3" loop

    if ian_lena_dating:
        $ fian = "confident"
    else:
        $ fian = "n"
    $ ian_look = 2

    scene ianroomnight with long
    show ian with short
return

label setup_CH12_S06:
    scene blackbg
    with long

    call gallVar_ian_chad from _call_gallVar_ian_chad_3

    $ fian = "confident"
    $ fjess = "n"
    $ ian_look = 2
    $ jess_look = 2

    # no music

    scene ianhomenight
    with long
    show ian at lef
    show jessb at rig
    with short
    i "I know that's not why you're here, but since you're spending the night here... It would be such a shame to not share the bed with you."
    "This was a chance I couldn't let slip past me... I was determined to see this through."
return

################################################################################
## CHAPTER 12b #################################################################
################################################################################

label setup_CH12_S07:
    scene blackbg
    with long

    $ fivy = "flirt"
    $ flena = "slutshy"
    $ fholly = "blush"

    $ lena_look = "charisma"
    $ lena_necklace = "seymour"
    $ lena_makeup = 2
    $ ivy_look = "sexy"
    $ holly_look = 2
    $ holly_glasses = True

    scene blazer
    with long
    show holly3 at rig3
    show ivy at left
    show lena at right
    with long

    show v7_mark
    with short
    menu:
        gal "How did Lena react when Ivy introduced Mark to Holly?"
        "She enticed Holly to let her inner slut out":
            $ holly_guy = 4

            scene blazer_wc
            show lena at right
            show ivy2 at left
            show v10_holly_mark
            with long
            pause (2)

        "She encouraged Holly":
            $ holly_guy = 2

            scene blackbg
            with long

            $ flena = "surprise"
            $ fivy = "flirt"

            $ ivy_look = "dress"
            $ lena_look = "black_dress"
            $ lena_makeup = 2
            $ lena_necklace = "seymour"
            $ lena_extras = "black_dress"
            $ ivy_extras = "bag"

            scene blazer_wc
            with long
            show lena at right
            show ivy2 at left
            with short

            show v10_holly_mark
            with short
            menu:
                gal "How did Lena react when Ivy showed her proof of Holly blowing Mark?"
                "She was supportive":
                    $ holly_guy = 3
                    $ flena = "flirtshy"
                    pause (2)

                "She didn't like it":
                    pass

        "She let Holly decide":
            $ holly_guy = 1

        "She protected Holly":
            $ holly_guy = 0

    $ lena_extras = 0
    $ lena_makeup = 0
    $ lena_necklace = 0
    $ ivy_extras = 0

    scene blackbg
    with long

    $ fholly = "smile"
    $ flena = "smile"
    $ fivy = "n"
    $ lena_look = 4
    $ lena_makeup = 1
    $ holly_look = 1
    $ ivy_look = 1

    scene ivyroomnight
    with long
    show lena at rig3
    show holly at lef3
    show ivy
    with short
    menu:
        gal "Did Holly have sex with one of the girls?"
        "Yes, with Lena":
            $ lena_holly_sex = True
            $ v8_holly_sex = "lena"
            scene v8_holly3
            if lena_tattoo2:
                show v8_holly3_t2
            if lena_tattoo3:
                show v8_holly3_t3
            with long
            pause (2)

        "Yes, with Lena and Ivy":
            $ v8_holly_sex = "lenaivy"
            scene v8_ivy8
            if lena_tattoo1:
                show v8_ivy8_t1
            if lena_tattoo2:
                show v8_ivy8_t2
            if lena_tattoo3:
                show v8_ivy8_t3
            if lena_piercing1:
                show v8_ivy8_p1
            elif lena_piercing2:
                show v8_ivy8_p2
            with long
            with long
            pause (2)

        "Yes, with Ivy":
            $ v8_holly_sex = "ivy"
            scene v8_ivy4
            with long
            pause (2)

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_makeup = 0

    if lena_holly_sex or (v10_lena_holly_sex and v8_holly_sex != "ivy" and v8_holly_sex != "lenaivy"):
        $ lena_holly_dating = True

    if holly_guy < 1:
        if lena_holly_sex and v8_holly_sex != "ivy" and v8_holly_sex != "lenaivy":
            $ lena_look = 4
            $ flena = "blush"
            $ fholly = "worried"
            $ holly_look = "summer"
            $ holly_glasses = True

            scene cafeteria 
            with long
            show lena at rig
            show holly3 at lef
            with short
            menu:
                gal "Was Lena in love with Holly?"
                "{image=icon_love.webp} Yes, she was":
                    $ lena_holly_love = True
                    $ flena = "n"
                    $ fholly = "blush"
                    pause (1)

                "No, she wan't":
                    $ flena = "worried"

            scene blackbg
            with long

    if holly_guy > 1:
        $ fivy = "flirt"
        $ flena = "sad"
        $ fholly = "blush"

        $ lena_look = 2
        $ lena_makeup = 0
        $ ivy_look = 2
        $ holly_look = 4
        $ holly_glasses =  False

        scene polegym
        with long
        show lena at rig3
        show ivy at lef3
        show holly3
        with short
        menu:
            gal "Did Lena introduce Holly to Robert?"
            "Yes, she did":
                $ lena_robert_sex = True
                $ holly_robert = True
                $ flena = "n"
            "No, she didn't":
                pass

        scene blackbg
        with long

    if v8_holly_sex == "ivy" or v8_holly_sex == "lenaivy":
        $ holly_ivy = True

        scene v11_shower1
        with long
        menu:
            gal "Did Lena join the fun?"
            "Yes, she did":
                scene v11_shower2b
                if lena_tattoo1:
                    show v11_shower2_t1
                if lena_tattoo2:
                    show v11_shower2_t2b
                if lena_tattoo3:
                    show v11_shower2_t3
                if lena_piercing1:
                    show v11_shower2_p1
                elif lena_piercing2:
                    show v11_shower2_p2
                with long
                pause (2)

                $ v11_shower_sex = "3some"

            "No, she didn't":
                pass

    else:
        $ flena = "blush"
        $ fholly = "worried"
        $ fivy = "flirt"
        scene gymshowers
        show ivynude2
        show hollynude2 at lef3
        show holly_towel at lef3
        show lenanude2 at rig3
        with long
        menu:
            gal "Did Lena make Holly join her and Ivy in the shower?"
            "Yes, she did":
                play sound "sfx/shower.mp3"
                scene v11_shower4
                if lena_tattoo3:
                    show v11_shower4_t3
                with long
                pause (2)

                $ holly_ivy = True
                $ v11_shower_sex = "3some"

            "No, she didn't":
                pass

    scene blackbg
    with long

    if ian_holly_dating == False and lena_holly_sex == False and lena_go_holly < 4:
        $ holly_clark = True

    if holly_ivy == False and holly_guy < 2 and holly_robert == False: # req for holly_slut
        gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
        jump setup_CH12_S07

    call gallVar_lena_smoke from _call_gallVar_lena_smoke

    $ flena = "n"
    $ lena_look = 1

    play music "music/calm.mp3" loop

    scene lenaoldroom
    with long
    if lena_smoke:
        show lenabra_smoke
    else:
        show lenabra
    with short

    play sound "sfx/sms.mp3"
    nvl clear
return

label setup_CH12_S08:
    scene blackbg
    with long

    call gallVar_toy_badboy

    $ flena = "flirtshy"

    scene lenaroom
    with long
    show lenanude at right
    show v5_stalkfap1_comp
    with short
    menu:
        gal "Was Lena putting in extra effort on Stalkfap?"
        "Yes, she was sending custom videos":
            show v9_stalkfap5
            with long
            pause (2)

            $ stalkfap_pro = 2
        "Yes, she was posting naughtier content":
            show v9_stalkfap1
            if lena_tattoo1:
                show v9_stalkfap1_t1
            if lena_tattoo2:
                show v9_stalkfap1_t2
            if lena_tattoo3:
                show v9_stalkfap1_t3
            if lena_piercing1:
                show v9_stalkfap1_p1
            elif lena_piercing2:
                show v9_stalkfap1_p2
            with long
            pause (2)

            $ stalkfap_pro = 1
        "No, she wasn't":
            $ stalkfap_pro = 0

    scene blackbg
    with long

    $ louise_look = 1
    $ lena_look = 1

    $ flena = "smile"
    $ flouise = "n"

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
    menu:
        gal "Has Lena fucked Jeremy?"
        "Yes, she woke him up after Louise was gone":
            $ lena_jeremy_dating = True
            scene v8_jeremy6b
            with long
            pause (2)
        "Yes, she had a threesome with him and Louise":
            $ lena_jeremy_dating = True
            scene v10_jeremy8b
            with long
            pause (2)
        "No, she hasn't":
            pass

    scene blackbg
    with long

    scene studio_black
    with long
    show v6_seymour0
    with short
    menu:
        gal "Was Lena working with Seymour?"
        "Yes, she was":
            $ seymour_desire = True
            $ toy_wand = True

            scene blackbg
            with long

            $ flena = "smile"
            $ fseymour = "smile"
            $ lena_look = "wits"
            $ seymour_look = 1
            scene seymourofficenight
            with long
            show seymour2 at lef
            show lena2 at rig
            with short
            menu:
                gal "Does Lena like working for Seymour?"
                "She obeys him":
                    $ seymour_disposition = 3
                    $ v9_seymour_orgasm = True
                "Yes, she does":
                    $ seymour_disposition = 2
                    $ v9_seymour_orgasm = True
                    $ fseymour = "n"
                "No, she doesn't":
                    $ seymour_disposition = 0
                    $ fseymour = "n"
                    $ flena = "worried"
        "No, she wasn't":
            scene blackbg
            with long

            $ flena = "flirt"
            $ femma = "smile"
            $ emma_look = 1
            $ lena_look = 4
            
            scene sexshop
            with long
            show emma at left
            show lena at right
            show toy_wand
            with short
            menu:
                gal "Did Lena buy the vibrating wand?"
                "{image=icon_pay.webp} Yes, she did":
                    $ flena = "slut"
                    $ toy_wand = True

                "No, she didn't":
                    $ flena = "n"
                    pass

    scene blackbg
    with long

    $ lena_look = 4
    $ flena = "n"

    scene mall
    with long
    show lena
    with short
    gal "Which dress did Lena buy for her night bartending at the club?"
    show lena at left
    with move
    call screen screen_choice(v11buydress)
    $ v11_lena_dress = _return

    scene blackbg
    with long

    scene lenaroomnight
    with long
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    show lena2 
    with short
    if v11_lena_dress == 1:
        l "There... This dress was definitely the right choice."
    elif v11_lena_dress == 2:
        l "There... Even though it's cheap, this dress looks really fancy! I love it."
    elif v11_lena_dress == 3:
        l "There... This dress is as comfortable as I expected. Perfect for tonight."
    elif v11_lena_dress == 4:
        l "There... Tonight I'll be the woman in red! I feel so sexy."
    menu galCH12S08dressprepare:
        "{image=icon_charisma.webp}Wear jewelry" if lena_necklace != "choker2":
            l "I need some jewelry to complete the look. Something simple should do."
            show lena_choker2 with short
            pause 1
            $ lena_necklace = "choker2"
            hide lena_choker2
            jump galCH12S08dressprepare

        "{image=icon_lust.webp}Wear stockings" if lena_extras != "stockings":
            $ flena = "flirt"
            l "Let me try fishnet stockings with this look..."
            show lena_lust1_stockings with short
            pause 1     
            $ lena_extras = "stockings"
            hide lena_lust1_stockings
            $ flena = "n"
            jump galCH12S08dressprepare

        "On second thought..." if lena_necklace == "choker2" or lena_extras == "stockings":
            $ flena = "sad"
            l "On second thought... I'm not convinced. Let's try something else."
            hide lena2 with short
            $ flena = "n"
            $ lena_necklace = 0
            $ lena_extras = 0
            show lena2 with short
            jump galCH12S08dressprepare

        "Ready":
            $ flena = "n"
            l "Alright, I'm ready."

    scene blackbg
    with long

    scene street2night
    with long
    show marcel at left5
    show jeremy at lef3
    show lena at rig3
    with short
    menu:
        gal "Did Lena suck off Marcel or Jeremy behind the club?"
        "Yes, Marcel":
            $ v11_bbc = "marcel"
            scene v11_bbc3_marcel
            if v11_lena_dress == 2:
                show v11_bbc3_charisma
            elif v11_lena_dress == 4:
                show v11_bbc3_lust
            if lena_necklace == "choker2":
                show v11_bbc3_choker
            if lena_tattoo2:
                show v11_bbc3_t2
            with long
            play sound "sfx/bj1.mp3"
            pause (2)
        "Yes, Jeremy":
            $ v11_bbc = "jeremy"
            scene v11_bbc3
            if v11_lena_dress == 2:
                show v11_bbc3_charisma
            elif v11_lena_dress == 4:
                show v11_bbc3_lust
            if lena_necklace == "choker2":
                show v11_bbc3_choker
            if lena_tattoo2:
                show v11_bbc3_t2
            with long
            play sound "sfx/bj1.mp3"
            pause (2)
        "No, she didn't":
            pass

    if v11_bbc == "marcel" or v11_bbc == "jeremy":
        menu:
            gal "Did she take pictures of the deed?"
            "Yes, she did":
                $ v11_bbc_pic = True
                if v11_bbc == "jeremy":
                    scene v11_bbc1
                    if v11_lena_dress == 2:
                        show v11_bbc1_charisma
                    elif v11_lena_dress == 4:
                        show v11_bbc1_lust
                    if lena_tattoo2:
                        show v11_bbc1_t2
                    if lena_necklace == "choker2":
                        show v11_bbc1_choker
                    with long
                    pause (2)

                else:
                    scene v11_bbc1_marcel
                    if v11_lena_dress == 2:
                        show v11_bbc1_charisma
                    elif v11_lena_dress == 4:
                        show v11_bbc1_lust
                    if lena_necklace == "choker2":
                        show v11_bbc1_choker
                    if lena_tattoo2:
                        show v11_bbc1_t2
                    with long
                    pause (2)

            "No, she didn't":
                pass
    scene blackbg
    with long

    $ flena = "sad"
    $ faxel = "smile"
    $ axel_look = 2

    scene blazer
    with long
    show axel at lef
    show lena at rig
    with short
    menu:
        gal "Did Lena hook up with Axel at the club?"
        "Yes, they fucked":
            $ lena_axel_desire = 2
            $ v9_axel_sex = True
            play sound "sfx/oh1.mp3"
            scene v11_axel6_animation with fps
            pause (2)

        "Yes, she blew him":
            $ lena_axel_desire = 1
            $ v9_axel_sex = True
            play sound "sfx/gag1.mp3"
            scene v11_axel5_animation1 with fps
            pause (2)

        "No, she didn't":
            scene blackbg
            with long

            $ flena = "slut"
            $ fjack = "smile"

            scene blazer
            with long
            show lena at rig
            show jack at lef
            with short
            menu:
                gal "Did Lena hook up with Jack in the club?"
                "Yes, she fucked him":
                    $ lena_jack = 4
                    scene v11_jack6a
                    if lena_necklace == "choker2":
                        show v11_jack6_earrings
                    if v11_lena_dress == 2:
                        show v11_jack6b
                    elif v11_lena_dress == 3:
                        show v11_jack6c
                    elif v11_lena_dress == 4:
                        show v11_jack6d
                    if lena_tattoo1:
                        show v11_jack6_t1
                    if lena_tattoo2:
                        show v11_jack6_t2
                    if lena_tattoo3:
                        show v11_jack6_t3
                    if lena_extras == "stockings":
                        show v11_jack6_stockings 
                    with long
                    pause (2)

                "Yes, she blew him":
                    $ lena_jack = 3
                    scene v11_jack4
                    if lena_necklace == "choker2":
                        show v11_jack4_earrings
                    show v11_jack4_dress
                    with long
                    pause (2)

                "No, she didn't":
                    $ lena_jack = 0

    # no music

    scene blackbg
    with long

    $ lena_necklace = 0
    $ lena_extras = 0
    $ lena_makeup = 0
    $ lena_look = 1

    $ flena = "flirtshy"

    scene lenaoldroom 
    with long
    show lenabra
    with short
return

label setup_CH12_S09:
    scene blackbg
    with long

    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_2

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple":
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

            $ ian_lena_love = True
            $ lena_ian_love = 1

            $ lena_cheating =  True

        "They were just seeing each other":
            $ ian_lena_dating = True
            $ ian_lena_love = True

            $ lena_ian_love = 1

        "They are just friends":
            pass

    scene blackbg
    with long


    $ flena = "sad"
    $ faxel = "smile"
    $ axel_look = 2
    $ v11_lena_dress = 2
    $ lena_makeup = 1
    $ lena_look = "clubdress"
    $ lena_necklace = "choker2"
    $ lena_extras = "stockings"

    scene blazer
    with long
    show axel at lef
    show lena at rig
    with short
    menu:
        gal "Did Lena hook up with Axel at the club?"
        "Yes, they fucked":
            $ lena_axel_desire = 2
            play sound "sfx/oh1.mp3"
            scene v11_axel6_animation with fps
            pause (2)

        "Yes, she blew him":
            $ lena_axel_desire = 1
            play sound "sfx/gag1.mp3"
            scene v11_axel5_animation1 with fps
            pause (2)

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_makeup = 0
    $ lena_necklace = False
    $ lena_extras = False

    call gallVar_lena_cheating_decision from _call_gallVar_lena_cheating_decision

    if lena_lust > 7 or stalkfap_pro:
        $ lena_look = "summer"
        $ lena_makeup = 1
        if lena_lust > 8 or stalkfap_pro > 1:
            $ lena_necklace = "choker2"
    else:
        $ lena_look = 4
    $ flena = "n"

    $ faxel = "smile"
    $ axel_look = 1

    # no music

return

label setup_CH12_S10:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym_3

    $ fholly = "blush"
    $ fian = "sad"
    $ holly_look = "summer"
    if v11_holly_change:
        $ holly_glasses = 2
    else:
        $ holly_glasses = True
    $ ian_look = 2

    scene ianhomenight 
    with long
    show holly2 at rig
    show ian at lef
    with short
    menu:
        gal "Did Ian accept his feelings for Holly and open up to her?"
        "Yes, he did":
            $ ian_holly_love = True

        "No, he didn't":
            pass
    scene blackbg
    with long

    scene v11_holly8 
    with long
    menu:
        gal "Did Ian encourage Holly to be bolder?"
        "Yes, he did":
            $ v11_holly_fuck = True
            scene v11_holly9_animation1 with fps
            play sound "sfx/moanlong.mp3"
            pause (2)

        "No, he didn't":
            pass
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look

    # no music

    if v11_holly_change:
        $ holly_glasses = 2
    else:
        $ holly_glasses = True
    if v11_holly_change:
        $ holly_hair = 2
    if v11_holly_change and holly_gym:
        $ holly_fit = True
    $ holly_look = "summer"
    $ fholly = "smile"
    $ fian = "smile"
return

label setup_CH12_S11:
    scene blackbg
    with long

    call gallVar_ian_chad from _call_gallVar_ian_chad_4

    $ lena_bikini = 2
    call gallVar_emma_bikini from _call_gallVar_emma_bikini

    $ fperry = "n"
    $ femma = "n"
    $ fian = "smile"
    $ fwade = "smile"
    $ fholly = "smile"
    $ holly_look = "summer"
    $ emma_look = "summer"
    $ perry_look = "summer"

    scene summerhouse
    with long
    show perry at right 
    show wade at left
    show emma at lef3
    show holly at centerlef
    show ian at rig
    with short
    menu:
        gal "Who was Ian sharing a room with?"
        "With Emma":
            $ v12_room = "emma"
            $ fian = "confident"
            $ femma = "flirt"
            $ fholly = "n"
            $ fperry = "sad"
        "With Wade":
            $ v12_room = "wade"
            $ fwade = "happy"
            $ fperry = "blush"
        "With Holly":
            $ v12_room = "holly"
            $ fholly = "shy"
            $ fperry = "sad"
        "With Lena":
            $ v12_room = "lena"
            $ fperry = "sad"
    pause (1)

    scene blackbg
    with long

    $ fian = "n"
    $ ian_look = 3
    $ emma_look = 1
    if ian_emma_sex or emma_bikini:
        $ emma_hair = "pink"
    else:
        $ emma_hair = 2
    scene summerroom
    with long

    # no music
return

label setup_CH12_S12:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    $ ivy_look = 2
    $ fivy = "n"
    $ lena_look = 2
    $ flena = "smile"
    $ holly_look = 3
    $ holly_glasses = False
    $ fholly = "smileshy"

    scene polegym
    with long
    show lena at rig
    show ivy at lef
    with short
    menu:
        gal "Did Holly join Lena and Ivy in pole dancing?"
        "Yes, she did":
            show ivy at lef3
            show lena at rig3
            with move
            show holly3
            with short
            pause (2)

            scene blackbg
            with long

            $ holly_gym = True
            if v11_holly_change:
                $ holly_fit = True

            $ holly_look = 5
            $ holly_glasses = 2
            $ fholly = "smile"

            $ lena_look = "black_dress"
            $ flena = "happy"
            $ lena_makeup = 2
            $ lena_extras = "black_dress"

            $ ivy_look = "dress"
            $ ivy_extras = "bag"

            $ fholly = "smile"
            $ flena = "smile"
            $ fivy = "n"
            scene blazer
            with long
            show ivy2
            show holly at lef3
            show lena at rig3
            with short
            menu:
                gal "Did Ivy and Lena encourage Holly to hook up with guys?"
                "Yes, they did":
                    $ holly_slut = True
                    scene blazer_wc
                    show v10_holly_mark
                    with long
                    pause (2)

                "No, they didn't":
                    pass

        "No, she didn't":
            pass

    scene blackbg
    with long

    # no music

    $ holly_hair = 1
    $ holly_look = "bikini"
    if holly_slut: #ToDO glasses, issue raised
        $ holly_glasses = False
    else:
        $ holly_glasses = True
    $ ian_look = "swim"
    $ emma_look = "bikini"
    $ perry_glasses = False
    $ perry_look = "swim"
    
return

label setup_CH12_S13:
    scene blackbg
    with long

    $ flena = "smile"
    $ lena_look = 1
    $ fian = "smile"
    $ ian_look = 3
    $ fholly = "n"

    scene park
    with long
    show ian at lef3
    show holly3
    show lena2 at rig3
    with short
    menu:
        gal "Was Ian dating Holly or Lena?"
        "Yes, he was a couple with Lena":
            hide holly3
            with short
            $ flena = "blush"
            $ fian = "blush"
            show lena at lef
            show ian at rig
            with move

            $ ian_lena_couple = True
            $ ian_lena_love = True
            $ ian_lena_dating = True

        "Yes, he was dating Holly":
            hide lena2
            with short
            $ fholly = "blush"
            $ fian = "blush"
            show holly3 at lef
            show ian at rig
            with move

            $ ian_holly_dating = True

        "No, he wasn't":
            pass

    scene blackbg
    with long

    scene v5_emma1
    with long
    menu:
        gal "Were Ian and Emma hooking up before the trip?"
        "Yes, they were":
            scene v5_emma7_animation
            with long
            pause(2)

            $ ian_emma_sex = True

            scene blackbg
            with long

            if not ian_holly_dating:
                $ femma = "flirt"
                $ fian = "cofident"
                $ emma_look = 4
                $ ian_look = 3

                scene summerroom
                with long
                show ianunder at lef
                show emmanude at rig
                menu:
                    gal "Did Ian and Emma have sex in the morning?"
                    "Yes, they did":
                        scene v12_emma7_animation with fps
                        pause (2)

                        $ v12_emma_sex1 = True

                    "No, they didn't":
                        pass

        "No, they weren't":
            pass

    scene blackbg
    with long

    call gallVar_v12_emma_topless from _call_gallVar_v12_emma_topless

    $ ian_look = "swim"
    $ emma_look = "bikini"
    if ian_emma_sex or emma_bikini:
        $ emma_hair = "pink"
    else:
        $ emma_hair = 2
    $ femma = "n"
    $ fian = "n"

    play music "music/normal_day5.mp3" loop

    scene v12_holly_beach1b
    show v12_holly_beach1_book
    with long
return

label setup_CH12_S14:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No":
            hide holly3
            with short
            $ holly_look = "summer"
            $ holly_change = 0
            show holly3
            with short

    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym_4

    $ ian_look = "swim"
    $ holly_glasses = False
    $ holly_hair = 1
    if v11_holly_change and holly_gym:
        $ holly_fit = True
    $ holly_look = "bikini"

    $ fholly = "n"
    $ fian = "sad"
    scene beach
    show ian at lef
    show holly at left
    with short

    play music "music/normal_day5.mp3" loop

return

label setup_CH12_S15:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    scene v11_holly8 
    with long
    menu:
        gal "Did Ian encourage Holly to be bolder?"
        "Yes, he did":
            $ v11_holly_fuck = True
            scene v11_holly9_animation1 with fps
            play sound "sfx/moanlong.mp3"
            pause (2)

        "No, he didn't":
            pass
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_1

    play music "music/date.mp3" loop

    #if v11_holly_change: #ToDO glasses, issue raised
    #    $ holly_glasses = 2
    #else:
    #    $ holly_glasses = True
    if v11_holly_change or holly_slut:
        $ holly_hair = 2
    $ holly_look = "summer"

    $ fholly = "smile"
    $ fian = "smile"

    scene summerroom
    with long
    show ian at lef
    show holly at rig
    with short

return

label setup_CH12_S16:
    scene blackbg
    with long

    $ ian_look = "lust1"
    $ fian = "confident"

    scene ianroom
    with long
    show ian at lef2
    with short
    menu:
        gal "How high was Ian's lust?"
        "Level 6 or more":
            $ ian_lust = 10

        "Level 6":
            $ ian_lust = 6

        "Level 5 or lower":
            $ ian_lust = 5

    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_5

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

        "They were just friends" if ian_lena_sex == False:
            gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
            jump setup_CH12_S16

    scene blackbg
    with long

    call gallVar_ian_lena_love from _call_gallVar_ian_lena_love_3
    call gallVar_lena_ian_love from _call_gallVar_lena_ian_love_1

    call gallVar_ian_lena_dom from _call_gallVar_ian_lena_dom_3

    call gallVar_ian_cheating from _call_gallVar_ian_cheating

    call gallVar_ian_cuck from _call_gallVar_ian_cuck_1

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_2

    call gallVar_ian_cheating_decision from _call_gallVar_ian_cheating_decision
    call gallVar_lena_cheating_decision from _call_gallVar_lena_cheating_decision_1

    call gallVar_ian_lena_crisis from _call_gallVar_ian_lena_crisis

    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look

    play music "music/sex_chill.mp3" loop

    # no scene
return

label setup_CH12_S17:
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_3

    call gallVar_ian_emma_love from _call_gallVar_ian_emma_love

    if ian_emma_sex or emma_bikini:
        $ emma_hair = "pink"
    else:
        $ emma_hair = 2

    # no music
return

label setup_CH12_S18:
    scene blackbg
    with long

    menu:
        gal "On which day is this scene taking place?"
        "On Sunday":
            $ day = "Sunday"
        "On Monday":
            $ day = "Monday"
    
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True
            $ holly_fit = True

            show holly
            with short

        "No":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    scene v11_holly8 
    with long
    menu:
        gal "Did Ian encourage Holly to be bolder?"
        "Yes, he did":
            $ v11_holly_fuck = True
            scene v11_holly9_animation1 with fps
            play sound "sfx/moanlong.mp3"
            pause (2)

        "No, he didn't":
            pass
    scene blackbg
    with long

    if day == "Monday":
        $ fian = "n"
        $ ian_look = 2

        scene mall
        with long
        show ian
        with short
        menu:
            gal "Did Ian buy a gift for Holly?"
            "{image=icon_pay.webp} Yes, he did":
                $ fian = "smile"
                $ v12_gift = "holly"
                pause(1)

            "No, he didn't":
                pass

        scene blackbg
        with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_4

    $ ian_look = "summer"
    $ holly_look = "summer"
    if v11_holly_change or holly_slut:
        $ holly_hair = 2
    $ holly_glasses = False

    # no music

    if day == "Monday":
        scene summerroomnight with long
        play sound "sfx/door.mp3"
        stop music fadeout 3.0
        show ian at lef
        show holly2 at rig
        with short
        "Holly sat on the bed and sighed."
        hide ian
        show ianunder at lef
        with short
        $ fholly = "flirt"
        i "Tired? A day at the beach really wears you out..."
        hide holly2
        show holly at rig
        with short
        h "I'm a bit tired, but I don't want to go to sleep yet..."
        show holly at centerrig with move
        "Holly stood up and placed her hands on my chest, staring into my eyes."
        jump v12hollysex3
    else:
        scene summerroomnight
        with long
return

label setup_CH12_S19:
    scene blackbg
    with long

    $ ian_look = "lust1"
    $ fian = "confident"

    scene ianroom
    with long
    show ian at lef2
    with short
    menu:
        gal "How high was Ian's lust?"
        "Level 6 or more":
            $ ian_lust = 10

        "Level 6":
            $ ian_lust = 6

        "Level 5 or lower":
            $ ian_lust = 5

    scene blackbg
    with long

    call gallVar_ian_lena_sex from _call_gallVar_ian_lena_sex_6

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

        "They were just friends" if ian_lena_sex == False:
            gal "Uh oh. Your choices ended up in a situation where this scene wouldn't have happened. Please try again."
            jump setup_CH12_S19

    scene blackbg
    with long

    call gallVar_ian_lena_love from _call_gallVar_ian_lena_love_4
    call gallVar_lena_ian_love from _call_gallVar_lena_ian_love_2

    call gallVar_ian_cheating from _call_gallVar_ian_cheating_1
    call gallVar_lena_cheating from _call_gallVar_lena_cheating_1

    call gallVar_ian_cuck from _call_gallVar_ian_cuck_2

    call gallVar_ian_lena_crisis from _call_gallVar_ian_lena_crisis_1

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_5

    call gallVar_ian_cheating_decision from _call_gallVar_ian_cheating_decision_1

    if ian_cheating != 1:
        $ v12_lena_sex1 = True

    call gallVar_lena_cheating_decision from _call_gallVar_lena_cheating_decision_2

    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_1

    # no music
    # no scene
return

label setup_CH12_S20:
    scene blackbg
    with long

    $ flena = "n"
    $ fian = "n"
    $ ian_look = 2
    $ lena_look = 4

    scene parknight
    with long
    show ian at left
    show lena at right
    with short
    menu:
        gal "Describe the relationship between Ian and Lena"
        "{image=icon_ring.webp}They are a devoted couple":
            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "{image=icon_lust.webp}/{image=icon_love.webp} They hook up occasionally / are dating":
            $ ian_lena_dating = True

        "They are just friends":
            pass

    if ian_lena_dating:
        scene blackbg
        with long

        $ fian = "surprise"
        $ ian_look = 2
        $ lena_look = "underwear2"
        $ flena = "slutshy"
        $ flouise = "blush"
        $ louise_look = 1

        scene lenahomenight
        with long
        show louisebra at lef3
        show lenabra at rig3
        show ian at truecenter
        with short
        menu:
            gal "Did Ian have a threesome with Lena and Louise?"
            "Yes, he did":
                $ v11_louise_3some = "ian"

                scene v11_3some5
                if lena_tattoo2:
                    show v11_3some5_t2
                if lena_tattoo1:
                    show v11_3some5_t1
                if lena_piercing1:
                    show v11_3some5_p1
                elif lena_piercing2:
                    show v11_3some5_p2
                with long
                pause (2)

            "No, he didn't":
                pass

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_6

    $ fian = "n"

    play music "music/calm.mp3" loop

    scene summerroom
    with long
    show ian
    with short
return

label setup_CH12_S21:
    scene blackbg
    with long

    $ fivy = "flirt"
    $ ivy_look = 2
    $ fian = "worried"
    $ ian_look = 8

    scene gym
    with long
    show wensmile at rig3
    show ian at lef3
    show ivy
    with short
    menu:
        gal "Did Ian agree to grapple with Ivy?"
        "Yes, and he won their impromptu match":
            $ v10_ivy_gym = 3
            scene v10_ivy_gym3
            with long
            pause (2)
        "Yes, but let go of the chokehold and lost":
            $ v10_ivy_gym = 2
            scene v10_ivy_gym4
            with long
            pause (2)
        "yes, but lost":
            $ v10_ivy_gym = 1
            scene v10_ivy_gym4
            with long
            pause (2)

        "No, he didn't":
            pass
    scene blackbg
    with long

    $ ivy_look = "sexy"
    $ ivy_extras = 0
    if v10_ivy_gym > 0:
        $ fivy = "flirt"
    else:
        $ fivy = "smile"
    $ ian_look = "charisma1"
    $ fian = "smile"

    scene streetnight
    with long
    show ivy2 at rig
    show ian at lef
    with short
    menu:
        gal "Did Ian flirt with Ivy after the gym?"
        "Yes, he did":
            $ v11_ivy_flirt = True
            $ fian = "confident"
            hide ivy2
            show ivy at rig
            with short
            $ fivy = "smile"
            call friend_xp ('ivy') from _call_friend_xp_1187

        "No, he didn't":
            $ fian = "n"
            $ fivy = "n"
            hide ivy2
            show ivy at rig
            with short
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_7

    $ fian = "n"

    play music "music/calm.mp3" loop

    scene summerroom
    with long
    show ian
    with short
return

label setup_CH12_S22:
    scene blackbg
    with long

    menu:
        gal "Do you want to do a quick replay or a custom one?"
        "Quick replay: Ian x Lena":
            $ lena_lust = 8

            $ ian_lena_sex = True
            $ ian_lena_dating = True
            $ ian_lena_couple = True

            $ stalkfap = False
            $ v10_tease_perry = False

            $ emma_bikini = True

            $ lena_cheating = False
            $ ian_cuck = False

            $ v12_emma_topless = False

            call gallVar_lena_bikini from _call_gallVar_lena_bikini_1

        "Quick replay: Lena x Wade":
            $ lena_lust = 8

            $ ian_lena_sex = True
            $ ian_lena_dating = True
            $ ian_lena_couple = True

            $ stalkfap = True
            $ stalkfap_pro = True
            $ v10_tease_perry = False

            $ emma_bikini = True

            $ lena_cheating = 2
            $ lena_axel_fuck = True
            $ ian_cuck = 2

            $ v12_emma_topless = 2

            call gallVar_lena_bikini from _call_gallVar_lena_bikini_2


        "Quick replay: Lena x Perry":
            $ lena_lust = 8

            $ ian_lena_sex = True
            $ ian_lena_dating = True
            $ ian_lena_couple = True

            $ stalkfap = True
            $ v10_tease_perry = True

            $ emma_bikini = True

            $ lena_cheating = False
            $ ian_cuck = False

            $ v12_emma_topless = 2

            call gallVar_lena_bikini from _call_gallVar_lena_bikini_3

        "Custom replay":
            $ ian_lena_sex = True # Needed for flow

            $ ian_look = 2
            $ lena_look = "sexy"
            $ fian = "n"
            $ flena = "n"

            scene parknight
            with long
            show ian at lef
            show lena at rig
            with short
            menu:
                gal "How serious was the relationship between Ian and Lena?"
                "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
                    $ fian = "blush"
                    $ flena = "blush"

                    $ ian_lena_dating = True
                    $ ian_lena_couple = True

                "They were just seeing each other": #CH5
                    $ ian_lena_dating = True

                "They were just friends" if ian_lena_sex == False:
                    pass

            scene blackbg
            with long

            scene lenaroomnight
            with long
            show lenanude
            with short
            menu:
                gal "Did Lena decide to check out Stalkfap?"
                "Yes, she did":
                    scene lenaroomnight
                    show v3_stalkfap2b
                    with long
                    pause (2)

                    $ stalkfap = True

                "No, she didn't":
                    pass

            scene blackbg
            with long

            call gallVar_lena_cheating from _call_gallVar_lena_cheating_2
            call gallVar_ian_cuck from _call_gallVar_ian_cuck_3

            if stalkfap:
                $ lena_look = "towel"

                scene ianhome
                show lenanude at right
                show perry at left
                with vpunch
                menu:
                    gal "Did Lena decide to tease Perry?"
                    "Yes, she did":
                        $ flena = "flirt"
                        $ fperry = "blush"
                        show lenanude at rig with move

                        $ v10_tease_perry = True
                    "No, she didn't":
                        hide lenanude
                        show lena at right
                        with short
                        $ flena = "blush"
                        $ fperry = "blush"
                scene blackbg
                with long


            call gallVar_lena_bikini from _call_gallVar_lena_bikini
            call gallVar_emma_bikini from _call_gallVar_emma_bikini_1

            call gallVar_v12_emma_topless from _call_gallVar_v12_emma_topless_1
            call gallVar_lena_cheating_decision from _call_gallVar_lena_cheating_decision_3

            if ian_lena_dating:
                if not v10_tease_perry:
                    if ian_cuck > 1 or lena_cheating > 0.5 and lena_axel_fuck:
                        pass # Lena x Wade
                    elif lena_cheating == 1:
                        gal "Uh oh. Your choices ended up in a situation where there would be nothing to see here. Please try again."
                        jump setup_CH12_S22
                    else:
                        pass # Lena x Ian
                else:
                    pass # Lena x Perry
            else:
                if not v10_tease_perry:
                    if not lena_axel_fuck:
                        gal "Uh oh. Your choices ended up in a situation where there would be nothing to see here. Please try again."
                        jump setup_CH12_S22
                    else:
                        pass # Lena x Wade
                else:
                    pass # Lena x Perry

    # no music

    $ perry_look = "swim"
    $ emma_look = "bikini"
    $ wade_look = "swim"
    $ lena_look = "bikini"
    $ ian_look = "swim"
    $ holly_look = "bikini"
    $ holly_hair = 1
    $ holly_glasses = False
    $ perry_glasses = False

    # no scene
return

label setup_CH12_S23:
    scene blackbg
    with long

    $ ian_look = 7

    scene gym
    with long
    show ian
    with short
    menu:
        gal "Was your Ian athletic?"
        "Yes, he was":
            $ ian_fit = True
        "No, he wasn't":
            pass
    
    scene blackbg
    with long

    scene lenaroomnight
    with long
    show lenanude
    with short
    menu:
        gal "Did Lena decide to check out Stalkfap?"
        "Yes, she did":
            scene lenaroomnight
            show v3_stalkfap2b
            with long
            pause (2)

            $ stalkfap = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple":
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

        "They were just friends" if ian_lena_sex == False:
            pass

    scene blackbg
    with long

    call gallVar_lena_cheating from _call_gallVar_lena_cheating_3
    call gallVar_ian_cuck from _call_gallVar_ian_cuck_4
    call gallVar_ian_lena_crisis from _call_gallVar_ian_lena_crisis_2

    # holly_trinity #ToDO

    # if not ian_lena_dating:
        # ian_holly_dating #ToDO

    $ holly_look = 1
    $ holly_glasses = True
    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    if ian_holly_dating == False and v11_holly_change == True:
        $ holly_look = 5
        $ holly_glasses = 2
        $ fholly = "smile"

        $ lena_look = "black_dress"
        $ flena = "happy"
        $ lena_makeup = 2
        $ lena_extras = "black_dress"

        $ ivy_look = "dress"
        $ ivy_extras = "bag"

        $ fholly = "smile"
        $ flena = "smile"
        $ fivy = "n"
        scene blazer
        with long
        show ivy2
        show holly at lef3
        show lena at rig3
        with short
        menu:
            gal "Did Ivy and Lena encourage Holly to hook up with guys?"
            "Yes, they did":
                $ holly_slut = True
                scene blazer_wc
                show v10_holly_mark
                with long
                pause (2)

            "No, they didn't":
                pass

        scene blackbg
        with long

        $ lena_extras = 0

    if holly_slut:
        $ v12_holly_compliment = "hot"
    if ian_holly_dating:
        $ v11_holly_fuck = True

    call gallVar_lena_bikini from _call_gallVar_lena_bikini_4
    call gallVar_emma_bikini from _call_gallVar_emma_bikini_2

    if not emma_bikini:
        call gallVar_v12_emma_topless from _call_gallVar_v12_emma_topless_2
    else:
        $ v12_emma_topless = 1
    if stalkfap or lena_lust > 8 or lena_bikini == 3:
        $ v12_lena_topless = True

    play music "music/normal_day5.mp3" loop

    $ perry_look = "swim"
    $ emma_look = "bikini"
    $ wade_look = "swim"
    $ lena_look = "bikini"
    $ ian_look = "swim"
    $ holly_look = "bikini"
    $ holly_hair = 1
    $ holly_glasses = False
    $ perry_glasses = False

    scene beach_full at beach
return

label setup_CH12_S26:
    scene blackbg
    with long

    $ ian_lena_sex = True # shortcut

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "How serious was the relationship between Ian and Lena?"
        "{image=icon_ring.webp} They were officially a couple" if ian_lena_sex: # and lena_ian_love and v8_jeremy_sex == False CH9
            $ fian = "blush"
            $ flena = "blush"

            $ ian_lena_dating = True
            $ ian_lena_couple = True

        "They were just seeing each other": #CH5
            $ ian_lena_dating = True

    scene blackbg
    with long

    call gallVar_ian_lena_love from _call_gallVar_ian_lena_love_5

    scene lenaroomnight
    with long
    show lenanude
    with short
    menu:
        gal "Did Lena decide to check out Stalkfap?"
        "Yes, she did":
            scene lenaroomnight
            show v3_stalkfap2b
            with long
            pause (2)
            $ stalkfap = True

            scene lenaroomnight
            with long
            show lenanude
            with short
            menu:
                gal "Did she decide to take it seriously and post naughtier content?"
                "Yes, she did":
                    scene lenaroomnight
                    show v5_stalkfap1
                    if lena_piercing1:
                        show v5_stalkfap1_p1
                    elif lena_piercing2:
                        show v5_stalkfap1_p2
                    with long
                    pause (2)
                    $ stalkfap_pro = 1
                "No, she didn't":
                    pass
        "No, she didn't":
            pass
    scene blackbg
    with long

    call gallVar_lena_cheating from _call_gallVar_lena_cheating_4
    call gallVar_ian_cuck from _call_gallVar_ian_cuck_5
    call gallVar_ian_lena_crisis from _call_gallVar_ian_lena_crisis_3

    $ lena_look = "wits"
    $ lena_makeup = 1
    $ lena_necklace = "seymour"
    $ flena = "smile"
    $ fseymour = "smile"

    scene seymourofficenight
    with long
    show lena2 at rig
    show seymour2 at lef
    with short
    menu:
        gal "Did Lena sign Seymour's contract?"
        "Yes, she did":
            scene v9_seymour6c
            show v9_seymour6_sy
            with long
            pause (2)

            $ seymour_desire = True
        "No, she didn't":
            pass

    scene blackbg
    with long

    call gallVar_lena_smoke from _call_gallVar_lena_smoke_1

    if ian_lena_dating:
        if not v10_tease_perry:
            if ian_cuck > 1 or lena_cheating > 0.5 and lena_axel_fuck:
                $ v12_lena_sunscreen = "wade"
            elif lena_cheating == 1:
                pass
            else:
                $ v12_lena_sunscreen = "ian"
        else:
            $ v12_lena_sunscreen = "perry"
    else:
        if not v10_tease_perry:
            if not lena_axel_fuck:
                pass
            else:
                $ v12_lena_sunscreen = "wade"
        else:
            $ v12_lena_sunscreen = "perry"


    play music "music/emmas_theme.mp3" loop

    $ flena = "n"
    $ ian_look = 3

    scene summerroom 
    with long
    show ianunder at lef
    with short
return

label setup_CH12_S27:
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_8

    $ fian = "n"

    # no  music

    scene summerroomnight
    with long
    show ian at truecenter 
    with short
return

label setup_CH12_S29:
    scene blackbg
    with long

    $ ian_look = 7

    scene gym
    with long
    show ian
    with short
    menu:
        gal "Was your Ian athletic?"
        "Yes, he was":
            $ ian_fit = True
        "No, he wasn't":
            pass
    
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_9

    $ emma_hair = "pink"

    $ femma = "n"
    $ emma_look = "summer"
    $ fwade = "n"
    $ wade_look = "summer"

    scene street
    with long
    show ian at lef3
    show emma 
    show wade at rig3
    show dog at rig
    with short
    menu:
        gal "What was Ian's reaction to Emma's dress?"
        "He told her it looked good on her":
            $ v12_emma_dress = 2
        "He told her she looked ridiculous":
            $ v12_emma_dress = 1
        "He told her he preferred it when she looked hot":
            $ v12_emma_dress = 3
        "He didn't comment on it":
            $ v12_emma_dress = 0

    scene blackbg
    with long

    if v12_emma_dress == 3:
        $ emma_look = "cool"
    elif v12_emma_dress == 1:
        $ emma_look = 1
    else:
        $ emma_look = "summer"

    call gallVar_ian_emma_love from _call_gallVar_ian_emma_love_1
    call gallVar_ian_emma_dom from _call_gallVar_ian_emma_dom

    # no music

    $ holly_look = "summer"
    $ perry_look = "summer"
    $ wade_look = "summer"
    $ lena_look = 4

    $ fholly = "happy"
    $ flena = "happy"
    $ fwade = "smile"
    $ fperry = "n"
    $ femma = "n"
    $ fian = "smile"

    scene beach_night at beachskybg5
    $ renpy.pause(3.5, hard=True)
    show bonfire
    with long
    show perry at rig3
    show wade at right5
    show wade_smoke at right5
    show emma at left
    show ian at centerlef2
    show holly at lef2 behind ian
    show lena at rig 
    with short
    p "And we're out of b--{w=0.5}beer too."
return

label setup_CH12_S30:
    scene blackbg
    with long

    scene v6_ian1
    if lena_piercing1:
        show v6_robert1_p1
    elif lena_piercing2:
        show v6_robert1_p2
    with long
    menu:
        gal "Did Lena lose her anal virginity?"
        "Yes, she did":
            $ lena_anal = 2

            $ lena_anal_first = "ian"
            scene v6_ian4b
            with long
            pause (2)
        "No, she didn't":
            $ lena_anal_first = "n"
            scene v6_ian4
            with long
            pause (2)

    scene blackbg
    with long

    $ fian = "n"
    $ ian_look = 2

    scene mall
    with long
    show ian
    with short
    menu:
        gal "Did Ian buy a gift for Lena?"
        "{image=icon_pay.webp} Yes, he did":
            $ fian = "smile"
            $ v12_gift = "lena"
            pause(1)

        "No, he didn't":
            pass

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_11
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_3

    if lena_lust > 7 or stalkfap_pro:
        $ lena_makeup = 1
        $ lena_necklace = "choker2"

    play music "music/ourredstring.mp3" loop

    scene beach_night
    with long
    show ian at lef
    show lena at rig
    with short
return

label setup_CH12_S31:
    scene blackbg
    with long

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Where Ian and Lena loyal to each other?"
        "Yes, they were":
            pass

        "No, Ian was cheating":
            $ ian_cindy_sex = True
            $ ian_cheating = 2

        "No, Lena was cheating" if ian_lena_sex == False:
            $ ian_lena_crisis = True

    scene blackbg
    with long

    scene v6_ian1
    if lena_piercing1:
        show v6_robert1_p1
    elif lena_piercing2:
        show v6_robert1_p2
    with long
    menu:
        gal "Did Lena lose her anal virginity?"
        "Yes, she did":
            $ lena_anal = 2

            $ lena_anal_first = "ian"
            scene v6_ian4b
            with long
            pause (2)

        "No, she didn't":
            $ lena_anal_first = "n"
            scene v6_ian4
            with long
            pause (2)

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_12
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_4

    if lena_lust > 7 or stalkfap_pro:
        $ lena_makeup = 1
        $ lena_necklace = "choker2"

    # no music

    scene beach_3nity
    with long
    show ian at lef
    show lena at rig
    with short
return

label setup_CH12_S32:
    scene blackbg
    with long

    $ fian = "smile"
    $ ian_look = "summer"
    $ ian_summer_look = "wits"

    play music "music/normal_day2.mp3" loop

    scene summerhousenight
    with long
return

label setup_CH12_S33:
    scene blackbg
    with long

    $ ian_look = 2
    $ lena_look = "sexy"
    $ fian = "n"
    $ flena = "n"

    scene parknight
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Where Ian and Lena loyal to each other?"
        "Yes, they were":
            pass

        "No, Lena was cheating" if ian_lena_sex == False:
            $ ian_lena_crisis = True

            $ lena_jeremy_dating = True
            $ lena_axel_desire = True

    scene blackbg
    with long

    scene v6_ian1
    if lena_piercing1:
        show v6_robert1_p1
    elif lena_piercing2:
        show v6_robert1_p2
    with long
    menu:
        gal "Did Lena lose her anal virginity?"
        "Yes, she did":
            $ lena_anal = 2

            $ lena_anal_first = "ian"
            scene v6_ian4b
            with long
            pause (2)

        "No, she didn't":
            $ lena_anal_first = "n"
            scene v6_ian4
            with long
            pause (2)

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_17
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_8

    if lena_lust > 7 or stalkfap_pro:
        $ lena_makeup = 1
        $ lena_necklace = "choker2"

    # no music

    $ flena = "sad"
    $ fian = "n"

    scene beach_3nity 
    with long
    show ian at lef
    show lena at rig
    with short
return

label setup_CH12_S34:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True

    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes, she did":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True
            $ holly_fit = True

            show holly
            with short

        "No, she didn't":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_10

    play music "music/ourredstring.mp3" loop

    $ fholly = "n"
    if ian_holly_love and v12_minerva_sex == False:
        $ fian = "smile"
    else:
        $ fian = "n"

    scene beach_3nity
    with long
    show ian at rig
    show holly3 at lef
    with short
return

label setup_CH12_S35:
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_13
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_5

    # no  music
    # no scene
return

label setup_CH12_S36:
    scene blackbg
    with long

    scene v6_ian1
    if lena_piercing1:
        show v6_robert1_p1
    elif lena_piercing2:
        show v6_robert1_p2
    with long
    menu:
        gal "Did Lena lose her anal virginity?"
        "Yes, she did":
            $ lena_anal = 2

            $ lena_anal_first = "ian"
            scene v6_ian4b
            with long
            pause (2)
        "No, she didn't":
            $ lena_anal_first = "n"
            scene v6_ian4
            with long
            pause (2)

    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_14
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_6

    $ ian_lena_couple = True
    call gallVar_ian_cheating from _call_gallVar_ian_cheating_2
    call gallVar_ian_cheating_decision from _call_gallVar_ian_cheating_decision_2

    scene beach_3nity 
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "What was the result of the talk between Ian and Lena"
        "Ian forgave Lena for cheating":
            $ ian_lena_crisis = "forgive"

        "Ian wanted to open the relationship" if ian_cheating:
            $ ian_lena_open = "ian"

        "Lena wanted to open the relationship":
            $ ian_lena_open = "lena"

    scene blackbg
    with long

    # no music

    scene summerroomnight
    with long
return

label setup_CH12_S37:
    scene blackbg
    with long

    $ holly_look = 1
    $ holly_glasses = True

    scene ianroom
    with long
    show holly3
    with short
    menu:
        gal "Did Holly want to be more like Lena?"
        "Yes, she did":
            hide holly3
            with short

            $ holly_look = "summer"
            $ fholly = "smile"
            $ holly_glasses = 2
            $ v11_holly_change = True

            show holly
            with short

        "No, she didn't":
            hide holly3
            with short

            $ holly_look = "summer"
            $ holly_change = 0

            show holly
            with short

    scene blackbg
    with long

    call gallVar_holly_gym from _call_gallVar_holly_gym_5

    call gallVar_lena_bikini from _call_gallVar_lena_bikini_5
    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_15
    call gallVar_lena_summer_look from _call_gallVar_lena_summer_look_7

    if lena_lust > 7 or stalkfap_pro:
        $ lena_makeup = 1
        $ lena_necklace = "choker2"
    $ holly_look = "summer"
    if v11_holly_change or holly_slut:
        $ holly_hair = 2
    if v11_holly_change and holly_gym:
        $ holly_fit = True
    # $ holly_glasses = 
    $ ian_look = "summer"

    scene beach_3nity
    with long
    show ian
    show holly2 at lef3
    show lena at rig3
    with short
    menu:
        gal "Which of the two girls was Ian dating?"
        "He was dating Lena":
            $ ian_lena_dating = True

        "He was dating Holly":
            $ ian_holly_dating = True

    scene blackbg
    with long

    $ flena = "smile"
    $ fian = "smile"
    $ fholly = "shy"

    play music "music/ourredstring.mp3" loop

    scene beach_3nity
    with long
    show ian
    show holly2 at lef3
    show lena at rig3
    with short
return

label setup_CH12_S38:
    scene blackbg
    with long

    scene summerroom 
    with long
    show ianunder at lef
    show lena at rig
    with short
    menu:
        gal "Had Ian just broken up with Lena?"
        "Yes, he had":
            $ flena = "cry"
            $ fian = "sad"

            $ v12_ian_lena_breakup = True

        "No, he had not":
            pass

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_16

    $ holly_look = "summer"
    $ v11_holly_change = True
    $ holly_fit = True
    $ holly_glasses = False
    $ holly_hair = 2

    # no music

    scene summerroomnight
    with long
return

label setup_CH12_S41:
    scene blackbg
    with long

    call gallVar_ian_summer_look from _call_gallVar_ian_summer_look_18

    play music "music/calm.mp3" loop
return

################################################################################
## CHAPTER 13 ##################################################################
################################################################################

label setup_CH13_S01:
    scene blackbg
    with long

    call gallVar_lena_seymour_dating from _call_gallVar_lena_seymour_dating_1
    call gallVar_seymour_disposition from _call_gallVar_seymour_disposition

    # no  music

    # no setup
return

label setup_CH13_S02:
    scene blackbg
    with long

    call gallVar_seymour_disposition from _call_gallVar_seymour_disposition_1
    call gallVar_v13_seymour_shoot from _call_gallVar_v13_seymour_shoot

    $ flena = "n"
    $ seymour_necklace = False
    $ lena_look = 1
    $ lena_makeup = 0
    $ lena_necklace = 0

    $ fseymour = "smile"
    $ seymour_look = 4

    play music "music/normal_day2.mp3" loop

    scene fancyhotel
    with long
    show lenanude
    show lena_towel
    with short
return

label setup_CH13_S03:
    scene blackbg
    with long

    call gallVar_seymour_disposition from _call_gallVar_seymour_disposition_2
    call gallVar_v13_seymour_shoot from _call_gallVar_v13_seymour_shoot_1
    if v13_seymour_shoot == 0:
        gal "Uh oh. Lena needs to join Seymour's shoot to unlock this scene, please try again."
        jump setup_CH13_S03


    scene fancyhotel
    with long
    show lenanude
    show lena_towel
    with short
    menu:
        gal "Which lingerie set did Lena choose to pose in?"
        "The Black lingerie set":
            hide lenanude
            hide lena_towel
            with long
            $ lena_look = "lingerie2b"

        "The White lingerie set":
            hide lenanude
            hide lena_towel
            with long
            $ lena_look = "lingerie2w"
    pause 1
    show lena with long
    pause 1
    if seymour_disposition > 1:
        l "I love it! It's super sexy and classy, and it looks great on me. Seymour has good taste!"
    elif seymour_disposition > 0:
        l "This is different... Very sexy, but classy too. Seymour has good taste..."
    else:
        l "This is different... Very sexy. I kinda like it, though."
    menu:
        "Try the other set":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Let me see how the other set looks on me..."
            hide lena with long
            if lena_look == "lingerie2b":
                $ lena_look = "lingerie2w"
            else:
                $ lena_look = "lingerie2b"
            show lena with long
            l "Mhh..."
            menu:
                "I like this one":
                    $ renpy.block_rollback()
                    $ flena = "smile"
                    l "I'm going with this one. This color definitely suits me best..."

                "I prefer the previous one":
                    $ renpy.block_rollback()
                    l "I think I prefer the other one..."
                    hide lena with long
                    if lena_look == "lingerie2b":
                        $ lena_look = "lingerie2w"
                    else:
                        $ lena_look = "lingerie2b"
                    show lena with long
                    $ flena = "smile"
                    l "Yeah, definitely."

        "I like this color":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I'm going with this one. This color definitely suits me best."

    scene blackbg
    with long

    $ flena = "crazy"
    $ lena_makeup = 0
    $ lena_necklace = "seymour3"

    $ fseymour = "evil"
    $ seymour_look = 4

    play music "music/necklace.mp3" loop

    if seymour_disposition > 2:
        scene v13_seymour4b
    else:
        scene v13_seymour4a
    with long
    pause 1
return

# 13b
label setup_CH13_S04:
    scene blackbg
    with long

    call gallVar_toy_badboy

    $ fstan = "shy"
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "wits"
    $ lena_necklace = "choker"

    scene rockbar
    with long
    show lena2 at rig
    show stan at lef
    with short
    menu:
        gal "Did Lena promise do to more photo shoots with Stan?"
        "Yes, she would do them free of charge":
            $ flena = "flirt"
            $ fstan = "perv"
            pause 1

            $ v10_stan_shoot = 2
        "Yes, but she would require payment":
            $ flena = "shy"
            $ fstan = "n"
            pause 1

            $ v10_stan_shoot = 1
        "She was undecided":
            pass
    scene blackbg
    with long
    $ lena_makeup = 0

    $ lena_look = 4
    $ stan_look = 1
    $ fstan = "sad"
    $ flena = "n"

    scene park
    with long
    show lena at rig
    show stan at lef
    with short
    menu:
        gal "Did Lena kiss Stan?"
        "{image=icon_lust.webp}+{image=icon_love.webp} Yes, she made out with him":
            scene v11_stan
            if lena_tattoo2:
                show v11_stan_t2
            with long
            pause 2.0

            $ v11_stan_kiss = 3
        "{image=icon_love.webp} Yes, she kissed him":
            scene v11_stan
            if lena_tattoo2:
                show v11_stan_t2
            with long
            pause 2.0

            $ v11_stan_kiss = 2
        "She teased him by mentioning the possibility":
            $ v11_stan_kiss = 1
        "No, she didn't":
            pass
    scene blackbg
    with long

    jump gallery_CH13_SceneStart
return

label setup_CH13_S05:
    scene blackbg
    with long

    call gallVar_toy_badboy

    $ flena = "smile"
    $ lena_look = 1

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
    play sound "sfx/door.mp3"
    hide louise with short
    $ flena = "shy"
    show lenabra at truecenter with move
    menu:
        gal "Did Lena sneak into Louise's room to wake Jeremy?"
        "Yes, she did":
            scene v8_jeremy1b
            with long
            pause (2)
            menu:
                gal "How far did Lena go with him?"
                "She only blew him":
                    $ v8_jeremy_sex = True
                    scene v8_jeremy5
                    with long
                    pause (2)

                "{image=icon_lust.webp} She went all the way":
                    $ v8_jeremy_sex = True
                    $ lena_jeremy_sex = True
                    scene v8_jeremy6c
                    with long
                    pause (2)
        "No, she didn't":
            pass

    scene blackbg
    with long

    scene v10_jeremy1
    if lena_tattoo2:
        show v10_jeremy1_t2
    if lena_tattoo3:
        show v10_jeremy1_t3
    with long
    menu:
        gal "Did Lena have a threesome with Louise and Jeremy?"
        "Yes, she did":
            scene v10_jeremy8b
            with long
            pause 2

            $ v10_jeremy_3some = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    if v8_jeremy_sex or v10_jeremy_3some:
        $ lena_jeremy_dating = True

    call gallVar_toy_mandingo

    jump gallery_CH13_SceneStart
return

label setup_CH13_S07:
    scene blackbg
    with long

    $ flena = "smile"
    $ lena_look = 1

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
    play sound "sfx/door.mp3"
    hide louise with short
    $ flena = "shy"
    show lenabra at truecenter with move
    menu:
        gal "Did Lena sneak into Louise's room to wake Jeremy?"
        "Yes, she did":
            scene v8_jeremy1b
            with long
            pause (2)
            menu:
                gal "How far did Lena go with him?"
                "She only blew him":
                    $ v8_jeremy_sex = True
                    scene v8_jeremy5
                    with long
                    pause (2)

                "{image=icon_lust.webp} She went all the way":
                    $ v8_jeremy_sex = True
                    $ lena_jeremy_sex = True
                    scene v8_jeremy6c
                    with long
                    pause (2)
        "No, she didn't":
            pass

    scene blackbg
    with long

    scene v10_jeremy1
    if lena_tattoo2:
        show v10_jeremy1_t2
    if lena_tattoo3:
        show v10_jeremy1_t3
    with long
    menu:
        gal "Did Lena have a threesome with Louise and Jeremy?"
        "Yes, she did":
            scene v10_jeremy8b
            with long
            pause 2

            $ v10_jeremy_3some = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    if v8_jeremy_sex or v10_jeremy_3some:
        $ lena_jeremy_dating = True

    play music "music/normal_day2.mp3" loop

    # no scene
return

label setup_CH13_S08:
    scene blackbg
    with long

    # if (lena_lust > lena_wits) and (lena_lust > lena_charisma):

    #ian_lena_couple
    #ian_cuck
    #ian_lena_open
    #lena_cheating

    scene v12_axel1_bg
    show v12_axel1b
    if lena_tattoo3:
        show v12_axel1_t3b
    if lena_tattoo2:
        show v12_axel1_t2
    if lena_piercing1:
        show v12_axel1_p1
    elif lena_piercing2:
        show v12_axel1_p2
    with long
    menu:
        gal "Did Lena fuck Axel right before going on the beach trip?"
        "Yes, she did":
            play sound "sfx/mh2.mp3"
            scene v12_axel15_animation2 with fps
            pause 4

            $ lena_axel_fuck = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = "wits"
    $ lena_makeup = 1
    $ lena_necklace = "seymour"
    $ flena = "smile"
    $ fseymour = "smile"

    scene seymourofficenight
    with long
    show lena2 at rig
    show seymour2 at lef
    with short
    menu:
        gal "Did Lena sign Seymour's contract?"
        "Yes, she did":
            scene v9_seymour6c
            show v9_seymour6_sy
            with long
            pause (2)

            $ seymour_desire = True

            scene blackbg
            with long
            $ lena_necklace = "n"
            $ lena_makeup = 0

            scene v13_seymour5
            show v13_seymour5b
            if lena_tattoo2:
                show v13_seymour5_t2
            with long
            menu:
                gal "Did Lena surrender herself to Seymour on their trip?"
                "Yes, she did":
                    scene v13_seymour13b
                    if lena_tattoo1:
                        show v13_seymour12_t1
                    if lena_tattoo2:
                        show v13_seymour12_t2
                    if lena_tattoo3:
                        show v13_seymour12_t3
                    show v13_seymour12_squirt
                    with long
                    pause 2

                    $ lena_seymour_sex = True
                "No, she didn't":
                    pass
        "No, she didn't":
            pass

    scene blackbg
    with long
    $ lena_necklace = "n"
    $ lena_makeup = 0

    play music "music/flirty3.mp3"

    $ flena = "smile"
    # $ lena_look = "charisma"/"summer"/4
    # $ lena_makeup =
    # $ lena_extras =
    # $ lena_necklace =

    scene street
    with long
    pause 0.5
    show lena at rig
    with long
return

label setup_CH13_S09:
    scene blackbg
    with long

    #ToDO
    menu:
        gal "Did Lena confess to having a threesome fantasy?"
        "Yes, she wants one with two guys":
            $ lena_fty_3some = 2
        "Yes, she wants one with two girls":
            $ lena_fty_3some = 2
        "No, she didn't":
            pass
    scene blackbg
    with long

    #v12_ian_lena_breakup

    #ian_lena_couple
    #ian_cuck
    #ian_lena_open
    #lena_cheating
    #ian_lena_love

    #v12_lena_rough

    scene v12_axel1_bg
    show v12_axel1b
    if lena_tattoo3:
        show v12_axel1_t3b
    if lena_tattoo2:
        show v12_axel1_t2
    if lena_piercing1:
        show v12_axel1_p1
    elif lena_piercing2:
        show v12_axel1_p2
    with long
    menu:
        gal "Did Lena fuck Axel right before going on the beach trip?"
        "Yes, she did":
            play sound "sfx/mh2.mp3"
            scene v12_axel15_animation2 with fps
            pause 4

            $ lena_axel_fuck = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    $ lena_look = "wits"
    $ lena_makeup = 1
    $ lena_necklace = "seymour"
    $ flena = "smile"
    $ fseymour = "smile"

    scene seymourofficenight
    with long
    show lena2 at rig
    show seymour2 at lef
    with short
    menu:
        gal "Did Lena sign Seymour's contract?"
        "Yes, she did":
            scene v9_seymour6c
            show v9_seymour6_sy
            with long
            pause (2)

            $ seymour_desire = True

            scene blackbg
            with long
            $ lena_necklace = "n"
            $ lena_makeup = 0

            scene v13_seymour5
            show v13_seymour5b
            if lena_tattoo2:
                show v13_seymour5_t2
            with long
            menu:
                gal "Did Lena surrender herself to Seymour on their trip?"
                "Yes, she did":
                    scene v13_seymour13b
                    if lena_tattoo1:
                        show v13_seymour12_t1
                    if lena_tattoo2:
                        show v13_seymour12_t2
                    if lena_tattoo3:
                        show v13_seymour12_t3
                    show v13_seymour12_squirt
                    with long
                    pause 2

                    $ lena_seymour_sex = True
                "No, she didn't":
                    pass
        "No, she didn't":
            pass

    scene blackbg
    with long
    $ lena_necklace = "n"
    $ lena_makeup = 0

    $ lena_robert_dating = True
    call gallVar_lena_analch13

    play music "music/flirty3.mp3"

    $ flena = "smile"
    # $ lena_look = "charisma"/"summer"/4
    # $ lena_makeup =
    # $ lena_extras =
    # $ lena_necklace =

    scene street
    with long
    pause 0.5
    show lena at rig
    with long
return

label setup_CH13_S10:
    scene blackbg
    with long

    # if (lena_lust > lena_wits) and (lena_lust > lena_charisma):

    #ToDO
    menu:
        gal "Did Lena confess to having a threesome fantasy?"
        "Yes, she wants one with two guys":
            $ lena_fty_3some = 2
        "Yes, she wants one with two girls":
            $ lena_fty_3some = 2
        "No, she didn't":
            pass
    scene blackbg
    with long

    scene v12_axel1_bg
    show v12_axel1b
    if lena_tattoo3:
        show v12_axel1_t3b
    if lena_tattoo2:
        show v12_axel1_t2
    if lena_piercing1:
        show v12_axel1_p1
    elif lena_piercing2:
        show v12_axel1_p2
    with long
    menu:
        gal "Did Lena fuck Axel right before going on the beach trip?"
        "Yes, she did":
            play sound "sfx/mh2.mp3"
            scene v12_axel15_animation2 with fps
            pause 4

            $ lena_axel_fuck = True
        "No, she didn't":
            pass
    scene blackbg
    with long

    #ToDO
    menu:
        gal "What is Lena and Ian's relationship status at the moment?"
        "They broke up on the beach trip":
            #ToDO
            $ v12_ian_lena_breakup = True
        "They are still a couple":
            #ToDO
            $ ian_lena_couple = True
            $ ian_lena_dating = True

            scene blackbg
            with long

            $ ian_look = "summer"
            $ ian_summer_look = "wits"
            $ flena = "sad"
            $ flena = "sad"
            # $ lena_look = #ToDO

            scene beach_3nity
            with long
            show ian at lef
            show lena at rig
            with short
            menu:
                gal "What was the result of their talk on the beach?"
                "Ian forgave Lena for cheating on him":
                    $ ian_lena_crisis = "forgive"
                "Ian demanded an open relationship":
                    $ ian_lena_open = "ian"
                "Lena wanted an open relationship":
                    $ ian_lena_open = "lena"
                "Ian has become a cuck":
                    $ ian_cuck = 2

            if ian_lena_crisis == "forgive" or ian_lena_open == "ian" or ian_lena_open == "lena":
                scene blackbg
                with long

                scene v12_lena30
                show v12_lena30_spank
                with long
                menu:
                    gal "Did Ian punish Lena?"
                    "Yes, he did":
                        scene v12_lena33
                        if lena_tattoo3:
                            show v12_lena33_t2
                        if lena_tattoo2:
                            show v12_lena33_t3
                        if lena_piercing1:
                            show v12_lena33_p1
                        elif lena_piercing2:
                            show v12_lena33_p2
                        with long
                        play sound "sfx/gasp3.mp3"
                        pause 2

                        $ v12_lena_rough = 2

                        scene blackbg
                        with long

                        scene v12_lena34
                        with long
                        pause 1
                        menu:
                            "Did he tell her that he loved her?"
                            "Yes, he did":
                                scene v12_lena35
                                if lena_piercing1:
                                    show v12_lena35_p1
                                elif lena_piercing2:
                                    show v12_lena35_p2
                                if lena_tattoo1:
                                    show v12_lena35_t1
                                if lena_tattoo1:
                                    show v12_lena35_t2
                                with long
                                pause 1

                                $ ian_lena_love = True

                            "No, he didn't":
                                pass
                    "No, he didn't":
                        pass
        "They were never a couple to begin with":
            pass
    scene blackbg
    with long

    $ lena_look = "wits"
    $ lena_makeup = 1
    $ lena_necklace = "seymour"
    $ flena = "smile"
    $ fseymour = "smile"

    scene seymourofficenight
    with long
    show lena2 at rig
    show seymour2 at lef
    with short
    menu:
        gal "Did Lena sign Seymour's contract?"
        "Yes, she did":
            scene v9_seymour6c
            show v9_seymour6_sy
            with long
            pause (2)

            $ seymour_desire = True

            scene blackbg
            with long
            $ lena_necklace = "n"
            $ lena_makeup = 0

            scene v13_seymour5
            show v13_seymour5b
            if lena_tattoo2:
                show v13_seymour5_t2
            with long
            menu:
                gal "Did Lena surrender herself to Seymour on their trip?"
                "Yes, she did":
                    scene v13_seymour13b
                    if lena_tattoo1:
                        show v13_seymour12_t1
                    if lena_tattoo2:
                        show v13_seymour12_t2
                    if lena_tattoo3:
                        show v13_seymour12_t3
                    show v13_seymour12_squirt
                    with long
                    pause 2

                    $ lena_seymour_sex = True
                "No, she didn't":
                    pass
        "No, she didn't":
            pass

    scene blackbg
    with long
    $ lena_necklace = "n"
    $ lena_makeup = 0

    call gallVar_lena_analch13

    play music "music/flirty3.mp3"

    $ flena = "smile"
    # $ lena_look = "charisma"/"summer"/4
    # $ lena_makeup =
    # $ lena_extras =
    # $ lena_necklace =

    scene street
    with long
    pause 0.5
    show lena at rig
    with long
return

label setup_CH13_S11:
    scene blackbg
    with long

    # $ ian_lena_dom = 
    # $ lena_seymour_sex = 
    # $ lena_axel_fuck = 
    # $ v13_seymour_lingerie = 
    # $ ian_lena_pure = 
    # $ ian_lena_couple = 
    # $ lena_fty_3some = 
    # $ ian_lena_mmf = 
    # $ lena_anal = 

    #$ flena =
    #$ lena_look = 
    #$ lena_makeup =

    #ToDO music
return

label setup_CH13_S12:
    scene blackbg
    with long

    # $ lena_lust > 5

    $ lena_look = 4
    $ stan_look = 1
    $ fstan = "sad"
    $ flena = "n"

    scene park
    with long
    show lena at rig
    show stan at lef
    with short
    menu:
        gal "Did Lena kiss Stan?"
        "{image=icon_lust.webp}+{image=icon_love.webp} Yes, she made out with him":
            scene v11_stan
            if lena_tattoo2:
                show v11_stan_t2
            with long
            pause 2.0

            $ v11_stan_kiss = 3
        "{image=icon_love.webp} Yes, she kissed him":
            scene v11_stan
            if lena_tattoo2:
                show v11_stan_t2
            with long
            pause 2.0

            $ v11_stan_kiss = 2
        "She teased him by mentioning the possibility":
            $ v11_stan_kiss = 1
        "No, she didn't":
            pass
    scene blackbg
    with long

    # $ v13_stan_reward = 

    $ flena = "smile"
    $ lena_look = 1
    $ lena_makeup = 0

    $ fstan = "smile"


    #no music
return

label setup_CH13_S13:
    scene blackbg
    with long

    #$ flena =
    #$ lena_look = 
    #$ lena_makeup =

    #ToDO music
return

label setup_CH13_S14:
    scene blackbg
    with long

    #$ flena =
    #$ lena_look = 
    #$ lena_makeup =

    #ToDO music
return

label setup_CH13_S15:
    scene blackbg
    with long

    $ flena = "smile"
    $ lena_look = 1

    scene lenahome
    with long
    show lenabra at rig
    show louise at lef
    with short
    play sound "sfx/door.mp3"
    hide louise with short
    $ flena = "shy"
    show lenabra at truecenter with move
    menu:
        gal "Did Lena sneak into Louise's room to wake Jeremy?"
        "Yes, she did":
            scene v8_jeremy1b
            with long
            pause (2)
            menu:
                gal "How far did Lena go with him?"
                "She only blew him":
                    $ v8_jeremy_sex = True
                    scene v8_jeremy5
                    with long
                    pause (2)

                "{image=icon_lust.webp} She went all the way":
                    $ v8_jeremy_sex = True
                    $ lena_jeremy_sex = True
                    scene v8_jeremy6c
                    with long
                    pause (2)
        "No, she didn't":
            pass

    scene blackbg
    with long

    scene v10_jeremy1
    if lena_tattoo2:
        show v10_jeremy1_t2
    if lena_tattoo3:
        show v10_jeremy1_t3
    with long
    menu:
        gal "Did Lena have a threesome with Louise and Jeremy?"
        "Yes, she did":
            scene v10_jeremy8b
            with long
            pause 2

            $ v10_jeremy_3some = True

        "No, she didn't":
            pass

    scene blackbg
    with long

    if v8_jeremy_sex or v10_jeremy_3some:
        $ lena_jeremy_dating = True

    call gallVar_toy_mandingo
    if toy_mandingo:
        if lena_jeremy_sex or v10_jeremy_3some:
            $ v13_bbc_dildo = True

    #no music

    scene lenaroomnight
    with long
    "Night fell, and I got ready for the other date I had today. One I had been eagerly anticipating..."
return

label setup_CH13_S16:
    scene blackbg
    with long

    $ lena_look = "underwear2"
    $ flena = "n"

    play music "music/normal_day2.mp3" loop

    scene lenaroomnight
    with long
    show lenabra
    with short
return

################################################################################
## CHAPTER 14 ##################################################################
################################################################################

## BASIC SCENE IN SETUP FILE ###################################################

# label setup_CH01_S01:
#     scene blackbg
#     with long

#     $ flena =
#     $ lena_look = 
#     $ lena_makeup =

#     #ToDO music
# return