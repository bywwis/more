def in_online(*names):
    match len(names):
        case 0:
            return 'Никого нет в сети'
        case 1:
            return f'{names[0]} в сети'
        case _:
            return f'{names[0]}, {names[len(names) - 1]} и ещё {len(names) - 2} в сети'
        case 2:
            return f'{names[0]} и {names[1]} в сети'

# данные


