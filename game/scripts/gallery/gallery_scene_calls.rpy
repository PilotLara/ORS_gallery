label gallVar_lena_bdick:
    scene v3_louise0
    with long
    show v3_louise1
    with fps
    menu:
        gal "Did Lena focus on Jeremy's big dick?" #CH3
        "Yes, she did":
            scene v3_louise4
            with long
            pause (2)

            $ lena_bdick = 1
            $ v3_spy = True
            $ v3_bbc = True
            $ v3_spy_full = True # auto if v3_bbc

        "No, she focused on Louise":
            scene v3_louise1b
            with long
            pause (2)

            $ v3_spy = True

        "No, she didn't peek":
            pass

    scene blackbg
    with long
return

label gallVar_ian_lena_sex:
    $ lena_look = 3
    $ ian_look = 3
    $ fian = "insecure"
    $ flena = "shy"

    scene street2night
    with long
    show ian at lef
    show lena at rig
    with short
    menu:
        gal "Have Ian and Lena had sex?" #CH4
        "Yes, they have":
            scene v4_lena1
            if lena_piercing1:
                show v4_lena1_p1
            if lena_piercing2:
                show v4_lena1_p2
            with long
            pause (2)

            $ ian_lena_sex = True

        "No, they haven't":
            pass

    scene blackbg
    with long
return

label gallVar_lena_anal1:
    scene lenaroomnight
    with long
    scene v4_solo1
    if lena_piercing1:
        show v4_solo1_p1
    elif lena_piercing2:
        show v4_solo1_p2
    with long
    menu:
        gal "Did Lena experiment with the anal plug?" #CH4
        "Yes, she did":
            scene v4_solo2_animation
            with long
            pause (2)

            $ lena_anal = 1

        "No, she didn't":
            $ lena_anal = 0

    scene blackbg
    with long
return

label gallVar_lena_anal2:
    if ian_lena_dating or lena_robert_dating or lena_mike_dating:
        if ian_lena_dating:
            scene v6_ian3
        elif lena_mike_dating:
            scene v6_mike5
        elif lena_robert_dating:
            scene v6_robert4
        if lena_piercing1:
                show v6_robert4_p1
        elif lena_piercing2:
            show v6_robert4_p2
        with long
        menu:
            gal "Had Lena lost her anal virginity? If so, to whom?" #CH6
            "Yes, to Ian" if ian_lena_dating:
                $ lena_anal = 2

                $ lena_anal_first = "ian"
                scene v6_ian4b
                with long
                pause (2)

            "Yes, to mike" if lena_mike_dating:
                $ lena_anal = 2

                $ lena_anal_first = "mike"
                scene v6_mike6_animation
                with long
                pause (2)

            "Yes, to Robert" if lena_robert_dating:
                $ lena_anal = 2

                $ lena_anal_first = "robert"
                scene v6_robert5
                show v6_robert5_bunny
                if lena_piercing1:
                    show v6_robert5_p1
                elif lena_piercing2:
                    show v6_robert5_p2
                with long
                pause (2)

            "No, she hadn't":
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
        scene blackbg
        with long
return

label gallVar_ian_chad:
    $ fian = "n"
    $ ian_look = 1

    scene ianroom
    with long
    show ian
    with short
    menu:
        gal "Which level of mainstream-ness, chad-ness, or alpha-ness has your Ian achieved?" #CH02
        "Level 5" if chapter > 6:
            $ fian = "confident"

            $ ian_chad = 5

        "Level 4" if chapter > 5:
            $ fian = "confident"

            $ ian_chad = 4

        "Level 3" if chapter > 4:
            $ fian = "confident"

            $ ian_chad = 3

        "Level 2" if chapter > 1:
            $ ian_chad = 2

        "Level 1 (base level)":
            $ ian_chad = 1

        "Level 0" if chapter > 1:
            $ ian_chad = 0

    if ian_lena_sex == False and chapter > 9: #CH10
        $ ian_chad = 0

    scene blackbg
    with long
return

label gallVar_holly_gym:
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

            $ holly_gym = True

        "No, she didn't":
            pass

    scene blackbg
    with long
return

label gallVar_ian_lena_love:
    if chapter > 9 and ian_lena_couple: #CH10
        $ ian_lena_love = True
    elif ian_lena_dating:
        if ian_lena_sex:
            $ fian = "smile"
        else: 
            $ fian = "n"
        $ fjeremy = "n"
        $ ian_look = "cool"
        $ jeremy_look = 3
        scene cocktailbar
        with long 
        show ian at lef
        show jeremy at rig
        with short
        menu:
            gal "Did Ian confess his love for Lena to Jeremy?" #CH7
            "{image=icon_love.webp} Yes, he said he was falling for her":
                $ fian = "shy"
                $ fjeremy = "sad"

                $ ian_lena_love = True

            "No, it was no-strings-attached fun for him":
                if ian_lena_sex:
                    $ fian = "happy"
                    $ fjeremy = "happy"

        scene blackbg
        with long
return

label gallVar_lena_ian_love:
    if ian_lena_couple:
        $ lena_ian_love = True # req for ian_lena_couple

        if chapter > 10:
            $ lena_ian_love = 1

            if ian_lena_sex:
                scene blackbg
                with long

                scene v11_ian2_animation
                if lena_tattoo2:
                    show v11_ian2_t2_animation
                if lena_tattoo3:
                    show v11_ian2_t3_animation
                with fps
                pause (3)
                menu:
                    gal "Did Lena proclaim her love during sex with Ian?" #CH11pro
                    "Yes, she did":
                        scene v11_ian4
                        if lena_tattoo2:
                            show v11_ian4_t2
                        if lena_tattoo3:
                            show v11_ian4_t3
                        show v11_ian4_iansad
                        show v11_ian4_lenasad
                        with long
                        pause (2)

                        $ lena_ian_love = 2

                    "No, she didn't":
                        pass
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

                if chapter > 10:
                    $ lena_ian_love = 1

                    if ian_lena_sex:
                        scene blackbg
                        with long

                        scene v11_ian2_animation
                        if lena_tattoo2:
                            show v11_ian2_t2_animation
                        if lena_tattoo3:
                            show v11_ian2_t3_animation
                        with fps
                        pause (3)
                        menu:
                            gal "Did Lena confess her love during sex as well?" #CH11pro
                            "Yes, she did":
                                scene v11_ian4
                                if lena_tattoo2:
                                    show v11_ian4_t2
                                if lena_tattoo3:
                                    show v11_ian4_t3
                                show v11_ian4_iansad
                                show v11_ian4_lenasad
                                with long
                                pause (2)

                                $ lena_ian_love = 2

                            "No, she didn't":
                                pass

            "No, she didn't":
                pass

        scene blackbg
        with long
return

label gallVar_ian_lena_dom:
    if ian_lena_sex:
        scene v6_lena6_animation
        if lena_necklace == "choker":
            show v6_lena6_choker_animation
        with long
        menu:
            gal "Did Ian guide Lena's head during the BJ?"
            "Yes, he did":
                scene v6_lena7_animation
                if lena_necklace == "choker":
                    show v6_lena7_choker_animation
                show v6_lena7_hand_animation
                with vpunch
                play sound "sfx/gag1.mp3"
                pause (2)

                $ ian_lena_dom += 1 #CH6

            "No, he didn't":
                pass
        if chapter > 7:
            if ian_lust > 5 or ian_lena_dom > 0:
                scene blackbg
                with long

                scene v8_lena6a
                if v8_sy:
                    show v8_lena6_sy
                elif v8_choker:
                    show v8_lena6_choker
                with long
                menu:
                    gal "Did Ian decide to change up their love making?" #CH8
                    "Yes, he fucked her harder":
                        scene v8_lena7
                        if v8_sy:
                            show v8_lena7_sy
                        elif v8_choker:
                            show v8_lena7_choker
                        with long
                        pause (2)

                        $ ian_lena_dom += 1
                        $ lena_satisfaction = 2

                    "Yes, he fucked her softly":
                        if v8_lena_anal:
                            scene v8_lena9b
                        else:
                            scene v8_lena9
                        if lena_piercing1:
                            show v8_lena9_p1
                        elif lena_piercing2:
                            show v8_lena9_p2
                        if v8_sy:
                            show v8_lena9_sy
                        if v8_choker:
                            show v8_lena9_choker
                        with long
                        pause 1

                        $ lena_satisfaction = 1
                    
                    "No, he kept the same pace":
                        $ lena_satisfaction = 0

            scene blackbg
            with long

        if chapter > 11:
            scene v11_lena8
            if lena_tattoo2:
                show v11_lena8_t2
            if lena_tattoo3:
                show v11_lena8_t3
            with long
            menu:
                gal "Did Ian choke Lena during sex?"
                "Yes, he did":
                    scene v11_lena8b
                    if lena_tattoo2:
                        show v11_lena8_t2
                    if lena_tattoo3:
                        show v11_lena8b_t3
                    with long
                    play sound "sfx/mh2.mp3"

                    if ian_lena_dom < 2:
                        $ ian_lena_dom += 1

                "No, he didn't":
                    pass
            scene blackbg
            with long

return

label gallVar_ian_cheating:
    if ian_lena_couple:
        $ ian_look = "charisma1"

        $ alison_blonde = True
        $ alison_look = "dress"

        $ cindy_look = 2

        $ minerva_look = "dress"

        label GallIanCheat:
            pass

        scene streetnight
        with long
        show ian at lef4
        show alison at truecenter
        show cindy at rig2
        show minerva at right5
        with short
        menu:
            gal "With whom did Ian cheat after becoming a couple with Lena? (Cherry and Holly are not possible)"
            "{image=icon_ring.webp} Ian doesn't cheat" if ian_cheating == False:
                pass

            "Alison" if ian_alison_fuck == False: #CH11
                scene v11_alison1_animation
                with long
                pause (2)

                $ ian_cheating = True
                $ ian_alison_fuck = True
                $ falison = "flirt"
                jump GallIanCheat

            "Cindy" if ian_cindy_dating == False: #CH9
                scene v9_cindy9
                with long
                pause (2)

                $ ian_cheating = True
                $ ian_cindy_dating = True
                $ fcindy = "flirt"
                jump GallIanCheat

            "Minerva" if ian_minerva_dating == False: #CH10
                scene v10_minerva6_animation with fps
                pause (2)

                $ ian_cheating = True
                $ ian_minerva_dating = True
                $ fminerva = "smile"
                jump GallIanCheat

            "That's everyone" if ian_cheating:
                pass

        scene blackbg
        with long
return

label gallVar_lena_cheating:
    if ian_lena_couple:
        $ lena_look = "black_dress"
        $ lena_extras = "black_dress"
        $ lena_necklace = "seymour"
        $ lena_makeup = 2
        $ flena = "flirt"

        $ axel_look = 2

        $ mike_look = 2
        $ mike_extras = "chain"

        label GallLenaCheat:
            pass

        scene blazer
        with long
        show lena at left5
        show axel at lef5
        if v11_bbc != "marcel":
            show bouncer at centerlef
        else:
            show bouncersmile at centerlef
        show mark at centerrig2
        show mike at rig3
        show jack at right5
        with short
        menu:
            gal "With whom did Lena cheat after becoming a couple with Ian? (Jeremy is not possible)"
            "{image=icon_ring.webp} Lena doesn't cheat" if lena_cheating == False:
                pass

            "Axel" if lena_axel_desire == False:
                scene v9_axel6_animation
                with long
                pause (2)

                $ lena_cheating = True
                if chapter > 10:
                    $ lena_axel_desire = 2 #CH11
                else:
                    $ lena_axel_desire = True

                $ v9_axel_sex = True #CH9
                if chapter > 11:
                    $ lena_axel_fuck = True #CH12
                $ faxel = "smile"
                jump GallLenaCheat

            "Marcel" if v11_bbc != "marcel":
                scene v11_bbc3_marcel
                show v11_bbc3_charisma
                show v11_bbc3_choker
                if lena_tattoo2:
                    show v11_bbc3_t2
                with long
                play sound "sfx/bj1.mp3"
                pause (2)

                $ lena_cheating = True
                $ v11_bbc = "marcel" #CH11
                jump GallLenaCheat

            "Mark" if v10_wc_bj != "mark" and v10_wc_bj != "mike":
                $ v10_wc_bj = "mark" #CH10
                $ fmark = "flirt"

                scene v10_wc5
                with long
                pause (2)

                $ lena_cheating = True
                jump GallLenaCheat

            "Mike" if v10_wc_bj != "mike" and v10_wc_bj != "mark":
                $ lena_mike_dating = True
                $ v10_wc_bj = "mike" #CH10
                $ fmike = "flirt"

                scene v10_wc5
                with long
                pause (2)
                
                $ lena_cheating = True
                jump GallLenaCheat

            "Jack" if lena_jack_dating == False:
                $ fjack = "smile"
                scene v11_jack6a
                show v11_jack6_earrings
                show v11_jack6b
                if lena_tattoo1:
                    show v11_jack6_t1
                if lena_tattoo2:
                    show v11_jack6_t2
                if lena_tattoo3:
                    show v11_jack6_t3
                show v11_jack6_stockings
                with long
                pause (2)

                $ lena_cheating = True
                $ lena_jack_dating = 2 #CH11
                $ lena_jack = 4
                jump GallLenaCheat
                # ToDO compatibility with axel

            "That's everyone" if lena_cheating:
                pass

        scene blackbg
        with long

        $ lena_extras = 0
        $ lena_necklace = 0
        $ lena_makeup = 0

        $ mike_extras = 0

    elif ian_lena_dating:
        gal "Casual hookups outside of Ian x Lena WIP"

        # ToDO
return

label gallVar_ian_cuck:
    if v9_axel_sex or (lena_seymour_dating and seymour_disposition < 2) or (ian_lena_sex == False and lena_robert_sex) or (ian_lena_sex == False and lena_mike_sex):
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

    if chapter > 10:
        if (ian_cuck and ian_lust < 6) or (ian_lena_sex == False and ian_lust < 6):
            $ v11_lena_dom = True #CH11pro
            if ian_cuck:
                $ ian_cuck = 1

        else:
            scene v11_ian0
            with long
            menu:
                gal "Did Lena ride Ian's face?" #CH11pro
                "Yes, she did":
                    scene v11_ian1
                    if lena_tattoo1:
                        show v11_ian1_t1
                    if lena_tattoo2:
                        show v11_ian1_t2
                    if lena_tattoo3:
                        show v11_ian1_t3
                    if lena_piercing1:
                        show v11_ian1_p1
                    elif lena_piercing2:
                        show v11_ian1_p2
                    with long
                    pause (2)

                    $ v11_lena_dom = True
                    if ian_cuck:
                        $ ian_cuck = 1

                "No, she didn't":
                    pass

            scene blackbg
            with long

        if ian_cuck and ian_lena_sex: #CH11pro
            scene v11_ian4
            if lena_tattoo3:
                show v11_ian4_t3
            show v11_ian4_iansad
            if lena_tattoo2:
                show v11_ian4_t2
            with long
            menu: 
                gal "Did Lena deny him sex?"
                "Yes, she did":
                    show v11_ian4_lenasad
                    with long

                    $ ian_cuck = 2

                "No, she didn't":
                    scene v11_ian2
                    if lena_tattoo2:
                        show v11_ian2_t2
                    if lena_tattoo3:
                        show v11_ian2_t3
                    with long
                    pause (2)

            scene blackbg
            with long

        elif ian_lena_sex == False:
            $ ian_cuck = 2

        if ian_lena_sex == False or ian_cuck or v11_lena_dom: #CH11a
            $ v11_lena_dom = True

            scene v11_lena4
            if lena_piercing1:
                show v11_lena4_p1
            elif lena_piercing2:
                show v11_lena4_p2
            if lena_tattoo1:
                show v11_lena4_t1
            if lena_tattoo2:
                show v11_lena4_t2
            if lena_tattoo3:
                show v11_lena4_t3
            with long
            menu:
                gal "What was Ian's reaction when she gave him a footjob?" #CH11a
                "{image=icon_lust.webp} He wanted to know where she learned to do this" if ian_cuck or ian_lust > 6:

                    label GallFeetCuck:
                        menu:
                            gal "Did Ian ask Lena to tell him more when she told him she learned it from a guy she used to date?" #CH11a
                            "Yes, he did":
                                scene v11_lena4b
                                if lena_tattoo2:
                                    show v11_lena4_t2
                                if lena_tattoo3:
                                    show v11_lena4_t3
                                with long
                                pause (2)

                                if ian_cuck < 2:
                                    $ ian_cuck += 1

                                if ian_cuck == 2 and ian_lena_sex:
                                    scene blackbg
                                    with long

                                    scene v11_lena4b
                                    if lena_tattoo2:
                                        show v11_lena4_t2
                                    if lena_tattoo3:
                                        show v11_lena4_t3
                                    with long
                                    menu:
                                        gal "Did Ian get turned on hearing about these things?"
                                        "{image=icon_sad.webp} Yeah...":
                                            pass
                
                                        "{image=icon_athletics.webp} Not really" if ian_chad > 2 or ian_athletics > 5:
                                            scene v11_lena7
                                            if lena_tattoo2:
                                                show v10_ian8_t2
                                            with long
                                            pause (2)

                                            $ ian_cuck = 1

                            "No, that was enough information for him":
                                $ ian_cuck = 0

                "He complimented her skill":
                    if ian_cuck == 2:
                        jump GallFeetCuck
                    else:
                        $ ian_cuck = False

                "...":
                    if ian_cuck:
                        jump GallFeetCuck

                "{image=icon_athletics.webp} He didn't like it" if (ian_chad > 2 and ian_lena_sex) or (ian_athletics > 5 and ian_lena_sex):
                    $ v11_lena_dom = False
                    $ ian_cuck = False

            scene blackbg
            with long

        if ian_cuck > 1:  # CH11epi
            $ lena_look = "sexy"
            $ ian_look = 2
            $ fian = "shy"
            $ flena = "n"

            scene ianhomenight 
            with long
            show ian at lef
            show lenatopless at rig 
            with short
            menu: 
                gal "Did Lena tease Ian?" # CH11epi
                "{image=icon_sad.webp} Yes, she did":
                    scene v11_lenaian1
                    if lena_tattoo1:
                        show v11_mark1_t1
                    if lena_piercing1:
                        show v11_mark1_p1
                    elif lena_piercing2:
                        show v11_mark1_p2
                    with long
                    pause (2)

                    $ ian_cuck = 3

                "No, she didn't":
                    pass

            scene blackbg
            with long
return

label gallVar_ian_lena_3some:
    if chapter > 10:
        if ian_lena_sex and ian_lena_dating and ian_cuck < 2: #CH11pro
            $ ian_look = 2
            $ lena_look = "ianshirt"
            $ fian = "n"
            $ flena = "flirtshy"

            scene lenahome with long
            show ian at lef
            show lenaunder at rig
            with short
            menu:
                gal "Did Lena say they could give a threesome a try?"
                "Yes, she did":
                    $ flena = "shy"
                    $ fian = "shy"

                    $ ian_lena_3some = True

                "No, she didn't":
                    pass

            scene blackbg
            with long
return

label gallVar_ian_summer_look:
    $ ian_look = 2
    $ fian = "n"

    scene mall
    with long
    show ian
    with short
    gal "Which outfit did Ian buy for the trip"
    label GallSummerShop:
        show ian at left
        with move
        call screen v12ian_clothingshop_gal
        hide ian 
        with short

        $ ian_look = "summer"
        $ fian = "smile"

        show ian
        with short
        menu:
            "Get this one":
                i "It's decided."

                hide ian
                with short

            "Try something else":
                $ fian = "n"
                i "Hm... I'm not convinced. Let's see this one..."

                hide ian
                with short
                $ ian_look = 2

                show ian
                with short
                jump GallSummerShop

    scene blackbg
    with long
return

label gallVar_ian_lena_crisis:
    if (v11_louise_3some == "ian" and v10_jeremy_3some) or lena_cheating:
        $ ian_lena_crisis = True #CH12
    elif ian_lena_dating and (lena_axel_desire or lena_mike_dating or v11_mark_sex or lena_jack > 2 or v11_bbc or v8_jeremy_sex or v10_jeremy_3some):
        $ ian_lena_crisis = True #CH12
return

label gallVar_ian_cheating_decision:
    if ian_cheating:
        if ian_summer_look == 0:
            gal "Error: ian_summer_look not defined"
            $ renpy.end_replay()
        $ ian_look = "summer"
        $ fian = "sad"

        scene summerroom
        with long
        show ian
        with short
        menu:
            gal "Has Ian made a decision concerning his cheating behaviour?" #CH12b
            "{image=icon_will.webp}{image=icon_ring.webp} Stop cheating":
                $ fian = "serious"
                call willdown from _call_willdown_75

                $ ian_cheating = 0.5

            "{image=icon_lust.webp} Continue cheating":
                $ fian = "n"

                $ ian_cheating = 2
                $ ian_lena_love = False

            "{image=icon_broken.webp} Break up with Lena":
                $ ian_cheating = 1
                $ ian_lena_love = False

        scene blackbg
        with long
return

label gallVar_lena_cheating_decision:
    if lena_cheating:
        $ flena = "worried"
        $ lena_look = 1

        scene lenaoldroom
        with long
        show lenabra at truecenter
        with short
        menu:
            gal "Has Lena made a decision concerning her cheating behaviour?"
            "{image=icon_will.webp}{image=icon_ring.webp} Stop cheating":
                $ flena = "cry"
                call willdown from _call_willdown_76

                $ lena_cheating = 0.5

            "{image=icon_lust.webp} Continue cheating" if lena_will > 0:
                $ flena = "crazyserious"

                $ lena_cheating = 2
                $ lena_ian_love = 0.5

            "{image=icon_broken.webp} Break up with Ian":
                $ flena = "sad"

                $ lena_cheating = 1
                $ lena_ian_love = 0.5

        scene blackbg
        with long
return

label gallVar_lena_summer_look:
    $ lena_look = 4
    $ flena = "smile"

    $ gall_lena_look = "summer"
    $ gall_flena = "smile"

    scene lenaoldroom
    with long
    show lena at right5
    show gall_lena at left5
    with short
    menu:
        gal "Which outfit did Lena choose for the summer trip"
        "← Left: {image=icon_lust.webp} > 7 and/or taking Stalkfap seriously":
            hide lena
            with short
            show gall_lena at truecenter
            with move

            $ lena_look = "summer"

            $ lena_lust = 10
            $ stalkfap = True
            $ stalkfap_pro = 1


        "Right: {image=icon_lust.webp} ≤ 7 and not putting in extra effort on Stalkfap →" if not stalkfap_pro == 1:
            hide gall_lena
            with short
            show lena at truecenter
            with move

            $ lena_lust = 7
            $ stalkfap_pro = 0

    scene blackbg
    with long
return

label gallVar_lena_smoke:
    $ fivy = "n"
    $ ivy_look = "gogo"

    $ flena = "n"
    $ lena_makeup = 1

    if v11_lena_dress == 0:
        $ v11_lena_dress = 4
    $ lena_look = "clubdress"

    $ lena_necklace = "choker2"
    $ lena_extras = "stockings"

    scene street2night
    with long
    show ivy at lef
    show lena at rig
    with short

    play sound "sfx/lighter.mp3"
    show ivy_smoke at lef
    with long
    $ ivy_extras = "smoke"
    hide ivy_smoke
    menu:
        gal "Did Lena accept Ivy's cigarette?"
        "Yes, she did":
            $ lena_smoke = True
            play sound "sfx/lighter.mp3"
            hide lena
            show lena_smoke at rig
            with long
            $ fivy = "smile"
            l "Ugh, I quit smoking these a long time ago..."

        "No, she didn't":
            pass

    scene blackbg
    with long

    $ lena_makeup = 0
    $ lena_necklace = 0
    $ lena_extras = 0

    $ ivy_extras = 0
return

label gallVar_lena_bikini:
    $ flena = "n"
    $ lena_look = 4

    scene mall
    with long
    show lena
    with short
    gal "Which bikini did Lena decide to buy?"
    hide lena
    with long
    label gallLenaBikini:
        hide lenabikini
        with short
        call screen screen_choice(v11bikinitry)
        $ lena_bikini = _return
    scene v11_bikini1_bg
    show v11_bikini1
    if lena_tattoo2:
        show v11_bikini1_t2
    if lena_tattoo3:
        show v11_bikini1_t3
    if lena_bikini == 1:
        show v11_bikini1a
    elif lena_bikini == 2:
        show v11_bikini1b
    elif lena_bikini == 3:
        show v11_bikini1c
    with long
    pause 1
    $ flena = "smile"
    scene mall
    show lenabikini
    with long
    menu:
        "Try another bikini":
            $ renpy.block_rollback()
            l "Let me try another one..."
            jump gallLenaBikini
            
        "Buy this one":
            $ renpy.block_rollback()
            l "I'm sold! I'll get this one."

    scene blackbg
    with long
return

label gallVar_emma_bikini:
    if lena_bikini == 0:
        gal "ERROR: lena_bikini not defined"
        $ renpy.end_replay()

    $ emma_look = 1
    $ femma = "n"
    $ flena = "smile"

    scene mall
    with long
    show lenabikini at rig
    show emmabikini at lef
    with short
    menu:
        gal "Did Lena encourage Emma to buy a hotter bikini?"
        "Yes, she did":
            scene v11_bikini1_bg
            show v11_bikini1_emma
            show v11_bikini1_emmab
            with long
            pause (2)

            $ emma_bikini = True

        "No, she didn't":
            scene v11_bikini1_bg
            show v11_bikini1_emma
            show v11_bikini1_emmaa
            with long
            pause (2)

    scene blackbg
    with long
return

label gallVar_ian_emma_love:
    if ian_summer_look == 0:
        gal "Error: ian_summer_look not defined"
        $ renpy.end_replay()
    $ ian_look = "summer"
    $ emma_hair = "pink"
    if v12_emma_dress == 3:
        $ emma_look = "cool"
    elif v12_emma_dress == 1:
        $ emma_look = 1
    else:
        $ emma_look = "summer"

    $ fian = "confident"
    $ femma = "flirt"

    scene summerhouse 
    with long
    show ian at lef3
    show emma at rig3
    with short
    menu:
        gal "How did Ian react to Emma's confession that she had her sights set on him?"
        "{image=icon_love.webp} He felt the same":
            $ fian = "smile"
            $ femma = "smile"

            $ ian_emma_love = 1

        "{image=icon_wits.webp} He called her out":
            $ femma = "sad"
            $ fian = "n"

            $ ian_emma_love = 0.5

        "{image=icon_lust.webp} He felt they had great chemistry":
            $ femma = "n"

            $ ian_emma_love = 0

    scene blackbg
    with long
return

label gallVar_ian_emma_dom:
    if ian_summer_look == 0:
        gal "Error: ian_summer_look not defined"
        $ renpy.end_replay()
    $ ian_look = "summer"
    $ emma_hair = "pink"
    if v12_emma_dress == 3:
        $ emma_look = "cool"
    elif v12_emma_dress == 1:
        $ emma_look = 1
    else:
        $ emma_look = "summer"

    $ fian = "smile"
    $ femma = "n"

    scene summerroomnight with long
    with long
    show ian at lef
    show emma at rig
    with short
    menu:
        gal "Did Ian act more dominant towards Emma?"
        "Yes, he degraded her":
            play sound "sfx/dp2.mp3"
            scene v12_emma15_animation with vpunch
            pause 2

            $ ian_emma_dom = 2

        "Yes, he was rough during anal sex":
            scene v12_emma13_animation with fps
            pause 2
    
            $ ian_emma_dom = 1

        "No, he wasn't":
            scene v12_emma16
            with long
            pause 2

            $ ian_emma_dom = 0

    scene blackbg
    with long
return

label gallVar_v12_emma_topless:
    scene beach_full at beach 
    hide screen sea_front
    with long

    $ holly_hair = 1
    $ holly_look = "bikini"
    $ holly_glasses = False #ToDO glasses, issue raised
    $ ian_look = "swim"
    $ emma_look = "bikini"
    $ perry_glasses = False
    $ perry_look = "swim"

    $ femma = "n"
    $ fian = "smile"
    $ fholly = "n"
    $ fperry = "sad"

    show holly at left
    show ian at lef
    show emma at rig
    show perry at right
    show dog at rig3
    with short
    menu:
        gal "Did Ian encourage Emma to go topless?"
        "Yes, he did":
            $ v12_emma_topless = 2
            $ fian = "confident"
            if ian_emma_sex:
                $ femma = "flirt"
            else:
                $ femma = "smile"
            if ian_holly_dating:
                $ fholly = "sad"
            hide emma
            show emmanude at rig behind dog
            $ fperry = "blush"
            pause (2)

        "No, he didn't":
            pass

    scene blackbg
    with long
return

label gallVar_lena_seymour_dating:
    $ flena = "smile"
    $ lena_makeup = 1
    $ lena_look = "wits"
    $ lena_necklace = "seymour"

    $ seymour_look = 1

    scene seymourofficenight
    with long
    show seymour at lef
    show lena2 at rig
    with short
    menu:
        gal "Did Lena sign the contract for Seymour?"
        "Yes, she did":
            $ lena_seymour_dating = True

            scene v9_seymour3
            if lena_tattoo1:
                show v9_seymour3_t1
            if lena_tattoo2:
                show v9_seymour3_t2
            if lena_piercing1:
                show v9_seymour3_p1
            elif lena_piercing2:
                show v9_seymour3_p2
            if v7_necklace_sell == False:
                show v9_seymour3_sy
            with long
            pause (2)

        "No, she refused":
            pass
    scene blackbg
    with long
return

label gallVar_seymour_disposition:
    $ flena = "smile"
    $ fseymour = "smile"
    $ lena_look = "wits"
    $ lena_necklace = "seymour"
    $ seymour_look = 1

    scene seymourofficenight
    with long
    show seymour2 at lef
    show lena2 at rig
    with short
    menu:
        gal "Does Lena like working for Seymour?"
        "Absolutely, she obeys him":
            $ seymour_disposition = 3

        "Yes, she does":
            $ seymour_disposition = 2

        "She's neutral about it":
            $ flena = "n"
            $ seymour_disposition = 1

        "No, she doesn't":
            $ seymour_disposition = 0

            $ fseymour = "n"
            $ flena = "worried"

    scene blackbg
    with long
    $ lena_necklace = False
return

label gallVar_v13_seymour_shoot:
    $ seymour_look = 2
    $ fseymour = "smile"
    $ flena = "smile"
    $ lena_look = "black_lingerie"
    $ lena_makeup = 2

    scene showroom
    with long
    show lenabra at rig
    show seymour2 at lef
    with short
    menu:
        gal "How did Lena behave during Seymour's Vanity Fair shoot?"
        "{image=icon_athletics.webp}She took control":
            $ v13_seymour_shoot = 2

            scene v13_seymour_pose3
            with long
            pause 2

        "{image=icon_wits.webp}She followed Seymour's lead":
            $ v13_seymour_shoot = 1

            scene v13_seymour_pose2
            if lena_piercing1:
                show v13_seymour_pose2_p1
            if lena_piercing2:
                show v13_seymour_pose2_p2
            if lena_tattoo2:
                show v13_seymour_pose2_t2
            if lena_tattoo3:
                show v13_seymour_pose2_t3
            with long
            pause 2
            menu:
                gal "Did she pull Seymour by his tie?"
                "{image=icon_athletics.webp}Yes, she did":
                    scene v13_seymour_pose3
                    with long
                    pause 2

                    $ v13_seymour_shoot = 1.5

                "No, she didn't":
                    pass

        "She refused to pose for the shoot":
            $ v13_seymour_shoot = 0

    if v13_seymour_shoot > 1:
        menu:
            gal "Did she ask Seymour to touch her?"
            "{image=icon_lust.webp}Yes, she did":
                scene v13_seymour_pose3
                show v13_seymour_pose3_hand
                with long
                pause 2

                $ v13_seymour_shoot = 3

            "No, she didn't":
                pass

    scene blackbg
    with long
    $ lena_look = 1
    $ lena_makeup = 0
return

label gallVar_toy_mandingo:
    $ lena_look = 4
    $ flena = "shy"

    scene sexshop
    with long
    show lena at right
    with short
    show toy_mandingo
    with short
    menu:
        gal "Did Lena buy the big black dildo?"
        "{image=icon_pay.webp} Yes, she did":
            $ flena = "flirtshy"
            pause 1

            $ toy_mandingo = True

        "No, she didn't":
            $ flena = "n"

    scene blackbg
    with long
return

label gallVar_toy_badboy:
    $ flena = "shy"
    $ lena_look = 1

    scene sexshop
    with long
    show lena at right
    with short
    show toy_badboy
    with short
    menu:
        gal "Did Lena buy the badboy dildo?"
        "{image=icon_pay.webp} Yes, she did":
            $ flena = "slut"
            pause 1

            $ toy_badboy = True

        "No, she didn't":
            $ flena = "n"

    scene blackbg
    with long
return

label gallVar_lena_analch13:
    scene blackbg
    with long
    if ian_lena_dating:
        scene v6_ian1
        if lena_piercing1:
            show v6_robert1_p1
        elif lena_piercing2:
            show v6_robert1_p2
    elif lena_robert_dating:
        scene v6_robert1
        if lena_piercing1:
            show v6_robert1_p1
        elif lena_piercing2:
            show v6_robert1_p2
    else:
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
                scene v6_ian4b
                with long
            elif lena_robert_dating:
                scene v6_robert5
                show v6_robert5_bunny
                if lena_piercing1:
                    show v6_robert5_p1
                elif lena_piercing2:
                    show v6_robert5_p2
                with long
            else:
                scene v6_mike6_animation
                with long
            pause (2)

        "No, she didn't":
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
            else:
                scene v6_mike6c
                with long
            pause (2)
    scene blackbg
    with long
return