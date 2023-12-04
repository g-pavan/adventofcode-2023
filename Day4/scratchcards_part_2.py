def scratchcards(winners_numbers, having_numbers, ind, cards):
    winners_numbers = set(map(int, winners_numbers.split()))
    having_numbers = list(map(int, having_numbers.split()))
    
    winning_count = 0

    for i in having_numbers:
        
        if i in winners_numbers:
            winning_count += 1
        
    j = ind+1
    adder = cards[ind]
    while(winning_count != 0 and j < len(cards)):
        cards[j] += adder
        j += 1
        winning_count -= 1

if __name__ == "__main__":

    ans = 0
    ind = 1
    cards = [1 for i in range(202)] # 202 is max cards in test case which is static I have taken need to make this dynamic

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            card, values = line.split(":")
            winners_numbers, having_numbers = values.split("|")
            
            scratchcards(winners_numbers, having_numbers, ind, cards)
            ind += 1
    
    cards[0] = 0
    # print(cards)
    print(sum(cards))