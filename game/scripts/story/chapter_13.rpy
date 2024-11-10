########################################################################################################################################################################################################################################
#### CHAPTER 13 ########################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################

# default lena_arthur = 2             # Lena's friendship stat towards Arthur
# default v13_seymour_shoot = 0       # Lena participates in the shoot with Seymour (1-follow his lead//1.5-follow+necktie//2-necktie//3-ask to be touched)
# default v13_seymour_show = 0        # Lena masturbates for Seymour (3-caught masturbating//2-caught wearing lingerie//1-asked to wear lingerie)
# default v13_seymour_fake = 0        # 2-Lena reaches orgasm//1-Lena fakes it//0-Lena stops (if v13_seymour_show > 0)
# default lena_seymour_sex = False    # Lena has sex with Seymour and fully commits to him

label chapter_thirteen:
    $ save_name = "Lena: Chapter 13"
    $ lena_active = True
    $ ian_active = False

    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0
    if seymour_desire == False:
        jump master_script # findme ---> change to v13lenastart

    call calendar(_month="August", _day="Wednesday", _week=2) from _call_calendar_128

    label gallery_CH13_S01:
        if _in_replay:
            call setup_CH13_S01 from _call_setup_CH13_S01

    $ seymour_look = 2
    $ fseymour = "smile"
    $ flena = "n"
    $ lena_look = "black_lingerie"
    $ lena_wardrobe_lingerie = True
    $ lena_makeup = 2
    $ fagnes = "smile"
    $ lena_necklace = 0
    $ lena_extras = 0

    play sound "sfx/camera.mp3"
    scene v13_seymour_pose1
    if lena_tattoo2:
        show v13_seymour_pose1_t2
    if lena_tattoo3:
        show v13_seymour_pose1_t3
    if lena_piercing1:
        show v13_seymour_pose1_p1
    elif lena_piercing2:
        show v13_seymour_pose1_p2 
    with flash
    play music "music/shooting.mp3" loop
    pause 1
    play sound "sfx/camera.mp3"
    with flash
    pause 1.5
    "The camera flashes dazzled my eyes as I struck yet another a pose."
    "After getting on the plane with Seymour, I now found myself surrounded by a group of elite photographers and high-profile enthusiasts, modeling for them in Rome, in a studio in the heart of the city."
    if lena_travel == "italy":
        "It was such a nice surprise... I had always dreamed of visiting the city, and I could finally do it."
    if lena_travel == "italy" or seymour_disposition > 1:
        "It was my first time traveling for work, and the experience was proving to be both fascinating and memorable."
    else:
        "It was my first time traveling for work, and the experience was proving to be both intriguing and remarkable."
    play sound "sfx/camera.mp3"
    with flash
    pause 1
    "We had likely been at going at this session for about two hours when the final flashes signaled its end."
    # photographers
    scene showroom
    show lenabra 
    with long
    "I rose from the chair, stretching my stiff muscles, as a familiar face approached me."
    if lena_seymour_dating:
        $ fdanny = "smile"
        show danny at lef3 with short
        dan "Thank you, Lena. That was wonderful, as always!"
        dan "I wasn't sure who the model we'd be working with would be, but I'm glad it's you. A very nice surprise indeed!"
        l "Yes, such a coincidence. I had no idea you'd be the one leading this workshop."
        dan "Well, yes, I recently won a rather prestigious photography award, and they offered me the chance to lead it..."
        $ flena = "smile"
        l "Wow, congratulations! I'm glad to see things are going so well for you."
        dan "Likewise..."
        show kent_smile at rig3 with short
        kent "I loved the workshop. Danny, you're a wizard when it comes to lighting. I learned a lot. And Lena, I'm impressed by the sensitivity you bring to your poses..."
        l "Oh, thanks."
        kent "I was wondering if I could book a session with you. I don't mind traveling..."
    else:
        show kent_smile at rig3 with short
        kent "Great work, Lena. Thank you!"
        kent "What a surprise to see you here. I had no clue you'd be the model for this workshop, but I'm glad to work with you again."
        l "Likewise."
        $ fdanny = "n"
        show danny at lef3 with short
        dan "I share the feeling... It's good to see you again, Lena."
        kent "Hey, Danny, great workshop. You're a wizard when it comes to lighting. I learned a lot."
        l "Danny... I had no idea you'd be the one leading this workshop."
        dan "Well, yes, I recently won a rather prestigious photography award, and they offered me the chance to lead it."
        l "Congratulations... I see things are going so well for you."
        dan "Thanks... You seem to be doing pretty alright yourself too, after all!"
        l "I guess..."
        kent "So, Lena, when can I book another session with you? I'd love to work together again..."
    # arthur
    show kent_smile at right 
    show danny at left
    show lenabra at rig
    with move
    $ farthur = "n"
    $ fdanny = "n"
    $ flena = "n"
    show arthur at lef with short
    ar "Well, get in line. I have a feeling a lot of people here will want to ask the same thing... including me, of course."
    l "I'm not sure that's possible... Right now, I'm under an exclusivity contract."
    ar "Of course... You're Seymour's new girl."
    menu:
        "Yes":
            $ renpy.block_rollback()
            hide danny
            hide kent_smile
            with short
            l "Yes, I am. I'm Lena, nice to meet you..."
            $ ar = "{color=#2E2927}Arthur{/color}"
            ar "Arthur."
            l "A pleasure, Arthur."
            call friend_xp ('arthur') from _call_friend_xp_1245
            $ lena_arthur = 3 
            $ farthur  = "smile"
            ar "The pleasure's mine. Seymour's a lucky bastard... He's found himself a real gem. A thing of beauty..."
            jump v13arthurcompliment

        "Have there been others?":
            $ renpy.block_rollback()
            hide danny
            hide kent_smile
            with short
            l "His new girl? Has there been others?"
            ar "Of course. As for how many, I can't say... I haven't known him for that long, I'm afraid."
            $ farthur = "smile"
            ar "But I can see why he might be smitten with you... You're a thing of beauty."
            menu v13arthurcompliment:
                "That's very nice of you":
                    $ renpy.block_rollback()
                    $ flena = "smile"
                    if lena_arthur < 3:
                        l "Oh, that's very nice of you..."
                        ar "Arthur."
                        $ ar = "{color=#2E2927}Arthur{/color}"
                        l "I appreciate the compliment, Arthur. Thanks."
                    else:
                        l "Oh, that's very nice of you... I appreciate the compliment, thanks."
                    if lena_arthur == 3 and lena_charisma < 10:
                        call xp_up ('charisma') from _call_xp_up_1141
                    else:
                        call friend_xp ('arthur') from _call_friend_xp_1246
                        $ lena_arthur = 3
                    ar "You're not only young and beautiful, but sweet too... Just how I like them."
                    menu:
                        "{image=icon_charisma.webp}+{image=icon_lust.webp}Flirt with Arthur" if lena_charisma > 6 and lena_lust > 6:
                            $ renpy.block_rollback()
                            $ flena = "flirt"
                            l "Then I'm glad about that too!"
                            ar "Oh, you are? And why's that?"
                            l "It's always nice being appreciated..."
                            ar "And you also like being told so, don't you?"
                            $ flena = "shy"
                            l "Who doesn't?"
                            ar "You're a feisty one, I see..."
                            call friend_xp ('arthur') from _call_friend_xp_1247
                            $ lena_arthur = 6

                        "...":
                            $ renpy.block_rollback()
                            $ flena = "sad"
                            l "Uh..."

                        "That's gross":
                            $ renpy.block_rollback()
                            $ flena = "serious"
                            l "Ew, what a gross thing to say."
                            call friend_xp ('arthur',-1) from _call_friend_xp_1248
                            $ lena_arthur = 0
                            ar "What's gross about it? You know full well what we like, and you know you have it. That's why you're here..."
                            $ flena = "worried"

                "Thanks":
                    $ renpy.block_rollback()
                    $ flena = "n"
                    l "Thanks..."
                    ar "You're welcome, my dear."

                "...":
                    $ renpy.block_rollback()
                    $ flena = "worried"
                    l "..."
                    call friend_xp ('arthur',-1) from _call_friend_xp_1249
                    ar "What's the matter? Cat got your tongue?"

        "What's that supposed to mean?":
            $ renpy.block_rollback()
            $ flena = "serious"
            hide danny
            hide kent_smile
            with short
            l "And what's that supposed to mean?"
            call friend_xp ('arthur',-1) from _call_friend_xp_1250
            $ lena_arthur = 1
            ar "What, am I mistaken? Are you not his... protegé?"
            l "Him and I have a business relationship... A professional one."
            $ farthur = "smile"
            ar "That's exactly what I meant, darling. No need to get riled up about it."

        "I'm not":
            $ renpy.block_rollback()
            $ flena = "serious"
            hide danny
            hide kent_smile
            with short
            l "No, I'm not. My name's Lena, and I'm my own girl."
            call friend_xp ('arthur',-1) from _call_friend_xp_1251
            $ lena_arthur = 0
            $ farthur = "smile"
            ar "I'm sure you are... But you're here on Seymour's behalf, are you not?"
            l "Him and I have a business relationship... A professional one."
            ar "That's exactly what I meant, darling. No need to get riled up about it."

# seymour and peter 
    $ farthur = "n"
    show lenabra at right
    show arthur at left
    with move
    show seymour at rig
    show peter at lef
    with short
    s "Very nice session, Doll... I see you've already acquainted yourself with Arthur."
    $ ar = "{color=#2E2927}Arthur{/color}"
    if lena_arthur > 2:
        $ flena = "smile"
        l "Yes, he was just giving me his compliments..."
        $ farthur = "smile"
        ar "You deserve every last one of them, {i}\"Doll\"{/i}."
    elif lena_arthur == 2:
        $ flena = "n"
        l "Yes..."
        ar "Sorry, I couldn't wait for you to make the introductions, Seymour. You've gotten yourself a real beauty."
    elif lena_arthur == 1:
        $ flena = "serious"
        l "Yes. He wasted no time in introducing himself."
    elif lena_arthur == 0:
        $ flena = "serious"
        l "Sadly, yes."
        $ farthur = "smile"
        ar "Seems we got off on the wrong foot, didn't we?"
    s "Always the charmer, Arthur..."
    $ farthur = "smile"
    ar "Can't help it, it's in the beast's nature!"
    if lena_arthur < 2:
        $ flena = "sad"
        $ flena = "n"
    $ farthur = "n"
    s "By the way, let me introduce you to Peter Prestley, the future mayor of Baluart."
    $ fpeter = "smile"
    pt "Pleased to finally meet you, Arthur. Seymour has mentioned that you're a man who knows how to do business... and one worth doing business with."
    ar "Indeed. I'm a man who isn't afraid to take risks, as long as there's a good return on my investment."
    pt "I've heard that's exactly how you made your fortune."
    $ farthur = "smile"
    ar "You know what they say: nothing ventured, nothing gained. Fortunately for me, I have both a good nose for business and luck on my side!"
    $ fpeter = "n"
    s "I'm sure you'll find the rewards of our enterprise succulent enough."
    ar "I have no doubts about it. You've already proven you're a man with a criteria I can trust, Seymour... And I'm sure Mr. Prestley is of the same mind."
    show agnes at lef3 with short
    if v6_axel_pose == 1:
        $ flena = "sad"
    ag "Excellent! May Lady Fortuna preside over this meeting of great minds."
    ag "Why don't we celebrate with dinner tonight and discuss the details of our mutual agreements?"
    pt "An excellent proposal."
    s "Without a doubt. I'll see you both tonight then, gentlemen."
    ar "See you later, alligator."
    hide arthur
    hide peter
    with short
    show lenabra at rig3
    show seymour at truecenter 
    with move
# agnes/photo shoot + comment on necklace
    if v6_seymour_shoot or v6_agnes_shoot:
        ag "Well, well. We meet again..."
        l "Lena."
        if v6_axel_pose == 3:
            ag "Of course. Lena. How could I forget such a lovely model? The pictures from that photo shoot have given me much pleasure. The results really captured my imagination..."
            $ flena = "blush"
        elif v6_axel_pose == 2:
            ag "Of course. Lena. How could I forget such a lovely model? I remember enjoying that photo shoot quite a bit."
            $ flena = "blush"
        elif v6_axel_pose == 1:
            ag "Of course. Lena... How could I forget your bold rebelliousness? I hope Seymour has managed to instill some good sense into you..."
    else:
        ag "And what about your lovely model? We've been introduced before, have we not?"
        s "I believe we crossed paths at the restaurant, once. This is Lena. Lena, this is Agnes Addingworth..."
        if lena_posh > 2:
            $ flena = "smile"
            if lena_posh > 3:
                l "I'm so thrilled to meet you, Ms. Addingworth. You're such a celebrated fashion icon..."
            else:
                l "I know about you, Ms. Addingworth... You're a very celebrated fashion icon."
            ag "Always happy to meet an admirer."
        else:
            s "I'm sure you're already familiar with her name and her celebrated fashion brand."
            l "I've heard about it..."
        ag "I see you're wearing a piece I designed recently. I'm quite proud of that gold and onyx necklace..."
        l "It was a gift from Seymour."
        ag "I must admit it really suits you. I must commend you for your good taste, Seymour..."
    show lenabra at right
    show seymour at rig 
    show agnes at lef
    with move   
    show danny at left with short
    dan "Excuse me, Mr. Ward. The room is cleared. Shall we get the shoot started?"
    $ flena = "n"
    s "Give me a moment. I believe Agnes had the courtesy of bringing a special outfit for this occasion..."
    ag "Oh, you're going to love the suit I made for you. Let me fetch it."
    dan "Ready when you are."
    hide danny 
    hide agnes
    with short
    show seymour at lef
    show lenabra at rig
    with move
    l "I thought we were finished... Another photo shoot?"
    s "Yes, but this time it's my turn to be in front of the camera."
    s "Turns out Vanity Affair magazine is publishing a feature on me, and they requested some photographs to accompany the article."
    if seymour_disposition > 1:
        $ flena = "happy"
        l "Really? Vanity Affair? That's amazing! Congratulations!"
        s "Thanks, Doll."
    elif seymour_disposition == 1:
        l "Oh, really? Congratulations..."
    else:
        $ flena = "sad"
        l "They're publishing an article about you?"
    s "I'm not someone who usually seeks media attention, but this is a prestigious magazine, and they've taken an interest in my work within the editorial and business worlds..." 
    s "I made them persist a bit, but I believe it could be advantageous for my reputation."
    show lenabra at rig3
    show seymour at truecenter
    with move
    show agnes at lef3 with short
    $ flena = "n"
    ag "You do love playing hard to get, my dear Seymour... Don't shy away from the spotlight, you're the kind of man who shines in it, and you know it."
    s "Especially when I'm wearing one of your exquisite suits, without a doubt."
    ag "Here, try it on... It should fit you like a glove."
    l "I'll go get changed then..."
    s "Hold on, Doll. I'd like you to join me in a few of the photos."
    if seymour_disposition > 1:
        $ flena = "smile"
        l "Really? But this article is about you..."
        s "And I'm proud to have you by my side. I'm inclined to let the world know."
        ag "Oh my, he's really smitten with you, darling. You're such a lucky young lady."
        $ flena = "shy"
        s "So, are you willing to participate?"
        jump v13syshootyes
    else:
        if seymour_disposition == 1:
            l "Oh... Me? Are you sure?"
            s "Of course. I'm proud to have you by my side, and I'm inclined to let the world know."
            ag "Oh my, he's really smitten with you, darling. You're such a lucky young lady."
            $ flena = "blush"
        else:
            $ flena = "sad"
            l "Me? Why?"
            s "I'm proud to have you by my side, and I'm inclined to let the world know."
            ag "Oh my, he's really smitten with you, darling. You're such a lucky young lady."
            $ flena = "worried"
        s "So, what do you say?"
        menu:
            "{image=icon_friend.webp}I'm honored" if seymour_disposition == 1:
                $ renpy.block_rollback()
                $ flena = "shy"
                label v13syshootyes:
                    $ v13_seymour_shoot = True
                l "Of course... I'm honored."
                if lena_seymour < 12:
                    call friend_xp('seymour') from _call_friend_xp_1252
                ag "I like her attitude... This might end up being a good idea after all."
                call friend_xp('agnes') from _call_friend_xp_1253
                ag "Alright, step aside darling." 
                hide lenabra with short
                ag "Seymour, let's get you changed..."

            "Alright":
                $ renpy.block_rollback()
                $ v13_seymour_shoot = True
                $ flena = "n"
                l "Alright... I can do that."
                ag "Good. Now, step aside darling." 
                hide lenabra with short
                ag "Seymour, let's get you changed..."

            "{image=icon_mad.webp}Do I have a choice?" if seymour_disposition < 1:
                $ renpy.block_rollback()
                $ flena = "serious"
                l "Do I have a choice?"
                $ fseymour = "n"
                $ fagnes = "mad"
                s "You know you do. The terms of the contract are clear, aren't they?"
                s "I'd like you to participate, but you're not under any obligation."
                ag "This is not a chance you let slide, girl."
                call friend_xp('agnes',-1) from _call_friend_xp_1254
                menu:
                    "I'll do it":
                        $ renpy.block_rollback()
                        $ v13_seymour_shoot = True
                        $ flena = "sad"
                        l "Alright then, if that's the case... I can do it."
                        $ fagnes = "n"
                        $ fseymour = "smile"
                        s "Good. I was hoping you would."
                        if lena_seymour < 12:
                            call friend_xp('seymour') from _call_friend_xp_1255
                        ag "Alright, step aside darling."
                        hide lenabra with short
                        ag "Seymour, let's get you changed..."

                    "I won't do it":
                        $ renpy.block_rollback()
                        stop music fadeout 4.0
                        l "Well then, if that's the case... I'd rather not take part."
                        $ fagnes = "n"
                        ag "It's alright, we don't need her. Let's get you changed..."
                        call friend_xp('seymour',-1) from _call_friend_xp_1256


            "I'd rather not do it":
                $ renpy.block_rollback()
                stop music fadeout 4.0
                $ flena = "sad"
                l "Actually... I'd rather not do it, if that's possible."
                call friend_xp('seymour',-1) from _call_friend_xp_1257
                $ fseymour = "n"
                $ fagnes = "mad"
                ag "This is not a chance you let slide, girl."
                call friend_xp('agnes',-1) from _call_friend_xp_1258
                l "As you yourself said, I'm not someone who really enjoys exposure... Not in these kinds of contexts."
                s "That's a weird thing to hear you say, Doll, but if that's how you feel... I'd like you to participate, but you're not under any obligation."
                $ fagnes = "n"
                ag "It's alright, we don't need her. Let's get you changed..."
    
# seymour posing
    stop music fadeout 2.0
    hide seymour
    hide agnes
    with long
    if v13_seymour_shoot == False:
        hide lenabra with short
    pause 1
    play music "music/seymours_theme.mp3" loop
    $ fseymour = "smile"
    $ seymour_look = 3
    show seymour2 with long
    s "How do I look?"
    show agnes at right with short
    ag "You look magnificent, dear! I knew these regal colors would fit you perfectly."

# LENA + SEYMOUR POSING #############################################################################################################################################################################################
    if v13_seymour_shoot:
        s "Let's get this started, then. I have no experience in posing, so I hope you can help ease me into it, Lena."
        show seymour2 at lef with move
        show lenabra at rig with short
        if seymour_disposition > 1:
            $ flena = "smile"
            l "Of course!"
        else:
            l "Sure..."
        hide agnes with short
        kent "Let's begin with some simple poses. Stand together in front of the camera..."
        hide seymour2
        show seymour at lef
        with long
        $ fseymour = "n"
        $ flena = "n"
        pause 0.5
        play sound "sfx/camera.mp3"
        with flash
        "Seymour confidently stood beside me, posing for the camera. Despite claiming to be inexperienced, he didn't look nervous or uncomfortable at all."
        kent "That's good. Let me take one more... Lena, can you interact with him a bit?"
        $ fseymour = "smile"
        if seymour_disposition > 1:
            $ flena = "smile"
        elif seymour_disposition == 0:
            $ flena = "sad"
        hide seymour
        show seymour2 at lef
        with short
        "Seymour glanced at me with his blue eyes and smiled."
        s "Is it okay if I touch you?"
        if seymour_disposition > 0:
            "He was following the terms of our contract: he couldn't touch me without my explicit permission..."
        else:
            "Per our contract, he couldn't touch me without my explicit permission... At least he was following the terms with diligence."
        menu:
            "{image=icon_wits.webp}Follow Seymour's lead": # (no req. just cool icon to contrast with below)
                $ renpy.block_rollback()
                $ v13_seymour_shoot = 1
                if seymour_disposition > 1:
                    l "Of course."
                elif seymour_disposition > 0:
                    l "It's alright."
                    "I didn't see any reason why I should object, so I acted professionally, like it was expected of me."
                else:
                    $ flena = "n"
                    l "It's alright..."
                    "I doubted he would try any funny business in front of the camera... Though it didn't seem like that was his intention anyway."
                # seymour 1 - holding hands
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
                pause 1
                "Seymour turned toward me and gently took my hands."
                kent "Perfect..."
                play sound "sfx/camera.mp3"
                with flash
                "His chest was close to mine, and his pleasant scent filled my nostrils."
                if seymour_disposition > 0:
                    "I felt my heart start to race. Until now, I had never been this close to Seymour. I had never felt the delicate touch of his hands like this before..."
                elif seymour_disposition > 0:
                    "It was the first time Seymour had gotten so close to me. The way he held was hands was delicate and not unpleasant at all..."
                else:
                    "I didn't feel entirely comfortable with how close Seymour was... Yet, his touch was delicate and not unpleasant at all."
                if lena_seymour < 12:
                    call friend_xp ('seymour') from _call_friend_xp_1259
                "I let Seymour guide me while Kent kept snapping photos, until I felt it was my turn to take the lead. I was the professional here, after all..."
                menu:
                    "{image=icon_athletics.webp}Pull Seymour by his tie" if lena_athletics > 4 or seymour_disposition > 1:
                        $ renpy.block_rollback()
                        $ v13_seymour_shoot = 1.5
                        jump v13sytakecontrol

                    "Sit Seymour down":
                        $ renpy.block_rollback()
                        scene v13_seymour_pose4b
                        if lena_tattoo1:
                            show v13_seymour_pose4_t1
                        with long
                        pause 1
                        "I held Seymour by the shoulders and made him sit in the chair I had been using during the shoot."
                        jump v13sychair

                    "...":
                        $ renpy.block_rollback()
                        if seymour_disposition > 0:
                            $ flena = "blush"
                        else:
                            $ flena = "sad"
                        $ fseymour = "n"
                        scene showroom
                        show lenabra2 at rig
                        show seymour2 at lef
                        with long
                        l "..."
                        if seymour_disposition > 0:
                            "I had let myself get caught up in the moment, and my mind went blank..."
                        elif seymour_disposition > 0:
                            "I wasn't exactly sure how to follow up. I felt a bit lost in that situation..."
                        else:
                            "I wasn't exactly sure how to follow up. This situation had me feeling a bit awkward..."
                        kent "Try sitting on the chair now. Look directly into the camera..."
                        scene v13_seymour_pose4
                        with long
                        pause 1
                        s "Like this?"
                        kent "That's it!"
                        play sound "sfx/camera.mp3"
                        with flash
                        ag "You're a natural at this, my dear!"
                        kent "Lena, why don't you try getting behind and leaning over?"
                        scene v13_seymour_pose4b
                        if lena_tattoo1:
                            show v13_seymour_pose4_t1
                        with long
                        pause 1
                        l "Sure..."
                        jump v13sychair
        
            "{image=icon_athletics.webp}Take control" if lena_athletics > 4 or seymour_disposition > 1:
                $ renpy.block_rollback()
                $ v13_seymour_shoot = 2
                if seymour_disposition > 0:
                    l "You could, if I said yes... But I'm gonna withhold it for a bit longer."
                else:
                    l "That won't be necessary..."
                label v13sytakecontrol:
                    # lena takes control
                    scene v13_seymour_pose3
                    with long
                    pause 1
                "I grabbed Seymour by the tie and gave it a quick, sharp tug. I could see the surprise on his face for a moment, then he smiled."
                l "There was nothing in our contract about me needing permission to touch you, was there?"
                s "I didn't believe it to be necessary..."
                play sound "sfx/camera.mp3"
                with flash
                if lena_charisma < 10:
                    call xp_up ('charisma') from _call_xp_up_1142
                "We turned our attention back to the camera. Kent was now working quietly, letting us lead the shoot."
                menu:
                    "{image=icon_lust.webp}Ask Seymour to touch you" if (lena_lust > 6 and seymour_disposition > 1) or (lena_lust > 7 and seymour_disposition > 0) or seymour_disposition > 2:
                        $ renpy.block_rollback()
                        if v13_seymour_shoot == 2:
                            l "The permission you were asking me... I'm giving it to you."
                            l "Go ahead and touch me..."
                        else:
                            l "I already gave you permission to touch me, so... Why don't you do it?"
                        show v13_seymour_pose3_hand with long
                        pause 1
                        "I felt Seymour's hand slide along my waist in a caress, settling a bit lower."
                        play sound "sfx/camera.mp3"
                        with flash
                        if seymour_disposition > 1:
                            "As his hand moved lower, I couldn't help but be drawn to him even more. The way he carried himself, the quiet authority in his actions..."
                            "It stirred something deep inside me. I wanted to impress him, to prove I was worthy of his attention, but at the same time, I felt the intoxicating pull of surrender."
                            "Seymour and I were engaged in a subtle game, one that was equally alluring and risky to me... A game I was happy to play."
                        else:
                            "My body leaned into him instinctively, but my heart raced with uncertainty."
                            "I felt the pull between wanting to give in and the nagging thought of crossing a line I wasn't sure I was ready for."
                            "Seymour and I were engaged in a subtle game, one that was equally tempting and dangerous to me... A game I had chosen to play."
                        scene v13_seymour_pose4b
                        if lena_tattoo1:
                            show v13_seymour_pose4_t1
                        with long
                        pause 1
                        "In this moment, I was calling the shots, and Seymour willingly followed my lead when I held him by the shoulders and made him sit in the chair I had been using during the shoot."
                        $ v13_seymour_shoot = 3
                        jump v13sychair

                    "Sit Seymour down":
                        $ renpy.block_rollback()
                        scene v13_seymour_pose4b
                        if lena_tattoo1:
                            show v13_seymour_pose4_t1
                        with long
                        pause 1
                        "I held Seymour by the shoulders and made him sit in the chair I had been using during the shoot."
                        label v13sychair:
                            play sound "sfx/camera.mp3"
                            with flash
                        if v13_seymour_shoot == 3 or seymour_disposition > 1: # touch ass
                            "Seymour was letting me take charge, his eyes watching me with a mixture of curiosity and something darker... Anticipation. My pulse quickened, knowing I had his full attention."
                            "I moved behind him, letting my hands glide down his chest as I leaned over his shoulder, gently resting my head against his."
                            "Every movement, every glance, was deliberate now. The admiration I felt for Seymour swirled with a new kind of desire: to show him I could match his confidence and strength."
                        elif v13_seymour_shoot > 1 or seymour_disposition > 0: # pull tie
                            "Seymour was letting me take charge, his eyes watching me with a mixture of curiosity and something darker... Anticipation."
                            "I moved behind him, letting my hands glide down his chest as I leaned over his shoulder, gently resting my head against his."
                            "Every movement, every glance, was deliberate now. I wanted to show Seymour I could match his confidence and strength."
                        else: # follow lead
                            "I moved behind Seymour, letting my hands glide down his chest as I leaned over his shoulder, gently resting my head against his."
                            "I had to earn my paycheck..."
                        play sound "sfx/camera.mp3"
                        with flash

        pause 1.5
        scene showroom with long
        "After a few more photos, both Seymour and Kent seemed satisfied and called the shoot to a close."
        "They stayed to review the shots and gave me permission to go get changed."
        $ renpy.end_replay()
        $ gallery_unlock_scene("CH13_S01")

# SEYMOUR ALONE
    else:
        s "Let's get this started, then. I have no experience posing, so bear with me."
        show kent at left with short
        kent "No problem, Mr. Ward. Let's start with a few warm-up shots..."
        $ fseymour = "n"
        hide seymour2
        show seymour
        with short
        play sound "sfx/camera.mp3"
        with flash
        pause 1
        kent "That's good... Let's try with a more interesting pose now."
        scene v13_seymour_pose4 with long
        pause 1
        play sound "sfx/camera.mp3"
        with flash
        ag "You're a natural at this, my dear!"
        "Thankfully they left me out of this... I didn't want to draw too much attention to my professional relationship with Seymour, and being featured with him in an article definitely wouldn't help."
        scene showroom with long
        "I left them to their own devices and went to get changed."
        $ renpy.end_replay()
# give the necklace back
    $ flena = "n"
    if lena_wardrobe_charisma1:
        $ lena_look = "charisma"
    elif lena_wardrobe_wits1:
        $ lena_look = "wits"
    else:
        $ lena_look = 3
    if v12_gift == "lena" and ian_lena_pure:
        $ lena_necklace = "gift"
    elif seymour_disposition > 1 or lena_posh > 4:
        $ lena_necklace = "seymour"
    $ fseymour = "smile"
    show lena at right with long
    show agnes at left
    show seymour at rig
    show kent at lef
    with long
    if v13_seymour_shoot == False:
        kent "Alright, I think this should do it. I got some really nice shots!"
        s "Good. Thanks for your labor, Kent."
    else:
        s "There are some good shots indeed... Thanks for your labor, Kent."
    kent "It's my pleasure, Mr. Ward. I hope we can work together again."
    hide kent with short
    show seymour at truecenter
    show agnes at lef3
    show lena at rig3
    with move
    ag "Turns out you have a gift for this too, dear, though it's no surprise. You've always had a commanding presence."
    s "Always so kind, Agnes. No doubt the suit you made for me has contributed greatly to that."
    s "Which reminds me..."
    if lena_necklace == "seymour":
        s "Your necklace, Doll... Would you mind returning it to Agnes?"
    elif lena_necklace == "gift":
        s "Your necklace, Doll... Would you mind returning it to Agnes?"
        $ flena = "worried"
        l "My... necklace?"
        $ fseymour = "n"
        s "Huh. Not this one... What's that you're wearing?"
        $ flena = "sad"
        l "It's a gift..."
        ag "Well, it's a tacky trinket, dear. You can spot it a mile away."
        s "Did you bring with you the necklace I gave you?"
        $ flena = "n"
        l "Yes, it's in my bag."
        s "Go fetch it, please. I'm afraid Agnes wants it back."
    else:
        $ fseymour = "n"
        s "Lena, the necklace I gave you... Do you have it?"
        l "I do..."
        ag "Well, where is it? Did you pack it in your luggage?"
        $ flena = "sad"
        l "Yes... I think it's in my bag."
        s "Go fetch it, please. I'm afraid Agnes wants it back."
    if lena_posh > 3 or seymour_disposition > 1:
        $ flena = "sad"
    else:
        $ flena = "n"
    menu:
        "I thought it was a gift":
            $ renpy.block_rollback()
            if lena_posh < 4:
                $ lena_posh += 1
            $ flena = "worried"
            l "But I thought it was a gift..."
            $ fagnes = "flirt"
            ag "Oh, I see you're quite fond of that jewel! Good. But won't you trust the creator of the piece with it?"
            s "Don't worry, Doll. You'll get it back."
            $ flena = "sad"
            $ fagnes = "smile"
            l "If that's the case... Alright."
            call friend_xp ('agnes') from _call_friend_xp_1260
            if lena_necklace == "seymour":
                show lena_sy_collar at rig3 
                $ lena_necklace = 0
                hide lena_sy_collar with short
            else:
                show lena at right with move
                hide lena with short
                pause 0.5
                show lena at rig3 with short
                l "Here."

        "What for?":
            $ renpy.block_rollback()
            l "What for?"
            $ fagnes = "n"
            ag "That's not something you should concern yourself with. Don't you trust the creator of the piece with it?"
            if lena_agnes > 0:
                call friend_xp ('agnes',-1) from _call_friend_xp_1261
            l "Uh... Alright."
            if lena_necklace == "seymour":
                show lena_sy_collar at rig3 
                $ lena_necklace = 0
                hide lena_sy_collar with short
            else:
                show lena at right with move
                hide lena with short
                pause 0.5
                show lena at rig3 with short
                l "Here."
            s "Don't worry. You'll get it back."
            $ fagnes = "smile"

        "Of course":
            $ renpy.block_rollback()
            if lena_posh > 3 or seymour_disposition > 1:
                l "Of course..."
            else:
                l "Of course."
            if lena_necklace == "seymour":
                show lena_sy_collar at rig3 
                $ lena_necklace = 0
                hide lena_sy_collar with short
            else:
                show lena at right with move
                hide lena with short
                pause 0.5
                show lena at rig3 with short
                l "Here."

    $ flena = "n"
    ag "We just launched this piece on the market, and it's causing quite a stir... The one you have is a tad more unique, being the prototype."
    ag "Anyway, I have some chores I need to attend to before dinner! I'll have the pleasure of seeing you again shortly, dear Seymour."
    s "Goodbye for now, Agnes."
    hide agnes with short
    show seymour at lef
    show lena at rig
    with move
    s "Alright, that's done. On to other matters now..."
    
#############################################################################################################################################################################################
# SEYMOUR TALK #############################################################################################################################################################################################
#############################################################################################################################################################################################

    if lena_travel == "italy":
        s "So, how are you liking your first time experiencing Rome? I know it was your dream destination."
        s "You must be thrilled."
    else:
        s "Tell me, had you ever been in Rome before?"
        l "No..."
        s "And how are you liking your first-time experience? Thrilling?"
    menu:
        "Yes!":
            $ renpy.block_rollback()
            if lena_travel == "italy":
                $ flena = "happy"
                l "Yes, absolutely! I've been wanting to visit this city since my student years, but never got the chance. All the plans I made ended up falling apart, for some reason or another..."
                s "Well, here you are, and in a good position to enjoy what this historic city has to offer. And you'll surely get the chance to come here again, as often as you like."
            else:
                $ flena = "smile"
                l "Yes, absolutely... I never got the chance to come here as a student, and always wondered what that would be like..."
                s "Well, here you are, and in a good position to enjoy what this historic city has to offer."
                if lena_travel == "dubai":
                    s "I know your dream destination is Dubai, but you'll have the opportunity to visit the city anytime you want."
                elif lena_travel == "japan":
                    s "I know your dream destination is Japan, but you'll have the opportunity to visit the country anytime you want."
            $ flena = "smile"
            l "That's good to know..."
            if lena_seymour < 12:
                call friend_xp ('seymour') from _call_friend_xp_1262
            elif lena_charisma < 10:
                call xp_up ('charisma') from _call_xp_up_1143
            s "Well, you'll have time to explore the city all you want in a moment. As you heard, I have business to attend to today."
            stop music fadeout 3.0
            s "But before I cut you loose, I want you to join me for a coffee."
            l "Of course."

        "...":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "..."
            $ fseymour = "n"
            s "So thrilling it's left you speechless, I see."
            $ flena = "n"
            l "No, sorry... I'm just feeling a bit tired after the trip and the photo shoot."
            $ fseymour = "smile"
            s "I understand... Well, you'll have time to relax and enjoy yourself this afternoon."
            stop music fadeout 3.0
            s "As you heard, I have business to attend to today, but before I cut you loose, join me for a coffee. I'm sure you could use one."
            l "I could."

        "Not really":
            $ renpy.block_rollback()
            if seymour_disposition > 1:
                $ flena = "sad"
                l "I wouldn't use the word thrilled... I mean... This is a business trip, after all."
            else:
                l "I wouldn't use the word thrilled... I mean, I'm here to work. This is a business trip, after all."
            $ fseymour = "n"
            if lena_travel == "dubai":
                s "That may be so, but that shouldn't prevent you from enjoying your stay here. I know your dream destination is Dubai, but you'd do well in appreciating the beauty of this city."
            elif lena_travel == "japan":
                s "That may be so, but that shouldn't prevent you from enjoying your stay here. I know your dream destination is Japan, but you'd do well in appreciating the beauty of this city."
            elif lena_travel == "italy":
                s "That may be so, but that shouldn't prevent you from enjoying your stay here, especially since you seemed so eager to visit Italy."
            call friend_xp ('seymour',-1) from _call_friend_xp_1263
            l "I guess I'm just feeling tired from all the traveling and the photo shoot. It's been a bit stressful."
            s "I see... Well, you'll have time to relax and enjoy yourself this afternoon. As you heard, I have business to attend to today."
            l "Sure..."
            $ fseymour = "smile"
            stop music fadeout 2.0
            s "Join me for a coffee before I cut you loose. You surely are in need of one."
            $ flena = "n"
            l "Alright..."

    scene romestreet with long
    play music "music/calm.mp3" loop
    if lena_look == "charisma":
        "We sat on the terrace of a cozy spot with an upscale clientele. We fit right in."
    elif lena_look == "wits":
        "We sat on the terrace of a cozy spot with an upscale clientele. We blended in well, though I felt a bit underdressed for the occasion..."
    elif lena_look == 3:
        "We sat on the terrace of a cozy spot with an upscale clientele. I felt quite underdressed for the occasion... Maybe I should've packed more elegant clothes."
    show lena2 at rig
    show seymour at lef
    with short
    s "I see you've made quite an impression on the workshop attendees. Many renowned photographers have taken notice of you, and I'm sure they'll want to work with you."
    l "Too bad I have an exclusivity contract with you, right?"
    s "For now, that's right. And I hope it lasts."
    if seymour_disposition > 1:
        l "I do too."
    elif seymour_disposition == 1:
        l "If everything goes well, I don't see why it shouldn't..."
    else:
        l "That remains to be seen."
    l "I see your trip here isn't just for a photography workshop. Anything else you've been keeping from me, besides the magazine article?"
    if v13_seymour_shoot == False:
        $ fseymour = "n"
        s "Such a shame you refused to take part in it. But no, aside from the business dinner I have scheduled, my only other reason is to enjoy your company."
    else:
        s "Well, aside from the business dinner I have scheduled, my only other reason is to enjoy your company."
    if seymour_disposition > 0:   
        if seymour_disposition > 1:
            l "I see... And what do you enjoy most about my company?"
            s "The conversations, without a doubt. You're a sharp and captivating conversationalist."
            $ flena = "n"
            l "The same goes for you, but you know that already..."
            $ flena = "sad"
        elif seymour_disposition == 1:
            s "I always find our conversations stimulating and captivating. You have a sharp mind, and I know you have the sensitivity  to see things for what they really are."
        if v3_seymour_date:
            l "During our first dinner together, I asked you why you wanted to work with me."
            l "You simply said I suited your taste, but I know you must've had other reasons. You could've chosen any other girl, models much more renowned than a nobody like me..."
        else:
            l "I've been wanting to ask you something... You went out of your way to have me work with you, and I can't help but wonder why."
            l "I know you could have chosen any other girl, models much more renowned than a nobody like me..."
        s "I saw something in you, obviously. Something special."
        l "And what's that?"
    else:
        l "And by that you mean...?"
        $ fseymour = "n"
        s "There's no need to be deliberately obtuse... You have a sharp mind, and I know you're able to see things for what they really are."
        l "Still, I'm not sure what you enjoy about my company so much."
        $ fseymour = "smile"
        s "The conversations, for one. You're challenging and stubborn, but I know you're not lacking in sensitivity and can see things for what they truly are."
        $ flena = "serious"
        l "Is that the reason you became so interested in me, despite me being a nobody? Because I was defiant to you?"
        $ fseymour = "n"
        s "Maybe that was part of it, if I have to be honest. But it's not your resistance what drew me to you in the first place. It's what I saw in you."
        l "And what was that?"
    # seymour on what lena means to him
    $ fseymour = "n"
    s "I find it difficult to put into words... Truthfully, I'm still uncertain about what exactly drew me to you."
    if seymour_disposition > 1:
        $ flena = "worried"
        l "Seriously? I know you well enough to realize you don't do things without a reason."
    elif seymour_disposition == 1:
        $ flena = "sad"
        l "You're uncertain...? I find that difficult to believe. You're not someone to do things without a reason, after all."
    else:
        l "Do you expect me to believe that answer...? I'm sure you know your reasons well, you just don't want to explain them to me."
    $ fseymour = "smile"
    s "You must think I value reason above all else, and that logic drives all my actions, but that's not the case..."
    if seymour_disposition < 1:
        l "So, are you saying that your motives behind all of this are irrational?"
    s "I'm a firm believer that there are things that the intellect cannot grasp."
    s "There are pivotal moments in life when a man must let himself be guided by intuition, and that's what I did."
    if seymour_disposition > 1:
        $ flena = "blush"
    else:
        $ flena = "sad"
    s "That's why you fascinate me so much, Lena... From the moment I saw you, I wanted you to reveal yourself to me."
    if seymour_disposition > 0:
        if seymour_disposition > 1:
            $ flena = "shy"
            l "That's... I don't know what to say. I wasn't expecting that to be your answer..."
        elif seymour_disposition == 1:
            $ flena = "n"
            l "I wasn't expecting that to be your answer, honestly..."
    else:
        s "If all I cared about was projecting myself in someone else, I could've chosen anyone. But I chose you."
    if lena_arthur > 2:
        $ flena = "n"
        l "Your friend Arthur mentioned something about your other \"companions\". I see I'm not the first girl you've taken under your wing."
    elif lena_arthur > 0:
        $ flena = "n"
        l "That man, Arthur, mentioned something about your other \"companions\". I see I'm not the first girl you've taken under your wing."
    else:
        $ flena = "sad"
        l "That unpleasant man from earlier mentioned something about your other \"companions\". I see I'm not the first girl you've taken under your wing."
    $ fseymour = "smile"
    s "Does it surprise you?"
    $ flena = "n"
    if v11seydinner3:
        l "Not really, but I wonder... You told me you never got married, but you fell in love once. It sounded like that happened a long time ago, though."
        s "Very perceptive of you. Yes, it was a long time ago, way before the first gray hairs started appearing in my beard."
        l "And none of the women you've met since then have stirred your feelings?"
        $ fseymour = "n"
        s "I found a good deal of them to be rather vapid or tedious. Others were more interesting, but as you say, they didn't manage to really stir my emotions."
    else:
        l "Not really, but I'm curious... Do you have any family? Did you ever get married?"
        $ fseymour = "n"
        s "No, I never did... Never had any offspring, either. My focus was always on other matters."
        l "So you never fell in love?"
        s "I did... Just once, but it was a long time ago. I'm afraid none of the women I've met since then have managed to really stir my emotions."
    menu:
        "{image=icon_friend.webp}What about me?" if seymour_disposition > 0:
            $ renpy.block_rollback()
            l "What about me? Do I stir your emotions?"
            $ fseymour = "smile"
            s "Better than anyone I know."
            if lena_charisma < 10:
                call xp_up ('charisma') from _call_xp_up_1144
            if seymour_disposition > 1:
                $ flena = "shy"
                l "I see... So you're revealing yourself to me too, little by little."
            elif seymour_disposition == 1:
                $ flena = "smile"
                l "Well, seems like you're also revealing yourself to me too, little by little."
            l "You come across as a man fully in control of his emotions, but I'm glad to see there are cracks in the armor after all."
            s "Of course. No matter how rational you claim to be, there's an emotional side to humans that can't be denied."
            s "We can try to free ourselves by being aware of it, but we're destined to desire."

        "Is that what you're looking for?":
            $ renpy.block_rollback()
            l "So that's what you're looking for? Someone who stirs your emotions?"
            s "Sometimes I think I do. One is hardly free to choose his desires, after all."
            if seymour_disposition > 0:
                l "I think it's just in human nature, is it not? We're more emotional than we are rational, at least most of us."
            else:
                l "You're human, after all... No matter how rational you claim to be, there's an emotional side that can't be denied."
            $ fseymour = "smile"
            s "On that we can agree. We can try to free ourselves by being aware of it, but we're destined to desire."

        "That seems difficult":
            $ renpy.block_rollback()
            l "Well, that sounds like a difficult task to accomplish."
            if seymour_disposition > 0:
                s "That's what you think? I know I might appear cold, but I believe you know me better than that already."
                if lena_seymour > 0:
                    call friend_xp ('seymour',-1) from _call_friend_xp_1264
                $ flena = "worried"
                l "I didn't mean it like that... It's just you seem to always be in control and have a firm grip on your emotions."
                $ fseymour = "smile"
                s "I try, but I'm still human after all. No matter how rational you claim to be, there's an emotional side that can't be denied."
            else:
                s "You're pretty good at it, even though you love trying to get a rise out of me."
                $ flena = "sad"
                if lena_seymour > 0:
                    call friend_xp ('seymour',-1) from _call_friend_xp_1265
                l "That's... I guess it makes me feel better knowing you don't have absolute control over everything, not even over yourself."
                s "Is that so? You're after the cracks in the armor, but I don't blame you."
                $ fseymour = "smile"
                s "No matter how rational you claim to be, there's an emotional side to humans that can't be denied. And I'm no different."
                $ flena = "n"
            s "We can try to free ourselves by being aware of it, but we're destined to desire."

    # if v3_seymour_date:
    #     "Lena ask about charles"
    # else:
    #     "Sy tells about charles"
    $ fseymour = "n"
    s "Which reminds me... What's the name of that activist friend of yours? The one who was kind enough to throw a drink on me?"
    $ flena = "worried"
    if v11_emma_date:
        if lena_emma > 7:
            l "You mean Emma...? She's a nice girl, it's just..."
        else:
            l "That'd be Emma... Why?"
    else:
        l "You mean Emma? We're not that close..."
    s "She's one of the people who's been stirring up the hornet's nest in Baluart, right? And from what I understand, she has close ties to Mayor Vermeer."
    $ flena = "sad"
    l "Well, she's friends with Perry, his son. But beyond that, I don't think she has much to do with the current mayor."
    $ fseymour = "smile"
    s "It's clear we got off on the wrong foot, but I'm sure she can be reasoned with. I'd like to smooth things over, considering she's someone in your circle."
    s "Could you extend an invitation for her to meet with me when we're back in the city?"
    if v11_emma_date:
        l "I guess I could, though I don't think she'll be too inclined to accept..."
    else:
        $ flena = "n"
        l "As I said, we're not that close, but if that's what you want... I can tell her, though I don't think she'll be too inclined to accept..."
    s "That's all I ask. At least they won't be able to blame me for not attempting to open a dialogue... Thanks, Lena."
    s "Anyway, I have to leave you. You've got the afternoon to do as you please, and if you're up for it, there's a restaurant I'd like to take you to tomorrow at noon."
    if seymour_disposition > 1:
        l "Sounds perfect. I hope your dinner goes well."
        s "Thanks, Doll. Business calls."
    elif seymour_disposition > 0:
        l "Sounds good. Enjoy your dinner."
        s "Business calls."
    else:
        l "Alright..."
    hide seymour with short
    show lena2 at truecenter with move
    hide lena2
    show lena
    with short
    if seymour_disposition > 1:
        l "I feel he's letting his guard down with me more and more... I feel I'm starting to see the man behind the suit."
    elif seymour_disposition > 0:
        l "That was... different. It felt like he was letting his guard down with me, in a way..."
        l "This man is a mystery."
    else:
        $ flena = "worried"
        l "That was... weird. It felt like he was maybe trying to open up to me, in a way...?"
        $ flena = "sad"
        l "I shouldn't let my guard down around him, I know that much. I'm sure he has more \"surprises\" coming my way."
    $ flena = "n"
    l "Anyway... What should I do with my afternoon?"
    menu:
        "Visit a museum":
            $ renpy.block_rollback()
            "I took the chance to visit one of the city's most renowned museums. I had been looking forward to seeing the ancient artworks they preserved, ones I had studied in art history."
            hide lena
            with long
            if lena_wits < 10:
                call xp_up ('wits') from _call_xp_up_1145
            stop music fadeout 2.0
            "When the museum closed, I stopped for dinner at a cozy Italian restaurant and headed back to my hotel, eager for a hot bath. It had been a long, tiring day."
            
        "Go shopping":
            $ renpy.block_rollback()
            if lena_posh < 5:
                $ lena_posh += 1
            $ lena_wardrobe_wits1 = True
            $ lena_wardrobe_charisma1 = True
            $ lena_wardrobe_athletics1 = True
            $ lena_wardrobe_lust1 = True
            $ lena_wardrobe_charisma1 = True
            $ lena_wardrobe_black_dress = True
            "I knew exactly how I wanted to spend the afternoon. I was in the heart of the city, surrounded by shops and boutiques."
            hide lena
            with long
            "I spent my time visiting them, buying clothes and accessories without much worry or hesitation. After all, the salary Seymour paid me allowed for those kinds of indulgences..."
            if lena_charisma < 10:
                call xp_up ('charisma') from _call_xp_up_1146
            stop music fadeout 2.0
            "When I felt satisfied, I stopped for dinner at a cozy Italian restaurant and headed back to my hotel, eager for a hot bath. It had been a long, tiring day."

        "Go sightseeing":
            $ renpy.block_rollback()
            hide lena
            with long
            "I took the opportunity to stroll around the old town, visiting the monuments and main points of interest."
            if lena_athletics < 10:
                call xp_up ('athletics') from _call_xp_up_1147
            stop music fadeout 2.0
            "When night began to fall, I stopped for dinner at a cozy Italian restaurant and headed back to my hotel, eager for a hot bath."
            "It had been a long, tiring day."

        "Go back to the hotel":
            $ renpy.block_rollback()
            if lena_posh < 5:
                $ lena_posh += 1
            "I was pretty tired and just wanted to get back to the hotel, order some room service, take a bath, and relax."
            stop music fadeout 2.0
            hide lena
            with long
            "I still had a couple more days to visit the city before going back to Baluart."

##########################################################################################################################################
## HOTEL ROOM ##########################################################################################################################################
##########################################################################################################################################
    play sound "sfx/shower.mp3"
    scene fancyhotel with long
    $ seymour_necklace = False
    pause 1
    play music "music/normal_day2.mp3" loop
    $ flena = "n"
    $ lena_look = 1
    $ lena_necklace = 0
    $ lena_makeup = 0
    show lenanude
    show lena_towel
    with long
    l "Ahh, that jacuzzi bath felt amazing... Between catching trains and planes, I've been running around like crazy these past few days."
    "Seymour had rented two adjoining suites in a five-star hotel. It was my first time in such a luxurious hotel room, and I had it all to myself."
# reflect on beach house event
# ian breakup
    if v12_ian_lena_breakup:
        $ flena = "worried"
        "I had been trying to distract myself and not think about Ian and how our relationship ended, but I wasn't managing to do so."
        if ian_cheating == 1:
            if lena_cheating == 1:
                $ flena = "sad"
                l "He decided to break up with me out of the blue... I had already decided to leave him, but he beat me to it."
                l "Seems like we were both feeling the same way... I know my reasons, but what were his? Was he cheating on me too...?"
                l "Well, it doesn't matter much anymore. I wonder if we'll be able to go back to being friends after this..."
            else:
                l "He decided to break up with me out of the blue... At the worst possible time, too."
                if lena_cheating == 2:
                    $ flena = "sad"
                    "I was in no position to really complain, was I? I had been cheating on Ian, and planned on keeping doing so."
                    l "It's best we broke up, I guess... But it was unexpected, and it hurt. I wonder if we'll be able to go back to being friends after this..."
                elif lena_cheating == 0.5:
                    "I knew I had no right to complain after having cheated on him, but now that I had decided to devote myself completely... Maybe it had been too late."
                    $ flena = "sad"
                    l "I guess this relationship wasn't gonna work out, no matter how much I wanted it to... I wonder what will become of us after this."
                    l "Can we even go back to being friends?"
                else:
                    "I felt so hurt and disappointed. I thought Ian really loved me, that I could lean on him, trust him... I had been naive again."
                    l "I wish things were different... I don't think we can go back to being friends after this..."
        elif lena_cheating == 1:
            $ flena = "sad"
            l "I had to break up with him... I thought I loved him, and maybe I did, but this relationship was not what I really wanted. I had to be honest with myself..."
            "But knowing the pain I'd caused Ian didn't bring me any comfort. It was the cost of my mistakes and my freedom..."
            l "There's no way we can continue to be friends after this, is there...?"
        else:
            if ian_lena_crisis:
                "I felt terrible about cheating on him. Or rather, I felt terrible about having been found out and called on it."
                l "I deserve this... I'm terrible, and he must really hate me now."
                l "There's no way we can continue to be friends after this, is there...?"
            elif ian_cindy_sex:
                $ flena = "mad"
                l "Him and Cindy... How could he do something like that? And he's been keeping it a secret from everyone, even from his closest friends. From Wade."
                $ flena = "serious"
                l "I had no idea Ian was this kind of person... He had me fooled, and I was too naive again."
                $ flena = "sad"
                l "At least he didn't try to hide it from me when I confronted him about it... But I don't even know how to treat him from now on."
                l "There's no way we can continue to be friends after this, is there...?"
        if lena_axel_desire:
            $ flena = "blush"
            l "I couldn't resist Axel in the end. Despite how hard I've tried, I'm still hung up on him... There's no denying it, now. And it brought consequences."
# trinity/ ian pure
    elif holly_trinity == 2 or ian_lena_pure:
        $ flena = "smile"
        l "I had a great time at the beach with Holly, Ian and his friends... I wish I was still there."
        $ flena = "shy"
        if holly_trinity == 2:
            l "I miss them already... I can't believe what happened between us. I guess we are a throuple, now..."
            if lena_will == 0:
                call will_up from _call_will_up_72
            $ flena = "sad"
            l "Which makes me feel even worse for being here. What am I doing?"
            l "I should be with them right now, not here, in Rome with Seymour... Still..."
            $ flena = "n"
            l "I need this. And my family does, too. I'm sure they understand..."
        else:
            l "I miss Ian already... I feel so happy to be with him. I don't think I've felt this connection with anyone before..."
            if lena_will == 0:
                call will_up from _call_will_up_73
            $ flena = "sad"
            l "Which makes me feel even worse for being here. What am I doing?"
            l "I should be with him right now, not here, in Rome with Seymour... Still..."
            $ flena = "n"
            l "I need this. And my family does, too. I'm sure he understands..."
# ian couple  
    elif ian_lena_couple:
        if ian_cuck > 1:
            $ flena = "smile"
            l "I had a great time at the beach with Holly, Ian and his friends... It allowed me to relax and unwind a little."
            $ flena = "evil"
            l "I really have Ian wrapped around my finger... I get the feeling he'll agree to anything I ask. It's only a matter of sweetening the request enough."
            $ flena = "shy"
            l "I'm having so much fun playing with him... And I think he enjoys it too, in his own way."
        elif ian_lena_crisis == "ignore":
            l "I had a great time at the beach with Holly, Ian and his friends... It allowed me to relax and unwind a little."
            l "Things with Ian seem to be going smoothly, but... I don't know, I still feel some stiffness coming from him."
            $ flena = "sad"
            l "Could it be that he suspects something...?"
            if lena_cheating == 2:
                "I wanted to keep cheating on Ian, but the situation also made me a bit paranoid. I had to relax..."
                $ flena = "n"
                "As long as I played my cards right, everything should go my way."
            else:
                l "I promised myself I would be faithful to him from now on. I just hope my past mistakes don't come back to bite me..."
        elif ian_lena_crisis:
            $ flena = "sad"
            "The beach getaway had its ups and downs. The conversation I had with Ian wasn't easy at all... I still got nervous just thinking about it."
            if ian_lena_crisis == "forgive":
                "The moment I had been dreading and trying to avoid finally happened. I had to confess about my cheating... and Ian forgave me."
                "I didn't expect it, and I felt like I didn't deserve it. Could I make it up to him somehow? Could I regain his trust?"
                "He had forgiven me, yes, but it was clear that healing the wound I'd caused would take time... if it ever fully healed."
                "I hoped it would..."
            elif ian_lena_open == "ian":
                if lena_cheating == 2:
                    "I was surprised when he proposed an open relationship. He was hurt by my cheating, but I expected a different reaction from him..."
                    "This meant I could still sleep around, which worked for me... But was the freedom to be with other girls enough of a perk for Ian to accept me having other partners?"
                    if ian_cindy_sex:
                        "Had he been sleeping with someone behind my back too...? With Cindy?"
                    else:
                        "Had he been sleeping with someone behind my back too...?"
                    "In any case, I knew shouldn't poke too much into it. Things had turned out my way, and an open relationship would allow me to enjoy the best of both worlds, which was what I wanted."
                else:
                    "How ironic was it that he proposed an open relationship after I had decided to fully commit to him?"
                    "Was the freedom to be with other girls enough of a perk for Ian to accept me having other partners...? Did I even want to go back to sleeping around?"
                    if ian_cindy_sex:
                        "Had Ian really been cheating on me too, with Cindy?"
                    else:
                        "Had Ian... been cheating on me too?"
                    "Despite my doubts, I had accepted. What else could I do? I didn't want to lose Ian, and maybe I could have the best of both worlds after all, like I had wanted."
            elif ian_lena_open == "lena":
                $ flena = "n"
                "In the end, though, things went my way. He had forgiven me and allowed me to keep sleeping around... granted he got to do the same."
                "I didn't mind too much. An open relationship seemed just fine... That way I got to have the best of both worlds, a free relationship."
            if v12_lena_rough:
                $ flena = "crazy"
                l "The sex we had afterward, though... He was so rough, but I deserved it. I came so hard..."
                if ian_lena_love:
                    $ flena = "shy"
                    l "And... Despite everything, I felt he still loves me."
            if ian_lena_crisis != "forgive":  
                $ flena = "sad"
                l "I know this doesn't change the fact that I've cheated on Ian and hurt him."
            l "I feel like I should be with him right now, not here with Seymour..."
            $ flena = "n"
            l "But I need this. And my family does, too. I'm sure he understands..."
        else:
            $ flena = "smile"
            l "I had a great time at the beach with Holly, Ian and his friends... I wish I was still there."
            $ flena = "n"
            l "Things with Ian seem to be going smoothly, but... I don't know, I still feel some stiffness coming from him."
            $ flena = "sad"
            l "After all this time, I was hoping he'd loosened up a bit more..."
# other
    else:
        $ flena = "smile"
        l "I had a great time at the beach with Holly, Ian and his friends... It allowed me to relax and unwind a little."
        # holly
        if lena_holly_love:
            $ flena = "shy"
            l "Holly... I'm so happy she came into my life. I never had a friend like her. I never felt for a friend what I feel for her now..."
            l "Which makes me feel even worse for being here. What am I doing?"
            l "I should be with her right now, not here, in Rome with Seymour... Still..."
            $ flena = "n"
            l "I need this. And my family does, too. I know she understands..."
        elif v12_ian_lena_over:
            $ flena = "sad"
            "Things had been a bit awkward with Ian, though, and they were bound to stay that way after we decided to stop hooking up."
            $ flena = "n"
            l "But we did it to avoid complications, so we could continue being friends in the long run... I think we'll manage."
        elif ian_lena_dating:
            "I was glad Ian and I had cleared up our relationship, assuring we wouldn't hurt each other's feelings. We both saw things the same way, so we should be fine."
            "We could continue being friends and enjoying sex together, for as long as that lasted."
# axel
    if lena_axel_desire:
        if lena_axel_fuck:
            $ flena = "blush"
            "I hadn't been able to get Axel out of my head these past few days. It was impossible, after what happened the other day..."
            l "What I'm supposed to do about him now? What does he want from me?"
            $ flena = "serious"
            l "It's not like I want to get back with him. I remember exactly how things ended, and I still haven't forgiven him."
            l "Plus, now he's out there with Cindy, playing some weird game. If he really wants to be with her, why is he still chasing me?"
            $ flena = "crazy"
            l "But the sex is simply amazing... It's even better than before. After so much time apart, our last two encounters... God..."
            $ flena = "blush"
            l "Ahh, what am I even thinking? I feel so stupid, and yet..."
            $ flena = "serious"
            "I tried to shake those frustrating thoughts from my mind. I was here, in Rome, living an incredible experience. Whatever Axel and Cindy were up to was none of my concern."
        else:
            $ flena = "n"
            "It was a relief to have ended things with Axel, too. I had a relapse, but maybe that was exactly what helped me move on for good."
            "After our farewell at the train station, I felt like I had finally put our relationship behind me. I hoped he felt the same..."
            $ flena = "sad"
            l "He seems pretty focused on Cindy now, after all..."
            $ flena = "serious"
            l "Whatever they've got going on, it's none of my business. They can figure it out on their own."
# mike
    if lena_mike_dating:
        $ flena = "sad"
        if ian_lena_pure or ian_lena_couple and lena_cheating < 1:
            "I still hadn't heard from Mike these past few days... And that was for the best."
            "It was the perfect time to step away from that mess. I had my partner, and Mike had his..."
        else:
            "I still hadn't heard from Mike these past few days... I wondered what he was up to. Was he with his girlfriend, or hooking up with other girls?"
            if lena_mike_love:
                "Did he think about me at all?"
                $ flena = "serious"
                if ian_lena_couple:
                    l "I don't know why I keep torturing myself by thinking about him. If he's ignoring me, forget him... I have Ian, after all."
                else:
                    l "I don't know why I keep torturing myself by thinking about him. If he's ignoring me, forget him... I have other options, after all."
            else:
                $ flena = "serious"
                l "Well, if he's ignoring me, so be it. I'm done with him anyway..."
            $ flena = "n"
            l "He's just an immature boy... The complete opposite of a man like Seymour."

    label gallery_CH13_S02:
        if _in_replay:
            call setup_CH13_S02 from _call_setup_CH13_S02

# seymour's gift
    $ seymour_look = 4
    $ flena = "n"
    l "Mhh...? What's this?"
    "I found a box tied with a ribbon on the coffee table, with my name on the tag."
    l "This must be from Seymour... What is it?"
    "I opened it and found a brand new lingerie set inside."
    if seymour_disposition > 1:
        $ flena = "shy"
        l "It looks so nice! Let's see how it fits me..."
        jump v13sytryon
    else:
        menu:
            "Try it on":
                $ renpy.block_rollback()
                if seymour_disposition > 0:
                    $ flena = "smile"
                    l "It looks nice... Let's see how it fits me!"
                else:
                    l "I guess I can try it on..."
                label v13sytryon:
                    l "There are two identical sets, but one is white and the other is black... Which one should I try on?"
                menu:
                    "Black lingerie":
                        $ renpy.block_rollback()
                        hide lenanude
                        hide lena_towel
                        with long
                        $ lena_look = "lingerie2b"
        
                    "White lingerie":
                        $ renpy.block_rollback()
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

            "Put it down":
                $ renpy.block_rollback()
                stop music fadeout 2.0
                
## TRIES LINGERIE
    if lena_look == "lingerie2w" or lena_look == "lingerie2b":
        $ v13_seymour_show = 2
        #  mirror
        if lena_look == "lingerie2b":
            scene v13_seymour0a
        else:
            scene v13_seymour0b
        if lena_tattoo1:
            show v13_seymour0_t1
        if lena_tattoo2:
            show v13_seymour0_t2
        if lena_tattoo3:
            show v13_seymour0_t3
        if lena_piercing1 or lena_piercing2:
            show v13_seymour0_p
        with long
        pause 1
        "I stood in front of the mirror, my eyes slowly tracing my reflection. A smile tugged at my lips as a rush of confidence washed over me."
        "The strappy lingerie hugged my body in all the right places, accentuating my curves with a perfect blend of elegance and sensuality." 
        "My reflection reminded me of how far I'd come... Despite all the hardships, I had found a way to soar to the top."
        "I was someone worthy of attention and admiration, someone meant to be desired, and craved."
        menu:
            "{image=icon_lust.webp}I'm getting aroused..." if (lena_lust > 7 and v13_seymour_shoot > 0) or (seymour_disposition > 0 and v13_seymour_shoot > 0):
                $ renpy.block_rollback()
                $ v13_seymour_show = 3
                stop music fadeout 2.0
                "I reveled in the feeling, fully embracing the allure I saw in myself."
                play music "music/sensual.mp3" loop
                if seymour_disposition > 1:
                    "Memories of my recent encounters with Seymour flooded my mind. The sensuality of those moments resonated within me, igniting my lust."
                elif seymour_disposition == 1:
                    "The feelings Seymour had managed to stir within me resonated throughout my body, igniting my arousal, making me remember..."
                else:
                    "I couldn't help it. Despite my reservations, the feelings Seymour had managed to stir within me resonated throughout my body, making me remember..."
                scene v11_seymour6b
                if lena_tattoo1:
                    show v11_seymour6_t1
                if lena_tattoo2:
                    show v11_seymour6_t2
                if lena_tattoo3:
                    show v11_seymour6_t3
                if lena_piercing1:
                    show v11_seymour6_p1
                elif lena_piercing2:
                    show v11_seymour6_p2
                with flash
                "His voice, his words, the pleasure he made me feel... it all echoed in the reflection staring back at me in the mirror."
                "The beautiful image of myself that he had revealed to me sent a tingling sensation through me..."
                play sound "sfx/ah1.mp3"
                # masturbate1
                scene v13_seymour1
                if lena_look == "lingerie2b":
                    show v13_seymour1a
                else:
                    show v13_seymour1b
                if lena_tattoo2:
                    show v13_seymour1_t2
                if lena_tattoo3:
                    show v13_seymour1_t3
                with long
                pause 1
                "I sat on the table, getting comfortable as I watched myself spread my legs, my hand sliding down my belly, caressing my pussy..."
                "As the speed of my fingers increased, the images and sensations grew sharper."
                scene v11_seymour7a
                if seymour_disposition > 1:
                    show v11_seymour7b
                if lena_tattoo1:
                    show v11_seymour7_t1
                if lena_tattoo2:
                    show v11_seymour7_t2
                if lena_piercing1:
                    show v11_seymour7_p1
                elif lena_piercing2:
                    show v11_seymour7_p2
                show v11_seymour7_mirror
                with flash
                "The memory of the vibrations coursing through my body, the pleasure flooding my mind, the feeling of weightlessness, of surrender, of pure release..."
                if seymour_disposition > 1:
                    $ flena = "crazy"
                    "I was still hungry for those sensations that I had never experienced before, eager to feel them again."
                elif seymour_disposition == 1:
                    $ flena = "blush"
                    "I couldn't deny it: I was still hungry for those sensations that I had never experienced before..."
                else:
                    $ flena = "blush"
                    "Even if I knew it was wrong, a part of me was hungry for those sensations that I had never experienced before..."
                play sound "sfx/door.mp3"
                scene v13_seymour1_seymour
                if lena_look == "lingerie2b":
                    show v13_seymour1a
                else:
                    show v13_seymour1b
                if lena_tattoo2:
                    show v13_seymour1_t2
                if lena_tattoo3:
                    show v13_seymour1_t3
                with long
                "I quickly turned my head, startled, as the door between the rooms opened."
                $ fseymour = "evil"
                "Seymour stood there, watching me with an enigmatic smile."
                s "Please, don't stop... I didn't mean to interrupt your enjoyment."
                if seymour_disposition > 1:
                    l "..."
                    play sound "sfx/mh3.mp3"
                    if lena_look == "lingerie2b":
                        scene v13_seymour2a
                    else:
                        scene v13_seymour2b
                    if lena_tattoo2:
                        show v13_seymour3_t2a
                    if lena_tattoo3:
                        show v13_seymour3_t3
                    show v13_seymour3_seymour
                    with long
                    pause 1
                    "I followed Seymour's command as he settled into the sofa, his gaze fixed on me."
                    "My heart raced, sending a surge of euphoria through my veins, making me feel light-headed."
                    s "I see you've found my gift... It looks stunning on you, just as I imagined. Do you like it?"
                    l "Yes... I love it... I look so beautiful in it..."
                else:
                    scene fancyhotel
                    show lena 
                    with long
                    l "Um, that's..."
                    show lena at rig
                    show seymour at lef3
                    with long
                    s "I see you've found my gift... It looks stunning on you, just as I imagined. Do you like it?"
                    if seymour_disposition == 1:
                        l "I do... It's a gorgeous lingerie set. Thank you..."
                    else:
                        l "I... Yes, it's a lovely lingerie set."
                        s "Lovely enough to arouse you, is it? I'm glad..."
                    show seymour at lef with move
                    "Seymour lounged on the sofa, getting comfortable as he watched me with those cold, penetrating eyes."
                    s "Go ahead. Continue with what you were doing... I'm in the mood for one of our private sessions. No cameras... just for my eyes only."

            "Take the lingerie off":
                $ renpy.block_rollback()
                stop music fadeout 2.0
                $ flena = "smile"
                scene fancyhotel
                show lena at rig
                with long
                "Satisfied with myself, I was about to take off the outfit and put it back in the box when I heard the door connecting the rooms open."
                play sound "sfx/door.mp3"
                $ fseymour = "smile"
                show seymour at lef3 with short
                play music "music/seymours_theme.mp3" loop
                s "I see you've found my gift... It looks stunning on you, just as I imagined. Do you like it?"
                if seymour_disposition > 1:
                    $ flena = "shy"
                else:
                    $ flena = "blush"
                show seymour at lef
                with move
                if seymour_disposition > 1:
                    l "I do... It's a gorgeous lingerie set. Thank you."
                else:
                    l "Yes, it's a lovely lingerie set... Um..."
                l "How was dinner?"
                s "Productive. I was thinking of inviting you for a drink to wrap up the day, but seeing as you're already wearing the set..."
                if seymour_disposition > 1:
                    l "What do you have in mind? One of our private sessions?"
                    s "That would please me very much. No cameras... just for my eyes only. Are you in the mood for it?"
                    stop music fadeout 2.0
                    $ flena = "flirtshy"
                    l "I wouldn't be a good professional if I said no, right?"
                    play music "music/sensual.mp3" loop
                    $ v13_seymour_show = 1
                else:
                    s "I'd love to indulge in one of our private sessions. No cameras... just for my eyes only."
                    $ config.menu_include_disabled = False
                    $ greyed_out_disabled = True
                    jump v13syprivate

# NO LINGERIE
    else:
        "I set the box back on the table and was about to finish freshening up when I heard the door to the room."
        play sound "sfx/door.mp3"
        $ fseymour = "smile"
        show seymour at left with short
        play music "music/seymours_theme.mp3" loop
        if seymour_disposition < 2:
            $ flena = "sad"
        s "Good evening, Doll."
        if seymour_disposition > 0:
            l "Hi...  How was dinner?"
            s "Productive. I was thinking of inviting you for a drink to wrap up the day..."
            show lenanude at rig
            show lena_towel at rig
            show seymour at lef
            with move
            s "Have you seen my gift?"
            l "The lingerie set? Yes..."
            s "Why don't you try it on?"
            l "Of course."
            "It was getting late, but I didn't mind Seymour's request. I knew this trip meant full-time work, after all."
        else:
            if seymour_disposition == 0:
                l "What happened to knocking?"
                $ fseymour = "n"
                s "My apologies. I didn't think you'd mind..."
                l "You're back from dinner already... I thought it would take you longer."
            else:
                l "Hi... You're back from dinner already. I thought it would take you longer."
            show lenanude at rig
            show lena_towel at rig
            show seymour at lef
            with move
            $ fseymour = "smile"
            s "We got straight to business. I was thinking of inviting you for a drink to wrap up the day, but tell me..."
            s "Have you seen my gift?"
            l "The lingerie set? Yes..."
            s "Aren't you going to try it on?"
            l "Right now?"
            s "I was hoping you would."
            $ flena = "n"
            l "Sure..."
            "It was getting late, but I knew this trip meant full-time work. If he wanted me to wear it now, he was paying well enough for me to go along with it."
        hide lenanude
        hide lena_towel
        with long
        $ lena_look = "lingerie2b"
        show lena at rig with long
        pause 1
        "I stood in front of the mirror, looking at my reflection while Seymour casually sat on the couch, his gaze fixed on me."
        s "What do you think?"
        if seymour_disposition > 1:
            $ flena = "smile"
            l "I love it! It's super sexy and classy, and it looks great on me... You have great taste."
            s "Thanks, Doll. I knew you'd like it. It looks just as good on you as I imagined."
            $ flena = "shy"
            l "So... I assume you asked me to put it on for one of our private sessions before the day ends?"
            $ fseymour = "evil"
            s "Exactly. No cameras, just for my eyes only... as long as you're feeling up to it."
            stop music fadeout 2.0
            $ flena = "flirtshy"
            l "I wouldn't be a good professional if I said no, right?"
            play music "music/sensual.mp3" loop
            $ v13_seymour_show = 1
        else:
            if seymour_disposition > 0:
                l "This is different... Very sexy, but classy too. You have good taste..."
                s "Thanks, Doll. I'm glad you like it. It looks just as good on you as I imagined."
                l "So... I take it you wanted me to wear this for one of our private sessions before the day ends?"
                s "That's right. No cameras, just for my eyes only... as long as you're feeling up to it."
            else:
                l "This is different... Very sexy, but kind of classy too."
                s "Do you like it?"
                l "It's fine..."
                s "It looks just as good on you as I imagined."
                l "So... what's the reason you had me put this on?"
                s "Can't you guess? I'd like to end the day with one of our private sessions."
                s "No cameras, just for my eyes only... as long as you're feeling up to it."
            $ config.menu_include_disabled = False
            $ greyed_out_disabled = True
            menu v13syprivate:
                "I can do it...":
                    $ renpy.block_rollback()
                    $ v13_seymour_show = 1
                    stop music fadeout 2.0
                    l "I wouldn't be a good professional if I said no, right...?"
                    if lena_seymour < 12:
                        call friend_xp ('seymour') from _call_friend_xp_1266
                    $ fseymour = "evil"
                    s "Good..."
                    play music "music/sensual.mp3" loop
                    if persistent.include_disabled:
                        $ config.menu_include_disabled = True
                    $ greyed_out_disabled = False
        
                "{image=icon_mad.webp}I'd rather not" if seymour_disposition == 0:
                    $ renpy.block_rollback()
                    $ flena = "sad"
                    l "Well, if I get to choose... I think I'd rather not. I'm feeling kinda tired."
                    jump v13rathernot

                "{image=icon_will.webp}I'd rather not" if lena_will > 0 and seymour_disposition > 0:
                    $ renpy.block_rollback()
                    call willdown from _call_willdown_85
                    $ flena = "sad"
                    l "Well, if I get to choose... I think I'd rather not. I'm feeling kinda tired."
                    label v13rathernot:
                        if persistent.include_disabled:
                            $ config.menu_include_disabled = True
                        $ greyed_out_disabled = False
                    $ fseymour = "n"
                    if v13_seymour_shoot == 0:
                        s "It's been a long day, hasn't it...? Although I've been getting a lot of refusals from you, and that worries me."
                        s "I thought you had already accepted the nature of our professional relationship, Lena."
                    else:
                        s "It's been a long day, hasn't it...? Although I was hoping you wouldn't have any objections to this."
                        s "You've already accepted the nature of our professional relationship, haven't you, Lena?"
                    $ flena = "worried"
                    if lena_seymour > 0:
                        call friend_xp ('seymour',-1) from _call_friend_xp_1267
                    if ian_lena_couple or lena_holly_dating or holly_trinity == 2:
                        s "What's the reason you're still wary of me? Let me guess..."
                        if ian_lena_couple:
                            s "This is about Ian Watts, isn't it? You're worried this will affect your relationship with him."
                            if ian_lena_pure:
                                "That was right. I felt my relationship with Seymour was jeopardizing things with Ian, and I didn't want to risk losing or hurting that for anything."
                                "I had already been keeping things from Ian, knowing he wouldn't feel comfortable at all knowing what was going on between Seymour and me."
                            elif ian_lena_crisis:
                                "He wasn't wrong... My relationship with Ian was already on shaky ground, and this only made things more complicated."
                                "I had already been keeping things from Ian, knowing he wouldn't feel comfortable at all knowing what was going on between Seymour and me."
                            else:
                                "He wasn't wrong... I had already been keeping things from Ian, knowing he wouldn't feel comfortable at all knowing what was going on between Seymour and me."
                        elif holly_trinity == 2:
                            s "This is about Ian Watts, isn't it? You're worried this will affect your relationship with him."
                            "Seymour wasn't wrong... And not only with Ian, but with Holly too. I didn't want this to pull me away from the relationship that was forming between us."
                        else:
                            s "You're worried that someone might feel uncomfortable with our relationship. You fear it will distance you from them, don't you?"
                            l "He wasn't wrong... What would Holly think of this? Would it make her uncomfortable, or maybe she would understand?"
                        "Seymour's patronage was very important to me at the moment, and it was true that, as of late, he had been very generous, almost indulgent, with me."
                    else:
                        s "I don't think you have any reason to be wary of me anymore... or am I wrong?"
                        "Of course I had reasons... Seymour's patronage was very important to me at the moment, and it was true that, as of late, he had been very generous, almost indulgent, with me."
                    $ flena = "sad"
                    "Still... I knew I couldn't trust him. I shouldn't."
                    if lena_wits < 10:
                        call xp_up ('wits') from _call_xp_up_1148
                    s "I'd rather not force you to perform something you're not comfortable with. I think you should reconsider whether it's worth continuing our professional relationship."
                    stop music fadeout 3.0
                    s "If not... Well, you know the terms of our contract."
                    s "Goodnight, Lena."
                    play sound "sfx/door.mp3"
                    hide seymour with short
                    show lena at truecenter with move
                    l "..."
                    l "I disappointed him, but I can't give in. I need to keep my guard up around him for as long as this relationship lasts..."
                    hide lena with long
                    pause 1
                    $ seymour_disposition = 0
                    scene black with long
                    pause 1
                    $ renpy.end_replay()
                    jump master_script

## POSING 4 SEYMOUR
    if v13_seymour_show > 0:
        $ seymour_necklace = True
    # asked to pose
        if v13_seymour_show < 3:
            # mirror
            if lena_look == "lingerie2b":
                scene v13_seymour0a
            else:
                scene v13_seymour0b
            if lena_tattoo1:
                show v13_seymour0_t1
            if lena_tattoo2:
                show v13_seymour0_t2
            if lena_tattoo3:
                show v13_seymour0_t3
            if lena_piercing1 or lena_piercing2:
                show v13_seymour0_p
            with long
            pause 1
            if v13_seymour_show == 1:
                if seymour_disposition > 1:
                    "I stood in front of the mirror, my eyes slowly tracing my reflection. A smile tugged at my lips as a rush of confidence washed over me."
                else:
                    "I stood in front of the mirror, my eyes slowly tracing my reflection, same as Seymour's."
                "The strappy lingerie hugged my body in all the right places, accentuating my curves with a perfect blend of elegance and sensuality." 
                "My reflection reminded me of how far I'd come... Despite all the hardships, I had found a way to rise to the top."
                "Seymour reminded me I was someone worthy of attention and admiration, someone meant to be desired, and craved."
            else:
                "I struck poses for Seymour in front of the mirror, each movement deliberately crafted under his watchful gaze."
                "My reflection showed me what his eyes were seeing... and I liked it."
            s "I want you to feel good, Lena. Show me the beauty of your pleasure."
            play sound "sfx/mh3.mp3"
            if lena_look == "lingerie2b":
                scene v13_seymour2a
            else:
                scene v13_seymour2b
            if lena_tattoo2:
                show v13_seymour3_t2a
            if lena_tattoo3:
                show v13_seymour3_t3
            show v13_seymour3_seymour
            with long
            pause 1
            if seymour_disposition > 1:
                "I followed Seymour's command without hesitation. My fingers caressed my pussy, legs spread wide so he could see."
                "My heart started to race, sending a surge of euphoria through my veins, making me feel light-headed."
                "There was no denying it: the allure this man was able to awaken in me was something I could hardly resist."
            else:
                if seymour_disposition == 1:
                    "I knew exactly what was expected of me, and I gave in without protest."
                else:
                    "I had anticipated something like this... I knew exactly what was expected of me, and I gave in without protest."
                "My heart started to race as my fingers caressed my pussy, legs spread wide so he could see."
                if seymour_disposition == 1:
                    "A part of me was still hesitant, but that voice inside of me was quieted by the surge of euphoria my beating chest was sending through my veins, making me feel light-headed."
                else:
                    "A part of me still wanted to resist, but another told me it was pointless. My heart started to race, making me feel light-headed."
                "I had already decided to accept the hand Seymour was extending to me, to give in to his desires..."
            s "Now let me see how pleasure washes over you, Doll. How you lose yourself in it."
    # caught masturbating
        else:
            if seymour_disposition < 2:
                play sound "sfx/mh3.mp3"
                # scene masturbate1
                # with long
                # pause 1
                "I knew exactly what was expected of me, and I gave in without protest."
                s "That's right... I want you to feel good, Lena. Show me the beauty of your pleasure."
                s "What do you think of my gift? It looks stunning on you, just as I imagined."
                if seymour_disposition == 1:
                    l "Yes... I love it... I look so beautiful in it..."
                    "A part of me was still hesitant, but that voice inside of me was quieted by the surge of euphoria my beating chest was sending through my veins, making me feel light-headed."
                else:
                    l "Yes... It's a gorgeous set of lingerie. I like how sexy I look in it..."
                    "A part of me still wanted to resist, but another knew it was pointless. My heart started to race, making me feel light-headed."
                "I had already decided to accept the hand Seymour was extending to me, to give in to his desires..."
                s "Now let me see how pleasure washes over you, Doll. How you lose yourself in it."
            else:
                s "You do. So beautiful, especially when pleasure washes over you... I want to see it again."
                "Seymour's voice commanded me, my fingers caressing my pussy with growing intensity. My reflection showed me what his eyes were seeing..."
                "And I loved it."
                s "Now let me see how pleasure washes over you, Doll. How you lose yourself in it."
                jump v13syorgasm

        menu:
            "Cum!":
                $ renpy.block_rollback()
                label v13syorgasm:
                    $ v13_seymour_fake = 2
                    if seymour_disposition > 1:
                        "His words were all I needed. My fingers, fueled by the fire he'd ignited, carried me over the edge."
                    elif seymour_disposition == 1:
                        "His words were all it took. My fingers, fueled by the fire he'd ignited, carried me over the edge."
                    else:
                        "In the end, I had no will to resist his words. My fingers, fueled by the fire he'd ignited, carried me over the edge."
                play sound "sfx/oh3.mp3"
                if lena_look == "lingerie2b":
                    scene v13_seymour3a
                else:
                    scene v13_seymour3b
                if lena_tattoo2:
                    show v13_seymour3_t2b
                if lena_tattoo3:
                    show v13_seymour1_t3
                show v13_seymour3_seymour
                with flash
                with vpunch
                pause 0.6
                with vpunch
                pause 0.6
                with vpunch
                s "Yes...! Do it for me."
                "My body trembled and my voice escaped me, shaken by the orgasmic release."
                if seymour_disposition > 1:
                    "Once again, I showed myself bare in front of Seymour's eyes, letting him gaze deep within me, without holding anything back."
                else:
                    "I felt exposed in front of Seymour's eyes, like he was gazing deep within me and I couldn't hold anything back."
                    if seymour_disposition == 0:
                        $ seymour_disposition = 1
                if lena_lust < 10:
                    call xp_up ('lust') from _call_xp_up_1149
                    pause 1
                $ flena = "crazy"
                scene fancyhotel
                show lena at rig
                show seymour at lef3
                with long
                stop music fadeout 3.0
                s "That was beautiful... Thank you, Lena."
                "Seymour stood up and reached for something in his pocket as he walked toward me."
                show seymour at lef with move
                s "Turn around, Doll."

            "Fake orgasm" if seymour_disposition < 2:
                $ renpy.block_rollback()
                $ v13_seymour_fake = 1
                "Once again, I felt control slipping through my fingers... Something inside me searched for a way to hold onto it."
                play sound "sfx/ah10.mp3"
                if lena_look == "lingerie2b":
                    scene v13_seymour2a
                else:
                    scene v13_seymour2b
                if lena_tattoo2:
                    show v13_seymour3_t2a
                if lena_tattoo3:
                    show v13_seymour3_t3
                show v13_seymour3_seymour
                with vpunch
                pause 1
                l "Ah, yes... So good...!"
                if seymour_disposition == 1:
                    "I faked my orgasm, moaning, trembling, tensing up my body. "
                else:
                    "I faked my orgasm, moaning, trembling, tensing up my body. I just wanted to end this situation as fast as possible." 
                s "..."
                if v13_seymour_show == 3:
                    $ fseymour = "evil"
                else:
                    $ fseymour = "n"
                $ flena = "blush"
                scene fancyhotel
                show lena at rig
                show seymour at lef3
                with long
                stop music fadeout 4.0
                if v13_seymour_show == 3 and v13_seymour_shoot > 0:
                    s "Good... That was beautiful."
                    l "Thanks..."
                    if lena_wits < 10:
                        call xp_up ('wits') from _call_xp_up_1150
                else:
                    s "Is that supposed to fool me?"
                    l "What? That's not..."
                    if lena_seymour > 0:
                        call friend_xp ('seymour',-1) from _call_friend_xp_1268
                    $ fseymour = "evil"
                    s "I know how you are when you're genuine, Lena. I've seen it before."
                    l "It's, uh... It's not so easy, you know. I need to feel relaxed and in the right mood to get there..."
                    $ fseymour = "smile"
                    s "Of course. My mistake... I shouldn't have rushed you. Maybe I should've started with this..."
                "Seymour stood up and reached for something in his pocket as he walked toward me."
                show seymour at lef with move
                s "Come here, Doll. Turn around."

            "Stop":
                $ renpy.block_rollback()
                $ fseymour = "n"
                if seymour_disposition < 3:
                    $ flena = "blush"
                scene fancyhotel
                show lena at rig
                show seymour at lef3
                with long
                stop music fadeout 4.0
                s "Mh? Why are you stopping?"
                if seymour_disposition > 1:
                    $ flena = "shy"
                    l "It's, um... We just got started. Are you in a rush tonight?"
                    $ fseymour = "smile"
                    s "No, quite the opposite... I just wanted you to feel the shooting climax before I give you this."
                else:
                    l "It's, uh... It's not so easy, you know. I need to feel relaxed and in the right mood to get there..."
                    s "Of course. My mistake... I shouldn't have rushed you."
                $ fseymour = "smile"
                "Seymour stood up and reached for something in his pocket as he walked toward me."
                show seymour at lef with move
                s "Come here, Doll. Turn around."

        play music "music/necklace.mp3" loop
        # necklace
        if seymour_disposition > 2:
            scene v13_seymour4b
        else:
            scene v13_seymour4a
        with long
        pause 1
        $ lena_necklace = "seymour3"
        if seymour_disposition > 1:
            "I felt Seymour place something cold around my neck. My necklace."
        elif seymour_disposition == 1:
            "I felt Seymour place something cold around my neck. The necklace."
        else:
            "I felt Seymour place something cold around my neck. His necklace."
        "However, something was different. When I looked in the mirror, I saw that the obsidian stone had been replaced with a sparkling, crystal-cut gem."
        s "Now, it's a jewel truly worthy of gracing your neck."
        menu:
            "{image=icon_money.webp}This must be so expensive!" if lena_posh > 3:
                $ renpy.block_rollback()
                if seymour_disposition == 0:
                    $ seymour_disposition = 1
                scene v13_seymour4b with long
                l "Oh my God... This is a diamond, isn't it? It's the biggest one I've ever seen!"
                l "This must be so incredibly expensive..."
                s "Both the piece and the diamond are one-of-a-kind pieces, their value hard to measure. Just like you..."
                s "It's only fitting that a jewel like you wears one of equal worth."
                "Seymour's voice whispered in my ear, sent a gentle shiver through me."
                "I felt a surge of excitement coursing through my veins. The jewel now adorning my neck was probably worth more than all the paychecks I'd ever earned combined."
                "And this was just another display of Seymour's power and generosity... with me as the fortunate recipient."
                if seymour_disposition > 1:
                    "It truly felt like living a dream, a fantastical tale coming to life just for me."
                else:
                    "It was hard not to feel like the protagonist of one of those fantastical stories, coming to life in an unbelievable way."
                    if seymour_disposition == 0:
                        $ seymour_disposition = 1
                        "I knew everything in this life had a price... But the benefits far outweighed the cost, or at least that's how I felt in that moment."

            "{image=icon_friend.webp}It is a wonderful gift" if lena_seymour > 5:
                $ renpy.block_rollback()
                if seymour_disposition > 1:
                    scene v13_seymour4b with long
                    l "Thank you so much...! It's another wonderful gift, truly... Wow..."
                else:
                    l "Thank you... It's another wonderful gift... truly."
                s "It's only fitting that a jewel like you wears one of equal worth."
                "Seymour's voice whispered in my ear, sent a gentle shiver through me."
                if lena_posh > 3 or seymour_disposition > 1:
                    "I felt a surge of excitement coursing through my veins. The jewel now adorning my neck was probably worth more than all the paychecks I'd ever earned combined."
                    "And this was just another display of Seymour's power and generosity... with me as the fortunate recipient."
                else:
                    "Nothing could have prepared me for what this man was making me experience. For the opportunities he was offering me."
                    if seymour_disposition == 0:
                        $ seymour_disposition = 1
                        "I knew everything in this life had a price... But the benefits far outweighed the cost, or at least that's how I felt in that moment."

            "Thanks...":
                $ renpy.block_rollback()
                if seymour_disposition > 1 or lena_posh > 4:
                    scene v13_seymour4b with long
                    l "Wow, this is... I'm at a loss for words. Thank you so much..."
                    s "I'm glad you appreciate it. Both the piece and the diamond are one-of-a-kind pieces, their value hard to measure. Just like you."
                elif seymour_disposition > 0:
                    l "It's... It's a lovely gift. Thank you."
                    s "Both the piece and the diamond are one-of-a-kind pieces, their value hard to measure. Just like you."
                else:
                    l "It's... It's such a thoughtful gesture. Thank you."
                    s "It's more than just a gesture... Both the piece and the diamond are one-of-a-kind pieces, their value hard to measure. Just like you."
                "Seymour's voice, whispered in my ear, sent a gentle shiver through me."
                if seymour_disposition > 2:
                    "I felt a surge of excitement coursing through my veins. The jewel now adorning my neck was probably worth more than all the paychecks I'd ever earned combined."
                    "And this was just another display of Seymour's power and generosity... with me as the fortunate recipient."
                else:
                    "Nothing could have prepared me for what this man was making me experience. For the opportunities he was offering me."
                    if seymour_disposition > 1:
                        "It was hard not to feel like the protagonist of one of those fantastical stories, coming to life in an unbelievable way."
                    else:
                        "A temptation I was struggling so much to resist..."

            "...":
                $ renpy.block_rollback()
                l "..."
                s "What's the matter? Did it leave you speechless?"
                if seymour_disposition > 1 or lena_posh > 3:
                    l "It's... It's such a lovely gift. Thank you."
                else:
                    l "It's... It's such a thoughtful gesture. Thank you."
                s "It's more than just a gesture... Both the piece and the diamond are one-of-a-kind pieces, their value hard to measure. Just like you."
                "Seymour's voice, whispered in my ear, sent a shiver through me."
                if seymour_disposition > 2:
                    "I felt a surge of excitement coursing through my veins. The jewel now adorning my neck was probably worth more than all the paychecks I'd ever earned combined."
                    "And this was just another display of Seymour's power and generosity... with me as the fortunate recipient."
                else:
                    "Nothing could have prepared me for what this man was making me experience. For the opportunities he was offering me."
                    if seymour_disposition > 1:
                        "It was hard not to feel like the protagonist of one of those fantastical stories, coming to life in an unbelievable way..."
                    else:
                        "A temptation I was struggling so much to resist..."

        if not _in_replay:
            $ gallery_unlock_scene("CH13_S02")
        if gallery_scene_unlocked('CH13_S03') or persistent.gallery_force_unlock:
            pass
        else:
            $ renpy.end_replay()

            label gallery_CH13_S03:
                if _in_replay:
                    call setup_CH13_S03 from _call_setup_CH13_S03

        # permission to touch
        if v13_seymour_shoot == 3:
            scene v13_seymour5
            if lena_look == "lingerie2b":
                show v13_seymour5a
            else:
                show v13_seymour5b
            if lena_tattoo2:
                show v13_seymour5_t2
            with long
            pause 1
            "Seymour's fingers glided along my neck, gently caressing my chin. His other hand rested softly on my hip, pulling me closer to him..."
            "My goosebumps intensified as I felt his warm fingertips brush my skin, just like during the photo shoot."
            s "Has something changed, or... do you still want me to touch you?"
        else:
            "Seymour's fingers lingered on my neck; his chest hovering just inches from my back."
            if v13_seymour_shoot == 1 or v13_seymour_shoot == 1.5:
                s "Do I still have your permission to touch you?"
                "My goosebumps intensified as I felt his warm fingertips brush my skin, just like during the photo shoot."
            else:
                if v13_seymour_shoot == 2:
                    s "I wonder... Would you grant me permission to touch you this time?"
                    "I had maintained control during the photo shoot, but now Seymour was making his move..."
                else:
                    s "I wonder... Would you grant me permission to touch you?"
                    "I had avoided posing with Seymour earlier to avoid this situation, but he was finally making his move..."
        $ config.menu_include_disabled = False
        $ greyed_out_disabled = True
        menu:
            "{image=icon_lust.webp}Give yourself over to Seymour":
                $ renpy.block_rollback()
                # stop music fadeout 2.0
                l "Yes... Yes, I do."
                # if seymour_disposition > 1:
                #     play music "music/sex_trascendence.mp3" loop
                # else:
                #     play music "music/seduction2.mp3" loop
                if v13_seymour_shoot != 3:
                    scene v13_seymour5
                    if lena_look == "lingerie2b":
                        show v13_seymour5a
                    else:
                        show v13_seymour5b
                    if lena_tattoo2:
                        show v13_seymour5_t2
                    with long
                    pause 1
                    "I felt his fingertips tracing the curve of my chin, sending a shiver down my spine, and his chest came in contact with my back."
                if seymour_disposition > 1:
                    "The moment had finally come. This is what I had wanted... This powerful, extraordinary man opening up to me."
                    "Seymour had recognized me as the object of his desire, and now he was asking me to recognize him back."
                elif seymour_disposition == 1:
                    "Who had I been trying to fool? I had been pretending there was a line I was never going to cross, but that was not what I wanted."
                    "I had decided to accept Seymour's proposal for a reason... A dark part of me longed to open up to him and fully accept the gift he was offering."
                else:
                    "I surprised myself with my own words, but the part of me I had been trying to suppress had finally wrestled control away from me."
                    "Despite my animosity toward Seymour, a dark part of me longed to open up to him and fully accept the gift he was offering."
                    "Who had I been trying to fool? That part of me had won from the moment I accepted his proposal. I wanted this..."
                if lena_look == "lingerie2b":
                    scene v13_seymour6a
                    show v13_seymour5a
                else:
                    scene v13_seymour6b
                    show v13_seymour5b
                if lena_tattoo2:
                    show v13_seymour6_t2
                    show v13_seymour5_t2
                if lena_tattoo3:
                    show v13_seymour6_t3
                with long
                pause 1
                "The warm, tender touch of his hands finally made real the feeling of our mutual connection."
                # relationships guilt
                if lena_holly_dating:
                    "I was suddenly stung by the cold needle of guilt, thinking about Holly."
                    "Whatever I felt for her... She was my best friend, but this was completely different."
                    "I couldn't deny the feelings and desires Seymour had instilled in me. And I could never get what I really wanted from Holly, could I...?"
                elif holly_trinity == 2:
                    if ian_lena_dating:
                        "I was suddenly stung by the cold needle of guilt, thinking about Ian... and Holly. I loved them, yet I was here, with this man..."
                        "They were both so special and dear to me, but couldn't deny the feelings and desires Seymour had instilled in me."
                        "Never had someone made me feel like Seymour did. Never had someone offered me what he offered..."
                    else:
                        "I was suddenly stung by the cold needle of guilt, thinking about Holly... and Ian."
                        "Whatever I felt for them... They were my best friends, very special ones. But I could never get what I really wanted from them..."
                        "The feelings and desires Seymour had instilled in me... Never had someone offered me what he offered."
                    "There was no one else who could." 
                elif ian_lena_pure:
                    "I was suddenly stung by the cold needle of guilt, thinking about Ian."
                    "Our relationship meant so much to me. I loved him, yet I was here, with this man..."
                    "But couldn't deny the feelings and desires Seymour had instilled in me. Never had someone made me feel like he did."
                    "Never had someone offered me what he offered... There was no one else who could."
                elif ian_lena_couple:
                    if ian_lena_open == "lena":
                        "I was suddenly struck by a thought of Ian... but he had agreed to open up our relationship. Giving in to Seymour's offer wasn't wrong, was it?"
                    elif ian_lena_open == "ian":
                        "I was suddenly struck by a thought of Ian. I had vowed to focus on our relationship, but he asked us to open it up..."
                        "Giving in to Seymour's offer wasn't wrong, was it?"
                    elif ian_lena_crisis == "forgive":
                        "I was suddenly struck by a thought of Ian. After what had happened at the beach house, and after he forgave my infidelity..."
                        "He shouldn't have done so... Temptation was knocking at my door again, and I had answered."
                    elif lena_cheating == 0.5:
                        "I was suddenly struck by a thought of Ian. I had vowed to focus on our relationship, to not betray him again, but now..."
                        "Temptation was knocking at my door again, and I had answered."
                    else:
                        "I was suddenly stung by the cold needle of guilt, thinking about Ian. I loved him, yet I was here, with this man..."
                    "I couldn't deny the feelings and desires Seymour had instilled in me. Never had someone made me feel like he did."
                    "Never had someone offered me what he offered... There was no one else who could."
                else:
                    "Never had someone made me feel like Seymour did. Never had someone offered me what he offered... There was no one else who could."
                "What an unreal feeling... Now, I had it all: wealth, power, security, endless possibilities..."
                "And pleasure too. All sorts of it."
                jump v13seymoursex

            "..." if v13_seymour_shoot != 3:
                $ renpy.block_rollback()
                l "..."
                scene v13_seymour5
                if lena_look == "lingerie2b":
                    show v13_seymour5a
                else:
                    show v13_seymour5b
                if lena_tattoo2:
                    show v13_seymour5_t2
                with long
                pause 1
                if seymour_disposition > 1:
                    "I felt his fingertips tracing the curve of my chin, eager for my response. I shivered with anticipation, too."
                    "What would happen if I said yes...?"
                elif seymour_disposition == 1:
                    "I felt his fingertips tracing the curve of my chin, eager for my response, but none was coming to my lips."
                    "I was with my back against the wall. I feared what might happen if I said no, and I was scared by how much I wanted to say yes..."
                else:
                    "I felt his fingertips tracing the curve of my chin, eager for my response. Why couldn't I just say no?"
                    "I wanted to, but a darker part of me also wanted to say yes, and was fighting to break free."
                # relationships hesitation
                if lena_holly_dating:
                    "I trembled with hesitation, thinking about Holly."
                    "Our friendship had been blooming into something bigger, into something deeper. But I couldn't deny the feelings and desires Seymour had instilled in me."
                    "What Holly meant to me... Was it enough for me to sacrifice what Seymour offered?"
                elif holly_trinity == 2:
                    if ian_lena_dating:
                        "I trembled with hesitation, thinking about Ian... and Holly."
                        "They were both so special and dear to me, but I couldn't deny the feelings and desires Seymour had instilled in me."
                        "Never had someone offered me what he offered..."
                    else:
                        "I trembled with hesitation, thinking about Holly... and Ian."
                        "Our friendship had been blooming into something bigger, into something deeper. But I couldn't deny the feelings and desires Seymour had instilled in me."
                        "What they meant to me... Was it enough for me to sacrifice what Seymour offered?"
                elif ian_lena_pure:
                    "I trembled with hesitation, thinking about Ian."
                    "Our relationship meant so much to me. I loved him, yet I was here, with this man..."
                    "But I couldn't deny the feelings and desires Seymour had instilled in me. Never had someone offered me what he offered..."
                    "And there was no one else who could."
                else:
                    if ian_lena_couple:
                        if ian_lena_open == "lena":
                            "I thought about Ian for a moment, but he had agreed to open up our relationship. Giving in to Seymour's offer wasn't wrong, was it?"
                        elif ian_lena_open == "ian":
                            "I thought about Ian, hesitant. I had vowed to focus on our relationship, but he asked us to open it up..."
                            "Giving in to Seymour's offer wasn't wrong, was it?"
                        elif ian_lena_crisis == "forgive":
                            "I trembled with hesitation, thinking about Ian. After what had happened at the beach house, and after he forgave my infidelity..."
                            "The temptation of sin was knocking at my door once again."
                        elif lena_cheating == 0.5:
                            "I trembled with hesitation, thinking about Ian. I had vowed to focus on our relationship, to not betray him again, but now..."
                            "The temptation of sin was knocking at my door once again."
                    if seymour_disposition > 1:
                        "The feelings and desires Seymour had instilled in me had been swelling more and more the longer I spent by his side."
                    elif seymour_disposition == 1:
                        "I couldn't deny the feelings and desires Seymour had instilled in me."
                    else:
                        "I was at odds with myself, with the feelings and desires Seymour had instilled in me."
                    "Never had someone offered me what he offered... And there was no one else who could."            
                if lena_look == "lingerie2b":
                    scene v13_seymour6a
                    show v13_seymour5a
                else:
                    scene v13_seymour6b
                    show v13_seymour5b
                if lena_tattoo2:
                    show v13_seymour6_t2
                    show v13_seymour5_t2
                if lena_tattoo3:
                    show v13_seymour6_t3
                with long
                pause 1
                "Seymour's hands grew bolder in my silence, sliding along my sides and waist, barely grazing my thighs. I shivered."
                "They demanded a response from me..."
                menu:
                    "{image=icon_lust.webp}Give yourself over to Seymour":
                        $ renpy.block_rollback()
                        # if seymour_disposition > 1:
                        #     play music "music/sex_trascendence.mp3" loop
                        # else:
                        #     play music "music/seduction2.mp3" loop
                        "I let out a long sigh and leaned back against Seymour's chest, allowing his hands to slip between my thighs."
                        l "Yes, touch me..."
                        if seymour_disposition > 1:
                            "This is what I had been wanting... This powerful, extraordinary man opening up to me."
                            "Seymour had recognized me as the object of his desire, and now he was asking me to recognize him back."
                        elif seymour_disposition == 1:
                            "Who had I been trying to fool? I had been pretending there was a line I was never going to cross, but that was not what I wanted."
                            "I had decided to accept Seymour's proposal for a reason... A dark part of me longed to open up to him and fully accept the gift he was offering."
                        else:
                            "I surprised myself with my own words, but the part of me I had been trying to suppress had finally wrestled control away from me."
                            "Who had I been trying to fool? That part of me had won from the moment I accepted his proposal. I had been wanting this..."
                        "It was an unreal feeling. Now, I could really have it all: wealth, power, security, endless possibilities..."
                        "And pleasure too."
                        jump v13seymoursex

                    "{image=icon_will.webp}Deny him" if lena_will > 0:
                        $ renpy.block_rollback()
                        call willdown from _call_willdown_86
                        pause 0.6
                        jump v13seymourdeny2

                    "Deny him" if v13_seymour_shoot == False:
                        $ renpy.block_rollback()
                        label v13seymourdeny2:
                            stop music fadeout 4.0
                        $ flena = "blush"
                        $ fseymour = "n"
                        scene fancyhotel
                        show seymour2 at lef
                        show lena at centerrig
                        with long
                        show lena at rig with move
                        "I stepped away from Seymour, tense and hesitant."
                        if lena_holly_dating or holly_trinity == 2 or ian_lena_couple:
                            l "I... I can't. We shouldn't..."
                        else:
                            l "This is... We shouldn't..."
                        s "..."
                        hide seymour2
                        show seymour at lef
                        with short
                        s "I see you still don't trust me, is that it?"
                        if seymour_disposition > 0:
                            $ flena = "worried"
                            l "That's... It's just that I think it wouldn't be a good idea if..."
                            l "I'd rather keep things within the boundaries of the contract."
                            s "I see..."
                        else:
                            $ flena = "serious"
                            l "I'm just following the terms of our contract, as should you."
                            s "Of course. I didn't intend to break them."
                        # relationships hesitation
                        if ian_lena_couple:
                            s "I suppose your refusal has to do with your relationship with Ian Watts, am I wrong? You're afraid this might interfere with it..."
                            if ian_lena_open == "lena":
                                l "That's... part of it."
                            elif ian_lena_open == "ian":
                                l "That's... Yes, that's right."
                            else:
                                l "That's right."
                        if lena_wits < 10:
                            call xp_up ('wits') from _call_xp_up_1151 
                        jump v13seymourdeny3
        
            "{image=icon_will.webp}Deny him" if lena_will > 0:
                $ renpy.block_rollback()
                call willdown from _call_willdown_87
                pause 0.6
                jump v13seymourdeny

            "Deny him" if v13_seymour_shoot == False:
                $ renpy.block_rollback()
                label v13seymourdeny:
                    stop music fadeout 4.0
                $ flena = "blush"
                $ fseymour = "n"
                scene fancyhotel
                show seymour2 at lef
                show lena at centerrig
                with long
                show lena at rig with move
                if seymour_disposition > 0:
                    "I stepped away from Seymour, tense and hesitant."
                else:
                    "I stepped away from Seymour, tense and defensive."
                l "This is... I can't. We shouldn't..."
                s "..."
                hide seymour2
                show seymour at lef
                with short
                s "I see you still don't trust me, is that it?"
                if seymour_disposition > 0:
                    $ flena = "worried"
                    l "That's... It's just that I think it wouldn't be a good idea if..."
                    s "I'd rather keep things within the boundaries of the contract."
                    s "I see..."
                else:
                    $ flena = "serious"
                    l "I'm just following the terms of our contract, as should you."
                    s "Of course. I didn't intend to break them."
                # relationships hesitation
                if lena_holly_dating or holly_trinity == 2 or ian_lena_couple:
                    if ian_lena_couple:
                        s "I suppose your refusal has to do with your relationship with Ian Watts, am I wrong? You're afraid this might interfere with it, aren't you?"
                        if holly_trinity == 2:
                            l "That's right."
                            "It wasn't just about Ian, but Holly too. I couldn't risk the bond I had just forged with them. I didn't want to taint something so beautiful."
                        elif ian_lena_pure:
                            l "That's right."
                            "Ian was so important to me... I didn't want to taint our relationship. I was risking things enough already... "
                        elif ian_lena_open == "lena":
                            $ flena = "sad"
                            l "That's... That's part of it..."
                            "Ian had agreed to open up our relationship, but still... Giving in to Seymour felt wrong."
                        elif ian_lena_open == "ian":
                            $ flena = "sad"
                            l "That's... That's right..."
                            "I had vowed to focus on our relationship, but he asked us to open it up... still, Giving in to Seymour felt wrong."
                        elif ian_lena_crisis == "forgive":
                            $ flena = "sad"
                            l "That's right."
                            "I couldn't betray him again. Not after what had happened at the beach house. Not after he after he forgave me..."
                        elif lena_cheating == 0.5: 
                            $ flena = "sad"
                            l "That's right..."
                            "I had vowed to focus on our relationship, to not betray him again. He didn't deserve it."
                        else:
                            l "That's right..."
                        s "I see. I wish I could persuade you to see things my way..."
                        if seymour_disposition > 0:
                            l "I... I'm sorry. I can't."
                        else:
                            "I'm sorry, but that's not going to happen."
                    elif lena_holly_dating or holly_trinity == 2:
                        if holly_trinity == 2:
                            "Thinking of Holly and Ian helped me hold steadfast. Our friendship had just bloomed into something bigger, into something deeper."
                        else:
                            "Thinking of Holly helped me hold steadfast. Our friendship had been blooming into something bigger, into something deeper."
                        "I didn't want to taint something so beautiful."
                if lena_wits < 10:
                    call xp_up ('wits') from _call_xp_up_1152 
                label v13seymourdeny3:
                    if persistent.include_disabled:
                        $ config.menu_include_disabled = True
                    $ greyed_out_disabled = False
                s "Alright, then. I won't force the issue."
                s "Forgive me if I made you feel uncomfortable tonight. Rest well, Lena."
                play sound "sfx/door.mp3"
                hide seymour with short
                "After saying this, Seymour disappeared, closing the door between our rooms."
                show lena at truecenter with move
                l "That was tense... But I had a feeling I'd have to face something like that."
                l "For now, I'm managing to keep control of the situation. I just hope I can continue like this."
                "I didn't want to give up the advantages Seymour offered. I couldn't. But doing so might jeopardize other aspects of my life."
                "I was playing a dangerous game... but so far, I was winning."
                hide lena with short
                "Or so I wanted to believe..."
                if seymour_disposition > 1:
                    $ seymour_disposition = 1
                scene black with long
                pause 1
                $ renpy.end_replay()
                jump master_script
###########################################################################################################################################################################
## SEYMOUR SEX SCENE ###########################################################################################################################################################################
###########################################################################################################################################################################
label v13seymoursex:
    if persistent.include_disabled:
        $ config.menu_include_disabled = True
    $ greyed_out_disabled = False
    $ lena_seymour_sex = True
    "My breath quickened at the entrancing sensation of Seymour's hands caressing my sensitive areas."
    play sound "sfx/mh3.mp3"
    # seymour kiss
    scene v13_seymour7
    with long
    pause 1
    if seymour_disposition > 1:
        "I turned to face him and found his lips waiting for mine. They came together, truly sealing our bond."
    else:
        "I turned to face him and found his lips waiting for mine. They came together, truly sealing our wicked bond."
    "The scent of his cologne, rich, refined, with a hint of something darker, wrapped around me, heightening the sensation."
    "His kiss was firm, yet gentle: controlled, like everything about him..."
    "I finally had the chance to see that control shattered. I wanted to peel his armor off and see what lay beneath."
    # pull pants
    play sound "sfx/zipper.mp3"
    scene v13_seymour8
    if lena_look == "lingerie2w":
        show v13_seymour8b
    if lena_tattoo2:
        show v13_seymour8_t2
    with long
    pause 1
    if seymour_disposition > 1:
        "I licked my lips as I got down to my knees, undoing Seymour's belt. My heart raced, feeling like unwrapping a present I had been longing for."
    elif seymour_disposition == 1:
        "My heart raced as I went down to my knees, undoing Seymour's belt.  I had been teetering on the edge of this moment, and now it was here."
    else:
        "My heart raced as I went down to my knees, undoing Seymour's belt. Somehow, I felt like I was watching my own motions, Both detached and engaged in the situation."
    "He remained silent, speaking to me only with his touch. His hands caressed my hair as I liberated him from his pants."
    "I ached to see what was concealed behind them. I craved to behold what unmistakably revealed the emotions I could evoke in him."
    "I wasn't disappointed."
    # bj
    scene v13_seymour9
    with long
    pause 1
    "His cock, hard and firm, sprung out, laying bare Seymour's feelings at last."
    "For the first time, his desire for me was tangible, real… For the first time, he was genuinely at my mercy."
    play sound "sfx/bj1.mp3"
    "I ran my fingers across the shaft and brushed the glans with my lips before teasing it with my warm, wet tongue."
    if seymour_disposition > 1:
        "A wicked satisfaction filled me when Seymour shuddered under my caresses. It was my chance to show him my real talent, to elevate his perception of me entirely."
        "I planned to take my time, to savor this moment, to make him ask for more..."
    else:
        "A wicked satisfaction filled me when Seymour shuddered under my caresses. This was my chance to dismantle this powerful and conceited man..."
        "I planned to take my time, to drive him to the edge, to make him desperate for more..."
    "But then he pulled away, gripping me under the arms and lifting me to my feet."
    if seymour_disposition > 1:
        $ flena = "crazysmile"
    else:
        $ flena = "crazy"
    $ fseymour = "evil"
    scene fancyhotel
    show lena at rig
    show seymournude at lef
    with long
    "I could see Seymour's body for the first time. I always knew he was lean, but he was really fit for a man his age."
    "He held my chin and looked directly into my eyes."
    s "You're so attentive... But today, I'm the one who wants to serve you."
    s "Did you bring the toy I gifted you, like I asked?"
    l "Yes..."
    s "Good. Come."
    # bed closeup
    if lena_look == "lingerie2b":
        scene v13_seymour10aa
    else:
        scene v13_seymour10bb
    if lena_tattoo2:
        show v13_seymour10_t2b
    with long
    pause 1
    if seymour_disposition > 1:
        "I let him guide me to the bed. His caresses continued to roam my body, and I closed my eyes, letting the sensations seep into me."
        "Once again, I relinquished all control to Seymour, confident that I was in the best possible hands."
    else:
        "I let him guide me to the bed. His caresses continued to roam my body, allowing the sensations he caused to seep deeply into my body."
        "I closed my eyes and relinquished all control to Seymour, quieting the doubts that still echoed faintly in my heart."
    # bedfull
    if lena_look == "lingerie2b":
        scene v13_seymour10a
    else:
        scene v13_seymour10b
    if lena_tattoo1:
        show v13_seymour10_t1
    if lena_tattoo2:
        show v13_seymour10_t2
    if lena_tattoo3:
        show v13_seymour10_t3
    # if lena_piercing1:
    #     show v13_seymour10_p1
    # if lena_piercing2:
    #     show v13_seymour10_p2
    with long
    play sound "sfx/moan4.mp3"
    pause 1
    "I felt his fingertips gently parting my labia, moistening with my own wetness."
    "His touch was slow and precise, quickly finding the exact spot that made me tremble. It was almost as if he knew my body beforehand..."
    if seymour_disposition > 1:
        "Giving myself to this man and his shining promises felt thrilling and intoxicating; a rush unlike any other."
        "He had made me wait so long for this, intensifying my craving and longing for this forbidden temptation."
    else:
        "I felt the last traces of resistance melt away from my body, fully yielding to the pleasure Seymour made me feel."
        "There was something thrilling and intoxicating about giving myself to this man and his dark promises."
        "A temptation I wasn't able to refuse."
    # grab cock
    if lena_look == "lingerie2b":
        scene v13_seymour11a
    else:
        scene v13_seymour11b
    if lena_tattoo1:
        show v13_seymour11_t1
    if lena_piercing1:
        show v13_seymour11_p1
    if lena_piercing2:
        show v13_seymour11_p2
    with long
    pause 1
    "I reached down with my hand, searching for his manhood, warm and hard."
    if seymour_disposition > 0:
        if ian_lena_couple or lena_holly_dating:
            "I wanted him to claim me with it. Whatever I stood to lose, the promise of what I could gain was far greater..."
            stop music fadeout 4.0
            "I wanted to completely shed the constraints of my old life and emerge from the cocoon, and soar above all those mundane troubles and anxieties, leaving them far behind."
        else:
            stop music fadeout 4.0
            "I wanted him to claim me with it. I wanted to completely shed the constraints of my old life and emerge from the cocoon, and soar above all those mundane troubles and anxieties, leaving them far behind."
    else:
        "I couldn't keep lying to myself. I wanted to be claimed by Seymour."
        if ian_lena_couple or lena_holly_dating:
            "Whatever I stood to lose, the promise of what I could gain was far greater..."
        stop music fadeout 4.0
        "I wanted to completely shed the constraints of my old life and emerge from the cocoon, and soar above all those mundane troubles and anxieties, leaving them far behind."
    # sex closeup pussy
    play music "music/sex_elation.mp3" loop
    if lena_look == "lingerie2b":
        scene v13_seymour11aa
    else:
        scene v13_seymour11bb
    if lena_tattoo1:
        show v13_seymour11ab_t1
    if lena_tattoo3:
        show v13_seymour11ab_t3
    with long
    play sound "sfx/ah8.mp3"
    pause 1
    "I guided Seymour's cock to my slit and felt parting my flesh, setting deep within me."
    if seymour_disposition > 1:
        "My entire body shuddered with a pleasure that seemed to penetrate my very core. I had longed for this for so long...!"
    else:
        "The sensation coursed through me, making my body shudder and my head spin. At last, I had been tainted with this forbidden desire..."
    # sex
    if lena_look == "lingerie2b":
        scene v13_seymour12a
    else:
        scene v13_seymour12b
    if lena_tattoo1:
        show v13_seymour12_t1
    if lena_tattoo2:
        show v13_seymour12_t2
    if lena_tattoo3:
        show v13_seymour12_t3
    # if lena_piercing1:
    #     show v13_seymour12_p1
    # if lena_piercing2:
    #     show v13_seymour12_p2
    with long
    pause 1
    if seymour_disposition > 1:
        if seymour_disposition == 3:
            "Seymour had made me his at last, gifting me with a sinful delight. In this moment, I belonged to him, heart and soul."
        else:
            "Seymour had made me his at last, gifting me with a sinful delight. In this moment, I belonged to him, body and mind."
        "His fingers laced with mine as he pressed his hips, sinking even deeper inside me."
    else:
        "A wicked and pleasurable stain that I had chosen myself, which consumed me in body and mind."
        "Seymour's fingers laced with mine  as he pressed his hips, sinking even deeper inside me."
    "The touch of his lips on my neck and his words gave me goosebumps, a tremor of weakness sweeping over me."
    # sex closeup face
    if lena_look == "lingerie2b":
        scene v13_seymour11aaa
    else:
        scene v13_seymour11bbb
    if lena_tattoo2:
        show v13_seymour11ab_t2
    with long
    play sound "sfx/pant1.mp3"
    pause 1
    s "Feel how your body responds to my touch... It craves me, just as you do. Just as I crave you."
    s "You feel like silk, Doll... So soft, so firm..."
    s "Let me unravel you. Let me weave you into something even more exquisite."
    # sex toy
    if lena_look == "lingerie2b":
        scene v13_seymour13a
    else:
        scene v13_seymour13b
    if lena_tattoo1:
        show v13_seymour12_t1
    if lena_tattoo2:
        show v13_seymour12_t2
    if lena_tattoo3:
        show v13_seymour12_t3
    with long
    play sound "sfx/vibrator.mp3"
    pause 0.5
    with hpunch
    "The tremor intensified tenfold when he placed the vibrator wand on my pussy, its walls contracting around Seymour's hard shaft."
    if seymour_disposition > 1:
        play sound "sfx/mh2.mp3"
        l "Oh God, yes...!!"
        "While he continued to thrust into me, waves of mind-melting pleasure pulsated through my body, making me melt in his arms."
        "Pleasure bubbled up inside me, escaping in passionate, breathless moans."
    else:
        play sound "sfx/oh1.mp3"
        l "Nhhh...!!"
        "While he continued to thrust into me, waves of mind-melting pleasure pulsated through my body, disarming me completely."
        "Pleasure bubbled up inside me, escaping in quiet, breathless moans."
    play sound "sfx/vibrator.mp3"
    s "Yes, give it to me, Lena. I want it."
    s "I want to be the architect of your bliss. I desire you, all of you."
    # lena cum
    scene v13_seymour14
    if lena_look == "lingerie2w":
        show v13_seymour14b
    if lena_tattoo2:
        show v13_seymour14_t2
    with flash
    play sound "sfx/oh3.mp3"
    with vpunch
    pause 0.6
    with vpunch
    pause 0.6
    with vpunch
    pause 0.6
    "My fingers clung to Seymour's as I trembled and shook in his arms."
    "Climax shattered me into pieces, exploding from deep within, my body besieged from every side at once."
    # sex toy + squirt
    if lena_look == "lingerie2b":
        scene v13_seymour13a
    else:
        scene v13_seymour13b
    if lena_tattoo1:
        show v13_seymour12_t1
    if lena_tattoo2:
        show v13_seymour12_t2
    if lena_tattoo3:
        show v13_seymour12_t3
    show v13_seymour12_squirt
    with long
    pause 1    
    "I lost sight of everything but my own pleasure, and the man who was holding me."
    "Seymour's caresses, the dampness of my thighs, my ragged breathing..."
    "In those drawn-out moments, my sensations blurred together, intertwined."
    # bed after
    if lena_look == "lingerie2b":
        scene v13_seymour15a
    else:
        scene v13_seymour15b
    if lena_tattoo1:
        show v13_seymour15_t1
    if lena_tattoo2:
        show v13_seymour15_t2
    if lena_tattoo3:
        show v13_seymour15_t3
    with long
    if seymour_disposition != 3:
        stop music fadeout 4.0
    pause 1
    "Slowly, my senses came back to me. It has been such an intense orgasm..."
    if seymour_disposition == 3:
        jump v13syholdhand
    menu:
        "{image=icon_love.webp}Hold Seymour's hand":
            $ renpy.block_rollback()
            label v13syholdhand:
                stop music fadeout 4.0
            "A warm feeling of soothing euphoria and security washed over me. It had finally happened."
            "I had really accepted Seymour inside me..."
            # bed after 2
            play music "music/sex_good.mp3" loop
            if lena_look == "lingerie2b":
                scene v13_seymour16a
            else:
                scene v13_seymour16b
            if lena_tattoo1:
                show v13_seymour15_t1
            if lena_tattoo2:
                show v13_seymour15_t2
            if lena_tattoo3:
                show v13_seymour15_t3
            with long
            pause 1
            "My hand sought Seymour's, fingers intertwining with his again. He gave a gentle squeeze, smiling at me."
            s "You keep showing me how amazing you are, Doll. I can't stop being amazed by it..."
            l "Really? I think I should be the one saying that... I'm trembling..."
            s "I'm pleased to be able to give you that, and so much more. Anything you want..."
            l "Anything I want...? In that case..."
            # bj bed
            if lena_look == "lingerie2b":
                scene v13_seymour17a
            else:
                scene v13_seymour17b
            if lena_tattoo2:
                show v13_seymour17_t2
            if lena_tattoo3:
                show v13_seymour17_t3
            show v13_seymour17_eyes
            with long
            play sound "sfx/bj5.mp3"
            pause 1
            s "Ohh..."
            "I leaned over Seymour, caressing his cock, still stiff, and brought it to my lips."
            l "I want to make you tremble too."
            "Seymour groaned when I took him into my mouth, sucking with my lips and twirling my tongue with lewd and devoted motions."
            l "Nhh... You taste like me..."
            s "Your mouth feels like Heaven, Doll..."
            hide v13_seymour17_eyes with long
            if lena_lust > 6:
                l "Oh, you have no idea... You haven't seen anything yet."
            else:
                l "Let me take you there..."
            "From that position, I could see our image reflected in the mirror. It made me tingle..."
            # bj bed closeup/mirror
            if lena_look == "lingerie2b":
                scene v13_seymour18a
            else:
                scene v13_seymour18b
            if lena_tattoo2:
                show v13_seymour18_t2
            with long
            pause 1
            if seymour_disposition == 1:
                "The mistrust I felt towards Seymour had melted away, just like my stubborn resistance. I had been holding myself back."
            elif seymour_disposition == 0:
                "The animosity I felt towards Seymour had melted away, just like my stubborn resistance. I had been holding myself back."
            "There was no room for ambiguity anymore: I was on Seymour's ship, determined to follow the path he had set for me."
            if holly_trinity == 2:
                "Even if that meant driving a wedge between Ian, Holly, and me... The kind of relationship Seymour offered far surpassed any other."
            elif ian_lena_couple:
                "Even if that meant driving a wedge between Ian and me... The kind of relationship Seymour offered far surpassed any other."
            s "Lena...! Oh, Lena...!"
            "Hearing my name in moans escape his lips only fueled my excitement. I was making him tremble. Right now, I had him in the palm of my hand..."
            play sound "sfx/bj6.mp3"
            show v13_seymour18_cum with flash
            s "Ahhh!!" with vpunch
            pause 0.6
            with vpunch
            pause 0.6
            with vpunch
            pause 0.6
            "My head spun as he spilled his hot, plentiful cum in my mouth, and I tasted him for the first time."
            scene v13_seymour19
            if lena_look == "lingerie2b":
                show v13_seymour19a
            else:
                show v13_seymour19b
            if lena_tattoo2:
                show v13_seymour19_t2
            with long
            play sound "sfx/mh3.mp3"
            pause 1
            "He was the remedy to all my ailments and worries. He would shield me and elevate me to any height I desired, showering me in gold."
            "In return, I would give him whatever he desired of me."
            "I would conquer his body and heart... just as he had done with mine."
            stop music fadeout 3.0
            $ seymour_disposition = 3

        "...":
            $ renpy.block_rollback()
            "It had finally happened. I had really accepted Seymour inside me..."
            if seymour_disposition < 2:
                "Somehow, I felt less conflicted than I should about it. Still... I was aware of what my choice meant."
            "There was no room for ambiguity anymore: I was on Seymour's ship, determined to follow the path he had set for me."
            if holly_trinity == 2:
                "Even if that meant driving a wedge between Ian, Holly, and me... The kind of relationship Seymour offered far surpassed any other."
            elif ian_lena_couple:
                "Even if that meant driving a wedge between Ian and me... The kind of relationship Seymour offered far surpassed any other."
            "I had won a once-in-a-lifetime lottery, and I could never forgive myself if I didn't cash it in."
            "For my family's sake... and for my own."
            if seymour_disposition < 2:
                $ seymour_disposition = 2
    pause 1
    scene black with long
    pause 2
    $ renpy.end_replay()
    $ gallery_unlock_scene("CH13_S03")
    jump master_script