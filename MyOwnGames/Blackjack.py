
#CURRENT MONEY RECORD  : $7,500
#CURRENT RECORD HOLDER : DIHAN

#PERSONAL MONEY RECORD : $42,400



import random
import sys
import os


playerMoney = 500.00

playerBet = 0
Games = 0
prefixNum = 0
suffixNum = 0
cardValue = 0
aceNum = 0
aceCheck = 0
DealerAceNum = 0
Draws = 0
DealerAceCheck = 0
playerValue = 0
dealerValue = 0
playerInput = 0
canHit = 0
prefix = " "
suffix = " "
dealerCard = " "
playerInputText = " "
smallLine = "--------------------------------------------"
line = "--------------------------------------------------------------------------------------------------------------------------------------"
blackjack = "      _____________ \n     /            /        +---    +--+            __        /------/ +---+  /---/        +---+      __        /------/  +---+  /---/ \n+---------+      /         |    \\  |  |           /  \\      /  /---/  |   | /   /         |   |     /  \\      /  /---/   |   | /   /  \n|         |     /          |    /  |  |          /    \\    |  |       |   |/   /          |   |    /    \\    |  |        |   |/   /   \n|         |    /           |   |   |  |         /      \\   |  |       |       /           |   |   /      \\   |  |        |       /    \n|         |   /            |   |   |  |        /   __   \\  |  |       |       \\           |   |  /   __   \\  |  |        |       \\    \n|         |  /             |    \\  |  |       /  /    \\  \\ |   \\_____ |   |\\   \\  ____   /    | /  /    \  \ |   \_____  |   |\   \   \n|         | /              |    /  |  +---+  /  /      \  \ \       / |   | \   \ \   \_/    / /  /      \  \ \       /  |   | \   \  \n|         |/               +---    +------+ +--+        +--+ \_____/  +---+  \---\ \________/ +--+        +--+ \_____/   +---+  \---\ \n+---------+ \n"
print(blackjack + "\nYou start with $" + str(playerMoney) + "\n")
def resetValues():
  global cardValue
  global aceNum
  global aceCheck
  global DealerAceNum
  global DealerAceCheck
  global Draws
  global playerValue
  global playerInput
  global dealerValue
  global canHit
  prefixNum = 0
  suffixNum = 0
  cardValue = 0
  aceNum = 0
  aceCheck = 0
  DealerAceNum = 0
  Draws = 0
  DealerAceCheck = 0
  playerValue = 0
  dealerValue = 0
  playerInput = 0
  canHit = 0
def Game():
  resetValues()
  global Games
  global playerBet
  global playerMoney
  global cardValue
  global aceNum
  global aceCheck
  global DealerAceNum
  global DealerAceCheck
  global Draws
  global playerValue
  global playerInput
  global canHit
  Games += 1
  if Games > 1:
    print("\n\n",line,"\n")
  def AssignCardDealer():
    global dealerValue
    global DealerAceNum
    global DealerAceCheck
    prefixNum = random.randint(1,13)
    suffixNum = random.randint(1,4)
    if prefixNum == 1:
      prefix = "Ace"
      DealerAceNum = DealerAceNum + 1
    elif prefixNum == 2:
      prefix = str(prefixNum)
    elif prefixNum == 3:
      prefix = str(prefixNum)
    elif prefixNum == 4:
      prefix = str(prefixNum)
    elif prefixNum == 5:
      prefix = str(prefixNum)
    elif prefixNum == 6:
      prefix = str(prefixNum)
    elif prefixNum == 7:
      prefix = str(prefixNum)
    elif prefixNum == 8:
      prefix = str(prefixNum)
    elif prefixNum == 9:
      prefix = str(prefixNum)
    elif prefixNum == 10:
      prefix = str(prefixNum)
    elif prefixNum == 11:
      prefix = "Jack"
    elif prefixNum == 12:
      prefix = "Queen"
    elif prefixNum == 13:
      prefix = "King"
    if suffixNum == 1:
      suffix = " of Hearts"
    elif suffixNum == 2:
      suffix = " of Clubs"
    elif suffixNum == 3:
      suffix = " of Spades"
    elif suffixNum == 4:
      suffix = " of Diamonds"
    if prefixNum <=10:
      if prefixNum != 1:
        cardValue = prefixNum
    if prefixNum >10:
      cardValue = 10
    if prefixNum == 1:
      cardValue = 11
    dealerValue += cardValue
    dealerCard = str(prefix) + suffix
    return dealerCard
  def GetCard():
    global aceNum
    global aceCheck
    global playerValue
    global Draws
    Draws = Draws + 1
    prefixNum = random.randint(1,13)
    suffixNum = random.randint(1,4)
    if prefixNum == 1:
      prefix = "Ace"
      aceNum = aceNum + 1
    elif prefixNum == 2:
      prefix = str(prefixNum)
    elif prefixNum == 3:
      prefix = str(prefixNum)
    elif prefixNum == 4:
      prefix = str(prefixNum)
    elif prefixNum == 5:
      prefix = str(prefixNum)
    elif prefixNum == 6:
      prefix = str(prefixNum)
    elif prefixNum == 7:
      prefix = str(prefixNum)
    elif prefixNum == 8:
      prefix = str(prefixNum)
    elif prefixNum == 9:
      prefix = str(prefixNum)
    elif prefixNum == 10:
      prefix = str(prefixNum)
    elif prefixNum == 11:
      prefix = "Jack"
    elif prefixNum == 12:
      prefix = "Queen"
    elif prefixNum == 13:
      prefix = "King"
    if suffixNum == 1:
      suffix = " of Hearts"
    elif suffixNum == 2:
      suffix = " of Clubs"
    elif suffixNum == 3:
      suffix = " of Spades"
    elif suffixNum == 4:
      suffix = " of Diamonds"
    if prefixNum <=10:
      if prefixNum != 1:
        cardValue = prefixNum
    if prefixNum > 10:
      cardValue = 10
    if prefixNum == 1:
      cardValue = 11
    print("You drew a " + prefix + suffix)
    return cardValue
  def FirstDealerDraw():
    print("\nThe dealer drew a " + str(AssignCardDealer()) + " and a ??? card.")
  def DealerDraw():
    global dealerValue
    print("\nThe dealer drew a " + str(AssignCardDealer()) + ".")
    print("The dealer is now on " + str(dealerValue) + ".\n")
  def DealerReveal():
    print("\nThe dealer's hidden card was a " + str(AssignCardDealer()) + ".\n")
  def action():
    playerInputText = input(smallLine + "\nWould you like to hit or stand?\n")
    print(smallLine)
    if playerInputText == "s":
      playerInput = 2
    elif playerInputText == "S":
      playerInput = 2
    elif playerInputText == "stand":
      playerInput = 2
    elif playerInputText == "Stand":
      playerInput = 2
    elif playerInputText == "STAND":
      playerInput = 2
    else:
      playerInput = 1
    return playerInput
  def stand():
    global dealerValue
    global playerValue
    global playerBet
    global playerMoney
    DealerReveal()
    if dealerValue > playerValue:
      playerMoney = playerMoney - playerBet
      print("The dealer had " + str(dealerValue - playerValue) + " more than you!\nYou now have $" + str(playerMoney))
      Game()
    if dealerValue <= 21:
      if dealerValue < 17:
        StandDealerFunction()
      else:
        if dealerValue < playerValue:
          playerMoney = playerMoney + playerBet
          print("The dealer is on " + str(dealerValue) + " and isn't able to hit! You win!\nYou now have $" + str(playerMoney))
        elif dealerValue == playerValue:
          print("Push!")
        else:
          playerMoney = playerMoney - playerBet
          print("The dealer had " + str(dealerValue - playerValue) + " more than you!\nYou now have $" + str(playerMoney))
        Game()
    else:
      playerMoney = playerMoney - playerBet
      print("The dealer went over 21! You won!\nYou now have $" + str(playerMoney))
      Game()
  def setBet():
    global playerBet
    global playerMoney


    if playerMoney > 0:
      playerBet = input("Enter bet: $")               # money entered
      try:
        playerBet = int(playerBet)
      except:
        print("Please input a real amount!")
        setBet()
      else:
        playerBet = int(playerBet)
    else:
      print("You're out of money!\n")
      print(line,"\n",blackjack)
      sys.exit()
    if playerBet <= 0:
      print("You cannot bet negative numbers, or bet nothing!")
      setBet()
    if playerBet > playerMoney:
      print("You cannot bet more than you have!")
      setBet()
  setBet()
  playerValue = playerValue + GetCard()
  playerValue = playerValue + GetCard()
  if playerValue == 21:
    print('\nYou drew Blackjack!\n')
    playerMoney = playerMoney + playerBet
    print("You have $" + str(playerMoney))
    Game()
  if playerValue > 21:
        if aceCheck != aceNum:
          aceCheck = aceCheck + 1
          if playerValue > 21:
            playerValue = playerValue - 10
  print("You are now on " + str(playerValue) + " points")
  FirstDealerDraw()
  def hit():
    global playerValue
    global aceNum
    global aceCheck
    global playerBet
    global playerMoney
    playerValue = playerValue + GetCard()
    if playerValue == 21:
      print('\nYou drew Blackjack!\n')
      playerMoney = playerMoney + playerBet
      print("You now have $" + str(playerMoney))
      Game()
    if playerValue > 21:
        if aceCheck != aceNum:
          aceCheck = aceCheck + 1
          if playerValue > 21:
            playerValue = playerValue - 10
    if playerValue > 21:
      if aceNum != 1:
        print("You hit to over 21. You have " + str(playerValue) + " points and " + str(aceNum) + " Aces.")
      else:
        print("You hit to over 21. You have " + str(playerValue) + " points and " + str(aceNum) + " Ace.")
      playerMoney = playerMoney - playerBet
      print("\nYou now have $" + str(playerMoney))
      Game()
    else:
      print("You are now on " + str(playerValue) + " points")
  def StandDealerFunction():
    global dealerValue
    global playerValue
    global DealerAceCheck
    global DealerAceNum
    global playerBet
    global playerMoney
    if dealerValue < 17:
      DealerDraw()
    else:
      playerMoney = playerMoney + playerBet
      print("Your score was " + str(playerValue - dealerValue) + " more than the dealer's\nYou now have $" + str(playerMoney))
      Game()
    if dealerValue > 21:
       if DealerAceCheck != DealerAceNum:
          DealerAceCheck = DealerAceCheck + 1
          if dealerValue > 21:
            dealerValue = dealerValue - 10
            print("But they had an ace! So their score is now " + str(dealerValue))
            StandDealerFunction()
       else:
         playerMoney = playerMoney + playerBet
         print("The dealer went over 21! You won!\nYou now have $" + str(playerMoney))
         Game()
    elif dealerValue == playerValue:
      print("Push! You don't win or lose.")
      Game()
    else:
      if dealerValue > playerValue:
        playerMoney = playerMoney - playerBet
        print("The dealer drew to more than you!\nYou now have $" + str(playerMoney))
        Game()
      else:
        StandDealerFunction()
  while canHit == 0:
    if action() == 1:
      hit()
    else:
      canHit = 1
      stand()
Game()
