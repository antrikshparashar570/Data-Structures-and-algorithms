string = "this is a test string"
pat = "tist"

def window(string, pat):

	len_str = len(string)
	len_pat = len(pat)

	if len_str < len_pat:
		return "not possible"

	hash_pat = [0]*256
	hash_str = [0]*256

	for i in range(len(pat)):
		hash_pat[ord(pat[i])] += 1

	start, start_index, min_len = 0, -1, 99999999

	count = 0

	for i in range(len(string)):
		hash_str[ord(string[i])] += 1

		if hash_pat[ord(string[i])] != 0 and hash_str[ord(string[i])] <= hash_pat[ord(string[i])]:
			count += 1

		if count == len_pat:

			while hash_pat[ord(string[start])] < hash_str[ord(string[start])] or hash_pat[ord(string[start])] == 0:

				if hash_pat[ord(string[start])] <= hash_str[ord(string[start])]:
					hash_str[ord(string[start])] -= 1
				start += 1

			len_window = i - start + 1

			if len_window < min_len:
				min_len = len_window
				start_index = start

	if start_index == -1:
		return "No window exists"

	return string[start_index: start_index + min_len]


print(window(string, pat))