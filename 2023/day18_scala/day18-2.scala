import scala.collection.mutable.ListBuffer
import scala.collection.mutable.Stack

val INPUT = s"""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

val lines = INPUT.split('\n')

//val dirs = Map("U" -> (0, -1), "D" -> (0, 1), "L" -> (-1, 0), "R" -> (1, 0))
val dirs = Map(3 -> (0, -1), 1 -> (0, 1), 2 -> (-1, 0), 0 -> (1, 0))

object HelloWorld {

  def maybeAdd(
      bitmap: Array[Array[Boolean]],
      stack: Stack[(Int, Int)],
      y: Int,
      x: Int
  ) = {
    if (
      y >= 0 && y < bitmap.length && x >= 0 && x < bitmap(0).length && !bitmap(
        y
      )(x)
    ) {
      stack.push((x, y))
    }
  }

  def main(args: Array[String]): Unit = {
    // first make a list of coordinates used in the trench
    // var coords = (0, 0) :: Nil
    val vertices = new ListBuffer[(Int, Int)]()

    vertices += ((0, 0))
    var currentPos = (0, 0)

    var circumfrence = 0

    lines.foreach(line => {
      val instruction = line.split(' ')
      val distance = Integer.parseInt(instruction(2).substring(2, 7), 16)
      val dir_num = Integer.parseInt(instruction(2).substring(7, 8), 16)
      circumfrence+=distance
      val dir = dirs.getOrElse(dir_num, (0, 0))

      currentPos =
        (currentPos._1 + dir._1 * distance, currentPos._2 + dir._2 * distance)
      vertices += currentPos
    })

    // ~~now make a bitmap from these coords~~ lmao don't do this

    if (vertices(vertices.length - 1) != (0, 0)) {
      println("aaaaaaaa its not a closed trench")
    }

    // calculate area of concave 2D shape (with only right angles?) (shoelace algm)

  
    var A:BigInt = 0
    for (i <- 0 until vertices.length-1) {
      val vi = vertices(i)
      val vj = vertices(i + 1) //ends with (0,0) so fine to not take mod
      val rect_area:BigInt = ((vi._2+vj._2).toLong) * ((vi._1 - vj._1).toLong)
      A += rect_area.toLong
      println(vi)
      println(vj)
      println(rect_area)
    }
    A /= 2
    // println(vertices)

    var NUM_FILLED = A + (circumfrence/2)+1
    println("DONE, NUM FILLED=" + NUM_FILLED.toString)
  }
}
