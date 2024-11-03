############################################################################################################################################################################
## LIST OF GALLERY SCENES ##################################################################################################################################################
############################################################################################################################################################################

define gallery_scenes = [
    ##################################################################################################################
    ## CHAPTER 1 #####################################################################################################
    ##################################################################################################################

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Ian watches porn"),
        img="v1_ianfap.webp",
        param="gallery_CH01_S01",
        unlocked_if="gallery_scene_unlocked('CH01_S01')",
        chars=['Ian'],
        scope=merge_two_dicts(cheatScope, lenaCleanBodyScope)
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=1,
        name=_("Ivy sends a nude to Jeremy"),
        img=["blackbg1.webp", "v1_selfiejeremy.webp"],
        param=["v1_selfiejeremy"],
        unlocked_if="renpy.seen_image('v1_selfiejeremy')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("First pole dance lesson"),
        img=["polegym.webp", "v1_pole2.webp"],
        param="gallery_CH01_S02",
        unlocked_if="gallery_scene_unlocked('CH01_S02')",
        chars=['Lena', 'Ivy'],
        scope=merge_three_dicts(cheatScope,lenaCleanBodyScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Photo shoot with Danny"),
        img="v1_pose1.webp",
        param="gallery_CH01_S03",
        unlocked_if="gallery_scene_unlocked('CH01_S03')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope,lenaCleanBodyScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Ian goes to a life drawing event"),
        img=["gallery2.webp", "v2_lenadraw1.webp"],
        param="gallery_CH01_S04",
        unlocked_if="gallery_scene_unlocked('CH01_S04')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope,lenaCleanBodyScope, {'v1_name': True})
    ),

    ##################################################################################################################
    ## CHAPTER 2 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=2,
        name=_("Ian and Perry look up Lena's PG"),
        img=["blackbg1.webp", "v1_peoplegram.webp"],
        param=["v1_peoplegram", "v1_pg2", "v1_pg3b"],
        unlocked_if="renpy.seen_image('v1_pg3')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="image",
        chapter=2,
        name=_("Alison sends a selfie to Ian"),
        img=["blackbg1.webp", "v2_alison_selfie1.webp"],
        param=["v2_alison_selfie1"],
        unlocked_if="renpy.seen_image('v2_alison_selfie1')",
        chars=['Alison']
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=2,
        name=_("Alison sends a selfie to Jeremy"),
        img=["blackbg1.webp", "v2_alison_selfie2.webp"],
        param=["v2_alison_selfie2"],
        unlocked_if="renpy.seen_image('v2_alison_selfie2')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ivy shows StalkFap during pole dance"),
        img=["polegym.webp", "v2_pole1.webp"],
        param="gallery_CH02_S01",
        unlocked_if="gallery_scene_unlocked('CH02_S01')",
        chars=['Lena', 'Ivy'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v1_talk_ivy': True, 
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Lena agrees to drinks"),
        img=["lenaroomnight.webp", "v2_robert5.webp"],
        param="gallery_CH02_S03",
        unlocked_if="gallery_scene_unlocked('CH02_S03')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'lena_robert': 5,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("The morning after"),
        img=["lenaroom.webp", "images/v2_robert6.webp"],
        param="gallery_CH02_S04",
        unlocked_if="gallery_scene_unlocked('CH02_S04')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v2_robert_home': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Third pole dance lesson"),
        img=["polegym.webp", "v2_gym.webp"],
        param="gallery_CH02_S05",
        unlocked_if="gallery_scene_unlocked('CH02_S05')",
        chars=['Lena', 'Ivy'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ian brings Cherry home after the bar"),
        img=["ianroomnight.webp", "v2_cherry5.webp"],
        param="gallery_CH02_S06",
        unlocked_if="gallery_scene_unlocked('CH02_S06')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts(cheatScope, lenaCleanBodyScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ian brings Alison home after the bar"),
        img=["ianroomnight.webp", "v2_alison5.webp"],
        param="gallery_CH02_S07",
        unlocked_if="gallery_scene_unlocked('CH02_S07')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope,lenaCleanBodyScope)
    ),

    ##################################################################################################################
    ## CHAPTER 3 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ivy posts on StalkFap"),
        img=["blackbg1.webp", "v3_ivyselfie1.webp"],
        param=["v3_ivyselfie1"],
        unlocked_if="renpy.seen_image('v3_stalkfap1')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Lena kisses Ian"),
        img="v2_ian_kiss2b.webp",
        param=["v2_ian_kiss1b", "v2_ian_kiss2b"],
        unlocked_if="renpy.seen_image('v2_ian_kiss2') or renpy.seen_image('v2_ian_kiss2b')",
        chars=['Lena', 'Ian']
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena has sex after her date"),
        img="v3_robert10b.webp",
        param="gallery_CH03_S01",
        unlocked_if="gallery_scene_unlocked('CH03_S01')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v2_robert_bj': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena spies on Louise and Jeremy"),
        img="v3_louise1.webp",
        param="gallery_CH03_S02",
        unlocked_if="gallery_scene_unlocked('CH03_S02')",
        chars=['Louise', 'Jeremy'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena agrees to model for Stan"),
        img=["lenahome.webp", "v3_stan2.webp"],
        param="gallery_CH03_S08",
        unlocked_if="gallery_scene_unlocked('CH03_S08')",
        chars=['Lena', 'Stan'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v2_stan_model': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Cherry wakes up Ian"),
        img="v3_cherry1.webp",
        param="gallery_CH03_S03",
        unlocked_if="gallery_scene_unlocked('CH03_S03')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts(cheatScope,lenaCleanBodyScope)
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ian looks at Cherry's Peoplegram"),
        img=["blackbg1.webp", "v3_peoplegram_cherry1.webp"],
        param=["v3_peoplegram_cherry1b", "v3_peoplegram_cherry2"],
        unlocked_if="renpy.seen_image('v3_peoplegram_cherry2')",
        chars=['Cherry']
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=3,
        name=_("Ian looks at Cindy's Peoplegram"),
        img=["blackbg1.webp", "v3_cindy_peoplegram.webp"],
        param=["v3_cindy_peoplegram"],
        unlocked_if="renpy.seen_image('v3_cindy_peoplegram')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ian thinks of Gillian"),
        img=["blackbg1.webp", "v3_gillian3.webp"],
        param=["v3_gillian1", "v3_gillian2", "v3_gillian3"],
        unlocked_if="renpy.seen_image('v3_gillian3')",
        chars=['Gillian']
    ),

    GalleryScene( # Unlocks in Ch 3/4 if ian_alison_sex == True
        kind="image",
        chapter=3,
        name=_("Alison sends a nude to Ian"),
        img=["blackbg1.webp", "v3_alison_selfie.webp"],
        param=["v3_alison_selfie"],
        unlocked_if="renpy.seen_image('v3_alison_selfie')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Ian goes on a date"),
        img="v3_alison7.webp",
        param="gallery_CH03_S04",
        unlocked_if="gallery_scene_unlocked('CH03_S04')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope,lenaCleanBodyScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena masturbates"),
        img="v3_solo1.webp",
        param="gallery_CH03_S05",
        unlocked_if="gallery_scene_unlocked('CH03_S05')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v3_spy': True,
            'v3_spy_full': True, 
            'v2_ian_date': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena calls Robert over"),
        img="v3_robert4.webp",
        param="gallery_CH03_S06",
        unlocked_if="gallery_scene_unlocked('CH03_S06')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaCleanBodyScope, {
            'v2_robert_home': True,
            'ian_active': False
        })
    ),

    ##################################################################################################################
    ## CHAPTER 4 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene( # Unlocks in Ch 4 if v3_bbc == True; in Ch 5 if louise_jeremy == False
        kind="image",
        chapter=4,
        name=_("Ivy shows Jeremy's nude"),
        img=["blackbg1.webp", "v5_jeremy_selfie.webp"],
        param=["v5_jeremy_selfie"],
        unlocked_if="renpy.seen_image('v5_jeremy_selfie')",
        chars=['Jeremy']
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena agrees to a photo shoot with Seymour"),
        img="v4_seymour6.webp",
        param="gallery_CH04_S01",
        unlocked_if="gallery_scene_unlocked('CH04_S01')",
        chars=['Lena', 'Seymour'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'lena_posh': 2,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena masturbates 2"),
        img="v4_solo1.webp",
        param="gallery_CH04_S02",
        unlocked_if="gallery_scene_unlocked('CH04_S02')",
        chars=['Lena', 'Axel'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v2_ian_date': True,
            'v3_robert_repeat': False,
            'v3_spy': True,
            'v4_seymour_date': True,
            'seymour_shoot': 4,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena blows Robert at work"),
        img="v4_restaurant2.webp",
        param="gallery_CH04_S03",
        unlocked_if="gallery_scene_unlocked('CH04_S03')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene( # Unlocks in Ch 4 if v3_alison_boobjob == True
        kind="image",
        chapter=4,
        name=_("Alison sends a boob pic to Ian"),
        img=["blackbg1.webp", "v4_alison_selfie.webp"],
        param=["v4_alison_selfie"],
        unlocked_if="renpy.seen_image('v4_alison_selfie')",
        chars=['Alison']
    ),

    GalleryScene( # Unlocks in Ch 4 if v4_cherry_sexting == True
        kind="image",
        chapter=4,
        name=_("Cherry sends a nude to Ian"),
        img=["blackbg1.webp", "v3_peoplegram_cherry2b.webp"],
        param=["v3_peoplegram_cherry2b"],
        unlocked_if="renpy.seen_image('v3_peoplegram_cherry2b')",
        chars=['Cherry']
    ),

    GalleryScene( # Unlocks in Ch 4 if ian_jeremy > 4; in Ch 6 (Lena's POV) if lena_bbc == True
        kind="image",
        chapter=4,
        name=_("Louise's private nudes"),
        img=["blackbg1.webp", "v4_louise_selfie1.webp"],
        param=["v4_louise_selfie1", "v4_louise_selfie2", "v4_louise_selfie3"],
        unlocked_if="renpy.seen_image('v4_louise_selfie3')",
        chars=['Louise', 'Jeremy']
    ),

    GalleryScene( # Unlocks in Ch 4/5 if alison_voyeur == True
        kind="image",
        chapter=4,
        name=_("Jeremy shares Alison's titfuck"),
        img=["blackbg1.webp", "v4_alison_jeremy.webp"],
        param=["v4_alison_jeremy"],
        unlocked_if="renpy.seen_image('v4_alison_jeremy')",
        chars=['Alison', 'Jeremy']
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Holly joins the pole dance lesson"),
        img="v4_gym_holly1.webp",
        param="gallery_CH04_S04",
        unlocked_if="gallery_scene_unlocked('CH04_S04')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena invites Ian over"),
        img="v4_lena6.webp",
        param="gallery_CH04_S06",
        unlocked_if="gallery_scene_unlocked('CH04_S06')",
        chars=['Lena', 'Ian'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    ##################################################################################################################
    ## CHAPTER 5 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian goes to Cindy's photo shoot"),
        img="v5_cindy7b.webp",
        param="gallery_CH05_S01",
        unlocked_if="gallery_scene_unlocked('CH05_S01')",
        chars=['Cindy'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ivy performs at the club"),
        img="v5_ivy1.webp",
        param="gallery_CH05_S02",
        unlocked_if="gallery_scene_unlocked('CH05_S02')",
        chars=['Ivy'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian brings Emma home after dancing"),
        img="v5_emma5.webp",
        param="gallery_CH05_S03",
        unlocked_if="gallery_scene_unlocked('CH05_S03')",
        chars=['Ian', 'Emma'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'alison_jeremy': True,
            'ian_alison_sex': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian brings Alison home after dancing"),
        img="v5_alison3.webp",
        param="gallery_CH05_S04",
        unlocked_if="gallery_scene_unlocked('CH05_S04')",
        chars=['Ian', 'Alison'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'v5_perry_club': False})
    ),

    GalleryScene( # Unlocks in Ch 5 if v2_alison_home == False + alison_voyeur == True
        kind="image",
        chapter=5,
        name=_("Jeremy shares his sex tape"),
        img=["blackbg1.webp", "v5_voyeur1.webp"],
        param=["alison_voyeur_v5"],
        unlocked_if="renpy.seen_image('v5_voyeur4')",
        chars=['Alison', 'Jeremy']
    ),

    GalleryScene( # Unlocks in Ch 5 if stalkfap_pro == 1; in Ch 8 if stalkfap == True + stalkfap_pro == 0
        kind="image",
        chapter=5,
        name=_("Lena took stalkfap more seriously"),
        img=["blackbg1.webp", "v5_stalkfap1.webp"],
        param=["v5_stalkfap1"],
        unlocked_if="renpy.seen_image('v5_stalkfap1_comp') or renpy.seen_image('v5_stalkfap1')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Louise seeks comfort"),
        img=["v5_louise1.webp", "v5_louise1_eyes2.webp", "v5_louise1_choker.webp"],
        param="gallery_CH05_S05",
        unlocked_if="gallery_scene_unlocked('CH05_S05')",
        chars=['Lena', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v4_confront_louise': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Lena brings Mike home from the club"),
        img="v5_mike5c.webp",
        param="gallery_CH05_S06",
        unlocked_if="gallery_scene_unlocked('CH05_S06')",
        chars=['Lena', 'Mike'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Lena needs more professional pictures"),
        img="v5_model2b.webp",
        param="gallery_CH05_S07",
        unlocked_if="gallery_scene_unlocked('CH05_S07') or gallery_scene_unlocked('CH05_S08')",
        chars=['Lena', 'Stan'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v3_stan_shoot': 3,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Robert sexts with Lena"),
        img=["blackbg1.webp", "v5_sexting2.webp"],
        param="gallery_CH05_S09",
        unlocked_if="gallery_scene_unlocked('CH05_S09')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v4_robert_sex': True,
            'ian_active': False
        })
    ),

    GalleryScene( # Unlocks in Ch 5 if stalkfap_pro > 0
        kind="image",
        chapter=5,
        name=_("Lena posted another selfie"),
        img=["blackbg1.webp", "v5_stalkfap2.webp"],
        param=["v5_stalkfap2"],
        unlocked_if="renpy.seen_image('v5_stalkfap2') or renpy.seen_image('v5_stalkfap2b')",
        chars=['Lena']
    ),

    ##################################################################################################################
    ## CHAPTER 6 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=6,
        name=_("Cindy's modeling pics"),
        img=["blackbg1.webp", "v6_cindy_pic2a.webp"],
        param=["v6_cindy_pic1", "v6_cindy_pic2a", "v6_cindy_pic2b"],
        unlocked_if="renpy.seen_image('v6_cindy_pic1') or renpy.seen_image('v6_cindy_pg2b')",
        chars=['Cindy']
    ),

    GalleryScene( # Unlocks if v5_cindy_shoot == True and v5_cindy_nude > 1
        kind="image",
        chapter=6,
        name=_("Ian asks Cindy for another one"),
        img=["blackbg1.webp", "v6_cindy_pic3.webp"],
        param=["v6_cindy_pic3"],
        unlocked_if="renpy.seen_image('v6_cindy_pic3')",
        chars=['Cindy']
    ),

    GalleryScene( # Unlocks in Ch 6 if v6_cherry_selfie == True
        kind="image",
        chapter=6,
        name=_("Cherry texts Ian"),
        img=["blackbg1.webp", "v6_cherry_selfie.webp"],
        param=["v6_cherry_selfie"],
        unlocked_if="renpy.seen_image('v6_cherry_selfie')",
        chars=['Cherry']
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=6,
        name=_("Perry shows Ivy's Peoplegram"),
        img=["blackbg1.webp", "v6_ivy_pg.webp"],
        param=["v6_ivy_pgb"],
        unlocked_if="renpy.seen_image('v6_ivy_pg')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian takes Alison home after bar"),
        img="v6_alison5.webp",
        param="gallery_CH06_S01",
        unlocked_if="gallery_scene_unlocked('CH06_S01')",
        chars=['Ian', 'Alison'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v6_rightaway': 'alison',
            'ian_alison_like': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian takes Cherry home after bar"),
        img="v6_cherry3.webp",
        param="gallery_CH06_S02",
        unlocked_if="gallery_scene_unlocked('CH06_S02')",
        chars=['Ian', 'Cherry'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'v6_rightaway': 'cherry'})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena & Ian have sex after date"),
        img="v6_lena3.webp",
        param="gallery_CH06_S03",
        unlocked_if="gallery_scene_unlocked('CH06_S03')",
        chars=['Ian', 'Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'lena_bj': 5})
    ),
    
    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian hatefucks Minerva"),
        img="v6_minerva5.webp",
        param="gallery_CH06_S04",
        unlocked_if="gallery_scene_unlocked('CH06_S04')",
        chars=['Ian', 'Minerva'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'holly_gym': True})
    ),

    GalleryScene( # Unlocks if v6_ian_selfie == True / lena_mike_dating == True / (v6_robert_date == True + v5_robert_sexting == True)
        kind="scene",
        chapter=6,
        name=_("Lena rewarded Ian / Teased Mike or Robert"),
        img=["blackbg1.webp", "v6_lena_selfie1.webp"],
        param="gallery_CH06_S15",
        unlocked_if="gallery_scene_unlocked('CH06_S15')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene( # Unlocks if stalkfap == True + v5_shoot == 0
        kind="image",
        chapter=6,
        name=_("Lena decides to please her fans"),
        img=["blackbg1.webp", "v6_stalkfap2.webp"],
        param=["v6_stalkfap2"],
        unlocked_if="renpy.seen_image('v6_stalkfap2')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Pole dance lesson 5"),
        img="v6_gym_ivy.webp",
        param="gallery_CH06_S05",
        unlocked_if="gallery_scene_unlocked('CH06_S05')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Holly gets kissed"),
        img="v6_holly2_ivy.webp",
        param="gallery_CH06_S06",
        unlocked_if="gallery_scene_unlocked('CH06_S06')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena is awakened by Louise"),
        img=["v6_louise1.webp", "v6_louise1b.webp"],
        param="gallery_CH06_S07",
        unlocked_if="gallery_scene_unlocked('CH06_S07')",
        chars=['Lena', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene( # Unlocks in Ch 6/7 if v6_stalkfap_ivy == True
        kind="image",
        chapter=6,
        name=_("Lena checks Ivy's Stalkfap posts"),
        img=["blackbg1.webp", "v6_stalkfap_ivy1.webp"],
        param=["v6_stalkfap_ivy1","v6_stalkfap_ivy2", "v6_stalkfap_twerk"],
        unlocked_if="renpy.seen_image('v6_stalkfap_ivy2')",
        chars=['Ivy']
    ),
    
    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena masturbates 3"),
        img="v4_solo2.webp",
        param="gallery_CH06_S08",
        unlocked_if="gallery_scene_unlocked('CH06_S08')",
        chars=['Lena', 'Jeremy', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena invited Mike over"),
        img="v6_mike2.webp",
        param="gallery_CH06_S09",
        unlocked_if="gallery_scene_unlocked('CH06_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Robert comes back from his trip"),
        img=["v6_robert1.webp", "v6_robert1_bunny.webp"],
        param="gallery_CH06_S10",
        unlocked_if="gallery_scene_unlocked('CH06_S10')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena invited Ian over"),
        img="v6_ian4b.webp",
        param="gallery_CH06_S11",
        unlocked_if="gallery_scene_unlocked('CH06_S11')",
        chars=['Lena', 'Ian'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena wakes Robert with a bj"),
        img="v2_robert7.webp",
        param="gallery_CH06_S12",
        unlocked_if="gallery_scene_unlocked('CH06_S12')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena has a photo shoot with Axel"),
        img="v6_axel4.webp",
        param="gallery_CH06_S13",
        unlocked_if="gallery_scene_unlocked('CH06_S13') or gallery_scene_unlocked('CH06_S14')",
        chars=['Lena', 'Axel', 'Seymour'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=6,
        name=_("Ivy shows her tattoo"),
        img="v6_ivy_tattoo.webp",
        param=["v6_ivy_tattoo"],
        unlocked_if="renpy.seen_image('v6_ivy_tattoo')",
        chars=['Ivy']
    ),

    ##################################################################################################################
    ## CHAPTER 7 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian masturbates to nudes"),
        img="v7_jerkoff1_gallery.webp",
        param="gallery_CH07_S01",
        unlocked_if="gallery_scene_unlocked('CH07_S01')",
        chars=['Ian'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian asks Jeremy for more"),
        img=["blackbg1.webp", "v7_alisonbbc1.webp"],
        param="gallery_CH07_S20",
        unlocked_if="gallery_scene_unlocked('CH07_S20')",
        chars=['Alison', 'Jeremy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v1_encourage_alison': True,
            'ian_alison_dating': False,
            'ian_alison_sex': False,
            'v3_alison_boobjob': False,
            'v5_alison_boobjob': False,
            'ian_alison_like': 0,
            'v6_alison_extra_pic': False,
            'v6_alison_cum': False,
            'v2_alison_home': False,
            'alison_voyeur': True,
            'v5_alison_jeremy': True,
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Cindy's second photo shoot"),
        img=["blackbg1.webp", "v7_cindy_pic2.webp"],
        param="gallery_CH07_S21",
        unlocked_if="gallery_scene_unlocked('CH07_S21')",
        chars=['Cindy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_cindy_model': True,
            'ian_go_cindy': 3,
            'v5_cindy_shoot': True,
            'wade_cindy': 0,
            'v5_cindy_nude': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Minerva needs Ian"),
        img="v7_minerva3.webp",
        param="gallery_CH07_S02",
        unlocked_if="gallery_scene_unlocked('CH07_S02')",
        chars=['Ian', 'Minerva'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian visits Lena's life drawing"),
        img="v7_drawing1a.webp",
        param="gallery_CH07_S03",
        unlocked_if="gallery_scene_unlocked('CH07_S03')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena had a sexy dream"),
        img="v7_dream2.webp",
        param="gallery_CH07_S04",
        unlocked_if="gallery_scene_unlocked('CH07_S04')",
        chars=['Lena', 'Axel'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena goes to another life drawing"),
        img=["v7_drawing4a.webp", "v7_drawing4_ian.webp"],
        param="gallery_CH07_S05",
        unlocked_if="gallery_scene_unlocked('CH07_S05')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena takes Robert home after life drawing"),
        img="v7_robert1.webp",
        param="gallery_CH07_S06",
        unlocked_if="gallery_scene_unlocked('CH07_S06')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena goes with Ian after life drawing"),
        img="v7_lena2.webp",
        param="gallery_CH07_S07",
        unlocked_if="gallery_scene_unlocked('CH07_S07')",
        chars=['Lena', 'Ian'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("The morning after life drawing with Robert"),
        img="v7_robert4.webp",
        param="gallery_CH07_S08",
        unlocked_if="gallery_scene_unlocked('CH07_S08')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_active': False,
            'lena_robert_dating': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("The morning after life drawing with Ian"),
        img="v7_lena8b.webp",
        param="gallery_CH07_S18",
        unlocked_if="gallery_scene_unlocked('CH07_S18')",
        chars=['Lena', 'Ian'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_active': False,
            'v7_ian_date': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena masturbates after her dream"),
        img="v7_solo1.webp",
        param="gallery_CH07_S19",
        unlocked_if="gallery_scene_unlocked('CH07_S19')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_active': False,
            'lena_axel_desire': True
        })
    ),

    GalleryScene( # Unlocks if holly_gym == True and v7_talkclubholly == True
        kind="image",
        chapter=7,
        name=_("Ivy shows off Mark"),
        img=["blackbg1.webp", "v7_mark.webp"],
        param=["v7_mark"],
        unlocked_if="renpy.seen_image('v7_mark')",
        chars=['Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena visits Mike at his dj booth"),
        img="v7_mike1a.webp",
        param="gallery_CH07_S09",
        unlocked_if="gallery_scene_unlocked('CH07_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v7mikemusic': 'latin',
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'lena_mike_dating': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena catches Louise masturbating"),
        img=["v7_louise1b.webp", "v7_louise1c.webp"],
        param="gallery_CH07_S10",
        unlocked_if="gallery_scene_unlocked('CH07_S10')",
        chars=['Lena', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'lena_louise_sex': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Party with Ivy, Jeremy, and Louise"),
        img="v7_ivy3.webp",
        param="gallery_CH07_S11",
        unlocked_if="gallery_scene_unlocked('CH07_S11')",
        chars=['Lena', 'Ivy', 'Jeremy', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v3_spy_full': True,
            'lena_bbc': True,
            'lena_axel_desire': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena records a video for Stalkfap"),
        img="v7_dance3.webp",
        param="gallery_CH07_S12",
        unlocked_if="gallery_scene_unlocked('CH07_S12')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'stan_simp': 1,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Emma visits before Wade's b-day party"),
        img="v7_emma2.webp",
        param="gallery_CH07_S13",
        unlocked_if="gallery_scene_unlocked('CH07_S13')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Alison visits before Wade's b-day party"),
        img="v7_alison2.webp",
        param="gallery_CH07_S14",
        unlocked_if="gallery_scene_unlocked('CH07_S14')",
        chars=['Ian', 'Alison'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'alison_sexy': 2})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian follows Cindy after her argument"),
        img="v7_cindy10.webp",
        param="gallery_CH07_S15",
        unlocked_if="gallery_scene_unlocked('CH07_S15')",
        chars=['Ian', 'Cindy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'ian_go_cindy': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian goes with Holly to the bookfair"),
        img="v7_holly4.webp",
        param="gallery_CH07_S16",
        unlocked_if="gallery_scene_unlocked('CH07_S16')",
        chars=['Ian', 'Holly'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {'v7_effort_holly': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena indulges her curiosity"),
        img=["v7_solo4a.webp", "v7_solo_bbc2.webp"],
        param="gallery_CH07_S17",
        unlocked_if="gallery_scene_unlocked('CH07_S17')",
        chars=['Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v7_game': True,
            'cafe_music': True,
            'ian_active': False
        })
    ),

    ##################################################################################################################
    ## CHAPTER 8 #####################################################################################################
    ##################################################################################################################
    
    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("The morning after"),
        img="v8_hotel1.webp",
        param="gallery_CH08_S01",
        unlocked_if="gallery_scene_unlocked('CH08_S01')",
        chars=['Ian', 'Holly'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v7_holly_bj': True,
            'v7_holly_rough': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena has sex at the restaurant"),
        img="v8_robert1.webp",
        param="gallery_CH08_S02",
        unlocked_if="gallery_scene_unlocked('CH08_S02')",
        chars=['Lena', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v8_robert_public': True,
            'ian_active': False
        })
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=8,
        name=_("Ivy's Peoplegram photos"),
        img=["blackbg1.webp", "v8_ivy_pg1.webp"],
        param=["v8_ivy_pg1","v8_ivy_pg2"],
        unlocked_if="renpy.seen_image('v8_ivy_pg2')",
        chars=['Ivy']
    ),

    GalleryScene( # Unlocks in all branches
        kind="image",
        chapter=8,
        name=_("Ed gives Lena his drawing"),
        img=["blackbg1.webp", "v8_ed_drawing.webp"],
        param=["v8_ed_drawing"],
        unlocked_if="renpy.seen_image('v8_ed_drawing')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena bought something for Louise"),
        img=["v8_louise1.webp", "v8_louise1_collar.webp"],
        param="gallery_CH08_S03",
        unlocked_if="gallery_scene_unlocked('CH08_S03')",
        chars=['Lena', 'Louise'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'v6_louise_orgasm': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena sexts with fans and friends"),
        img=["lenaroomnight.webp", "v8_sexting2.webp"],
        param="gallery_CH08_S04",
        unlocked_if="gallery_scene_unlocked('CH08_S04')",
        chars=['Lena', 'Ian', 'Jeremy', 'Mike', 'Robert'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'lena_money': 3,
            'ian_active': False
        })
    ),

    ## CH8 - B ##

    GalleryScene( # Unlocks if ian_alison_dating == True
        kind="image",
        chapter=8,
        name=_("Alison sends Ian a present at work"),
        img=["blackbg1.webp", "v8_selfie_alison1.webp"],
        param=["v8_selfie_alison1"],
        unlocked_if="renpy.seen_image('v8_selfie_alison1')",
        chars=['Alison']
    ),

    GalleryScene( # Unlocks if emma_jeremy == True
        kind="image",
        chapter=8,
        name=_("Jeremy shares a pic of him and Emma"),
        img=["blackbg1.webp", "v8_emma_jeremy.webp"],
        param=["v8_emma_jeremy"],
        unlocked_if="renpy.seen_image('v8_emma_jeremy')",
        chars=['Jeremy', 'Emma']
    ),

    GalleryScene( # Unlocks if v8_alison_sexting > 0
        kind="image",
        chapter=8,
        name=_("Ian sexts with Alison"),
        img=["blackbg1.webp", "v8_selfie_alison3.webp", "v8_selfie_alison3_p.webp"],
        param=["v8_selfie_alison3","v8_selfie_alison4", "v8_selfie_alison5", "v8_selfie_dick"],
        unlocked_if="renpy.seen_image('v8_selfie_alison5')",
        chars=['Ian','Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Ian goes into Minerva's office"),
        img="v8_minerva1.webp",
        param="gallery_CH08_S05",
        unlocked_if="gallery_scene_unlocked('CH08_S05')",
        chars=['Ian', 'Minerva'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_minerva_sex': True,
            'v7_minerva_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Sex after the concert"),
        img="v8_lena2.webp",
        param="gallery_CH08_S06",
        unlocked_if="gallery_scene_unlocked('CH08_S06')",
        chars=['Ian', 'Lena'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'ian_lena_sex_late': False,
            'v7_cindy_kiss': False,
            'ian_lena_love': True,
            'lena_ian_love': True,
            'lena_bj': 4,
            'ian_dirty_talk': 2,
            'lena_wardrobe_wits1': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=8,
        name=_("Ian teases Cherry"),
        img=["blackbg1.webp", "v8_selfie_cherry.webp"],
        param=["v8_sexting_ian","v8_selfie_cherry"],
        unlocked_if="renpy.seen_image('v8_selfie_cherry')",
        chars=['Ian', 'Cherry']
    ),

    GalleryScene( # Unlocks if ian_lena_dating == True
        kind="image",
        chapter=8,
        name=_("Ian shows Axel's PG to his friends"),
        img=["blackbg1.webp", "v9_axel_pg1.webp"],
        param=["v9_axel_pg1", "v9_axel_pg2"],
        unlocked_if="renpy.seen_image('v9_axel_pg2')",
        chars=['Axel']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Ian walks in on Perry & Emma"),
        img="v8_perry.webp",
        param="gallery_CH08_S08",
        unlocked_if="gallery_scene_unlocked('CH08_S08')",
        chars=['Emma', 'Perry'],
        scope=merge_two_dicts(cheatScope,lenaNoTattooScope)
    ),

    ## CH8 - C ##

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena wakes up Jeremy"),
        img="v8_jeremy1.webp",
        param="gallery_CH08_S09",
        unlocked_if="gallery_scene_unlocked('CH08_S09')",
        chars=['Lena', 'Jeremy'],
        scope=merge_three_dicts(cheatScope, lenaNoTattooScope, {
            'lena_bbc': True,
            'v3_spy_full': True,
            'v7_bbc_cum': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("The girls have a drink"),
        img="v8_ivy3.webp",
        param="gallery_CH08_S10",
        unlocked_if="gallery_scene_unlocked('CH08_S10')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_ivy': 5,
            'lena_go_holly': 3,
            'holly_change': 2,
            'lena_bdick': 3,
            'lena_axel_desire': True,
            'holly_gym': True,
            'v6_holly_kiss': 'lena',
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Holly goes home with Lena"),
        img="v8_holly3.webp",
        param="gallery_CH08_S12",
        unlocked_if="gallery_scene_unlocked('CH08_S12')",
        chars=['Lena', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'lena_go_holly': 3,
            'holly_change': 2,
            'holly_gym': True,
            'v6_holly_kiss': 'lena',
            'ian_active': False
        })
    ),

    ## CH8 - D ##

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Emma wakes Ian after doing drugs"),
        img="v8_emma1.webp",
        param="gallery_CH08_S07",
        unlocked_if="gallery_scene_unlocked('CH08_S07')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'v8_trip': True,
            'v7_emma_bj': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena invites Mike over"),
        img="v8_mike1.webp",
        param="gallery_CH08_S11",
        unlocked_if="gallery_scene_unlocked('CH08_S11')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts(cheatScope, {
            'v8_lena_sexting': 'mike',
            'v7_mike_bj': True,
            'mike_dirty_talk': 2,
            'lena_anal_first': 'mike',
            'ian_active': False
        })
    ),

    ##################################################################################################################
    ## CHAPTER 9 #####################################################################################################
    ##################################################################################################################

    GalleryScene( # Unlocks if ian_lena_dating == True + ian_lena_sex == True
        kind="image",
        chapter=9,
        name=_("Lena kept Ian's shirt"),
        img=["blackbg1.webp", "v9_lena_selfie1.webp"],
        param=["v9_lena_selfie1_comp"],
        unlocked_if="renpy.seen_image('v9_lena_selfie1_comp')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Holly gives Ian a blowjob"),
        img="v9_holly4.webp",
        param="gallery_CH09_S01",
        unlocked_if="gallery_scene_unlocked('CH09_S01')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'holly_change': 3,
            'ian_chad': 4,
            'v8_holly_bj': True,
            'holly_look': '1skirt'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian texts Emma"),
        img=["blackbg1.webp", "v9_emma2.webp"],
        param="gallery_CH09_S13",
        unlocked_if="gallery_scene_unlocked('CH09_S13')",
        chars=['Ian', 'Emma'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian texts Jeremy"),
        img=["blackbg1.webp", "v9_emma6.webp"],
        param="gallery_CH09_S14",
        unlocked_if="gallery_scene_unlocked('CH09_S14')",
        chars=['Emma', 'Jeremy'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian confesses to Cherry"),
        img="v9_cherry5.webp",
        param="gallery_CH09_S02",
        unlocked_if="gallery_scene_unlocked('CH09_S02')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'v6_cherry_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian accompanies Alison on her trip"),
        img="v9_alison13.webp",
        param="gallery_CH09_S03",
        unlocked_if="gallery_scene_unlocked('CH09_S03')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope, {
            'alison_sexy': 2,
            'alison_extras': 1,
            'ian_alison_like': 2,
            'alison_satisfaction': 5,
            'v6_alison_cum': True,
            'v8_alison_sext': 3,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene( # Unlocks if ian_holly_dating == True / holly_guy == True
        kind="image",
        chapter=9,
        name=_("Holly steps out of her comfort zone"),
        img=["blackbg1.webp", "v9_holly_selfie1.webp"],
        param=["v9_holly_selfie1"],
        unlocked_if="renpy.seen_image('v9_holly_selfie1')",
        chars=['Holly']
    ),

    GalleryScene( # Unlocks if ian_holly_dating == True
        kind="image",
        chapter=9,
        name=_("Holly misses Ian"),
        img=["blackbg1.webp", "v9_holly_selfie2.webp"],
        param=["v9_holly_selfie2"],
        unlocked_if="renpy.seen_image('v9_holly_selfie2')",
        chars=['Holly']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian welcomes Lena back"),
        img="v9_lena8a.webp",
        param="gallery_CH09_S04",
        unlocked_if="gallery_scene_unlocked('CH09_S04')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_lena_couple': True,
            'ian_lena_sex': True,
            'lena_bj': 4,
            'ian_chad': 4
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Jeremy sends a video from Alison's trip"),
        img=["blackbg1.webp", "v9_bbc2.webp"],
        param="gallery_CH09_S05",
        unlocked_if="gallery_scene_unlocked('CH09_S05')",
        chars=['Alison', 'Billy', 'Jeremy'],
        scope=merge_two_dicts(cheatScope, {
            'alison_sexy': 2,
            'v9alisonphone': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian accompanies Cindy to Axel's shoot"),
        img="v9_cindy_shoot1b.webp",
        param="gallery_CH09_S06",
        unlocked_if="gallery_scene_unlocked('CH09_S06')",
        chars=['Axel', 'Cindy'],
        scope=merge_two_dicts(cheatScope, {
            'v5_cindy_shoot': True,
            'v5_cindy_nude': 2,
            'v7_axel_date': True,
            'ian_cindy_model': True,
            'v7_cindy_kiss': True,
            'ian_cindy_sex': True,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian confesses to Cindy"),
        img="v9_cindy6.webp",
        param="gallery_CH09_S07",
        unlocked_if="gallery_scene_unlocked('CH09_S07')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene( # Unlocks if stalkfap == True
        kind="image",
        chapter=9,
        name=_("Lena posted to Stalkfap"),
        img=["blackbg1.webp", "v9_stalkfap1.webp"],
        param=["v9_stalkfap1"],
        unlocked_if="renpy.seen_image('v9_stalkfap1')",
        chars=['Lena']
    ),

    GalleryScene( # Unlocks if stalkfap_pro == 2
        kind="image",
        chapter=9,
        name=_("Lena's home videos"),
        img=["blackbg1.webp", "v9_stalkfap2.webp"],
        param=["v9_stalkfap2", "v9_stalkfap3", "v9_stalkfap4", "v9_stalkfap5"],
        unlocked_if="renpy.seen_image('v9_stalkfap5')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Robert helps Lena unpack"),
        img="v9_robert1.webp",
        param="gallery_CH09_S08",
        unlocked_if="gallery_scene_unlocked('CH09_S08')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Mike helps Lena unpack"),
        img=["v9_mike2.webp", "v9_mike2_bunny.webp"],
        param="gallery_CH09_S09",
        unlocked_if="gallery_scene_unlocked('CH09_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts(cheatScope, {
            'lena_anal': 2,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena poses for Axel"),
        img="v9_lena_shoot3b.webp",
        param="gallery_CH09_S10",
        unlocked_if="gallery_scene_unlocked('CH09_S10')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts(cheatScope, {
            'v6_axel_pose': 3,
            'axel_disposition': 2,
            'axel_pictures_watch': True,
            'lena_axel_desire': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena submits to Axel"),
        img="v9_axel6a.webp",
        param="gallery_CH09_S11",
        unlocked_if="gallery_scene_unlocked('CH09_S11')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts(cheatScope, {
            'v6_axel_pose': 3,
            'axel_disposition': 2,
            'axel_pictures_watch': True,
            'lena_axel_desire': True,
            'ian_active': False
        })
    ),

    GalleryScene( # Unlocks if v8_holly_sex == "ivy"/"lenaivy"
        kind="scene",
        chapter=9,
        name=_("Holly greets Ivy"),
        img="v9_holly8.webp",
        param="gallery_CH09_S15",
        unlocked_if="gallery_scene_unlocked('CH09_S15')",
        chars=['Holly', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena signs the contract"),
        img=["v9_seymour3.webp", "v9_seymour3_sy.webp"],
        param="gallery_CH09_S12",
        unlocked_if="gallery_scene_unlocked('CH09_S12')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts(cheatScope, {
            'seymour_disposition': 3,
            'ian_active': False
        })
    ),

    ##################################################################################################################
    ## CHAPTER 10 ####################################################################################################
    ##################################################################################################################

    # Ian
    ## Sunday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian pays to see Lena's exclusive content"),
        img=["blackbg1.webp", "v10_stalkfap2c.webp"],
        param="gallery_CH10_S19",
        unlocked_if="gallery_scene_unlocked('CH10_S19')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_lena_couple': True,
            'stalkfap': True,
            'ian_stalkfap': True,
            'stalkfap_pro': 2,
            'v7_dance': 2,
            'v7_dance_provoke': 3
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Ian teases the ladies"),
        img=["blackbg1.webp", "v10_selfie_ian.webp"],
        param=["v10_selfie_ian"],
        unlocked_if="renpy.seen_image('v10_selfie_ian')",
        chars=['Ian']
    ),

    GalleryScene( # Unlocks if ian_alison_dating == True
        kind="image",
        chapter=10,
        name=_("Alison responds to teasing"),
        img=["blackbg1.webp", "v10_selfie_alison.webp"],
        param=["v10_selfie_alison"],
        unlocked_if="renpy.seen_image('v10_selfie_alison')",
        chars=['Alison']
    ),

    GalleryScene( # Unlocks if ian_cherry_love == True
        kind="image",
        chapter=10,
        name=_("Cherry rewards a caring Ian"),
        img=["blackbg1.webp", "v10_selfie_cherry.webp"],
        param=["v10_selfie_cherry"],
        unlocked_if="renpy.seen_image('v10_selfie_cherry')",
        chars=['Cherry']
    ),

    GalleryScene( # Unlocks if ian_cindy_dating == True + v10_text_cindy == 2
        kind="image",
        chapter=10,
        name=_("Cindy responds to teasing"),
        img=["blackbg1.webp", "v10_selfie_cindy1.webp"],
        param=["v10_selfie_cindy1"],
        unlocked_if="renpy.seen_image('v10_selfie_cindy1')",
        chars=['Cindy']
    ),

    GalleryScene( # Unlocks if ian_holly_dating == True + holly_change > 2
        kind="image",
        chapter=10,
        name=_("Holly gives something in return"),
        img=["blackbg1.webp", "v10_selfie_holly.webp"],
        param=["v10_selfie_holly"],
        unlocked_if="renpy.seen_image('v10_selfie_holly')",
        chars=['Holly']
    ),

    GalleryScene( # Unlocks if ian_lena_dating == True
        kind="image",
        chapter=10,
        name=_("Lena says good night"),
        img=["blackbg1.webp", "v10_selfie_lena1.webp"],
        param=["v10_selfie_lena1"],
        unlocked_if="renpy.seen_image('v10_selfie_lena1')",
        chars=['Lena']
    ),
    ## Monday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian and Holly stop by Ian's place"),
        img="v10_holly8.webp",
        param="gallery_CH10_S04",
        unlocked_if="gallery_scene_unlocked('CH10_S04')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'holly_change': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian brings Lena home after the park"),
        img="v10_ian4.webp",
        param="gallery_CH10_S02",
        unlocked_if="gallery_scene_unlocked('CH10_S02')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),
    ## Tuesday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian looks up Jess online"),
        img="v10_jess0.webp",
        param="gallery_CH10_S01",
        unlocked_if="gallery_scene_unlocked('CH10_S01')",
        chars=['Jessica'],
        scope=merge_two_dicts(cheatScope, {
            'v10_text_jess': 3
        })
    ),
    ## Wednesday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian meets Minerva after work"),
        img="v10_minerva2.webp",
        param="gallery_CH10_S21",
        unlocked_if="gallery_scene_unlocked('CH10_S21')",
        chars=['Ian', 'Minerva'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'v8_minerva_sex': True
        })
    ),
    ## Thursday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian wrestles with Ivy"),
        img="v10_ivy_gym2.webp",
        param="gallery_CH10_S05",
        unlocked_if="gallery_scene_unlocked('CH10_S05')",
        chars=['Ian', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {'jiujitsu': 4})
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Emma ambushes Ian in the restroom"),
        img="v10_emma1.webp",
        param="gallery_CH10_S06",
        unlocked_if="gallery_scene_unlocked('CH10_S06')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'ian_lena_dating': True,
            'emma_jeremy': True,
            'v9_emma_sext': 2,
            'emma_satisfaction': 1
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian goes with Lena after the concert"),
        img="v10_ian7.webp",
        param="gallery_CH10_S20",
        unlocked_if="gallery_scene_unlocked('CH10_S20')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'cafe_help': True,
            'stalkfap': True,
            'ian_stalkfap': 2,
            'ian_lena_couple': True,
            'ian_lena_sex': True,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),
    ## Friday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Cindy and Ian have an overdue talk"),
        img="v10_cindy9.webp",
        param="gallery_CH10_S03",
        unlocked_if="gallery_scene_unlocked('CH10_S03')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts(cheatScope, {
            'v10_text_cindy': True,
            'cindy_satisfaction': 3,
            'v9cindycunnilingus': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Cindy promises to meet again soon"),
        img=["blackbg1.webp", "v10_selfie_cindy2.webp"],
        param=["v10_selfie_cindy2"],
        unlocked_if="renpy.seen_image('v10_selfie_cindy2')",
        chars=['Cindy']
    ),
    ## Saturday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian has a threesome with Alison and Jeremy"),
        img="v10_alison1.webp",
        param="gallery_CH10_S07",
        unlocked_if="gallery_scene_unlocked('CH10_S07')",
        chars=['Ian', 'Alison', 'Jeremy'],
        scope=merge_two_dicts(cheatScope, {
            'alison_jeremy_3some': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian goes over for lunch to Alison's"),
        img="v10_alisonian4.webp",
        param="gallery_CH10_S17",
        unlocked_if="gallery_scene_unlocked('CH10_S17')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope, {
            'ian_alison_love': True,
            'v9_alison_trip': True,
            'v10ianshoppedwine': True,
            'v10_wine': True
        })
    ),

    # Lena
    ## Thursday
    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Mike teases Lena during the concert"),
        img=["blackbg1.webp", "v10_selfie_mike.webp"],
        param=["v10_selfie_mike"],
        unlocked_if="renpy.seen_image('v10_selfie_mike')",
        chars=['Mike']
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena invites Mike after the concert"),
        img="v10_mike5.webp",
        param="gallery_CH10_S18",
        unlocked_if="gallery_scene_unlocked('CH10_S18')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v10_lena_sex': 0,
            'lena_mike_love': True,
            'v9_axel_sex': True
        })
    ),

    GalleryScene( # Thursday / Friday
        kind="scene",
        chapter=10,
        name=_("Lena gives Louise some much needed attention"),
        img=["v10_louise2.webp", "v10_louise2_collar.webp"],
        param="gallery_CH10_S12",
        unlocked_if="gallery_scene_unlocked('CH10_S12')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v5_louise_orgasm': True,
            'v6_louise_orgasm': True,
            'v8_louise_sex': True
        })
    ),
    ## Saturday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena thinks about Axel"),
        img="v10_axel1.webp",
        param="gallery_CH10_S15",
        unlocked_if="gallery_scene_unlocked('CH10_S15')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v10_axel_text': 1,
            'v9_axel_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Holly has her first shoot"),
        img="v10_holly11.webp",
        param="gallery_CH10_S08",
        unlocked_if="gallery_scene_unlocked('CH10_S08')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_go_holly': 4
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Holly goes with Mark"),
        img=["blackbg1.webp", "v10_holly_mark.webp"],
        param=["v10_holly_mark"],
        unlocked_if="renpy.seen_image('v10_holly_mark')",
        chars=['Holly', 'Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena and her dance partner need to cool off"),
        img="v10_wc3_dress.webp",
        param="gallery_CH10_S09",
        unlocked_if="gallery_scene_unlocked('CH10_S09')",
        chars=['Lena', 'Ian', 'Mark', 'Mike'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v10_lena_drug': True,
            'billy_model': True,
            'billy_trust': 1,
            'lena_mike_dating': True,
            'v10_mark_flirt': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_lust1': True,
            'lena_wardrobe_black_dress': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena goes home with the birthday girl"),
        img="v10_ivy4.webp",
        param="gallery_CH10_S10",
        unlocked_if="gallery_scene_unlocked('CH10_S10')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v10_lena_drug': True,
            'v8_holly_sex': 'lenaivy'
        })
    ),
    ## Sunday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Shoot for Stalkfap"),
        img=["v10_shoot2c.webp", "v10_shoot1_stan.webp"],
        param="gallery_CH10_S13",
        unlocked_if="gallery_scene_unlocked('CH10_S13')",
        chars=['Lena', 'Ian', 'Mike', 'Stan'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_wardrobe_bunny': True,
            'lena_wardrobe_lingerie': True,
            'stalkfap_pro': 2
        })
    ),
    ## Monday
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena finally gets another professional shoot"),
        img="v10_shooting1.webp",
        param="gallery_CH10_S14",
        unlocked_if="gallery_scene_unlocked('CH10_S14')",
        chars=['Lena', "Seymour"],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena has a threesome with Louise and Jeremy"),
        img="v10_jeremy2.webp",
        param="gallery_CH10_S11",
        unlocked_if="gallery_scene_unlocked('CH10_S11')",
        chars=['Lena', 'Jeremy','Louise'],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    ##################################################################################################################
    ## CHAPTER 11 ####################################################################################################
    ##################################################################################################################

    # Prologue
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena uses Louise for pleasure"),
        img="v11_louise1.webp",
        param="gallery_CH11_S01",
        unlocked_if="gallery_scene_unlocked('CH11_S01')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'toy_double': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian invites Lena to dinner"),
        img="v11_ian2.webp",
        param="gallery_CH11_S02",
        unlocked_if="gallery_scene_unlocked('CH11_S02')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v11iandinner': True,
            'cafe_help': True
        })
    ),

    # Ian
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian dreams of Gillian"),
        img="v11_gillian1.webp",
        param="gallery_CH11_S03",
        unlocked_if="gallery_scene_unlocked('CH11_S03')",
        chars=['Gillian'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Cindy invites Ian when Wade is away"),
        img="v11_cindy2.webp",
        param="gallery_CH11_S04",
        unlocked_if="gallery_scene_unlocked('CH11_S04')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_cindy_love': True,
            'v10_cindy_bj': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Holly meet up before Emma's event"),
        img="v11_holly1b.webp",
        param="gallery_CH11_S05",
        unlocked_if="gallery_scene_unlocked('CH11_S05')",
        chars=['Ian', 'Holly'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Alison look at art"),
        img=["v11_gallery1_bg1.webp", "v11_gallery1b.webp"],
        param="gallery_CH11_S06",
        unlocked_if="gallery_scene_unlocked('CH11_S06')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian celebrates Cherry's art exhibition"),
        img="v11_cherry3.webp",
        param="gallery_CH11_S07",
        unlocked_if="gallery_scene_unlocked('CH11_S07')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts(cheatScope, {
            'ian_cherry_love': True,
            'v6_cherry_anal': 2,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Alison invites Ian over after the exhibition"),
        img="v11_alison4.webp",
        param="gallery_CH11_S08",
        unlocked_if="gallery_scene_unlocked('CH11_S08')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts(cheatScope, {
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'alison_satisfaction': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Holly makes Ian feel better"),
        img="v11_holly8.webp",
        param="gallery_CH11_S09",
        unlocked_if="gallery_scene_unlocked('CH11_S09')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'ian_holly_love': True,
            'holly_gym': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Lena watch a movie and chill"),
        img="v11_lena3.webp",
        param="gallery_CH11_S10",
        unlocked_if="gallery_scene_unlocked('CH11_S10')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_lena_dating': True
        })
    ),

    # Lena
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena is bored in her old room"),
        img="v11_solo1.webp",
        param="gallery_CH11_S11",
        unlocked_if="gallery_scene_unlocked('CH11_S11')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_lena_dating': True,
            'lena_mike_dating': True,
            'lena_robert_dating': True,
            'lena_axel_desire': True,
            'lena_seymour_dating': True,
            'v8_jeremy_flirt': True,
            'v8_jeremy_sex': True,
            'lena_jeremy_sex': True,
            'v10_jeremy_3some': True,
            'lena_cheating': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena talks with a subscriber"),
        img="v11_solo5b.webp",
        param="gallery_CH11_S11b",
        unlocked_if="gallery_scene_unlocked('CH11_S11b')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'stalkfap': True,
            'stalkfap_pro': 2,
            'v10_stalkfap': 'ian',
            'toy_badboy': True,
            'lena_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena had some self-care time"),
        img="v11_solo2.webp",
        param="gallery_CH11_S11c",
        unlocked_if="gallery_scene_unlocked('CH11_S11c')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Mike had been dying to see Lena again"),
        img="v11_mike3.webp",
        param="gallery_CH11_S13",
        unlocked_if="gallery_scene_unlocked('CH11_S13')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Robert catches up with Lena"),
        img="v11_robert1.webp",
        param="gallery_CH11_S14",
        unlocked_if="gallery_scene_unlocked('CH11_S14')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts(cheatScope, {'ian_active': False})
    ),

    GalleryScene(
        kind="image",
        chapter=11,
        name=_("Ivy shows how Holly and Mark's date went"),
        img=["blackbg1.webp", "v11_holly_mark1.webp"],
        param=["v11_holly_mark1", "v11_holly_mark2"],
        unlocked_if="renpy.seen_image('v11_holly_mark2')",
        chars=['Holly', 'Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("The girls show what they have learned"),
        img="v11_poledance1.webp",
        param="gallery_CH11_S15",
        unlocked_if="gallery_scene_unlocked('CH11_S15')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True,
            'v11_holly_change': True,
            'lena_holly_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("The girls have fun in the showers"),
        img="v11_shower1b.webp",
        param="gallery_CH11_S16",
        unlocked_if="gallery_scene_unlocked('CH11_S16')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Just two best friends showering together"),
        img="v11_shower2.webp",
        param="gallery_CH11_S16b",
        unlocked_if="gallery_scene_unlocked('CH11_S16b')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True,
            'v10_ivy_sex': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena makes Holly feel special"),
        img="v11_holly20.webp",
        param="gallery_CH11_S17",
        unlocked_if="gallery_scene_unlocked('CH11_S17')",
        chars=['Lena', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_holly_dating': True,
            'ian_holly_dating': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena had a surprise for Ian"),
        img="v11_3some6.webp",
        param="gallery_CH11_S18",
        unlocked_if="gallery_scene_unlocked('CH11_S18')",
        chars=['Lena', 'Louise', 'Ian'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_lena_couple': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena invites Louise to join her and Mike"),
        img="v11_3some5_mike.webp",
        param="gallery_CH11_S19",
        unlocked_if="gallery_scene_unlocked('CH11_S19')",
        chars=['Lena', 'Louise', 'Mike'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_mike_love': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=11,
        name=_("Lena and Stan have their first kiss"),
        img=["blackbg1.webp", "v11_stan.webp"],
        param=["v11_stan"],
        unlocked_if="renpy.seen_image('v11_stan')",
        chars=['Lena', 'Stan']
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena plays with her reflection"),
        img="v11_seymour2.webp",
        param="gallery_CH11_S20",
        unlocked_if="gallery_scene_unlocked('CH11_S20')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_black_dress': True,
            'seymour_necklace': True
        })
    ),
    
    # Epilogue

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena and Emma go shopping"),
        img=["v11_bikini2.webp","v11_bikini2b.webp"],
        param="gallery_CH11_S21",
        unlocked_if="gallery_scene_unlocked('CH11_S21')",
        chars=['Lena', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v11_lena_dress': 4,
            'v11_emma_date': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena flirts with Jeremy"),
        img="v11_bbc1.webp",
        param="gallery_CH11_S22",
        unlocked_if="gallery_scene_unlocked('CH11_S22')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'v11sms2_jeremy': True,
            'lena_jeremy_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Marcel heard rumors"),
        img=["v11_bbc2b_marcel.webp","v11_bbc2b_lust.webp"],
        param="gallery_CH11_S23",
        unlocked_if="gallery_scene_unlocked('CH11_S23')",
        chars=['Lena', 'Marcel'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena and Axel figure things out"),
        img="v11_axel3.webp",
        param="gallery_CH11_S24",
        unlocked_if="gallery_scene_unlocked('CH11_S24')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'axel_disposition': 3,
            'lena_axel_desire': True,
            'lena_axel_dating': True,
            'lena_drugs': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena visits the VIP"),
        img=["v11_jack2a.webp", "v11_jack2b.webp"],
        param="gallery_CH11_S27",
        unlocked_if="gallery_scene_unlocked('CH11_S27')",
        chars=['Lena', 'Jack'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena brings Mark home after bartending"),
        img="v11_mark2.webp",
        param="gallery_CH11_S25",
        unlocked_if="gallery_scene_unlocked('CH11_S25')",
        chars=['Lena', 'Mark'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'stalkfap_pro': True,
            'lena_anal': 2,
            'v10_wc_bj': 'mark'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena goes to Ian's after bartending"),
        img="v11_lenaian1.webp",
        param="gallery_CH11_S26",
        unlocked_if="gallery_scene_unlocked('CH11_S26')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False
        })
    ),

    ##################################################################################################################
    ## CHAPTER 12 ####################################################################################################
    ##################################################################################################################

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cherry wakes Ian"),
        img="v12_cherry4.webp",
        param="gallery_CH12_S01",
        unlocked_if="gallery_scene_unlocked('CH12_S01')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts(cheatScope, {
            'ian_cherry_love': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Cindy is choosing her bikini"),
        img=["blackbg1.webp", "v12_cindy_selfie1.webp"],
        param=["v12_cindy_selfie1", "v12_cindy_selfie2"],
        unlocked_if="renpy.seen_image('v12_cindy_selfie2')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Alison invites Ian to her place"),
        img=["blackbg1.webp", "v12_alison_selfie1.webp"],
        param=["v12_alison_selfie1"],
        unlocked_if="renpy.seen_image('v12_alison_selfie1')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Minerva requires assistance in her office"),
        img="v12_minerva5b.webp",
        param="gallery_CH12_S02",
        unlocked_if="gallery_scene_unlocked('CH12_S02')",
        chars=['Ian', 'Minerva'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cindy struggles with her feelings"),
        img="v12_cindy7b.webp",
        param="gallery_CH12_S03",
        unlocked_if="gallery_scene_unlocked('CH12_S03')",
        chars=['Ian', 'Cindy'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Alison has a stressful day"),
        img="v12_alison3.webp",
        param="gallery_CH12_S04",
        unlocked_if="gallery_scene_unlocked('CH12_S04')",
        chars=['Ian', 'Alison'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian pays for Lena's exclusive content"),
        img=["ianroomnight.webp", "v12_stalkfap6b.webp"],
        param="gallery_CH12_S05",
        unlocked_if="gallery_scene_unlocked('CH12_S05')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'lena_wardrobe_bunny': True,
            'lena_wardrobe_lingerie': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Jess needs a place to crash"),
        img="v12_jess1.webp",
        param="gallery_CH12_S06",
        unlocked_if="gallery_scene_unlocked('CH12_S06')",
        chars=['Ian', 'Jessica'],
        scope=merge_two_dicts(cheatScope, {
            'v10_jess_porn': True
        })
    ),

    ## Lena

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Lena admires her pictures"),
        img=["blackbg1.webp", "v12_bbc_phone1.webp"],
        param=["v12_bbc_phone1"],
        unlocked_if="gallery_scene_unlocked('CH12_I03')",
        chars=['Lena', 'Jeremy']
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Lena admires her pictures"),
        img=["blackbg1.webp", "v12_bbc_phone2.webp"],
        param=["v12_bbc_phone2"],
        unlocked_if="gallery_scene_unlocked('CH12_I04')",
        chars=['Lena', 'Marcel']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ivy shows Holly's slutty side"),
        img=["lenaoldroom.webp", "v12_holly_slut4.webp"],
        param="gallery_CH12_S07",
        unlocked_if="gallery_scene_unlocked('CH12_S07')",
        chars=['Holly', 'Clark', 'Robert'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'holly_gym': True,
            'holly_slut': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena remembers that night at Blazer's"),
        img="v12_solo2.webp",
        param="gallery_CH12_S08",
        unlocked_if="gallery_scene_unlocked('CH12_S08')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Axel meets Lena at the station"),
        img = "v12_axel15b.webp",
        param="gallery_CH12_S09",
        unlocked_if="gallery_scene_unlocked('CH12_S09')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts(cheatScope, {
            'v9_axel_sex': True,
            'ian_active': False
        })
    ),

    ## Ian

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly get settled in their room"),
        img = "v12_holly4c.webp",
        param="gallery_CH12_S10",
        unlocked_if="gallery_scene_unlocked('CH12_S10')",
        chars=['Ian', 'Holly'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian wakes to Emma"),
        img = "v12_emma1.webp",
        param="gallery_CH12_S11",
        unlocked_if="gallery_scene_unlocked('CH12_S11')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'ian_emma_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Holly enjoys the beach"),
        img=["v12_holly_beach1b.webp", "v12_holly_beach1_book.webp"],
        param="gallery_CH12_S12",
        unlocked_if="gallery_scene_unlocked('CH12_S12')",
        chars=['Holly'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian protects Emma against sunburns"),
        img=["v12_emma_beach1.webp", "v12_emma_beach1_ian1a.webp"],
        param="gallery_CH12_S13",
        unlocked_if="gallery_scene_unlocked('CH12_S13')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'v12_emma_dress': 3,
            'emma_bikini': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly try to cool off in the sea"),
        img = "v12_holly_sea2b.webp",
        param="gallery_CH12_S14",
        unlocked_if="gallery_scene_unlocked('CH12_S14')",
        chars=['Ian', 'Holly'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian helps Holly relax in the afternoon"),
        img = "v12_holly6a.webp",
        param="gallery_CH12_S15",
        unlocked_if="gallery_scene_unlocked('CH12_S15')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'ian_holly_love': True,
            'v12_holly_sea_sex': True,
            'v12_holly_sex1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena arrives at the summer house"),
        img = ["v12_lena5a.webp", "v12_lena5a_spit.webp"],
        param="gallery_CH12_S16",
        unlocked_if="gallery_scene_unlocked('CH12_S16')",
        chars=['Ian', 'Lena'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Emma weren't ready for sleep"),
        img = "v12_emma10.webp",
        param="gallery_CH12_S17",
        unlocked_if="gallery_scene_unlocked('CH12_S17')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'ian_emma_sex': True,
            'v12_emma_sex1': True,
            'v12_emma_sunscreen': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly had a talk about Lena"),
        img = "v12_holly14a.webp",
        param="gallery_CH12_S18",
        unlocked_if="gallery_scene_unlocked('CH12_S18')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'v12_holly_sea_sex': True,
            'v12_holly_sex2': True,
            'holly_trinity': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian supports Lena in the evening"),
        img = ["v12_lena13b_choker.webp", "v12_lena13b_squirt3.webp"],
        param="gallery_CH12_S19",
        unlocked_if="gallery_scene_unlocked('CH12_S19')",
        chars=['Ian', 'Lena'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Louise decides to text Ian"),
        img=["summerroom.webp", "v12_louise3.webp"],
        param="gallery_CH12_S20",
        unlocked_if="gallery_scene_unlocked('CH12_S20')",
        chars=['Louise'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ivy rewards Ian for his victory"),
        img=["summerroom.webp", "v12_ivy2.webp"],
        param="gallery_CH12_S21",
        unlocked_if="gallery_scene_unlocked('CH12_S21')",
        chars=['Ivy'],
        scope=cheatScope
    ),

    # 12c

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena needs help with sunscreen"),
        img = "v12_lena_beach2_gall.webp",
        param="gallery_CH12_S22",
        unlocked_if="gallery_scene_unlocked('CH12_S22')",
        chars=['Lena', 'Ian', 'Perry', 'Wade'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Photo shoot at the beach"),
        img = "v12_holly_beach6b_gall.webp",
        param="gallery_CH12_S23",
        unlocked_if="gallery_scene_unlocked('CH12_S23')",
        chars=['Lena', 'Emma', 'Holly', 'Wade'],
        scope=merge_two_dicts(cheatScope, {
            'v12_fireworks': True,
            'v11_emma_pics': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Louise wishes Ian a good morning"),
        img=["blackbg1.webp", "v12_louise5.webp"],
        param=["v12_louise5"],
        unlocked_if="gallery_scene_unlocked('CH12_I24')",
        chars=['Louise']
    ),
    
    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Cindy posts images of her Wildcats shoot"),
        img=["blackbg1.webp", "v12_cindy_pg2.webp"],
        param=["v12_cindy_pg1", "v12_cindy_pg2b_gall"],
        unlocked_if="gallery_scene_unlocked('CH12_I25')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian takes Lena's pictures"),
        img = ["v12_lena_22.webp", "v12_lena_22_cig.webp"],
        param="gallery_CH12_S26",
        unlocked_if="gallery_scene_unlocked('CH12_S26')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'v10_stalkfap': 'ian',
            'lena_bikini': 3,
            'v12_lena_bikini': 3,
            'lena_background': 'lust',
            'lena_fty_3some': 1,
            'ian_lena_3some': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cindy replies to Ian's messages"),
        img = ["summerroomnight.webp", "v12_cindy_selfie2a.webp"],
        param="gallery_CH12_S27",
        unlocked_if="gallery_scene_unlocked('CH12_S27')",
        chars=['Cindy'],
        scope=merge_two_dicts(cheatScope, {
            'ian_fit': True,
            'cindy_ass': True,
            'cindy_satisfaction': 4,
            'v12_cindy_cum': 1,
            'ian_cindy_love': True,
            'v12_cindy_rel': 1,
            'v12_gift': 'cindy'
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Ian touches Minerva's heart"),
        img=["blackbg1.webp", "v12_minerva_selfie.webp"],
        param=["v12_minerva_selfie"],
        unlocked_if="gallery_scene_unlocked('CH12_I28')",
        chars=['Minerva']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Emma have to be quick"),
        img = "v12_emma18.webp",
        param="gallery_CH12_S29",
        unlocked_if="gallery_scene_unlocked('CH12_S29')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts(cheatScope, {
            'lena_background': 'wits',
            'v12_emma_sex2': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Lena make love under the stars"),
        img = "v12_lena25.webp",
        param="gallery_CH12_S30",
        unlocked_if="gallery_scene_unlocked('CH12_S30')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'v11_lena_squirt': True,
            'v12_lena_squirt': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Lena had a heart to heart"),
        img = "v12_lena23.webp",
        param="gallery_CH12_S31",
        unlocked_if="gallery_scene_unlocked('CH12_S31')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_lena_couple': True,
            'ian_chad': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Perry finally scores"),
        img = "v12_perry.webp",
        param="gallery_CH12_S32",
        unlocked_if="gallery_scene_unlocked('CH12_S32')",
        chars=['Emma', 'Perry'],
        scope=cheatScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Farewell sex"),
        img = "v12_lena24.webp",
        param="gallery_CH12_S33",
        unlocked_if="gallery_scene_unlocked('CH12_S33')",
        chars=['Ian', 'Lena'],
        scope=cheatScope
    ),

    #GalleryScene(
    #    kind="scene",
    #    chapter=12,
    #    name=_("Ian gifts Holly the necklace"),
    #    # img = ".webp",
    #    img = "wipbg.webp",
    #    # param="gallery_CH12_S34",
    #    unlocked_if="gallery_scene_unlocked('CH12_S34')",
    #    chars=['Ian', 'Holly'],
    #    scope=merge_two_dicts(cheatScope, {
    #        'ian_holly_love': True,
    #        'v12_gift': 'holly'
    #    })
    #),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena discusses a MFM threesome with Ian"),
        img = "v12_lena37b.webp",
        param="gallery_CH12_S35",
        unlocked_if="gallery_scene_unlocked('CH12_S35')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'lena_fty_bbc': True,
            'lena_mike_dating': True,
            'v11_mark_sex': True,
            'lena_robert_dating': True,
            'ian_lena_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian punishes Lena"),
        img = "v12_lena30_gall.webp",
        param="gallery_CH12_S36",
        unlocked_if="gallery_scene_unlocked('CH12_S36')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_chad': 5,
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("The Holly trinity"),
        img = "v12_trinity6.webp",
        param="gallery_CH12_S37",
        unlocked_if="gallery_scene_unlocked('CH12_S37')",
        chars=['Ian', 'Holly', 'Lena'],
        scope=merge_two_dicts(cheatScope, {
            'v12_never_ever': True,
            'holly_trinity': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Holly makes her move on Ian"),
        img = "v12_holly24a.webp",
        param="gallery_CH12_S38",
        unlocked_if="gallery_scene_unlocked('CH12_S38')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts(cheatScope, {
            'holly_slut': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Axel adds Cindy to his project"),
        img=["blackbg1.webp", "v12_axelpg2.webp"],
        param=["v12_axelpg1", "v12_axelpg2"],
        unlocked_if="gallery_scene_unlocked('CH12_I39')",
        chars=['Cindy']
    ),

    ##################################################################################################################
    ## CHAPTER 13 ####################################################################################################
    ##################################################################################################################

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Seymour joins Lena in front of the camera"),
        # img = ".webp",
        img = "wipbg.webp",
        # param="gallery_CH13_S01",
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH13_S01')",
        chars=['Lena', "Seymour"],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'lena_travel': 'italy',
            'lena_posh': 4,
            'seymour_desire': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena discovers Seymours gift"),
        # img = ".webp",
        img = "wipbg.webp",
        # param="gallery_CH13_S02",
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH13_S02')",
        chars=['Lena'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'ian_lena_couple': True,
            'ian_lena_pure': True,
            'seymour_desire': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena gives herself completely to Seymour"),
        # img = ".webp",
        img = "wipbg.webp",
        # param="gallery_CH13_S03",
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH13_S03')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts(cheatScope, {
            'ian_active': False,
            'seymour_desire': True
        })
    ),

    ##################################################################################################################
    ## CHAPTER 14 ####################################################################################################
    ##################################################################################################################
    
    ## BASIC SCENE TEMPLATE ########################################################
    # GalleryScene(
    #     kind="scene",
    #     chapter=13,
    #     name=_(""),
    #     # img = ".webp",
    #     img = "wipbg.webp",
    #     # param="gallery_CH13_S01",
    #     param= "gallery_WIP",
    #     unlocked_if="gallery_scene_unlocked('CH13_S01')",
    #     chars=[''],
    #     scope=cheatScope
    # ),

    ## BASIC IMAGE TEMPLATE ########################################################
    # GalleryScene(
    #     kind="image",
    #     chapter=13,
    #     name=_(""),
    #     # img=["blackbg1.webp", ""],
    #     img = "wipbg.webp",
    #     # param=[""],
    #     param=["wipbg"],
    #     unlocked_if="renpy.seen_image('')",
    #     chars=['']
    # ),
]