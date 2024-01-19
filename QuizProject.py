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
        try:
            languageChoice = int(input("Your answer: "))
            if languageChoice > 1:
                print("Incorrect answer, try again")
            else:
                break
        except ValueError:
            print("Invalid input, please use integer")
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
        if languageChoice == 0:
            print("There was a error while trying to open file " + name + ", program will be closed.")
        else:
            print("Virhe avattaessa tiedostoa " + name + ", ohjelma suljetaan.")
        sys.exit(0)
    
    return languages
0


def preInfo(languages, languageChoice):
    for i in range (len(languages)):
        print(languages[i] [languageChoice])
    while True:
        try:
            lenghtOfGame = int(input(": "))
            if lenghtOfGame == 0 or lenghtOfGame > 10:
                if languageChoice == 0:
                    print("Incorrect answer, try again")
                else:
                    print("Virheellinen vastaus, yritä uudestaan")
            else:
                break
        except ValueError:
            if languageChoice == 0:
                print("Invalid input, please use integer")
            else:
                print("Virheellinen syöte, käytä kokonaislukua")
    return lenghtOfGame

def askQuestions(lenght, languageChoice):
    if languageChoice == 0: 
        QUESTIONS = { 
                    "In which year Finland won the latest World Championship?": ["2022","2011","2021","2019"],
                    "Who has the most games played in Finland's national team?": ["Raimo Helminen","Jari Kurri","Teemu Selänne","Ville Peltonen"],
                    "From which city is SaiPa from?": ["Lappeenranta", "Lahti", "Saimaanharju", "Kerava"],
                    "Which team is reigning Liiga champion?": ["Tappara", "IFK", "Kärpät", "TPS"],
                    "Which team is reigning Mestis champion?": ["Kiekko-Espoo", "Ketterä", "RoKi", "TuTo"],
                    "Who is current captain of SaiPa?" : ["Miska Siikonen", "Ville Koho", "Jori lehterä", "Greg Moro"],
                    "Who hold the record of longest single shift in Liiga season 2022-23?" : ["Greg Moro","Atte Ohtamaa","Otto Hokkanen","Colby Sissons"],
                    "How long is the record shift?" : ["4:57","3:23","3:46","2:58"],
                    "Which player holds the record of total games withouth having scored a single goal?": ["Rami Määttä","Matti Hana","Jere Sneck","Elias Ulander"],
                    "Which player holds the record of total penalty minutes in Liiga?": ["Markus Kankaanperä","Toni Mäkiaho","Pauli Levokari","Jyri Marttinen"],
    }
    else:
        QUESTIONS = { 
                    "Milloin Suomi on viimeksi voittanut jääkiekon maailmanmestaruuden?": ["2022","2011","2021","2019"],
                    "Kenellä pelaajalla on eniten pelattuja pelejä Suomen maajoukkueessa?": ["Raimo Helminen","Jari Kurri","Teemu Selänne","Ville Peltonen"],
                    "Mistä kaupungista SaiPa on kotoisin?": ["Lappeenranta", "Lahti", "Saimaanharju", "Kerava"],
                    "Kuka on hallitseva Liiga mestari?": ["Tappara", "IFK", "Kärpät", "TPS"],
                    "Kuka on hallitseva Mestis mestari?": ["Kiekko-Espoo", "Ketterä", "RoKi", "TuTo"],
                    "Kuka on nykyinen SaiPan kapteeni?" : ["Miska Siikonen", "Ville Koho", "Jori lehterä", "Greg Moro"],
                    "Kuka pitää hallussaan kauden 2022-23 Liigan pisintä yksittäistä vaihtoa" : ["Greg Moro","Atte Ohtamaa","Otto Hokkanen","Colby Sissons"],
                    "Kuinka pitkä tämä vaihto oli?" : ["4:57","3:23","3:46","2:58"],
                    "Kuka pelaaja pitää hallussaan ennätystä eniten pelatuista peleistä tekemättä yhtään maalia?": ["Rami Määttä","Matti Hana","Jere Sneck","Elias Ulander"],
                    "Kuka pelaaja pitää hallussaan eniten jäähyminuutteja Liigan historiassa?": ["Markus Kankaanperä","Toni Mäkiaho","Pauli Levokari","Jyri Marttinen"],
        }


    score = 0

    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=0):
            
            if num == lenght:
                break
            if (languageChoice == 0):
                print(f"\nQuestion {num + 1}:")
            if (languageChoice == 1):
                print(f"\nkysymys {num + 1}:")
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
                    if languageChoice == 0:
                        print("invalid answer, try again")
                    else:
                        print("Virheellinen vastaus, yritä uudestaan")


            answer = taggedAlternatives.get(answerTag)


            if answer == correctAnswer:
                if languageChoice == 0:
                    print("Correct, " + " the right answer was "+ correctAnswer)
                else:
                    print("Oikein," + " oikea vastaus oli " + correctAnswer)
                score += 1
            else:
                if (languageChoice == 0):
                    print(f"Good try but the correct answer is {correctAnswer!r}, not {answer!r}")
                else:
                    print(f"Hyvä yritys, mutta oikea vastaus on {correctAnswer!r}, eikä {answer!r}")

    return score



def main():
    menuLanguages = []
    nameOfLanguage = "QuizProjectLanguage.txt"

    languageChoice = selectLanguage()
    menuLanguages = readLanguageTextFile(nameOfLanguage, menuLanguages, languageChoice)
    lenghtOfGame = preInfo(menuLanguages, languageChoice)
    
    score = askQuestions(lenghtOfGame, languageChoice)

    rating = score / lenghtOfGame * 100

    print()
    print()
    if languageChoice == 0:
        print("Statistics:")
        if (rating > 90):
            print("Your score is {}/{} ({:.1f} %), you are a true hockey fanatic!".format(score, lenghtOfGame, rating * 100))
        elif (rating > 70):
            print("Your score is {}/{} ({:.1f} %), good job".format(score, lenghtOfGame, rating))
        elif (rating > 50):
            print("Your score is {}/{} ({:.1f} %), solid".format(score, lenghtOfGame, rating))   
        else:
            print("Your score is {}/{} ({:.1f} %), better luck next time".format(score, lenghtOfGame, rating))   
    else:
        print("Tulokset:")
        if (rating > 90):
            print("Tuloksesi on {}/{} ({:.1f} %), olet oikea jääkiekkoguru!".format(score, lenghtOfGame, rating))
        elif (rating > 70):
            print("Tuloksesi on {}/{} ({:.1f} %), hienoa tiedät paljon enemmän kuin keskiverto ihminen!".format(score, lenghtOfGame, rating))
        elif (rating > 50):
            print("Tuloksesi on {}/{} ({:.1f} %), hyvää työtä".format(score, lenghtOfGame, rating))   
        else:
            print("Tuloksesi on {}/{} ({:.1f} %), kohtalainen suoritus, mutta suunta ei ole kuin ylöspäin".format(score, lenghtOfGame, rating))   

    print()
    return None


main()
