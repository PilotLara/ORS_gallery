############################################################################################################################################################################
## SCENE REPLAY GALLERY ####################################################################################################################################################
############################################################################################################################################################################

init offset = -2

define gallery_characters = [None, 'Lena', 'Ian', 'Alison', 'Axel', 'Billy', 'Cherry', 'Cindy', 'Emma', 'Gillian', 'Holly', 'Ivy', 'Jeremy', 'Jessica', 'Louise', 'Marcel', 'Mark', 'Mike', 'Minerva', 'Robert', 'Seymour', 'Stan']

init python:
    def merge_two_dicts(x, y):
        z = x.copy()   # start with keys and values of x
        z.update(y)    # modifies z with keys and values of y
        return z

    def merge_three_dicts(w, x, y):
        z = w.copy()
        z.update(x)
        z.update(y)
        return z

    def get_scenes_for_char(char, chapter=0):
        global gallery_scenes

        scenes = []
        for item in gallery_scenes:
            if item.is_for_char(char, chapter):
                scenes.append(item)

        return scenes

define cheatScope = {
    # IAN
    'ian_active': True,
    # IAN STATS
    'ian_wits': 99,
    'ian_charisma': 99,
    'ian_athletics': 99,
    'ian_lust': 99,
    'ian_will': 2,
    'ian_money': 50,
    # IAN RELATIONSHIPS
    'ian_perry': 12,
    'ian_lena': 12,
    'ian_cindy': 12,
    'ian_wade': 12,
    'ian_alison': 12,
    'ian_holly': 12,
    'ian_jeremy': 12,
    'ian_emma': 12,
    'ian_louise': 12,
    'ian_ivy': 12,
    'ian_axel': 12,
    'ian_seymour': 12,
    'ian_stan': 12,
    'ian_default': 12,
    'ian_minerva': 12,
    'ian_wen': 12,
    'ian_robert': 12,
    'ian_mark': 12,
    'ian_cherry': 12,
    'ian_lola': 12,
    'ian_dad': 12,
    'ian_gillian': 12,
    'ian_yuri': 12,
    'ian_mike': 12,
    'ian_jess': 12,
    'ian_nat': 12,
    'ian_clark': 12,
    # LENA
    # LENA STATS
    'lena_wits': 99,
    'lena_charisma': 99,
    'lena_athletics': 99,
    'lena_lust': 99,
    'lena_will': 2,
    'lena_money': 50,
    # LENA RELATIONSHIPS
    'lena_perry': 12,
    'lena_cindy': 12,
    'lena_wade': 12,
    'lena_alison': 12,
    'lena_holly': 12,
    'lena_jeremy': 12,
    'lena_emma': 12,
    'lena_louise': 12,
    'lena_ivy': 12,
    'lena_axel': 12,
    'lena_seymour': 12,
    'lena_stan': 12,
    'lena_default': 12,
    'lena_ed': 12,
    'lena_molly': 12,
    'lena_robert': 12,
    'lena_mark': 12,
    'lena_danny': 12,
    'lena_lenamom': 12,
    'lena_lenadad': 12,
    'lena_cherry': 12,
    'lena_producer': 12,
    'lena_lola': 12,
    'lena_gillian': 12,
    'lena_mike': 12,
    'lena_agnes': 12,
    'lena_jess': 12,
    # LENA BODY MODS // EDIT HERE
    'lena_piercing1': False,    # Barbell piercing
    'lena_piercing2': False,    # Bowknot piercing
    'lena_tattoo1': False,      # Small Hip Tattoo
    'lena_tattoo2': False,      # Medium Shoulder Tattoo
    'lena_tattoo3': False       # Big Thigh Tattoo
}

define lenaCleanBodyScope = { # DO NOT EDIT // USED TO PROTECT IMG CONTINUITY IN CHAPTERS BEFORE LENA GOT PIERCINGS/TATTOO
    'lena_piercing1': False,
    'lena_piercing2': False,
    'lena_tattoo1': False,
    'lena_tattoo2': False,
    'lena_tattoo3': False
}

define lenaNoTattooScope = { # DO NOT EDIT // USED TO PROTECT IMG CONTINUITY IN CHAPTERS BEFORE LENA GOT A TATTOO
    'lena_tattoo1': False,
    'lena_tattoo2': False,
    'lena_tattoo3': False
}

default gall_lena_look = 1
default gall_flena = "n"

############################################################################################################################################################################
## PHONE IMAGE GALLERY #####################################################################################################################################################
############################################################################################################################################################################
# The lists where the pictures for Ian's and Lena's phone galleries are stored. Default state is empty.

## IAN #########################################################

default ian_alison_pics = []
default ian_axel_pics = []
default ian_cherry_pics = []
default ian_cindy_pics = []
default ian_emma_pics = []
default ian_gillian_pics = []
default ian_holly_pics = []
default ian_ian_pics = []
default ian_ivy_pics = []
default ian_jeremy_pics = []
default ian_lena_pics = []
default ian_louise_pics = []
default ian_mike_pics = []
default ian_misc_pics = []
default ian_minerva_pics = []
default ian_perry_pics = []
default ian_robert_pics = []
default ian_seymour_pics = []
default ian_stan_pics = []
default ian_wade_pics = []

## LENA ########################################################

default lena_alison_pics = []
default lena_axel_pics = []
default lena_cindy_pics = []
default lena_emma_pics = []
default lena_holly_pics = []
default lena_ian_pics = []
default lena_ivy_pics = []
default lena_jeremy_pics = []
default lena_lena_pics = []
default lena_louise_pics = []
default lena_mike_pics = []
default lena_misc_pics = []
default lena_minerva_pics = []
default lena_perry_pics = []
default lena_robert_pics = []
default lena_seymour_pics = []
default lena_stan_pics = []
default lena_wade_pics = []