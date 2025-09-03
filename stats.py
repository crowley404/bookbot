def get_num_words(text):
	words = text.split()
	return len(words)

def get_num_characters(text):
	character_count = {}
	characters = text.lower()
	for character in characters:
		if character in character_count:
			character_count[character] += 1
		else: 
			character_count[character] = 1
	return character_count
