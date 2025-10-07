# 💡 Python String Methods – Complete Demo

text = "  Hello, Python World!  "
word = "python"
digits = "12345"
mix = "Python3"
sentence = "welcome to python programming"

# 1️⃣ Case conversion methods
print(text.upper())          # '  HELLO, PYTHON WORLD!  '
print(text.lower())          # '  hello, python world!  '
print(text.title())          # '  Hello, Python World!  '
print(text.strip().capitalize())     # 'Hello, python world!' # capitalizes first letter of the string
print(text.swapcase())       # '  hELLO, pYTHON wORLD!  '

# 2️⃣ Whitespace handling
print(text.strip())          # 'Hello, Python World!'
print(text.lstrip())         # 'Hello, Python World!  '
print(text.rstrip())         # '  Hello, Python World!'

# 3️⃣ Searching and counting
print(text.find("Python"))   # 9 (first index) | If not found returns -1 no error
print(text.rfind("o"))       # 17 (last occurrence) - from right first index
print(text.index("World"))   # 16 (raises error if not found) | Same as find except index throws error when not found; find returns -1 if not found
print(text.count("o"))       # 3 (number of occurrences)
print("python" in text)      # True (substring check)
print("Java" not in text)    # True (substring not present)

# 4️⃣ Checking content type
print(word.isalpha())        # True (only letters)
print(digits.isdigit())      # True (only digits)
print(mix.isalnum())         # True (letters + numbers)
print(" ".isspace())         # True (only whitespace)
print("Python".islower())    # False
print("PYTHON".isupper())    # True
print("Title Case".istitle())# True

# 5️⃣ Replacing and splitting
print(text.replace("Python", "Java"))   # '  Hello, Java World!  '
print(text.replace(" ", "_"))           # '__Hello,_Python_World!__'

print(text.split())        # ['Hello,', 'Python', 'World!'] (splits on space if separator not mentioned by default)
print(text.split(","))     # ['  Hello', ' Python World!  ']
print("""Hello
World""".splitlines(keepends=True))
print(".".join(["A", "B", "C"]))   # 'A.B.C'
print("-".join(["Python", "Rocks"])) # 'Python-Rocks'

# 6️⃣ Alignment and padding
print(word.center(20, "-"))  # '-------python-------' | if character not mentioned then adds space by default
print(word.ljust(15, "."))   # 'python.........'
print(word.rjust(15, "."))   # '.........python'
print("Python".zfill(9))       # '000Python' #pads zeros to any string until length mentioned is reached
print("Python Language".zfill(9)) # 'Python Language' If length is already >= 9, then does not pad and retains the original string 

# 7️⃣ Start/End checks
print(text.startswith("  He"))  # True
print(text.endswith("!  "))     # True

# 8️⃣ Formatting (old & new)
name = "Alice"
lang = "Python"
print("Hello, {}!".format(name))                 # 'Hello, Alice!'
print("Hi, {0}. You love {1}.".format(name, lang))  # positional
print("Hi, {n}. You love {lng}.".format(n=name, lng=lang)) # keyword
print(f"Hi, {name}. You love {lang}.")           # f-string

# 9️⃣ Encoding & decoding
s = "Python"
encoded = s.encode("utf-8")
print(encoded)                  # b'Python'
print(encoded.decode("utf-8"))  # 'Python'

# 🔟 Miscellaneous
print(sentence.replace(" ", "_").title())  # 'Welcome_To_Python_Programming'
print(sentence.split(" ", 2))              # ['welcome', 'to', 'python programming']
print(sentence.partition("to"))            # ('welcome ', 'to', ' python programming')
print(sentence.rpartition("to"))           # ('welcome ', 'to', ' python programming')
print(sentence.expandtabs(4))              # handles tab expansion if any tabs are present

# 1️⃣1️⃣ Combine many methods
msg = "   learning PYTHON is Fun!   "
print(msg.strip().capitalize().replace("Python", "Java"))
# 'Learning java is fun!'

# 1️⃣2️⃣ Check all case transformations
print("python".casefold())  # aggressive lowercase for comparison
print("PYTHON".lower())     # standard lowercase

# 1️⃣3️⃣ Example: removing punctuation
import string
phrase = "Hello, world, 123!!!"
remove_whitespace = str.maketrans('', '', string.whitespace)
remove_puncs = str.maketrans('', '', string.punctuation)
remove_digits = str.maketrans('', '', string.digits)
remove_chars = str.maketrans('', '', 'Hold!')
print(phrase.translate(remove_digits))      # 'Hello, world, !!!'
print(phrase.translate(remove_puncs))       # 'Hello world 123'
print(phrase.translate(remove_whitespace))  # 'Hello,world,123!!!'
print(phrase.strip('Hold!'))                # 'ello, world, 123'
print(phrase.translate(remove_chars))       # 'e, wr, 123'
# Note: Strip removes the characters only if the characters are surrounding the string
# Note: translate removes the characters from anywhere around or within the string

# 1️⃣4️⃣ Example: counting vowels
vowels = "aeiou"
count = sum(1 for ch in text.lower() if ch in vowels)
print(f"Number of vowels in text: {count}")  # 5
