import requests,random,hashlib,traceback
def btcPriceGet():
  price = 0
  key = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
  r = requests.get(key)
  data = r.json()["result"]["XXBTZUSD"]["c"]
  price = round(float(data[0]))
  return price

def colorText(word, color):
  if color=="red":
    print("\33[31m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="green":
    print("\33[32m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="yellow":
    print("\33[33m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="blue":
    print("\33[34m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="magenta":
    print("\33[35m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="cyan":
    print("\33[36m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  elif color=="white":
    print("\33[37m", word, sep="", end="")
    print("\33[0m", sep="", end="")
  else:
    print(word, sep="", end="")

def animalEmoji(animal):
  if animal == "cat":
    return "ðą"
  elif animal == "dog":
    return "ð"
  elif animal == "mouse":
    return "ð­"
  elif animal == "cow":  
    return "ðŪ"
  elif animal == "horse":
    return "ð" 
  elif animal == "sheep":
    return "ð"
  elif animal == "snake":
    return "ð"
  elif animal == "bird":
    return "ðĶĪ"
  elif animal == "fish":
    return "ð"
  elif animal == "monkey":
    return "ð"
  elif animal == "rabbit":
    return "ð"
  elif animal == "goat":
    return "ð"
  elif animal == "pig":
    return "ð―"
  elif animal == "turtle":
    return "ðĒ"
  elif animal == "penguin":
    return "ð§"
  else:
    return "error"

def rNum(x,y):
  return random.randint(x,y)

def s256(s):
  return hashlib.sha256(s.encode()).hexdigest()
  
def prettyPrint(list,color):
  for row in list:
    for item in row:
      print(f"{cConvert(color)}{item: ^10}", end=" | \33[0m")
    print()
    
def cConvert(color):
  if color=="red":
    return "\33[31m"
  elif color=="green":
    return "\33[32m"
  elif color=="yellow":
    return "\33[33m"
  elif color=="blue":
    return "\33[34m"
  elif color=="magenta":
    return "\33[35m"
  elif color=="cyan":
    return "\33[36m"
  elif color=="white":
    return "\33[37m"
  elif color==None:
    return "\33[0m"
  else:
    return "\33[0m"

def trace():
  return f"Error: {traceback.format_exc()}"

def saveList(fileName, list):
  with open(fileName, "w") as f:
    for subArray in list:
     f.write(' '.join(map(str,subArray)) + '\n')

def loadList(fileName):
  l = []
  with open(fileName, "r") as f:
    for line in f:
      l.append(line.split())
    return l