from collections import Counter

VALUES = {
    '1':1,
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
DESC=True

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
    card_count = Counter()
    for card in cards:
        card_count[VALUES.get(card[0])] += 1
    count_keys = list(card_count.keys())
    count_values = list(card_count.values())
    if len(count_keys) >= 5:
        if has_flush(cards):
            candidates = get_flush(cards)
            if has_straight(candidates):
                combination = get_straight(candidates)
                return [FLUSH_STRAIGHT, get_values(combination)]
            else:
                return [FLUSH, get_values(candidates[:COMPARE_NUM])]
        elif has_straight(cards):
            return [STRAIGHT, get_values(get_straight(cards))]


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


def get_flush(cards):
    flush_cards = []
    suit_count = Counter()
    for card in cards:
        suit_count[card[1]] += 1
    count_keys = list(suit_count.keys())
    count_values = list(suit_count.values())
    for k, v in suit_count.items():
        if v >= 5:
            flush_cards.extend([card for card in cards if card[1]==k])
            return sort_cards(flush_cards, DESC)
    raise 'No flush combination found'


def get_straight(cards):
    unique_cards = remove_duplicates(cards)
    sorted_cards=sort_cards(unique_cards, DESC)
    for card in sorted_cards:
        if card[0]=='A':
            sorted_cards.append('1'+card[1])
    for i in range(len(sorted_cards)-COMPARE_NUM + 1):
        current = sorted_cards[i:(i+COMPARE_NUM)]
        if is_straight(current):
            if check_card_in_cards('A', current) and check_card_in_cards('2', current):
                temp = '1' + current[0][1]
                current = current[1:]
                current.append(temp)
            return current
    raise 'No straight combination found'


def has_straight(cards):
    unique_cards = remove_duplicates(cards)
    sorted_cards=sort_cards(unique_cards, DESC)
    for card in sorted_cards:
        if card[0]=='A':
            sorted_cards.append('1'+card[1])
    for i in range(len(sorted_cards)-COMPARE_NUM + 1):
        current = sorted_cards[i:(i+COMPARE_NUM)]
        if is_straight(current):
            return True
    return False

def has_flush(cards):
    suit_count = Counter()
    for card in cards:
        suit_count[card[1]] += 1
    count_keys = list(suit_count.keys())
    count_values = list(suit_count.values())
    for k, v in suit_count.items():
        if v >= 5:
            return True
    return False

def is_straight(cards):
    assert len(cards) == 5
    sorted_values = sort_cards(cards, DESC, True)
    if 2 in sorted_values and 14 in sorted_values:
        sorted_values.remove(14)
        sorted_values.append(1)
    current_range = []
    for v in sorted_values:
        if len(current_range) == 0:
            current_range.append(v)
            continue
        if v == current_range[-1] - 1:
            current_range.append(v)
        else:
            return False
    return True

def is_flush(cards):
    suits = set(map(lambda s:s[1], cards))
    return len(suits)==1

def get_values(cards):
    return sorted(map(lambda s:VALUES.get(s[0]), cards), reverse=DESC)

def get_value(card):
    return VALUES.get(card[0])

def rank(card):
    return card[0]

def suit(card):
    return card[1]

def sort_cards(cards, reverse=False, return_values=False):
    if return_values:
        return sorted(map(lambda s:VALUES.get(s[0]), cards), reverse=reverse)
    else:
        return sorted(cards, key=lambda s:VALUES.get(s[0]), reverse=reverse)

def check_card_in_cards(card, cards):
    return (get_value(card) in get_values(cards))

def remove_duplicates(cards):
    unique_cards = {}
    for card in cards:
        value = get_value(card)
        if unique_cards.get(value, None):
            continue
        else:
            unique_cards[value] = card
    return list(unique_cards.values())
