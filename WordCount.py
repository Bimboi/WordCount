import matplotlib.pyplot as plt
import re
import docx


def start():
    not_done = True

    while not_done:
        count_words()
        not_done = again()


def count_words():
    # create a new dictionary
    dict1 = dict()
    try:
        file = input("Enter filename or file directory: ")
        if file[-3:] == "txt":
            txt = open(file)
            # read text file per enter line
            for line in txt:
                dict1 = get_dict(line)

            txt.close()
        elif file[-4:] == "docx":
            doc = docx.Document(file)
            full_text = []
            for para in doc.paragraphs:
                # join paragraphs into one line in index 0 of full_text
                full_text.append(para.text)

            dict1 = get_dict(full_text[0])
        else:
            raise FileNotFoundError

        # sort in ascending order
        sorted_dict1 = sorted(dict1.items())
        # separate words for x-labels and their count for y-labels
        sorted_words = list(item[0] for item in sorted_dict1)
        words_count = list(item[1] for item in sorted_dict1)

        print(sorted_dict1)

        plt.figure(figsize=(22, 8))
        plt.bar(sorted_words, words_count)
        plt.xlabel("Words")
        plt.ylabel("Word Count")
        plt.title("Number of times a word is used")

        plt.xticks(rotation=90)
        plt.grid()
        plt.tight_layout()
        plt.savefig('wc_figure.png', bbox_inches='tight', dpi=350)

    except FileNotFoundError:
        print("File not found")


def get_dict(words):
    temp_dict = dict()
    # for each enter line, split it to have a set of words
    # for each word, remove special characters, start and end spaces, then format to lowercase
    alpha_num_list = filter(str.strip, [re.sub('[^a-zA-Z]+', '', _).lower() for _ in words.split()])
    for word in alpha_num_list:
        if word in temp_dict:
            temp_dict[word] = temp_dict[word] + 1
        else:
            # first time counting the word
            temp_dict[word] = 1
    print(temp_dict)
    return temp_dict


def again():
    flag = True
    val = True

    while flag:
        choice = str(input("\nTry again (Y/N): "))

        if choice == "Y" or choice == "y":
            print("\nLoading program...\n")
            val = True
            flag = False
        elif choice == "N" or choice == "n":
            val = False
            flag = False
        else:
            print("\nInvalid input, '" + choice + "'!")

    return val


start()
