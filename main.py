import random
def spel() :

  Pogingen = 6

  def drawgalgjes():
    if Pogingen == 5:
        print("Jammer, je hebt nog 4 pogingen over")
        print("""     ____
      | \|
      o  |
         |
         |
         |
    _____|""")

    if Pogingen == 4:
        print("Jammer, je hebt nog 3 pogingen over")
        print("""     ____
      | \|
      o  |
      |  |
         |
         |
    _____|""")

    if Pogingen == 3:
        print("Jammer, je hebt nog 2 pogingen over")
        print("""     ____
      | \|
      o  |
     /|\ |
         |
         |
    _____|""")

    if Pogingen == 2:
        print("je hebt nog 1 pogingen over")
        print("""     ____
      | \|
      o  |
     /|\ |
     / \ |
         |
    _____|""")

    if Pogingen == 1:
        print("""     ____
      | \|
      o  |
     /|\ |
     / \ |
         |
    _____|""")

           print("Je hebt verloren! Het woord was:" + GeheimWoord)
        print("Je kan het nog een keer proberen, type ja of nee")


 woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

  MogelijkeLetters = "a", "b", "c", "d", "", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"

    
  GeheimWoord= random.choice(woordenlijst)
  lengtewoord = len(GeheimWoord)
  streepjes = [" - "] *lengtewoord
  ja = "ja"
  nee = "nee"
 

  game = True

  print("Raad de letters en als je het woord weet typ het dan in.")
  print()
  print("het woord heeft " + str(lengtewoord) + " letters")