# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define protag = Character("Максим", color="#c976f0")
define old_web_guy = Character("Разработчик из прошлого", color="#ad6941")
define present_web_guy = Character("Высший разум", color="#5a9deb")
define future_web_guy = Character("Разработчик из будущего", color="#ff394a")
define phone = Character("Лёша", color="#a0eb5a")

# Переменные для отслеживания где был игрок
define been_old = False
define been_present = False
define been_future = False

# Музыка
define audio.m_real_world = "music/On-My-Way-Lofi-Study-Music.mp3"
define audio.m_old_city = "music/City-Life.mp3"
define audio.m_pres_city = "music/Way-Home.mp3"
define audio.m_future_city = "music/Ghostrifter-Official-Vigilance.mp3"

# Звуки

define audio.notif = "sounds/notification.mp3"
define audio.steps = "sounds/steps.mp3"
define audio.ring = "sounds/ring.mp3"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg real_world with dissolve

    protag "Фух, эта подработка так уматывает."

    protag "Сколько я уже без настоящего места работы? Ай, не важно, главное закончить мой новый дизайн сайта."

    protag "Я хочу творить и создавать, а не заниматься ерундой. Осталось только отправить мое портфолио сайтов в компанию и тогда заживём!"

    protag "Правда, это уже третья попытка. Но ничего, я исправил свои ошибки и буду стараться дальше."

    protag "Письмо отправлено, надеюсь на этот раз они его рассмотрят."

    protag "*Зевок* {w}Как же спать хочется…"
    
    stop music fadeout 1

    scene bg black with Dissolve(3.0)

    pause 3.0

    scene bg hub with Dissolve(3.0)
    
    play music m_pres_city

    protag "Так, стоп...{w=0.5} Что происходит?{w}{cps=*2} Я во сне?!{/cps}{w=1} {cps=*0.5}Как будто я оказался в интернете...{/cps}"

    protag "Не так я себе представлял осознанный сон. {w=0.5} Мне нужно проснуться."

    pause 1.5

    with hpunch

    pause 1.5

    protag "{cps=*0.1}...{/cps}"

    pause 1.5

    with hpunch

    pause 1.5

    protag "{cps=*0.5}Хм...{/cps} Не получается. Придется ждать пока я проснусь или найти другой способ разбудить себя." 

    menu hub_fork_1:
        "Ну а пока можно осмотреть здешние места."

        "Пойти в сторону старых зданий":
            call old_web from _call_old_web
        
        "Пойти в сторону обычных зданий":
            call present_web from _call_present_web

        "Пойти в сторону небоскребов":
            call future_web from _call_future_web
    
    stop music fadeout 1

    scene bg hub with Fade(0.5, 1, 0.5)

    play music m_pres_city

    protag "Хм... эта развилка выглядит знакомо."

    menu hub_fork_2:
        "Делать все равно нечего, пойду в другую сторону."

        "Пойти в сторону старых зданий" if not been_old:
            call old_web from _call_old_web_1
        
        "Пойти в сторону обычных зданий" if not been_present:
            call present_web from _call_present_web_1

        "Пойти в сторону небоскребов" if not been_future:
            call future_web from _call_future_web_1
    
    stop music fadeout 1

    scene bg hub with Fade(0.5, 1, 0.5)

    play music m_pres_city

    protag "Ну, осталось всего одно место, где я не был."

    python:
        if not been_old:
            renpy.call("old_web")
        elif not been_present:
            renpy.call("present_web")
        else:
            renpy.call("future_web")

    protag "А! Так это название сайта! Если сложить все надписи вместе и ввести это в строку в самом начале?"

    stop music fadeout 1

    scene bg hub with Fade(0.5, 1, 0.5)

    play music m_pres_city

    protag ""

    protag "Так, была не была."

    scene bg black with Fade(0.5, 0.2, 0.5)

    python:
        renpy.show_screen("popup_notification_www", posargs=[0.15,0.15])
        renpy.show_screen("popup_notification_dreambo", posargs=[0.80,0.23])
        renpy.show_screen("popup_notification_ok", posargs=[0.50,0.70])
        while True:
            if renpy.call_screen("cite_name_input") == "www.dreambo.ok":
                break
            renpy.say(protag,"Хмм, что-то не так.", interact=True)
        renpy.hide_screen("popup_notification_www")
        renpy.hide_screen("popup_notification_dreambo")
        renpy.hide_screen("popup_notification_ok")

    "Система" "Введите запрос."

    protag "О! Получилось!"

    protag "Так. *Кхм* Как мне проснуться?"

    "Система" "По вашему запросу найден 1 ответ. Нажмите на ссылку."

    protag "Была не была."

    stop music

    scene bg black with Fade(0.5, 0.2, 0.5)

    pause 0.5

    scene bg real_world with dissolve

    play music m_real_world

    protag "Неужели? Я проснулся! Это была тяжелая ночь, как будто и не спал."

    protag "Однако… Никогда не думал, что мой мозг покажет мне настолько поучительный сон."
    
    protag "Мне это даже понравилось."

    play sound ring loop
    "*Звонок телефона*"
    stop sound

    phone "Алло?"

    protag "Да, Лёша, чего?"

    phone "Я тебе что звоню, помнишь ты говорил, что тебе нужна работа?"

    protag "Да, было такое."

    phone "Так вот, у меня есть парочка предложений. Грузчик или кассир, что думаешь?"

    protag "Лёш, погоди сек."

    "Здравствуйте, вы приняты на работу ... "

    protag "Не, Лёш, хватит с этими  подработками. Кажется я наконец нашел то, чем хотел бы заниматься..."

    pause 0.5

    window hide

    show bg black with dissolve

    centered "{size=80}The end{/size}"

    pause 1.5

    return

label old_web:

    stop music fadeout 1

    play sound steps

    scene bg old_city with Fade(0.5, 1, 0.5)

    play music m_old_city

    protag "Ну и вид… Зачем столько непонятных ссылок? Может нажать на одну?"

    protag "*Тык* Э-э-э... Нет. Не работает."

    protag "М? Там кто-то есть. Хэй!"

    protag "Извините! Простите! Ауу!"

    show old_web_char standing

    old_web_guy "Чего кричишь?"

    protag "Пытался привлечь ваше внимание!"

    old_web_guy "Ну и что тебе нужно от меня?"

    protag "Не подскажете где это я?"

    old_web_guy "В моем детстве."

    protag "Э? Что?"

    old_web_guy "Посмотри вокруг. Какой грубый дизайн сайта, невозможность что-либо понять. Но именно в этом своя прелесть."

    old_web_guy "Маленький я сидел днями и ночами в интернете, конечно, интерфейс оставлял желать лучшего.  Не у многих людей был доступ к интернету. Да и технологии были не так развиты, но мне и этого хватало, чтобы каждый день туда возвращаться."

    old_web_guy "Я думаю тебе следует поспрашивать в других местах, там твозможно смогут дать ответ на свой твой вопрос."

    old_web_guy "Держи. Скажешь, что ты от меня."

    protag "А? Сообщение?"

    hide old_web_char

    play sound notif

    "{size=60}\"www.\"{/size}"

    protag "Что это значит? И... куда он делся?"

    $ been_old = True

    return

label present_web:

    stop music fadeout 1

    play sound steps

    scene bg present_city with Fade(0.5, 1, 0.5)

    play music m_pres_city

    protag "Кажется, тут какой-то форум. Может я смогу узнать как мне проснуться?"

    protag "Извините! Могу ли я задать вам вопрос?"

    show present_web_char standing

    present_web_guy "Конечно можно! Спрашивайте!"

    protag "Я бы хотел узнать как мне проснуться."

    present_web_guy "Но вы же сейчас разговариваете со мной в данный момент, как вы можете спать? Вы лунатик?"

    protag "Да вроде нет. Я думаю, что вы часть моего сна."

    present_web_guy "Это исключено. Я не могу быть просто плодом чьей-то фантазии!"

    present_web_guy "Но всё же. Что вы делали перед тем, как попасть в, как вы говорите, \"сон\"?"

    protag "Я сидел у своего компьютера и …"

    protag "Кажется, я делал дизайн сайта. Если честно я не помню подробностей."

    present_web_guy "Я - Высший разум, я ответил на более 40 тысяч различных вопросов пользователей, но …"

    present_web_guy "Я не знаю, что вам делать."

    protag "М-да, спасибо за помощь."

    protag "Здесь такой странный интерфейс, Вам нравится находится на таком сайте?"

    present_web_guy "Не совсем, но что мне остаётся делать? Конечно, в последнее время появились более приятные глазу сайты, но я достиг здесь таких высот и не хочу оставлять их."
    
    protag "Тогда, может быть его можно улучшить?"

    present_web_guy "Может и можно, я был бы благодарен вам за это. Но разве вы по этой причине пришли сюда? Вас даже не волнует то, что вы совершенно не знаете где вы?"

    protag "Это странно, но я и сам не знаю почему. Появляется ощущение, что я найду ответ когда придёт время. Поэтому я пока что просто хожу по разным местам."

    present_web_guy "Ладно, мне нет до этого дела. Но вопросы не ждут, десятки пользователей хотят получить ответ от меня!"

    present_web_guy "Было приятно пообщаться, вы указали на мои пробелы в знаниях. Возьмите."

    hide present_web_char

    play sound notif

    "{size=60}\"δreαmβo\"{/size}"

    $ been_present = True

    return

label future_web:

    stop music fadeout 1

    play sound steps

    scene bg future_city with Fade(0.5, 1, 0.5)

    play music m_future_city

    show future_web_char standing

    future_web_guy "Левее! Левее я сказал. Передвинь на 2 пикселя!"
    
    future_web_guy "А ты что тут встал, не мешайся."

    protag "Что вы делаете?"

    future_web_guy "Проектирую новый сайт."

    protag "Вау. У него очень приятный интерфейс. Выглядит как строительство, но в мире сети."

    protag "Я бы тоже хотел стать веб-дизайнером, но мои работы никому не нужны."

    future_web_guy "Почему вы так считаете?"

    protag "Я уже многие месяцы тружусь, не покладая рук, но получается мусор. Я хотел бы связать свою жизнь с этой сферой, но мне не хватает вдохновения."

    future_web_guy "Толковые веб-дизайнеры нужны. Конечно, возможно придётся подождать, чтобы ваши навыки заметили, но это дело времени."

    future_web_guy "Начинать надо с малого, а потом по мере развития ваших навыков, продолжать достигать новые вершины."

    protag "Спасибо за совет. А можно я попробую также как вы подвигать те блоки?"

    future_web_guy "М? Конечно же нет."

    protag "…"

    future_web_guy "Не мешайся. Возьми вот это и иди старайся над своими сайтами."

    protag "Опять что-то непонятное?"

    hide future_web_char

    play sound notif

    "{size=60}\".ok\"{/size}"

    $ been_future = True

    return