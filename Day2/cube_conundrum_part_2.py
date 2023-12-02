def cube_conundrum(picks):

    max_picks = {"red": 0, "green": 0, "blue":0}

    for pick in picks.split(";"):
        for ball in pick.split(","):
            value, color = ball.split()
            value = int(value)
            max_picks[color] = max(max_picks[color], value) 

    power_value = 1

    for color, value in max_picks.items():
        power_value *= value

    # print(picks, max_picks, power_value)

    return power_value


if __name__ ==  "__main__":

    ans = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            game_code, picks = line.split(":")    
            ans += cube_conundrum(picks)
    
    print(ans)