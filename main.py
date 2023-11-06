import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

keep_asking = True
while keep_asking:
    try:
        word = input("Enter a word: ").upper()
        if word == "EXIT":
            keep_asking = False
        else:
            phon_word = [data_dict[letter] for letter in word]
            print(phon_word)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
