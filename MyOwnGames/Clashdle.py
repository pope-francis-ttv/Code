#                HIT CONTROL + ENTER TO PLAY, OR THE PLAY BUTTON IN THE TOP LEFT
#
#                YOU MAY NEED TO WAIT THE FIRST TIME YOU PLAY, AS RUNTIME CONNECTION IS SLOW INITIALLY
#
#                THE GAME NOW AUTOMATICALLY PLAYS AGAIN IF YOU GET THE CARD RIGHT
#
#                ALTERNATE SPELLINGS ARE NOW PERMITTED (EG: EBARBS, SKARMY)
#
#                THERE ARE MULTIPLE CARDS THAT FIT SOME CATEGORIES:
#                IF EVERY OPTION IS GREEN, THE ANSWER IS ANOTHER CARD THAT FITS ALL OF THOSE CATEGORIES





#  git config --global user.email "you@example.com"
#  git config --global user.name "Your Name"














import os
import sys
import random
import time

def returner():
    global guess
    global guessAmount
    global e
    global r
    global typ
    global evo
    global ac
    global ar
    global ae
    global at
    global atarg
    global targ
    g  = "    Ground    "
    ag = "Air and Ground"
    b  = "   Buildings  "
    n  = "     N/A      "
    if guess == 'little prince':
      e = 3
      r = 5
      typ = 1
      evo = False
      targ = ag
    if guess == 'golden knight':
      e = 4
      r = 5
      typ = 1
      evo = False
      targ = g
    if guess == 'skeleton king':
      e =4
      r = 5
      typ = 1
      evo = False
      targ = g
    if guess == 'mighty miner':
      e = 4
      r = 5
      typ = 1
      evo = False
      targ = g
    if guess == 'archer queen':
      e = 5
      r = 5
      typ = 1
      evo = False
      targ = ag
    if guess == 'goblinstein':
      e = 5
      r = 5
      typ = 1
      evo = False
      targ = ag
    if guess == 'monk':
      e = 5
      r = 5
      typ = 1
      evo = False
      targ = g
    if guess == 'boss bandit':
      e = 6
      r = 5
      typ = 1
      evo = False
      targ = g

    if guess == 'the log':
      e = 2
      r = 4
      typ = 3
      evo = False
      targ = g
    if guess == 'miner':
      e = 3
      r = 4
      typ = 1
      evo = False
      targ = g
    if guess == 'princess':
      e = 3
      r = 4
      typ = 1
      evo = False
      targ = ag
    if guess == 'ice wizard':
      e = 3
      r = 4
      typ = 1
      evo = False
      targ = ag
    if guess == 'royal ghost':
      e = 3
      r = 4
      typ = 1
      evo = True
      targ = g
    if guess == 'bandit':
      e = 3
      r = 4
      typ = 1
      evo = False
      targ = g
    if guess == 'fisherman':
      e = 3
      r = 4
      typ = 1
      evo = False
      targ = g
    if guess == 'ewiz':
      guess == 'electro wizard'
    if guess == 'electro wizard':
      e = 4
      r = 4
      typ = 1
      evo = False
      targ = ag
    if guess == 'inferno dragon':
      e = 4
      r = 4
      typ = 4
      evo = True
      targ = ag
    if guess == 'phoenix':
      e = 4
      r = 4
      typ = 4
      evo = False
      targ = ag
    if guess == 'magic archer':
      e = 4
      r = 4
      typ = 1
      evo = False
      targ = ag
    if guess == 'lumberjack':
      e = 4
      r = 4
      targ = g
      typ = 1
      evo = True
    if guess == 'night witch':
      e = 4
      r = 4
      typ = 1
      targ = g
      evo = False
    if guess == 'mother witch':
      e = 4
      r = 4
      targ = ag
      typ = 1
      evo = False
    if guess == 'ram rider':
      e = 5
      r = 4
      typ = 1
      targ = b
      evo = False
    if guess == 'graveyard':
      e = 5
      r = 4
      typ = 3
      targ = g
      evo = False
    if guess == 'goblin machine':
      e = 5
      r = 4
      typ = 1
      targ = ag
      evo = False
    if guess == 'sparky':
      e = 6
      r = 4
      typ = 1
      targ = g
      evo = False
    if guess == 'spirit empress':
      e = 6
      r = 4
      typ = 4
      targ = ag
      evo = False
    if guess == 'mega knight':
      e = 7
      r = 4
      typ = 1
      targ = g
      evo = True
    if guess == 'lava hound':
      e = 7
      r = 4
      typ = 4
      targ = b
      evo = False

    if guess == 'mirror':
      e = 0
      r = 3
      typ = 3
      targ = n
      evo = False

    if guess == 'barb barrel':
      guess = 'barbarian barrel'
    if guess == 'barbarian barrel':
      e = 2
      r = 3
      targ = g
      typ = 3
      evo = False
    if guess == 'wall breakers':
      e = 2
      r = 3
      typ = 1
      targ = b
      evo = True
    if guess == 'goblin curse':
      e =2
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'rage':
      e = 2
      r = 3
      targ = ag
      typ = 3
      evo = False
    if guess == 'gob barrel':
      guess = "goblin barrel"
    if guess == 'goblin barrel':
      e = 3
      r = 3
      typ = 3
      targ = g
      evo = True
    if guess == 'guards':
      e = 3
      r = 3
      targ = g
      typ = 1
      evo = False
    if guess == 'scarmy':
      guess = 'skeleton army'
    if guess == 'skarmy':
      guess = 'skeleton army'
    if guess == 'skeleton army':
      e = 3
      r = 3
      targ = g
      typ = 1
      evo = True
    if guess == 'vines':
      e = 3
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'clone':
      e = 3
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'tornado':
      e = 3
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'void':
      e = 3
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'baby dragon':
      e = 4
      r = 3
      targ = ag
      typ = 4
      evo = True
    if guess == 'dark prince':
      e = 4
      r = 3
      typ = 1
      targ = g
      evo = False
    if guess == 'freeze':
      e = 4
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'poison':
      e = 4
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'rune giant':
      e = 4
      r = 3
      typ = 1
      targ = b
      evo = False
    if guess == 'hunter':
      e = 4
      r = 3
      typ = 1
      targ = ag
      evo = True
    if guess == 'goblin drill':
      e = 4
      r = 3
      typ = 2
      targ = g
      evo = True
    if guess == 'witch':
      e = 5
      r = 3
      typ = 1
      targ = ag
      evo = True
    if guess == 'balloon':
      e = 5
      r = 3
      typ = 4
      targ = b
      evo = False
    if guess == 'prince':
      e = 5
      r = 3
      typ = 1
      targ = g
      evo = False
    if guess == 'electro dragon':
      e = 5
      r = 3
      typ = 4
      targ = ag
      evo = True
    if guess == 'bowler':
      e = 5
      r = 3
      typ = 1
      targ = g
      evo = False
    if guess == 'executioner':
      e = 5
      r = 3
      typ = 1
      targ = ag
      evo = True
    if guess == 'cannon cart':
      e = 5
      r = 3
      typ = 1
      targ = g
      evo = False
    if guess == 'giant skeleton':
      e = 6
      r = 3
      typ = 1
      targ = g
      evo = False
    if guess == 'lightning':
      e = 6
      r = 3
      typ = 3
      targ = ag
      evo = False
    if guess == 'goblin giant':
      e = 6
      r = 3
      typ = 1
      targ = b
      evo = True
    if guess == 'x bow':
      guess = 'x-bow'
    if guess == 'xbow':
      guess = 'x-bow'
    if guess == 'x-bow':
      e = 6
      r = 3
      typ = 2
      targ = g
      evo = False
    if guess == 'pekka':
      guess = 'p.e.k.k.a'
    if guess == 'p.e.k.k.a':
      e = 7
      r = 3
      typ = 1
      targ = g
      evo = True
    if guess == 'electro giant':
      e = 7
      r = 3
      typ = 1
      targ = b
      evo = False
    if guess == 'golem':
      e = 8
      r = 3
      typ = 1
      targ = b
      evo = False


    if guess == 'heal spirit':
      e = 1
      r = 2
      typ = 1
      targ = ag
      evo = False
    if guess == 'ice golem':
      e = 2
      r = 2
      typ = 1
      targ = b
      evo = False
    if guess == 'suspicious bush':
      e = 2
      r = 2
      typ = 1
      targ = b
      evo = False
    if guess == 'tombstone':
      e = 3
      r = 2
      typ = 2
      targ = g
      evo = False
    if guess == 'mega minion':
      e = 3
      r = 2
      typ = 4
      targ = ag
      evo = False
    if guess == 'dart goblin':
      e = 3
      r = 2
      typ = 1
      targ = ag
      evo = True
    if guess == 'eq':
      guess = 'earthquake'
    if guess == 'earthquake':
      e = 3
      r = 2
      typ = 3
      targ = g
      evo = False
    if guess == 'elixir golem':
      e = 3
      r = 2
      typ = 1
      targ = b
      evo = False
    if guess == 'fireball':
      e = 4
      r = 2
      typ = 3
      targ = ag
      evo = False
    if guess == 'mini pekka':
      guess = 'mini p.e.k.k.a'
    if guess == 'mini p.e.k.k.a':
      e = 4
      r = 2
      typ = 1
      targ = g
      evo = False
    if guess == 'musketeer':
      e = 4
      r = 2
      typ = 1
      targ = ag
      evo = True
    if guess == 'diddy cage':
      guess = 'goblin cage'
    if guess == 'goblin cage':
      e = 4
      r = 2
      typ = 2
      targ = g
      evo = True
    if guess == 'goblin hut':
      e = 4
      r = 2
      targ = ag
      typ = 2
      evo = False
    if guess == 'valk':
      guess = 'valkyrie'
    if guess == 'valkyrie':
      e = 4
      r = 2
      typ = 1
      targ = g
      evo = True
    if guess == 'battle ram':
      e = 4
      r = 2
      typ = 1
      targ = b
      evo = True
    if guess == 'bomb tower':
      e = 4
      r = 2
      typ = 2
      targ = g
      evo = False
    if guess == 'flying machine':
      e = 4
      r = 2
      typ = 4
      targ = ag
      evo = False
    if guess == 'hog rider':
      e = 4
      r = 2
      typ = 1
      evo = False
      targ = b
    if guess == 'battle healer':
      e = 4
      r = 2
      typ = 1
      evo = False
      targ = g
    if guess == 'furnace':
      e = 4
      r = 2
      typ = 1
      evo = True
      targ = ag
    if guess == 'zappies':
      e = 4
      r = 2
      typ = 1
      evo = False
      targ = ag
    if guess == 'goblin demolisher':
      e = 4
      r = 2
      typ = 1
      targ = g
      evo = False
    if guess == 'giant':
      e = 5
      r = 2
      typ = 1
      targ = b
      evo = False
    if guess == 'inferno tower':
      e = 5
      r = 2
      typ = 2
      targ = ag
      evo = False
    if guess == 'wizard':
      e = 5
      r = 2
      typ = 1
      targ = ag
      evo = True
    if guess == 'royal hogs':
      e = 5
      r = 2
      typ = 1
      targ = b
      evo = True
    if guess == 'rocket':
      e = 6
      r = 2
      typ = 3
      targ = ag
      evo = False
    if guess == 'barb hut':
      guess = 'barbarian hut'
    if guess == 'barbarian hut':
      e = 6
      r = 2
      typ = 2
      targ = g
      evo = False
    if guess == 'elixer pump':
      guess = 'elixer collector'
    if guess == 'elixir collector':
      e = 6
      r = 2
      typ = 2
      targ = n
      evo = False
    if guess == 'three musketeers':
      e = 9
      r = 2
      typ = 1
      targ = ag
      evo = False

    if guess == 'skellies':
      guess == 'skeletons'
    if guess == 'larry':
      guess == 'skeletons'
    if guess == 'skellys':
      guess == 'skeletons'
    if guess == 'skeletons':
      e = 1
      r = 1
      typ = 1
      targ = g
      evo = True
    if guess == 'electro spirit':
      e = 1
      r = 1
      typ = 1
      targ = ag
      evo = False
    if guess == 'fire spirit':
      e = 1
      r = 1
      typ = 1
      targ = ag
      evo = False
    if guess == 'ice spirit':
      e = 1
      r = 1
      typ = 1
      targ = ag
      evo = True
    if guess == 'goblins':
      e = 2
      r = 1
      targ = g
      typ = 1
      evo = False
    if guess == 'spear goblins':
      e = 2
      r = 1
      typ = 1
      targ = ag
      evo = False
    if guess == 'bomber':
      e = 2
      r = 1
      typ = 1
      targ = g
      evo = True
    if guess == 'bats':
      e = 2
      r = 1
      targ = ag
      typ = 4
      evo = True
    if guess == 'zap':
      e = 2
      r = 1
      typ = 3
      targ = ag
      evo = True
    if guess == 'snowball':
      guess = 'giant snowball'
    if guess == 'giant snowball':
      e = 2
      r = 1
      typ = 3
      targ = ag
      evo = True
    if guess == 'berserker':
      e = 2
      r = 1
      typ = 1
      targ = g
      evo = False
    if guess == 'archers':
      e = 3
      r = 1
      targ = ag
      typ = 1
      evo = True
    if guess == 'arrows':
      e = 3
      r = 1
      typ = 3
      targ = ag
      evo = False
    if guess == 'knight':
      e = 3
      r = 1
      typ = 1
      targ = g
      evo = True
    if guess == 'minions':
      e = 3
      r = 1
      typ = 4
      targ = ag
      evo = False
    if guess == 'cannon':
      e = 3
      r = 1
      typ = 2
      targ = g
      evo = True
    if guess == 'goblin gang':
      e = 3
      r = 1
      typ = 1
      evo = False
      targ = ag
    if guess == 'skeleton barrel':
      e = 3
      r = 1
      typ = 4
      targ = b
      evo = True
    if guess == 'firecracker':
      e = 3
      r = 1
      typ = 1
      targ = ag
      evo = True
    if guess == 'royal delivery':
      e = 3
      r = 1
      typ = 3
      targ = ag
      evo = False
    if guess == 'skeleton dragons':
      e = 4
      r = 1
      typ = 4
      targ = ag
      evo = False
    if guess == 'mortar':
      e = 4
      r = 1
      typ = 2
      targ = g
      evo = True
    if guess == 'tesla':
      e = 4
      r = 1
      typ = 2
      targ = ag
      evo = True
    if guess == 'barbs':
      guess = 'barbarians'
    if guess == 'barbarians':
      e = 5
      r = 1
      typ = 1
      targ = g
      evo = True
    if guess == 'minion horde':
      e = 5
      r = 1
      typ = 4
      targ = ag
      evo = False
    if guess == 'rascals':
      e = 5
      r = 1
      typ = 1
      evo = False
      targ = ag
    if guess == 'royal giant':
      e = 6
      r = 1
      typ = 1
      targ = b
      evo = True
    if guess == 'ebarbs':
      guess = 'elite barbarians'
    if guess == 'e barbs':
      guess = 'elite barbarians'
    if guess == 'elite barbarians':
      e = 6
      r = 1
      typ = 1
      targ = g
      evo = False
    if guess == 'royal recruits':
      e = 7
      r = 1
      typ = 1
      targ = g
      evo = True

    if guessAmount == 0:
      ar = r
      ae = e
      at = typ
      ac = evo
      atarg = targ
    else:
      if guess == answer:
          clear()
          print(guessbank)
          print(f"You got it!! The card was {answer.title()}!\n\n")
          game()
          pass
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def guessdef():
  global l
  global t
  global e
  global r
  global targ
  global typ
  global evo
  global evotxt
  global guessbank
  global guessAmount
  global answer
  global cards
  global real_cards
  global red
  global green
  global guess
  global ae #elixer
  global ac #has an evo
  global ar #rarity
  global at #type
  global atarg
  if guessAmount == 6:
    guess = input(f"Enter your last guess: ").lower().strip()
  else:
    guess = input(f"Enter guess {guessAmount}: ").lower().strip()
  if guess == answer:
    clear()
    print(guessbank)
    print(f"You got it!! The card was {answer.title()}!\n\n")
    game()
    pass
  elif guess not in cards:
    if guess == "cards":
      print(real_cards)
    else:
      print("\nThis card input is not valid!\nPlease re-input your guess, or type 'Cards' to get a list of valid cards (inputs are not case-sensitive)")
    guessdef()
    return
  else:
    returner()



  xe = ["↑", "↓","\033[1;32m "]
  xtyp = ["\033[1;32m" , "\033[1;31m"]

  xxe = ""
  xxr = ""
  xxtyp = ""
  xxevo = ""


  if ae < e:
    xxe = xe[1]
  elif ae > e:
    xxe = xe[0]
  else:
    xxe = xe[2]

  if ar < r:
    xxr = xe[1]
  elif ar > r:
    xxr = xe[0]
  else:
    xxr = xe[2]

  if atarg == targ:
    xxtarg = xtyp[0]
  else:
    xxtarg = xtyp[1]

  if at == typ:
    xxtyp = xtyp[0]
  else:
    xxtyp = xtyp[1]
  if ac == evo:
    xxevo = xtyp[0]
  else:
    xxevo = xtyp[1]

  evotxt = enumer()
  guessbank = (f"{guessbank}\n | {xxe}{e}\033[0m | {xxr}{r}\033[0m | {xxtyp}{typ}\033[0m | {xxtarg}{targ}\033[0m | {xxevo}{evotxt}\033[0m| {guess.title()}\033[0m \n{l}")

def enumer():
  global r
  global typ
  global evo
  global ae
  global ac
  global ar
  global at
  if r == 1:
    r = " Common  "
  elif r == 2:
    r = "  Rare   "
  elif r == 3:
    r = "  Epic   "
  elif r == 4:
    r = "Legendary"
  else:
    r = " Champion"
  if typ == 1:
    typ = "Ground Troop"
  elif typ == 2:
    typ = "  Building  "
  elif typ == 3:
    typ = "   Spell    "
  elif typ == 4:
    typ = "Flying troop"
  if evo:
    evotxtreturn = " Has an Evolution  "
  else:
    evotxtreturn = "Doesn't have an Evo"
  return evotxtreturn


cards = [
'little prince', 'golden knight', 'skeleton king', 'mighty miner', 'archer queen', 'goblinstein', 'monk', 'boss bandit',
 'the log', 'miner', 'princess', 'ice wizard', 'royal ghost', 'bandit', 'fisherman', 'electro wizard', 'inferno dragon', 'phoenix', 'magic archer', 'lumberjack', 'night witch', 'mother witch', 'ram rider', 'graveyard', 'goblin machine', 'sparky', 'spirit empress', 'mega knight', 'lava hound',
 'mirror', 'barbarian barrel', 'wall breakers', 'goblin curse', 'rage', 'goblin barrel', 'guards', 'skeleton army', 'vines', 'clone', 'tornado', 'void', 'baby dragon', 'dark prince', 'freeze', 'poison', 'rune giant', 'hunter', 'goblin drill', 'witch', 'balloon', 'prince', 'electro dragon', 'bowler', 'executioner', 'cannon cart', 'giant skeleton', 'lightning', 'goblin giant', 'xbow', 'pekka', 'electro giant', 'golem',
 'heal spirit', 'ice golem', 'suspicious bush', 'tombstone', 'mega minion', 'dart goblin', 'earthquake', 'elixir golem', 'fireball', 'mini pekka', 'musketeer', 'goblin cage', 'goblin hut', 'valkyrie', 'battle ram', 'bomb tower', 'flying machine', 'hog rider', 'battle healer', 'furnace', 'zappies', 'goblin demolisher', 'giant', 'inferno tower', 'wizard', 'royal hogs', 'rocket', 'barbarian hut', 'elixir collector', 'three musketeers',
 'skeletons', 'electro spirit', 'fire spirit', 'ice spirit', 'goblins', 'spear goblins', 'bomber', 'bats', 'zap', 'giant snowball', 'berserker', 'archers', 'arrows', 'knight', 'minions', 'cannon', 'goblin gang', 'skeleton barrel', 'firecracker', 'royal delivery', 'skeleton dragons', 'mortar', 'tesla', 'barbarians', 'minion horde', 'rascals', 'royal giant', 'elite barbarians', 'royal recruits',
 'skarmy', 'scarmy', 'mini p.e.k.k.a', 'eq', 'x bow','xbow', 'p.e.k.k.a', 'ebarbs', 'e barbs', 'barb barrel', 'skellies', 'larry', 'barb hut', 'elixer pump', 'diddy cage', 'barbs', 'valk', 'snowball', 'skellys', 'ewiz','gob barrel',
]

real_cards = [
 'little prince', 'golden knight', 'skeleton king', 'mighty miner', 'archer queen', 'goblinstein', 'monk', 'boss bandit',
 'the log', 'miner', 'princess', 'ice wizard', 'royal ghost', 'bandit', 'fisherman', 'electro wizard', 'inferno dragon', 'phoenix', 'magic archer', 'lumberjack', 'night witch', 'mother witch', 'ram rider', 'graveyard', 'goblin machine', 'sparky', 'spirit empress', 'mega knight', 'lava hound',
 'mirror', 'barbarian barrel', 'wall breakers', 'goblin curse', 'rage', 'goblin barrel', 'guards', 'skeleton army', 'vines', 'clone', 'tornado', 'void', 'baby dragon', 'dark prince', 'freeze', 'poison', 'rune giant', 'hunter', 'goblin drill', 'witch', 'balloon', 'prince', 'electro dragon', 'bowler', 'executioner', 'cannon cart', 'giant skeleton', 'lightning', 'goblin giant', 'x-bow', 'p.e.k.k.a', 'electro giant', 'golem',
 'heal spirit', 'ice golem', 'suspicious bush', 'tombstone', 'mega minion', 'dart goblin', 'earthquake', 'elixir golem', 'fireball', 'mini p.e.k.k.a', 'musketeer', 'goblin cage', 'goblin hut', 'valkyrie', 'battle ram', 'bomb tower', 'flying machine', 'hog rider', 'battle healer', 'furnace', 'zappies', 'goblin demolisher', 'giant', 'inferno tower', 'wizard', 'royal hogs', 'rocket', 'barbarian hut', 'elixir collector', 'three musketeers',
 'skeletons', 'electro spirit', 'fire spirit', 'ice spirit', 'goblins', 'spear goblins', 'bomber', 'bats', 'zap', 'giant snowball', 'berserker', 'archers', 'arrows', 'knight', 'minions', 'cannon', 'goblin gang', 'skeleton barrel', 'firecracker', 'royal delivery', 'skeleton dragons', 'mortar', 'tesla', 'barbarians', 'minion horde', 'rascals', 'royal giant', 'elite barbarians', 'royal recruits']
t = "  Cost   Rarity      Type            Targets          Evolution            Name"
l = " +----+------------+--------------+----------------+--------------------+--------------"
e = 0
r = ""
typ = ""
evo = False
ac = 0
ar = 0
at = 0
ae = 0
def game():
  global guessbank
  global answer
  global guess
  global guessAmount
  guessAmount = 0
  guessbank = (f"{t}\n{l}")
  answer = random.choice(real_cards)
  guess = answer
  returner()
  while guessAmount < 7:
      if guessAmount != 0:
       clear()
      guessAmount += 1
      print(guessbank)
      if guessAmount >= 7:
        print(f"You're out of guesses!! The card was {answer.title()}\n\n")
        game()
        pass
      guessdef()
game()