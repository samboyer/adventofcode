import java.util.*;
import java.io.*;


class Main {
  public static String[] read_stdin(){
    ArrayList<String> ss = new ArrayList<String>();
    try {
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    String line;
    while((line = br.readLine()) != null) {
        // Do something with line
        ss.add(line);
    }
    br.close();
    } catch (IOException e){
    }
    String[] arr = new String[ss.size()];
    return ss.toArray(arr);
  }

  private static Coord getLowestDistanceCoord(HashMap<Coord, Integer> coord_map) {
    Coord min_coord = null;
    int min_dist = Integer.MAX_VALUE;
    for (Coord coord: coord_map.keySet()) {
        int dist = coord_map.get(coord);
        if (dist < min_dist) {
            min_dist = dist;
            min_coord = coord;
        }
    }
    return min_coord;
  }

  public static void maybe_add(Coord new_coord, int new_dist, HashMap<Coord, Integer> cells_in_consideration, Set<Coord> done_cells, String[] lines){
    if (!done_cells.contains(new_coord) && (!cells_in_consideration.containsKey(new_coord) || cells_in_consideration.get(new_coord) > new_dist)){
      // System.out.println("pushing " + new_coord.x + ", "+new_coord.y+", dist="+new_dist);
      cells_in_consideration.put(new_coord, new_dist);
    }
  }
  
  public static void main(String[] args) {
      String[] lines = read_stdin();
      // System.out.println(String.join("\n",lines));

      //basically just do dijkstras
      int SIZE_X = lines[0].length();
      int SIZE_Y = lines.length;
      Coord GOAL = new Coord(SIZE_X-1, SIZE_Y-1, "");

      int MIN_ROLL_DIST = 4;
      int MAX_ROLL_DIST = 10;

      // (vals are current distance to this node)
      HashMap<Coord, Integer> cells_in_consideration = new HashMap<Coord, Integer>();

      Set<Coord> done_cells = new HashSet<Coord>();

      cells_in_consideration.put(new Coord(0,0, ""),0);

      while(cells_in_consideration.size()!=0){
        // get the node with lowest current distance
        Coord current_cell = getLowestDistanceCoord(cells_in_consideration);
        int dist_to_current_cell = cells_in_consideration.get(current_cell);
        cells_in_consideration.remove(current_cell);
        done_cells.add(current_cell);
        // System.out.println("current cell is " + current_cell.x + ", " + current_cell.y + ", dir="+current_cell.prev_dir+", dist=" + dist_to_current_cell);
        // System.out.println(new ArrayList<>(done_cells));

        if (current_cell.x == GOAL.x && current_cell.y == GOAL.y){
          System.out.println("GOAL FOUND! DIST IS "+dist_to_current_cell);
          // System.out.println("dir is "+current_cell.prev_dir);
          break;
        }

        // Add neighbours if not already visited & not too straight
        if (current_cell.prev_dir != "down" && current_cell.prev_dir !="up"){
          int new_dist = dist_to_current_cell;
          for(int j=-1;j>=-MAX_ROLL_DIST; j--){
            if (current_cell.y+j<0) continue;
            new_dist+=Integer.parseInt("" + lines[current_cell.y+j].charAt(current_cell.x));
            if(j>-MIN_ROLL_DIST){continue;}
            maybe_add(new Coord(current_cell.x, current_cell.y+j, "up"), new_dist, cells_in_consideration, done_cells, lines);
          }
        }
        if (current_cell.prev_dir != "down" && current_cell.prev_dir !="up"){
          int new_dist = dist_to_current_cell;
          for(int j=1;j<=MAX_ROLL_DIST; j++){
            if (current_cell.y+j>=SIZE_Y) continue;
            new_dist+=Integer.parseInt("" + lines[current_cell.y+j].charAt(current_cell.x));
            if(j<MIN_ROLL_DIST){continue;}
            maybe_add(new Coord(current_cell.x, current_cell.y+j, "down"), new_dist, cells_in_consideration, done_cells, lines);
          }
        }
        if (current_cell.prev_dir != "left" && current_cell.prev_dir != "right"){
          int new_dist = dist_to_current_cell;
          for(int i=-1;i>=-MAX_ROLL_DIST; i--){
            if (current_cell.x+i<0) continue;
            new_dist+=Integer.parseInt("" + lines[current_cell.y].charAt(current_cell.x+i));
            if(i>-MIN_ROLL_DIST){continue;}
            maybe_add(new Coord(current_cell.x+i, current_cell.y, "left"), new_dist, cells_in_consideration, done_cells, lines);
          }
        }
        if (current_cell.prev_dir != "left" && current_cell.prev_dir != "right"){
          int new_dist = dist_to_current_cell;
          for(int i=1;i<=MAX_ROLL_DIST; i++){
            if (current_cell.x+i>=SIZE_X) continue;
            new_dist+=Integer.parseInt("" + lines[current_cell.y].charAt(current_cell.x+i));
            if(i<MIN_ROLL_DIST){continue;}
            maybe_add(new Coord(current_cell.x+i, current_cell.y, "right"), new_dist, cells_in_consideration, done_cells, lines);
          }
        }
      }
    }
}



class Coord{
  int x;
  int y;
  String prev_dir;
  public Coord(int x, int y, String prev_dir){
    this.x=x;
    this.y=y;
    this.prev_dir=prev_dir;
  }

  // Overriding equals() to compare two Coord objects
  @Override
  public boolean equals(Object o) {
        // If the object is compared with itself then return true
        if (o == this) {
            return true;
        }

        /* Check if o is an instance of Coord or not
          "null instanceof [type]" also returns false */
        if (!(o instanceof Coord)) {
            return false;
        }

        // typecast o to Coord so that we can compare data members
        Coord c = (Coord) o;

        // Compare the data members and return accordingly
        return x==c.x && y==c.y && prev_dir == c.prev_dir;
    }
    @Override
    public int hashCode(){
      return x*1000001+y*10002 + prev_dir.hashCode();
    }
}








