friends = ["Jack", "Kevin", "Tom"]
for index in range(len(friends)):
    print(friends[index])


def raiseToPower(baseNumber, powNumber):
    result = 1
    for i in range(powNumber):
        result *= baseNumber
    return result

print(raiseToPower(2, 4))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate("CIsco"))