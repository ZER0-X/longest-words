###input from a file
words_file = open(input("file_path:")).read()

###input from keyboard
# words_file = input("type:")

words_list = list(reversed(sorted(words_file.split(), key=len)))

max_len = len(words_list[0])

printed_words = []

for word in words_list:
    if len(word) == max_len and word not in printed_words:
        repetition = words_list.count(word)
        if repetition == 1:
            print(f"-----> {word}")
        else:
            print(f"-----> {word} [{repetition}]")
        printed_words.append(word)

print(f"max length = {max_len}")