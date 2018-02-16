from score import *

# flush straight 8
# four-of-a-kind 7
# full house 6
# flush 5
# straight 4
# three-of-a-kind 3
# two pairs 2
# one pair 1
# high cards 0

# # test score
# test_cases1 = {
#                 'AS 2S 3S 4S 5S JC QC':8,
#                 '3S 3C 3D 3H 2S 4S 4C':7,
#                 'JS JD JH 4S 4H 2D 3C':6,
#                 'AS KS QH JS TS 8S 8H':5,
#                 'AC KS QH JS TS 8S 8H':4,
#                 'AC KS QH JS 8C 8S 8H':3,
#                 '3S 3C 5D QH 2S 4S 4C':2,
#                 'AS KS QH JS 7S 8C 8H':1,
#                 'AS KS TC 9C 5S 4H 2D':0
#               }
#
# print('Test score: ')
# for key, value in test_cases1.items():
#     cards = key.split(' ')
#     result = get_score(cards)[0]
#     try:
#         assert result==value
#     except AssertionError:
#         line = 'Result of '+ key + ' should be ' + str(value) + ', but got ' + str(result)
#         print(line)
# print('Done!')
#
#
# #test is_straight
# test_cases2 = {'2S 4S 3S 5S AS':True,
#               '3S 3C 3D 3H 2S':False,
#               'JS JD JH 4S 4H':False,
#               'AS KS QH JS TS':True,
#               'KS QH JS TS 9S':True
#               }
#
# print('Test is_straight')
# for key, value in test_cases2.items():
#     cards = key.split(' ')
#     result = is_straight(cards)
#     try:
#         assert result==value
#     except AssertionError:
#         line = 'Result of '+ key + ' should be ' + str(value) + ', but got ' + str(result)
#         print(line)
# print('Done!')
#
# # test is_flush
# test_cases3 = {'AS 2S 3S 4S 5S':True,
#               '3S 3C 3D 3H 2S':False,
#               'JS JD JH 4S 4H':False,
#               'AH JH TH 2H 4H':True}
#
# print('Test is_flush')
# for key, value in test_cases3.items():
#     cards = key.split(' ')
#     result = is_flush(cards)
#     try:
#         assert result==value
#     except AssertionError:
#         line = 'Result of '+ key + ' should be ' + str(value) + ', but got ' + str(result)
#         print(line)
# print('Done!')

# test score 2
test_cases4 = {
                'AS 2S 3S 4S 5S JC QC':[8, [5, 4, 3, 2, 1]],
                'AS KS QS JS TS AH KD': [8, [14, 13, 12 ,11, 10]],
                '2S 3S 4S 5S 6S 6C 6H':[8, [6, 5, 4, 3, 2]],
                '2S 3D 4S 5S 6S 6C 6H':[4, [6, 5, 4, 3, 2]],
                'AS 2S 3S 4S 5S 2C 3C':[8, [5, 4, 3, 2, 1]],
                '8S 9S 4S AS JS 7S QS':[5, [14, 12, 11, 9, 8]],
                '8S 9S TS AS JS 7S QS':[8, [12, 11, 10, 9, 8]],
                '8S 9S TS AS JS 7C QS':[8, [12, 11, 10, 9, 8]],
                '9D TS 7H KH QH 2C 3C':[0, [13, 12, 10, 9, 7]],
                '9D TS 7H KH JH 2C 3C':[0, [13, 11, 10, 9, 7]],
                '3S 3C 3D 3H 2S 4S 4C':[7, [3, 3, 3, 3, 4]],
                'JS JD JH 4S 4H 2D 3C':[6, [11, 11, 11, 4, 4]],
                'AS KS QH JS TS 8S 8H':[5, [14, 13, 11, 10, 8]],
                'AC KS QH JS TS 8S 8H':[4, [14, 13, 12, 11, 10]],
                'AC KS QH JS 8C 8S 8H':[3, [8, 8, 8, 14, 13]],
                '3S 3C 5D QH 2S 4S 4C':[2, [4, 4, 3, 3, 12]],
                'AS KS QH JS 7S 8C 8H':[1, [8, 8, 14, 13, 12]],
                'AS KS TC 9C 5S 4H 2D':[0, [14, 13, 10, 9, 5]],
              }

print('Test score step2 ')
for key, value in test_cases4.items():
    cards = key.split(' ')
    result = get_score(cards)
    try:
        assert result==value
    except AssertionError:
        line = 'Result of '+ key + ' should be ' + str(value) + ', but got ' + str(result)
        print(line)
print('Done!')
