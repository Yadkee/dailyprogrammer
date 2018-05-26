#! python3

OPTIONS = {i for i in range(1, 10)}


def sure_cell(sudoku):
    run = True
    while run:
        run = False
        for a, i in enumerate(sudoku):
            if i != 0:
                continue
            n = OPTIONS - set(near(sudoku, a))
            if len(n) == 1:
                sudoku[a] = n.pop()
                run = True
    return sudoku


def least_posibilities(sudoku):
    possibilities = [(OPTIONS - set(near(sudoku, a)), a)
                     for a, i in enumerate(sudoku) if i == 0]
    return min(possibilities, key=lambda x: len(x[0]))


def solve(sudoku):
    sudoku = sure_cell(sudoku)

    if sudoku.count(0) == 0:
        return sudoku  # Sudoku solved

    # Try the cell that has the least number of options
    n, cell = least_posibilities(sudoku)
    for option in n:  # Try every option on cell
        optional = sudoku.copy()
        optional[cell] = option
        optional = solve(optional)
        if optional:
            return optional
    return False  # No cell worked


def near(sudoku, n):
    block = n // 27 * 3 + n % 9 // 3
    i = block // 3 * 27 + block % 3 * 3
    return (sudoku[n % 9:81:9] +  # Column + Row + Block
            sudoku[n // 9 * 9:9 + n // 9 * 9] +
            sudoku[i:i + 3] + sudoku[i + 9:i + 12] + sudoku[i + 18:i + 21])


def is_legit(sudoku):
    for a, i in enumerate(sudoku):
        if i == 0 or near(sudoku, a).count(i) <= 3:
            continue
        return False
    return True


def to_string(sudoku):
    return "".join(str(i) for i in sudoku)


def from_string(sudoku):
    return bytearray(int(i) for i in sudoku)
