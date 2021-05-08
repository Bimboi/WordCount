import matplotlib.pyplot as plt
import re


def start():
    not_done = True

    while not_done:
        count_words()
        not_done = again()


def count_words():
    dict1 = dict()
    try:
        file = open(input("Enter filename or file directory: "))
        for line in file:
            alpha_num_list = filter(str.strip, [re.sub('[^a-zA-Z]+', '', _).lower() for _ in line.split()])
            for word in alpha_num_list:
                if word in dict1:
                    dict1[word] = dict1[word] + 1
                else:
                    dict1[word] = 1

        sorted_dict1 = sorted(dict1.items())
        sorted_words = list(item[0] for item in sorted_dict1)
        words_count = list(item[1] for item in sorted_dict1)

        plt.figure(figsize=(22, 8))
        plt.bar(sorted_words, words_count)
        plt.xlabel("Words")
        plt.ylabel("Word Count")
        plt.title("Number of times a word is used")

        plt.xticks(rotation=90)
        plt.grid()
        plt.tight_layout()
        plt.savefig('wc_figure.png', bbox_inches='tight', dpi=350)

    except Exception:
        print("File not found")


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
