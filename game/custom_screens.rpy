style centered_style:
    xalign .5
    yalign .5

screen cite_name_input():
    modal True
    fixed:
        xsize 1920 ysize 1080
        add "gui/web_search_shine.png" align (.5,.5)
        #background "#242424"
        input:
            style "centered_style"
            default ""
            text_align .5
            size 60
            min_width 1000
            pixel_width 1000
            default_focus True

screen popup_notification_www(posargs):
    fixed:
        xmaximum 535
        ymaximum 225
        add "gui/notification popup.png"
        xalign posargs[0]
        yalign posargs[1]
        text "www." yalign 0.5 xalign 0.5 size 65

screen popup_notification_dreambo(posargs):
    fixed:
        xmaximum 535
        ymaximum 225
        add "gui/notification popup.png"
        xalign posargs[0]
        yalign posargs[1]
        text "dreambo" yalign 0.5 xalign 0.5 size 65

screen popup_notification_ok(posargs):
    fixed:
        xmaximum 535
        ymaximum 225
        add "gui/notification popup.png"
        xalign posargs[0]
        yalign posargs[1]
        text ".ok" yalign 0.5 xalign 0.5 size 65