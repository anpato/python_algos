letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
    unique = 0
    for char in letters:
        if char in word:
            unique += 1

    print(unique)
    return unique

# print(unique_english_letters("mississippi"))
# print(unique_english_letters("Apple"))


def count_char_x(word, x):
    count = 0
    for char in word:
        if char == x:
            count += 1
    return count

# print(count_char_x("mississippi", "s"))


def count_multi_char_x(word, x):
    new_word = word.split(x)
    return len(new_word)-1


# print(count_multi_char_x("mississippi", "iss"))
# print(count_multi_char_x("apple", "pp"))


def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    if start_index == -1 or end_index == -1:
        return word
    return word[start_index + 1: end_index]


# substring_between_letters("apple", "p", "e")

def x_length_words(sentence, count):
    for s in sentence.split():
        if len(s) >= count:
            return True
        else:
            return False


# print(x_length_words("i like apples", 2))
# print(x_length_words("he likes apples", 2))


def check_for_name(sentence, name):
    if not sentence.lower().find(name.lower()) == -1:
        return True
    return False


# print(check_for_name("My name is Samantha", "Jamie"))


def every_other_letter(word):
    string = ""
    skip = False
    if not len(word):
        return word
    for i in range(len(word)):
        if i % 2 != 0:
            skip = True
        else:
            skip = False
        if not skip:
            string += word[i]
    return string


print(every_other_letter("Hello world!"))
