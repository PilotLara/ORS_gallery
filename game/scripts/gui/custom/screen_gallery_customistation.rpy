screen screen_gallery_customisation():
    tag menu

    use game_menu(_("Customise"), gallery_nav_custom=True):
        vbox:
            spacing 50
            yalign 0.5

            hbox:
                xalign 0.5
                spacing 50

                if persistent.gall_lena_tattoo1:
                    imagebutton idle "gui/gall_tattoo1_owned.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo1", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                else:
                    imagebutton idle "gui/gall_tattoo1.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo1", True) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                if persistent.gall_lena_tattoo2:
                    imagebutton idle "gui/gall_tattoo2_owned.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo2", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                else:
                    imagebutton idle "gui/gall_tattoo2.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo2", True) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                if persistent.gall_lena_tattoo3:
                    imagebutton idle "gui/gall_tattoo3_owned.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo3", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                else:
                    imagebutton idle "gui/gall_tattoo3.webp" focus_mask True action SetVariable("persistent.gall_lena_tattoo3", True) , [ Play ("ch_one", "sfx/paper_click.mp3") ]

            hbox:
                xalign 0.5
                spacing 50

                if persistent.gall_lena_piercing1:
                    imagebutton idle "gui/gall_piercing1_owned.webp" focus_mask True action SetVariable("persistent.gall_lena_piercing1", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                else:
                    imagebutton idle "gui/gall_piercing1.webp" focus_mask True action SetVariable("persistent.gall_lena_piercing1", True) , SetVariable("persistent.gall_lena_piercing2", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]

                if persistent.gall_lena_piercing2:
                    imagebutton idle "gui/gall_piercing2_owned.webp" focus_mask True action SetVariable("persistent.gall_lena_piercing2", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]
                else:
                    imagebutton idle "gui/gall_piercing2.webp" focus_mask True action SetVariable("persistent.gall_lena_piercing2", True) , SetVariable("persistent.gall_lena_piercing1", False) , [ Play ("ch_one", "sfx/paper_click.mp3") ]

            hbox:
                text "WIP: game needs to restart before these changes are reflected in the gallery"