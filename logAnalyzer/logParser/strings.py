import re

r_capitalizedWord = re.compile
r_number = re.compile('[0-9]+')
r_endsWithPeriod = re.compile('[^ ]*\.')

r_playerLetter = re.compile('[A-Z]')
r_gameNum = re.compile('\#[0-9]*\,')
r_moneyIndicator = re.compile('\(\+\$[0-9]+\)')

s_intro_game = 'Game'
s_intro_unrated = 'unrated'
s_intro_starts = 'starts'
s_intro_with = 'with'

s_turn = 'Turn'

s_draws = 'draws'
s_shuffles = 'shuffles'
s_plays = 'plays'
s_buys = 'buys'
s_gains = 'gains'
s_trashes = 'trashes'

s_card = 'card'
s_cards = 'cards'
s_deck = 'deck'

s_their = 'their'
s_and = 'and'
s_a = 'a'
s_an = 'an'

s_hyphen = '-'

s_END = 'Players'
