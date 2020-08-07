###input from a file
words_list = open(str(input("file_path:"))).read().split()

###input from keyboard
# words_list = input("type:").split()

longest_words = []
words_len = []

for word in words_list:
    words_len.append(len(word))

max_length = max(words_len)

for word in words_list:
    if len(word) == max_length:
        longest_words.append(word)

longest_words_not_repeated = set(longest_words)


print(f"""
max length = {max_length}
""")

for word in longest_words_not_repeated:
    repeated = longest_words.count(word)
    
    if repeated == 1 :
        print(f"---->'{word}'")
        
    elif repeated != 1 :
        print(f"---->'{word}' [{repeated}]")
        
    print("")


print(f"""

The max length is {max_length} Letters""")