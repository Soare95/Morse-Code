morse_code = {
    "a": ". _", "b": "_ . . .", "c": "_ . _ .", "d": "_ . .", "e": ".", "f": ". . _ .", "g": "_ _ .",
	"h": ". . . .", "i": ". .", "j": ". _ _ _", "k": "_ . _", "l": ". _ . .", "m": "_ _", "n": "_ .",
	"o": "_ _ _", "p": ". _ _ .", "q": "_ _ . _", "r": ". _ .", "s": ". . .", "t": "_", "u": ". . _",
	"v": ". . . _", "w": ". _ _", "x": "_ . . _", "y": "_ . _ _", "z": "_ _ . .", "1": ". _ _ _ _", "2": ". . _ _ _",
	"3": ". . . _ _", "4": ". . . . _", "5": ". . . . .", "6": "_ . . . .", "7": "_ _ . . .", "8": "_ _ _ . .",
	"9": "_ _ _ _ .", "0": "_ _ _ _ _", ",": "_ _ . . _ _", ".": ". _ . _ . _", "?": ". . _ _ . .", ";": "_ . _ . _ .",
	":": "_ _ _ . . .", "/": "_ . . _ .", "-": "_ . . . . _", "`": ". _ _ _ _ .", '"': ". _ . . _ .", "_": ". . _ _ . _",
	"(": "_ . _ _ .", ")": "_ . _ _ . _", "=": "_ . . . _", "+": ". _ . _ .", "*": "_ . . _", "@": ". _ _ . _ ."
	}

question = input("What do you want to translate in Morse Code? ")
question_split = list(question)
morse_response = []

for letter in question_split:
	for key, value in morse_code.items():
		if letter == key:
			morse_response.append(value)

print(morse_response
