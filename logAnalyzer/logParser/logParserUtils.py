from logAnalyzer.logParser.strings import *  # all prefixed with s_ or r_


def getGameIdFromLog(log):
    lines = log.split('\n')
    for line in lines:
        words = line.split()
        if len(words) >= 2:
            if len(words[0]) == 1:
                return None
            if words[0] == s_intro_game:
                return words[1][1:-1]
