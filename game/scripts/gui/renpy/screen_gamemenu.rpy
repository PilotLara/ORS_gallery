## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

init offset = -1

screen game_menu(title, scroll=None, yinitial=0.0, cols=1, vpgrid_xspacing=50, vpgrid_yspacing=20, left_margin=120, gallery_nav=False, gallery_nav_custom=False, gallery_char=None, gallery_page=1, gallery_char_page=1, gallery_chapter=0):
    style_prefix "game_menu"

    #if main_menu:
    #    add gui.main_menu_background
    #else:
    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
                label title xalign 0.5 yoffset -60

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        
                        xalign 0.5

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    left_margin 0
                    vbox style "empty":
                        vpgrid:
                            cols cols
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            left_margin left_margin
                            right_margin 59
                            xspacing vpgrid_xspacing
                            yspacing vpgrid_yspacing

                            xfill True
                            
                            transclude

                else:
                    transclude

    if gallery_nav:
        use navigation_gallery(page=gallery_page, selected_char=gallery_char, char_page=gallery_char_page, chapter=gallery_chapter)
    elif gallery_nav_custom:
        use navigation_gallery_customisation()
    else:
        use navigation

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")



style game_menu_outer_frame is empty:
    bottom_padding 66
    top_padding 68

style game_menu_navigation_frame is empty:
    xsize 364
    yfill True

style game_menu_content_frame is empty:
    xfill True
    xmargin 50

style game_menu_viewport is gui_viewport:
    xsize 1380

style game_menu_scrollbar is gui_vscrollbar
style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side is gui_side:
    spacing 15

style game_menu_label is gui_label:
    xpos 75
    ysize 180

style game_menu_label_text is gui_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style return_button_text is navigation_button_text