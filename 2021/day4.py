f = open('day4.txt')
lines = f.readlines()
f.close()

numbersCalled = [int(s) for s in lines[0].split(',')]

numBoards = int((len(lines)-1)/6)
print(numBoards)
boards=[]
for b in range(0, numBoards):
  boardData = lines[6*b+2:6*b+7]
  board = [line.replace('  ',' ').strip().split(' ') for line in boardData]
  for i in range(0, 5):
    board[i] = [int(x) for x in board[i]]
  boards.append(board)

marked = [[[False]*5 for j in range(0, 5)] for b in range(0, numBoards)]

def printBoard(b):
  for j in range(0, 5):
    print(b[j])

scores = []
hasWonYet = [False]*numBoards

for call in numbersCalled:
  # print(call)

  # mark this number on any board
  for b in range(0, numBoards):
    if hasWonYet[b]: continue

    for i in range(0, 5):
      for j in range(0, 5):
        if(boards[b][j][i] == call):
          marked[b][j][i] = True

    # look for a winning row/column
    anyWinningLine = False
    for row in range(0, 5):
      if anyWinningLine: break
      won = True
      for i in range(0, 5):
        won = won and marked[b][row][i]
      anyWinningLine = anyWinningLine or won
    for col in range(0, 5):
      if anyWinningLine: break
      won = True
      for j in range(0, 5):
        won = won and marked[b][j][col]
      anyWinningLine = anyWinningLine or won

    if anyWinningLine:
      # calculate score
      s = 0
      for i in range(0, 5):
        for j in range(0, 5):
          if not marked[b][j][i]:
            s += boards[b][j][i]
      hasWonYet[b] = True
      scores.append((b, s * call))

print("First winner: {}, score= {}".format(scores[0][0], scores[0][1]))
print("Last winner: {}, score= {}".format(scores[-1][0], scores[-1][1]))

