# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define m = Character("Главный герой", color="#ff00fc")
define z = Character("Не главный герой", color="#00ff3c")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg scene1

    "Сцена 1 (здесь могла бы быть ваша реклама)"
    
    scene bg scene2

    show character1 happy

    m "(Здесь могла быть ваша фраза)"

    scene bg scene3

    show character1 sad:
        xalign 0.3
    show character2 normal:
        xalign 0.75

    z "(Здесь могла быть ваша реплика)"

    return
