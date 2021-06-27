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
s_discards = 'discards'
s_exiles = 'exiles'
s_exile = 'exile'
s_recieves = 'recieves'
s_returns = 'returns'

s_card = 'card'
s_cards = 'cards'
s_deck = 'deck'
s_pile = 'pile'

s_their = 'their'
s_and = 'and'
s_a = 'a'
s_an = 'an'
s_from = 'from'
s_to = 'to'
s_the = 'the'

s_hyphen = '-'

s_END = 'Players'

s_Horse = 'Horse'
