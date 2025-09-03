def get_num_words(text):
	words = text.split()
	return len(words)

def sort_on(items):
    return items["num"]

def get_all_characters(text):
	all_characters = {}
	text = text.lower()
	for character in text :
		if character in all_characters :
			all_characters[character] += 1
		else :
			all_characters[character] = 1
	char_list = []
	for key, value in all_characters.items() :
		if key.isalpha():
			char_list.append({"char" : key, "num" : value})
	char_list.sort(reverse=True, key=sort_on)
	return char_list
