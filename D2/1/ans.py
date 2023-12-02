colors = ['red', 'green', 'blue']
# Max number of each color in a draw
maxInDraws = [12, 13, 14]

def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def separateDraws(game: str):
    game = game[8:]
    draws = game.split(';')
    colours = []
    for draw in draws:
        colours.append([x for x in draw.split(',') if x])
    for col in colours:
        for i in range(len(col)):
            col[i] = col[i].replace('\n', '')
            col[i] = [x for x in col[i].split(' ') if x]
    return colours

def checkDraw(draw: list):
    for numColor in draw:
      if numColor[1][0] == 'r':
        if int(numColor[0]) > maxInDraws[0]:
          return False
      elif numColor[1][0] == 'g':
        if int(numColor[0]) > maxInDraws[1]:
          return False
      elif numColor[1][0] == 'b':
        if int(numColor[0]) > maxInDraws[2]:
          return False
    return True

def main():
    games = parser()
    parsedGames = []
    for game in games:
        parsedGames.append(separateDraws(game))

    ans = []
    gameNum = 1
    for game in parsedGames:
        valid = True
        for draw in game:
            if not checkDraw(draw):
                valid = False
                break
        if valid:
            ans.append(gameNum)
        gameNum += 1
    return sum(ans)
           


print(main())