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