import emoji

# Gets command form the user to be converted into an emoji
command = input("Input: ")
emoji_command = emoji.emojize(command)
emoji_alias = emoji.emojize(command, language = "alias")
# Outputs user input converted into an emoji
if emoji_command != command:
    print("Output: ",emoji_command)
else:
    print("Output: ",emoji_alias)