# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1626242
API_HASH = "c0de5b3edc5524437daf5bbdb3c0939d"

# Get this from @Botfather
TOKEN = "983775109:AAFYNqKzhAdexzODsDOmZw_bc5gaycKniPE"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1121888573,
    892443177,
    1035120498
    

]

# The ID of the group where your bot streams
GROUP = -1001268736347

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# Remove downloaded files after playing
REMOVE_AFTER_PLAYING = False

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
