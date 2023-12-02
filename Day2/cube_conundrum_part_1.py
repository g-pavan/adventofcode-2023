def get_game_code(game):
    return int(game.split()[-1])


def cube_conundrum(picks):

    max_picks = {"red": 12, "green": 13, "blue":14}

    for pick in picks.split(";"):
        for ball in pick.split(","):
            value, color = ball.split()
            value = int(value)
            if(value > max_picks[color]):
                return False
    
    return True


if __name__ ==  "__main__":

    ans = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            game_code, picks = line.split(":")
            
            if(cube_conundrum(picks)):
                ans += get_game_code(game_code)
    
    print(ans)