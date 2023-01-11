
FILE_PATH = "streaks_infos.txt"


def save_streak_infos(total:int, max:int, average:int, total_correct:int) -> None:
    with open(FILE_PATH, 'w') as file:
        file.write(f'total numbers of streaks\n{total}\n')
        file.write(f'greater streak\n{max}\n')
        file.write(f'average\n{average}\n')
        file.write(f'total of correct answers\n{total_correct}')


def load_streak_infos() -> tuple:
    total = 0
    max = 0
    average = 0
    total_correct = 0

    with open(FILE_PATH, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                total = int(line)
            elif i == 4:
                max = int(line)
            elif i == 6:
                average = int(line)
            elif i == 8:
                total_correct = int(line)

    return total, max, average, total_correct



# import random as r

# def rdt(max:int) -> int:
#     return r.randint(max//2, max)

# save_streak_infos(rdt(300), rdt(40), rdt(15), rdt(1534))
# a, b, c, d = load_streak_infos()

# print(a, b, c, d)