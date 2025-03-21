## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init offset = -1

screen navigation():
    style_prefix "navigation"

    frame:
        vbox:
            imagebutton:
                xalign 0.5
                auto "gui/main_patreon_%s.webp"
                hovered Play ("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), OpenURL ("https://www.patreon.com/Evakiss")

            if _in_replay:
                imagebutton:
                    auto "gui/gm_endreplay_%s.webp"
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action Play("ch_three", "sfx/paper_click.mp3"), EndReplay(confirm=False)
            else:
                imagebutton:
                    auto "gui/gm_load_%s.webp"
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("load")
            
            imagebutton:
                auto "gui/gm_settings_%s.webp"
                hovered Play("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("preferences")
            
            imagebutton:
                auto "gui/gm_gallery_%s.webp"
                hovered Play("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("screen_gallery")

            imagebutton:
                auto "gui/gm_credits_%s.webp"
                hovered Play("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("about")

            if renpy.variant("pc"):
                ## Help isn't necessary or relevant to mobile devices.
                imagebutton:
                    auto "gui/gm_controls_%s.webp"
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("help")

            fixed:
                xysize (258, 95)
                if _in_replay:
                    imagebutton:
                        auto "gui/gm_mainmenu_%s.webp"
                        hovered Play("ch_one", "sfx/paper_hover.mp3")
                        action Play("ch_three", "sfx/paper_click.mp3"), MainMenu(confirm=False)
                elif not main_menu:
                    imagebutton:
                        auto "gui/gm_mainmenu_%s.webp"
                        hovered Play("ch_one", "sfx/paper_hover.mp3")
                        action Play("ch_three", "sfx/paper_click.mp3"), MainMenu()
                else:
                    imagebutton:
                        auto "gui/gm_mainmenu_%s.webp"
                        hovered Play("ch_one", "sfx/paper_hover.mp3")
                        action Play("ch_three", "sfx/paper_click.mp3"), Return()
                    
                add "gui/gm_back.webp" yalign 0.5 xpos 36


style navigation_frame is empty:
    xsize 356
    yfill True
    top_margin 130
    bottom_margin 80
    # background "#f005"

style navigation_vbox:
    align (0.5, 1.0)
    spacing 18

style navigation_vbox:
    variant "small"
    spacing 38


# style navigation_button is gui_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

# style navigation_button_text is gui_button_text:
#     properties gui.button_text_properties("navigation_button")


define navigation_gallery_rows = 4
define navigation_gallery_pages = len(gallery_characters) // navigation_gallery_rows + 1

screen navigation_gallery(selected_char=None, char_page=1, chapter=0, page=1):
    style_prefix "navigation"

    default char = selected_char

    frame:
        # background "#f003"
        xsize 369
        top_margin 270
        vbox:
            yalign 0.0
            yoffset -130
            text _("Chapter") style "about_text" size gui.label_text_size xalign 0.5
            hbox:
                xalign 0.5
                spacing 6
                textbutton "<<":
                    top_padding 0
                    top_margin 0
                    text_selected_color gui.idle_color
                    text_selected_hover_color gui.hover_color
                    if chapter > 1:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=1, _page=1)
                    elif chapter == 1:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=0, _page=1)
                
                textbutton "<":
                    top_padding 0
                    top_margin 0
                    text_selected_color gui.idle_color
                    text_selected_hover_color gui.hover_color
                    if chapter > 0:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=chapter - 1, _page=1)

                if chapter == 0:
                    textbutton _("All") style "navigation_gallery_chapter_button" text_color gui.idle_color action NullAction()
                else:
                    textbutton str(chapter) style "navigation_gallery_chapter_button" text_selected_color gui.idle_color text_selected_hover_color gui.hover_color action ShowMenu('screen_gallery', char=selected_char, chapter=0, _page=1)

                textbutton ">":
                    top_padding 0
                    text_selected_color gui.idle_color
                    text_selected_hover_color gui.hover_color
                    if chapter < chapters:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=(chapter + 1), _page=1)

                textbutton ">>":
                    top_padding 0
                    text_selected_color gui.idle_color
                    text_selected_hover_color gui.hover_color
                    if chapter < chapters:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=chapters, _page=1)
                    elif chapter == chapters:
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page, chapter=0, _page=1)

        vbox:
            yalign 0.0

            $nav_slots = 0
            for i in range((char_page-1) * navigation_gallery_rows, min(char_page * navigation_gallery_rows, len(gallery_characters))):
                $name = gallery_characters[i]
                $nav_slots += 1
                fixed:
                    xysize (250, 104)
                    imagebutton:
                        idle "gui/gm_button_gallery_idle.webp"
                        hover "gui/gm_button_gallery_hover.webp"
                        selected_idle "gui/gm_button_gallery_hover.webp"
                        hovered Play("ch_one", "sfx/paper_hover.mp3")
                        action SelectedIf(SetScreenVariable('char', name)), Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("screen_gallery", char=name, char_page=char_page, chapter=chapter, _page=1)
                    
                    hbox style "navigation_gallery_char_hbox":
                        if name is None:
                            add "gui/icon_gallery_all.webp"
                            text _('All') style "navigation_gallery_text"
                        else:
                            add "gui/icon_gallery_%s.webp" % name.lower()
                            text name style "navigation_gallery_text"

            for i in range(navigation_gallery_rows - nav_slots):
                fixed:
                    xysize (250, 104)
                    imagebutton idle "gui/gm_button_gallery_idle.webp"

            hbox:
                xalign 0.5
                style_prefix "page"
                spacing 2

                textbutton "<<":
                    if char_page > 1:
                        text_selected_color gui.idle_color
                        text_selected_hover_color gui.hover_color
                        action ShowMenu('screen_gallery', char=selected_char, char_page=1, chapter=chapter, _page=page)

                textbutton "<":
                    if char_page > 1:
                        text_selected_color gui.idle_color
                        text_selected_hover_color gui.hover_color
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page - 1, chapter=chapter, _page=page)

                textbutton ">":
                    if char_page < navigation_gallery_pages:
                        text_selected_color gui.idle_color
                        text_selected_hover_color gui.hover_color
                        action ShowMenu('screen_gallery', char=selected_char, char_page=char_page + 1, chapter=chapter, _page=page)

                textbutton ">>":
                    if char_page < navigation_gallery_pages:
                        text_selected_color gui.idle_color
                        text_selected_hover_color gui.hover_color
                        action ShowMenu('screen_gallery', char=selected_char, char_page=navigation_gallery_pages, chapter=chapter, _page=page)

            hbox:
                xysize (258, 95)
                xalign 0.5
                imagebutton:
                    auto "gui/gm_controls_%s.webp" #ToDO Placeholder
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu('screen_gallery_customisation')

            fixed:
                xysize (258, 95)
                xalign 0.5
                imagebutton:
                    auto "gui/gm_mainmenu_%s.webp"
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action Play("ch_three", "sfx/paper_click.mp3"), Return()
                add "gui/gm_back.webp" yalign 0.5 xpos 36

style navigation_gallery_text is gui_label_text:
    yalign 0.5
    color "#111"

style navigation_gallery_text is gui_label_text:
    yalign 0.5
    color "#111"

style navigation_gallery_char_hbox is navigation_hbox:
    yalign 0.5
    yoffset 2
    spacing 15

style navigation_gallery_chapter_button is button:
    xsize 40
    top_padding 0

style navigation_gallery_chapter_button_text is gui_label_text:
    xalign 0.5

screen navigation_gallery_customisation():
    style_prefix "navigation"

    frame:
        xsize 369
        vbox:
            imagebutton:
                xalign 1.0
                offset (-30, -450)
                idle "gui/support_lara.png"
                hovered Play ("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), OpenURL ("https://subscribestar.adult/pilotlara")

            fixed:
                xysize (258, 95)
                xalign 0.5
                imagebutton:
                    auto "gui/gm_gallery_%s.webp"
                    hovered Play("ch_one", "sfx/paper_hover.mp3")
                    action [Play("ch_three", "sfx/paper_click.mp3"), Function(update_all_gallery_images), ShowMenu("screen_gallery")]
                add "gui/gm_back.webp" yalign 0.5 xpos 36