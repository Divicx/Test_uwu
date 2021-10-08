
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            print("Letter: " + letter)
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a sentence you want to translate: ")))
