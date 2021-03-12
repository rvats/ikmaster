def caesarCipherEncryptor(string, key):
	result = ""
	while (key > 26):
		key-=26
	for char in string:
		temp = ord(char)+key
		if temp >= 123:
			temp=(temp-123) + 97
		result+=chr(temp)
	return str(result)

print(caesarCipherEncryptor("abc",2))
print(caesarCipherEncryptor("abc",52))
print(caesarCipherEncryptor("xyz",52))
print(caesarCipherEncryptor("xyz",2))