def get_word_count(text):
    word_list = text.split()
    return len(word_list)


def get_char_heatmap(text):
    heatmap = {}

    for char in text:
        lower_char = char.lower()
        if lower_char not in heatmap:
            heatmap[lower_char] = 1
        else:
            heatmap[lower_char] += 1

    return heatmap


def sort_heatmap_by_count(heatmap_entry):
    return heatmap_entry["count"]


def get_sorted_char_heatmap(heatmap):
    charcount_list = []
    for char in heatmap:
        count = heatmap[char]
        charcount_list.append({"char": char, "count": count})

    charcount_list.sort(reverse=True, key=sort_heatmap_by_count)

    return charcount_list