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
            dict1 = get_dict(txt)

            txt.close()
        elif file[-4:] == "docx":
            doc = docx.Document(file)
            full_text = []
            for para in doc.paragraphs:
                # list paragraphs
                full_text.append(para.text)

            dict1 = get_dict(full_text)
        else:
            raise FileNotFoundError

        length = len(dict1)
        print("Unique word count: " + str(length))
        if 201 > length > 0:
            get_figures(dict1, length)
        elif 201 < length:
            print("\nNumber of unique words exceed: " + str(length))
        else:
            print("\nFile does not contain a word!")

    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Unable to open file")


def get_dict(words):
    temp_dict = dict()
    # for each string, split it to have a set of words
    # for each word, remove special characters, start and end spaces, then format to lowercase
    for line in words:
        alpha_num_list = filter(str.strip, [re.sub('[^a-zA-Z]+', '', _).lower() for _ in line.split()])
        for word in alpha_num_list:
            if word in temp_dict:
                temp_dict[word] = temp_dict[word] + 1
            else:
                # first time counting the word
                temp_dict[word] = 1
    return temp_dict


def get_figures(dict1, length):
    # sort in ascending order
    sorted_dict1 = sorted(dict1.items())
    # separate words for x-labels and their count for y-labels
    sorted_words = list(item[0] for item in sorted_dict1)
    words_count = list(item[1] for item in sorted_dict1)

    if 201 > length > 150:
        # round down
        one_fourth_index = length // 4
        half_index = one_fourth_index * 2
        three_fourth_index = one_fourth_index * 3

        # split both lists into four
        first_sorted = sorted_words[:one_fourth_index]
        second_sorted = sorted_words[one_fourth_index:half_index]
        third_sorted = sorted_words[half_index:three_fourth_index]
        fourth_sorted = sorted_words[three_fourth_index:]
        first_count = words_count[:one_fourth_index]
        second_count = words_count[one_fourth_index:half_index]
        third_count = words_count[half_index:three_fourth_index]
        fourth_count = words_count[three_fourth_index:]

        # first figure
        get_two_plots(first_sorted, second_sorted, first_count, second_count)
        plt.savefig('wc-figures/wc_figure1.png', bbox_inches='tight', dpi=200)

        # second figure
        get_two_plots(third_sorted, fourth_sorted, third_count, fourth_count)
        plt.savefig('wc-figures/wc_figure2.png', bbox_inches='tight', dpi=200)

    elif 151 > length > 100:
        # round down
        one_third_index = length // 3
        two_third_index = one_third_index * 2

        # split both lists into three
        first_sorted = sorted_words[:one_third_index]
        second_sorted = sorted_words[one_third_index:two_third_index]
        third_sorted = sorted_words[two_third_index:]
        first_count = words_count[:one_third_index]
        second_count = words_count[one_third_index:two_third_index]
        third_count = words_count[two_third_index:]

        # first figure
        get_two_plots(first_sorted, second_sorted, first_count, second_count)
        plt.savefig('wc-figures/wc_figure1.png', bbox_inches='tight', dpi=200)

        # second figure
        get_one_plot(third_sorted, third_count)
        plt.savefig('wc-figures/wc_figure2.png', bbox_inches='tight', dpi=200)

    elif length > 50:
        # round down
        middle_index = length // 2

        # split both lists into two
        first_sorted = sorted_words[:middle_index]
        second_sorted = sorted_words[middle_index:]
        first_count = words_count[:middle_index]
        second_count = words_count[middle_index:]

        get_two_plots(first_sorted, second_sorted, first_count, second_count)
        plt.savefig('wc-figures/wc_figure.png', bbox_inches='tight', dpi=200)

    else:
        get_one_plot(sorted_words, words_count)
        plt.savefig('wc-figures/wc_figure.png', bbox_inches='tight', dpi=200)


def get_one_plot(sorted1, count1):
    # figsize=(width, height)
    # barh - plot horizontal bar
    # grid(axis='x') - add only vertical lines of a grid
    plt.figure(figsize=(11, 9))
    plt.barh(sorted1, count1)
    plt.title("Number of times a word is used")
    plt.xlabel("Word count")
    plt.ylabel("Words in the file")
    plt.grid(axis='x')


def get_two_plots(sorted1, sorted2, count1, count2):
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 9))
    ax1.barh(sorted1, count1)
    ax2.barh(sorted2, count2)

    ax1.grid(axis='x')
    ax2.grid(axis='x')
    # main title
    fig.suptitle("Number of times a word is used")
    # common y-label
    fig.text(0.5, 0, 'Word count', ha='center')
    # common x-label
    fig.text(0, 0.5, 'Words in the file', va='center', rotation='vertical')
    plt.tight_layout(pad=1.0)


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
