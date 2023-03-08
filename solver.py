
#follow the format: [ a, b, c | d, e, f | g, h, i | j, k, l] where three letter in a row correspond to the same edge
letters = ['z','o','y','e','k','t','i','l','v','a','u','c']
letters_set = set(letters)

def is_word(ele):
    for e in ele:
        if e not in letters_set:
            return False
    return True

dictionary_file = open("twl06.txt", "r")

# reading the file
data = dictionary_file.read()

words_list = data.split("\n")
words_list = [ele for ele in words_list if len(ele) >= 3]
words_list = [ele for ele in words_list if is_word(ele)]

word_splits = [set() for _ in range(len(words_list))]

for i in range(len(words_list)):
    for j in range(len(words_list[i])-1):
        word_splits[i].add(words_list[i][j]+words_list[i][j+1])

print(words_list)

#improper pairings
imp_pairs = []
for i in range(4): #four edges of cube
    sub_letters = [letters[i*3],letters[(i*3)+1],letters[(i*3)+2]]
    for j in range(3): #number of possible combinations of 3 letters in pairs of 2
        for k in range(3):
            imp_pairs.append(sub_letters[j]+sub_letters[k])

print(imp_pairs)
imp_pairs_set = set(imp_pairs)

def is_possible_word(splits):
    for e in splits:
        if e in imp_pairs_set:
            return False
    return True
        
#find possible words
possible_words = []
for i in range(len(words_list)):
    if is_possible_word(word_splits[i]):
        possible_words.append(words_list[i])

print()
print("ALL POSSIBLE WORDS:")
print(possible_words)

longestWordLength = len(max(possible_words, key=len))
result = [textword for textword in possible_words if len(textword) >= longestWordLength-2]

print()
print("LONGEST WORD:", result)

two_word_combinations = []

for word in possible_words:
    next_words = [ele for ele in possible_words if ele[0] == word[-1]]
    for word2 in next_words:
        if set(word+word2) == letters_set:
            two_word_combinations.append(word + ' + ' + word2)

print()
print("BEST COMBINATIONS:",end='')
if two_word_combinations:
    print(" (two word solutions)")
    print(two_word_combinations)



three_word_combinations = []

if not two_word_combinations:
    for word in possible_words:
        next_words = [ele for ele in possible_words if ele[0] == word[-1]]
        for word2 in next_words:
            next_words2 = [ele for ele in possible_words if ele[0] == word2[-1]]
            for word3 in next_words2:
                if set(word+word2+word3) == letters_set:
                    three_word_combinations.append(word + ' + ' + word2 + ' + ' + word3) 
    print(" (three word solutions)")
    print(three_word_combinations)