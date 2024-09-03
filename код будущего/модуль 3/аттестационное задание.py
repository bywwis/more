import random
from prettytable import PrettyTable


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.is_mine = False
        self.is_flag = False
        self.is_open = False
        self.count_mines_sosedi = 0

    def __str__(self):
        if self.is_open:
            if self.is_mine:
                return'*'
            else:
                return str(self.count_mines_sosedi)
        elif self.is_flag:
            return 'F'
        else:
            return '.'


class Game:
    def __init__(self, rows=5, cols=5, mines=5):
        self.rows = rows
        self.cols = cols
        self.mines = mines if mines < int(0.5 * self.rows * self.cols) else int(0.5 * self.rows, self.cols)
        self.board = []
        self.count_is_open = 0

    def initialisation_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(Cell(i, j))
            self.board.append(row)

        row_mines = random.choices(range(self.rows), k=self.mines)
        col_mines = random.choices(range(self.cols), k=self.mines)
        coords_mine = list(zip(row_mines, col_mines))

        for el in coords_mine:
            self.board[el[0]][el[1]].is_mine = True

        for i in range(self.rows):
            for j in range(self.cols):
                self.count_mines(i, j)

    def count_mines(self, row, col):
        coords_sosedi = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                         (row, col - 1), (row, col + 1),
                         (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        count_mines = 0
        for el in coords_sosedi:
            if (0 <= el[0] < self.rows and 0 <= el[1] < self.cols) and self.board[el[0]][el[1]].is_mine:
                count_mines += 1
        self.board[row][col].count_mines_sosedi = count_mines

    def print_board(self):
        pt = PrettyTable()
        pt.field_names = ['\\'] + [str(el) for el in range(self.cols)]
        for i, row in enumerate(self.board):
            pt.add_row([str(i)] + [*row])
        print(pt)

    def gameSession(self):
        self.initialisation_board()
        self.print_board()

        while True:
            for i in range(self.rows):
                row = int(input('Введите номер строки '))
                if row > self.rows:
                    print('Введено некорректное значение строки. Повторите попытку.')
                else:
                    break

            for j in range(self.cols):
                col = int(input('Введите номер столбца '))
                if col > self.cols:
                    print('Введено некорректное значение столбца. Повторите попытку.')
                else:
                    break

            action = int(input('1 - открыть / 2 - пометить флагом '))
            if action == 1:
                self.board[row][col].is_open = True
                self.count_is_open += 1
            elif action == 2:
                self.board[row][col].is_flag = True
            else:
                print('Введено некорректное значение. Повторите попытку.')
            self.print_board()

            if self.board[row][col].is_mine and self.board[row][col].is_open:
                print('Вы попали на мину! Игра закончена.')
                Game().restart_game()
                break
            if self.board[row][col].is_mine == False and self.rows * self.cols - self.mines == self.count_is_open:
                print('Вы выиграли! Игра закончена')
                Game().restart_game()
                break

    def restart_game(self):
        while True:
            print('Хотите перезапустить игру? 1 - перезапустить с настройками по умолчанию, 2 - выйти в меню')
            restart = input()
            if restart == '1':
                Game().gameSession()
                break
            elif restart == '2':
                Game().menu()
                break
            else:
                print('Введено некорректное значение. Повторите попытку.')

    def menu(self):
        while True:
            print("Сапёр")
            print("Меню:")
            print("1. Играть")
            print('2. Настройки поля')
            print("3. Выход")
            choice = input("Выберите пункт меню: ")

            if choice == '1':
                Game().gameSession()
                break
            elif choice == '2':
                Game().settings()
                break
            elif choice == '3':
                break
            else:
                print('Введено некорректное значение. Повторите попытку.')

    def settings(self):
        while True:
            print('Настройка параметров поля')
            print('1. Поле по умолчанию (5х5 с 5-ю минами)')
            print('2. Поле 3х3 с 3-мя минами')
            print('3. Поле с пользовательскими параметрами')
            settings = input('Выберите пункт ')

            if settings == '1':
                Game()
                print('Настройки применены. 1 - вернуться в меню, чтобы сбросить настройки, 2 - играть')
                back_menu = input()
                if back_menu == '1':
                    Game().menu()
                    break
                elif back_menu == '2':
                    Game().gameSession()
                    break

            elif settings == '2':
                Game(3, 3, 3)
                print('Настройки применены. 1 - вернуться в меню, чтобы сбросить настройки, 2 - играть')
                back_menu = input()
                if back_menu == '1':
                    Game(3, 3, 3).menu()
                    break
                elif back_menu == '2':
                    Game(3, 3, 3).gameSession()
                    break

            elif settings == '3':
                row = int(input('Введите количество строк: '))
                col = int(input('Введите количество столбцов: '))
                mine = int(input('Введите количество мин: '))
                game = Game(row, col, mine)
                print('Настройки применены. 1 - вернуться в меню, чтобы сбросить настройки, 2 - играть')
                game.gameSession()
                break

            else:
                print('Введено некорректное значение. Повторите попытку.')

if __name__ == '__main__':
    Game().menu()




# Хороший интерфейс для игрока, с учётом возможных ошибок (если пользователь задал значение row/col больше, чем положено) - выполнено
# Окончание игры в случае победы - выполнено

# Возможность перезапуска игры в случае победы или поражения - выполнено
# При запуске или перезапуске игры запрашивать параметры поля и количество мин (сделан отдельный пункт меню в настройками поля)

# Сделать открытие всех соседей с 0 мин от текущей открытой ячейки с 0 мин - не выполнено