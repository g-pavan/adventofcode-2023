class Camel_Cards():
    def __init__(self, cards, bids) -> None:
        self.cards = cards
        self.bids = bids
        self.strengths = {'A': 14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    
    def get_strength(self, label):
        return self.strengths.get(label, 0)
    
    def custom_sort_function(self, card):
        return [self.get_strength(label) for label in card]
    
    def sort_cards(self, cards_bids):
        return sorted(cards_bids, key=lambda card:self.custom_sort_function(card[0]))

    def get_card_frequency(self, card):
        freq = {}

        for i in card:
            freq[i] = freq.get(i, 0)+1
        
        return freq
    
    def type_cards(self):
        fiver_fer = []
        four_of_kind = []
        full_house = []
        three_of_kind = []
        two_pair = []
        one_pair = []
        high_card = []

        for card, bid in zip(self.cards, self.bids):
            card_frequency = self.get_card_frequency(card)
            
            # print("before", card, card_frequency)

            j_card_count = card_frequency.get('J', 0)

            if(j_card_count > 0 and j_card_count < 5):
                max_label = ''
                max_value = 0
                for label in card_frequency:
                    if(label != 'J' and card_frequency[label] > max_value):
                        max_label = label
                        max_value = card_frequency[label]
                card_frequency[max_label] += j_card_count
                card_frequency.pop('J')
            
            length = len(card_frequency)
            values = list(card_frequency.values())


            # print("after", card, card_frequency, values)


            if(length == 1):
                fiver_fer.append((card, bid))
            elif(length == 2):
                if(min(values) <= 1):
                    four_of_kind.append((card, bid))
                else:
                    full_house.append((card, bid))
            elif(length == 3):
                if(max(values) >= 3):
                    three_of_kind.append((card, bid))
                else:
                    two_pair.append((card, bid))
            elif(length == 4):
                one_pair.append((card, bid))
            else:
                high_card.append((card, bid))

        fiver_fer = self.sort_cards(fiver_fer)
        four_of_kind = self.sort_cards(four_of_kind)
        full_house = self.sort_cards(full_house)
        three_of_kind = self.sort_cards(three_of_kind)
        two_pair = self.sort_cards(two_pair)
        one_pair = self.sort_cards(one_pair)
        high_card = self.sort_cards(high_card)
        
        # print("fiver_fer", fiver_fer)
        # print("four_of_kind", four_of_kind)
        # print("full_house", full_house)
        # print("three_of_kind", three_of_kind)
        # print("two_pair", two_pair)
        # print("one_pair", one_pair)
        # print("high_card", high_card)

        rank = 1
        ans = 0

        for card_and_bid in high_card:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in one_pair:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in two_pair:
            # print(card_and_bid)
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in three_of_kind:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in full_house:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in four_of_kind:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        for card_and_bid in fiver_fer:
            ans += (card_and_bid[1]*rank)
            rank += 1
        # print("++++++++")
        # print(rank, ans)
        return ans


if __name__ == "__main__":

    cards = []
    bids = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            cards.append(line.split()[0])
            bids.append(int(line.split()[-1]))

    camel_cards = Camel_Cards(cards, bids)

    ans = camel_cards.type_cards()

    print(ans)