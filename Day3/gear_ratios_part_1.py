def isSymbol(charcter):
    return not charcter.isdigit() and charcter != '.'


def extract_numbers_positions_in_string(string, pos):
    if (not string[pos].isdigit()):
        return []

    positions = [pos]

    i = pos
    j = pos + 1

    while (i >= 0 and string[i].isdigit()):
        positions.append(i)
        i -= 1

    while (j < len(string) and string[j].isdigit()):
        positions.append(j)
        j += 1

    positions.sort()

    return positions


def gear_ratios(matrix):
    N = len(matrix)
    check = [[False for j in range(N)] for i in range(N)]
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    ans = 0

    for i in range(N):
        for j in range(N):
            if (isSymbol(matrix[i][j])):

                for k in range(len(dx)):
                    X = i + dx[k]
                    Y = j + dy[k]

                    if (X >= 0 and X < N and Y >= 0 and Y < N and check[X][Y] != True):
                        positions = extract_numbers_positions_in_string(
                            matrix[X], Y)

                        for pos_y in positions:
                            check[X][pos_y] = True

                        check[X][Y] = True

                        if (len(positions) > 1):
                            ans += int(matrix[X][positions[0]:positions[-1]+1])

    return ans


if __name__ == "__main__":

    matrix = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(line)

    print(gear_ratios(matrix))
