"""Aim is to print emoji names with symbols in a dict format
    keys will be emoji name and values will be emoji symbols"""
import emoji
from configuration.emoji_config import *  # imports emoji symbol names from the emoji config file

# medals
for md in medals:
    print({md: emoji.emojize(":{}:".format(md))})

# buttons
for btn in buttons:
    print({btn: emoji.emojize(":{}:".format(btn))})

# flags
for flg in flags:
    print({flg: emoji.emojize(":{}:".format(flg))})

# sun sign
for ss in sun_signs:
    print({ss: emoji.emojize(":{}:".format(ss))})

# arrow
for arw in arrow:
    print({arw: emoji.emojize(":{}:".format(arw))})

# japanese sign
for jpn in japanese:
    print({jpn: emoji.emojize(":{}:".format(jpn))})

# couples
for cpl in couples:
    print({cpl: emoji.emojize(":{}:".format(cpl))})
