# Jääkiekko aiheinen tietovisa peli? Luo kysymyspankki, josta ohjelma hakee randomilla kysymyksen ja kysyy sitä.

# Ensiksi voi valita, kuinka pitkän pelin haluaa
# Tee tämä kahdella kielellä
# enkun kielinen kysymyspankki
# suomen kielinen kysymyspankki


import sys
from string import ascii_lowercase


def selectLanguage():
    print("The great hockey quiz")
    print("Select language")
    print("0) English")
    print("1) Finnish")
    while (True):
        languageChoice = int(input("Your answer: "))
        if languageChoice > 1:
            print("Incorrect answer, try again")
        else:
            break
    return languageChoice


def readLanguageTextFile(name, languages, languageChoice):
    try:
        file = open(name, "r", encoding="UTF-8")
        row = file.readline()[:-1]
        while (len(row) > 0):
            information = row.split(";")
            languages.append(information)
            row = file.readline()[:-1]
        file.close()
    except Exception:
        print("There was a error while trying to open file " + name + ", program will be closed.")
        sys.exit(0)
    
    return languages



def preInfo(languages, languageChoice):
    for i in range (len(languages)):
        print(languages[i] [languageChoice])

    lenghtOfGame = int(input(": "))
    return lenghtOfGame

def askQuestions(lenght):
    QUESTIONS = { "From which city is SaiPa from?": ["Lappeenranta", "Lahti", "Saimaanharju", "Kerava"],
                "Which team is reigning Liiga champion?": ["Tappara", "IFK", "Kärpät", "TPS"],
                "Which team is reigning Mestis champion?": ["Kiekko-Espoo", "Ketterä", "RoKi", "TuTo"],
                "Who is current captain of SaiPa?" : ["Miska Siikonen", "Ville Koho", "Jori lehterä", "Greg Moro"],
                
    }

    score = 0

    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=0):
            
            if num == lenght:
                break

            print(f"\nQuestion {num}:")
            print(f"{question}")
            correctAnswer = alternatives[0]
            taggedAlternatives = dict(zip(ascii_lowercase, sorted(alternatives)))

            for tag, alternative in taggedAlternatives.items():
                print(f"    {tag} {alternative}")  


            while True:
                answerTag = input("\nChoice? ")
                if answerTag in taggedAlternatives:
                    break
                else:
                    print("invalid answer, try again")


            answer = taggedAlternatives.get(answerTag)


            if answer == correctAnswer:
                print("Correct")
                score += 1
            else:
                print(f"Good try but the correct answer is {correctAnswer!r}, not {answer!r}")

    return score



def main():
    menuLanguages = []
    nameOfLanguage = "QuizProjectLanguage.txt"

    languageChoice = selectLanguage()
    menuLanguages = readLanguageTextFile(nameOfLanguage, menuLanguages, languageChoice)
    lenghtOfGame = preInfo(menuLanguages, languageChoice)
    
    score = askQuestions(lenghtOfGame)


    print()
    print()
    print("Statistics:")
    if (score / lenghtOfGame * 100 > 90):
        print("Your score is {}/{} ({:.1f} %), nice job".format(score, lenghtOfGame, score / lenghtOfGame * 100))
    elif (score / lenghtOfGame * 100 > 70):
        print("Your score is {}/{} ({:.1f} %), good job".format(score, lenghtOfGame, score / lenghtOfGame * 100))
    elif (score / lenghtOfGame * 100 > 50):
        print("Your score is {}/{} ({:.1f} %), solid".format(score, lenghtOfGame, score / lenghtOfGame * 100))   
    else:
        print("Your score is {}/{} ({:.1f} %), you can do better".format(score, lenghtOfGame, score / lenghtOfGame * 100))   
    
    return None


main()
