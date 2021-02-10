def balancedBrackets(string):
	openingBrackets = ['(', '[', '{']
	closingBrackets = [')', ']', '}']
	stack = []
	for i in range(len(string)):
		if string[i] in openingBrackets:
			stack.append(string[i])
		elif (not stack and string[i] in closingBrackets) or (string[i] in closingBrackets and openingBrackets.index(stack.pop()) != closingBrackets.index(string[i])):
			return False
	if not stack:
		return True
	else:
		return False

print(balancedBrackets("(141[])(){waga}((51afaw))()hh()"))
print(balancedBrackets("([])(){}(())(({{[[]]}}))"))
print(balancedBrackets("((({{{[[[]]]}}})))"))
print(balancedBrackets("((({{{[[[]]]}}})))}"))
print(balancedBrackets("{((({{{[[[]]]}}})))"))