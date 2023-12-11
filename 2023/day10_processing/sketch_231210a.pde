import java.util.Arrays;

class Coord {
  public int x;
  public int y;
  Coord(int yy, int xx) {
    x=xx;
    y=yy;
  }

  @Override
    public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Coord that = (Coord) o;
    return this.x == that.x && this.y == that.y;
  }
}

Coord coord(int y, int x) {
  return new Coord(y, x);
}

String[] input;
boolean[][] isVisited;
ArrayList<Coord> frontier; //list of [y,x] pairs




char grid(int y, int x) {
  return input[y].charAt(x);
}


void print_frontier() {
  print("Frontier: ");
  frontier.forEach(coord-> {
    print(coord.y, coord.x);
  }
  );
}

int OFFSETX = 5;
int OFFSETY = 20;
int FONT_SIZE = 6;
  
void drawBase() {
  background(0);
  fill(70);
  //text(String.join("\n", input), OFFSETX, OFFSETY);
}

void drawState() {
  fill(0,0,0,3);
  square(0, 0, 2000);

  fill(255);
  frontier.forEach(coord ->{
    char c = grid(coord.y, coord.x);
    text(c, OFFSETX+coord.x*FONT_SIZE, OFFSETY+coord.y*FONT_SIZE);
  });
}

void setup() {
  //TEST INPUT
  //input = loadStrings("input_test");
  //size(400, 400);
  //PFont mono  = createFont("ComicMono", 16);

  // REAL INPUT
  input = loadStrings("input");
  size(900,1200);
  PFont mono  = createFont("ComicMono", FONT_SIZE);

  textFont(mono);
  frameRate(10000);

  print(input.length, input[0].length());
  isVisited = new boolean[input.length][input[0].length()];
  frontier = new ArrayList<Coord>();

  //@@@ FIND S
  boolean s_found = false;
  for (int j=0; j<input.length && !s_found; j++) {
    for (int i=0; i<input[0].length() && !s_found; i++) {
      if (grid(j, i) == 'S') {
        frontier.add(coord(j, i));
        isVisited[j][i] = true;
        s_found = true;
      }
    }
  }
  drawBase();
}


boolean STABLE_STATE = false;
int iters=0;


ArrayList<Coord> cellsConnectedTo(Coord coord) {
  if (coord.x<0 || coord.x>=input[0].length() || coord.y<0 || coord.y>=input.length) {
    return new ArrayList<Coord>();
  }
  char pipeShape = grid(coord.y, coord.x);

  if (pipeShape == '|') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y-1, coord.x),
      coord(coord.y+1, coord.x)
      ));
  } else if (pipeShape == '-') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y, coord.x-1),
      coord(coord.y, coord.x+1)
      ));
  } else if (pipeShape == 'L') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y-1, coord.x),
      coord(coord.y, coord.x+1)
      ));
  } else if (pipeShape == 'J') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y-1, coord.x),
      coord(coord.y, coord.x-1)
      ));
  } else if (pipeShape == '7') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y+1, coord.x),
      coord(coord.y, coord.x-1)
      ));
  } else if (pipeShape == 'F') {
    return new ArrayList<>(Arrays.asList(
      coord(coord.y+1, coord.x),
      coord(coord.y, coord.x+1)
      ));
  } else if (pipeShape == 'S') {
    var res = new ArrayList<Coord>();
    if (cellsConnectedTo(coord(coord.y-1, coord.x)).contains(coord)) {
      res.add(coord(coord.y-1, coord.x));
    }
    if (cellsConnectedTo(coord(coord.y+1, coord.x)).contains(coord)) {
      res.add(coord(coord.y+1, coord.x));
    }
    if (cellsConnectedTo(coord(coord.y, coord.x-1)).contains(coord)) {
      res.add(coord(coord.y, coord.x-1));
    }
    if (cellsConnectedTo(coord(coord.y, coord.x+1)).contains(coord)) {
      res.add(coord(coord.y, coord.x+1));
    }
    return res;
  } else { //'.'
    return new ArrayList<Coord>();
  }
}


void iterate() {
  var newFrontier = new ArrayList<Coord>();
  STABLE_STATE = true;

  frontier.forEach(coord -> {
    ArrayList<Coord> adjs = cellsConnectedTo(coord);

    adjs.forEach(adj -> {
      if (!isVisited[adj.y][adj.x]) {
        isVisited[adj.y][adj.x] = true;
        newFrontier.add(adj);
        STABLE_STATE = false;
      }
    }
    );
  }
  );
  frontier = newFrontier;
  if (STABLE_STATE) {
    print("DONE IN "+iters);
  }
  iters+=1;
}

int ITERS_PER_FRAME = 1;

void draw() {
  if (!STABLE_STATE) {
    iterate();
    if (iters%ITERS_PER_FRAME==0){ 
      drawState();
      print(iters,'\n');
    }
  }
}
