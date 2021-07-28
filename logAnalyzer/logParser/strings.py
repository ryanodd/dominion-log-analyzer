import re

r_capitalizedWord = re.compile
r_number = re.compile('[0-9]+')
r_endsWithPeriod = re.compile('[^ ]*\.')

r_playerLetter = re.compile('[a-zA-Z]')
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
s_Exile = 'Exile'
s_receives = 'receives'
s_returns = 'returns'
s_sets = 'sets'
s_puts = 'puts'

s_card = 'card'
s_cards = 'cards'
s_deck = 'deck'
s_Pile = 'Pile'
s_mat = 'mat'
s_trash = 'trash'
s_hand = 'hand'

s_their = 'their'
s_and = 'and'
s_a = 'a'
s_an = 'an'
s_from = 'from'
s_to = 'to'
s_the = 'the'
s_with = 'with'
s_on = 'on'
s_aside = 'aside'
s_onto = 'onto'
s_into = 'into'
s_back = 'back'

s_hyphen = '-'

s_END = 'Players'

s_Horse = 'Horse'
s_Native = 'Native'
s_Village = 'Village'
s_Island = 'Island'
s_Druid = 'Druid'
s_CryptBrackets = '(Crypt)'
s_CargoLeftBracket = '(Cargo'
s_ShipRightBracket = 'Ship)'
s_minus_Coin = '-Coin'
