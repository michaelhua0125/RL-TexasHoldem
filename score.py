from collections import Counter

VALUES = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}
COMPARE_NUM = 5

# define combination scores
FLUSH_STRAIGHT = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
ONE_PAIR = 1
HIGH_CARDS = 0

def get_score(cards):
    assert len(set(cards)) == 7
    ## FIXME: might be wrong with multiple cards have the same suit
    flush_flag = has_flush(cards)
    straint_flag = has_straight(cards)
    if flush_flag:
        if is_straight(flush_flag[-1]):
            return [FLUSH_STRAIGHT, get_values(flush_flag[-1])]
        else:
            return [FLUSH, get_values(flush_flag[-1])]
    elif straint_flag:
        return [STRAIGHT, get_values(straint_flag[-1])]
    card_count = Counter()
    for card in cards:
        card_count[VALUES.get(card[0])] += 1
    count_keys = list(card_count.keys())
    count_values = list(card_count.values())
    if len(card_count) == 7: # no pairs or plus
        return [HIGH_CARDS, sorted(count_keys, reverse=True)[:COMPARE_NUM]]
    elif len(card_count) == 6: # one pair
        pair_card = count_keys[count_values.index(2)]
        count_keys.remove(pair_card)
        high_combination = [pair_card] * 2
        high_combination.extend(count_keys[:COMPARE_NUM - 2])
        return [ONE_PAIR, high_combination]
    elif len(card_count) == 5:
        if 3 in count_values: # 3 of a kind
            pair_card = count_keys[count_values.index(3)]
            count_keys.remove(pair_card)
            high_combination = [pair_card] * 3
            high_combination.extend(count_keys[:COMPARE_NUM - 3])
            return [THREE_OF_A_KIND, high_combination]
        else: # 2 pairs
            high_combination = []
            for i in range(2):
                pair_card = count_keys[count_values.index(2)]
                count_keys.remove(pair_card)
                count_values.remove(2)
                high_combination.extend([pair_card] * 2)
            high_combination = sorted(high_combination, reverse=True)
            high_combination.append(max(count_keys))
            return [TWO_PAIRS, high_combination]
    elif 4 in count_values:
        pair_card = count_keys[count_values.index(4)]
        high_combination = [pair_card] * 4
        high_combination.append(max(count_keys))
        return [FOUR_OF_A_KIND, high_combination]
    elif len(card_count) == 4:
        pair_card = count_keys[count_values.index(3)]
        high_combination = [pair_card] * 3
        pair_card = count_keys[count_values.index(2)]
        high_combination.extend([pair_card] * 2)
        return [FULL_HOUSE, high_combination]
    elif len(card_count) == 3:
        if 1 in count_values: #331
            single_card = count_keys[count_values.index(1)]
            count_keys.remove(single_card)
            three_card = max(count_keys)
            pair_card = min(count_keys)
            high_combination = [three_card] * 3
            high_combination.extend([pair_card] * 2)
            return [FULL_HOUSE, high_combination]
        else: #322
            three_card = count_keys[count_values.index(3)]
            count_keys.remove(three_card)
            pair_card = max(count_keys)
            high_combination = [three_card] * 3
            high_combination.extend([pair_card] * 2)
            return [FULL_HOUSE, high_combination]
    else:
        raise 'Unexpected combination'


def get_values(cards):
    return sorted(map(lambda s:VALUES.get(s[0]), cards), reverse=True)


def has_straight(cards):
    sorted_cards=sort_cards(cards, True)
    for card in cards:
        if card[0]=='A':
            sorted_cards.append(card)
    for i in range(len(sorted_cards)-COMPARE_NUM, -1, -1):
        current = sorted_cards[i:(i+COMPARE_NUM)]
        if is_straight(current):
            return [True, current]
    return False

def has_flush(cards):
    suit_count = Counter()
    for card in cards:
        suit_count[card[1]] += 1
    count_keys = list(suit_count.keys())
    count_values = list(suit_count.values())
    # FIXME: should be more than 5
    if 5 in count_values:
        suit = count_keys[count_values.index(5)]
        high_combination = [card for card in cards if card[1]==suit]
        return [True, high_combination]
    return False

def is_straight(cards):
    assert len(cards) == 5
    sorted_values = sorted(map(lambda s:VALUES.get(s[0]), cards))
    current_range = []
    for v in sorted_values:
        if len(current_range) == 0:
            current_range.append(v)
            continue
        if v == current_range[-1] + 1:
            current_range.append(v)
        elif v == 14 and current_range == [2,3,4,5]:
            break
        else:
            return False
    return True

def is_flush(cards):
    suits = set(map(lambda s:s[1], cards))
    return len(suits)==1

def sort_cards(cards, reverse=False):
    return sorted(cards, key=lambda s:VALUES.get(s[0]), reverse=reverse)
