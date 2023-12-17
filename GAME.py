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

    for guess in range(3):
        word_guess = input("guess the word:".format(guess + 1))
        if word_guess.lower() == i["word"].lower():
            print("Correct!\n")
            break
        else:
            if guess < 2:
                print("Incorrect. Try again")
            else:
                print("Incorrect. You have reached your max number of attempt")
                print("The correct word is:", i["word"], "\n")