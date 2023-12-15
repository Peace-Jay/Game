Game = [{
    "word": "peace",
    "hint": "state of no war"
},
    {
        "word":"Dog",
        "hint":"always barks"
    },
    {
        "word" : "Bible",
        "hint":"what you feed your spirit man"
    }]

for i in Game:
    hint = i["hint"]
    print("hint:", hint)

    word_guess = input("guess the word:")

    if word_guess == i["word"]:
        print("Correct!\n")
    else:
        print("Incorrect. The correct word is:",  i["word"], "\n")
        print("hint:", hint, "\n")