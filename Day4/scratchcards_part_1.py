def scratchcards(winners_numbers, having_numbers):
    winners_numbers = set(map(int, winners_numbers.split()))
    having_numbers = list(map(int, having_numbers.split()))

    points = 0

    for i in having_numbers:
        if i in winners_numbers:
            if points == 0:
                points += 1
            else:
                points *= 2
    
    return points


if __name__ == "__main__":

    ans = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            card, values = line.split(":")
            winners_numbers, having_numbers = values.split("|")
            
            ans += scratchcards(winners_numbers, having_numbers)

    print(ans)