

INPUT = ".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."

# puts INPUT
$lines=INPUT.split("\n")
# puts $lines


def num_energized_when_starting_at(x,y,dir_x,dir_y)
  lines_to_do_later = [[x,y,dir_x,dir_y]]

  energized_tiles = Array.new($lines.length) {|e| e = Array.new($lines[0].length) {|f| f= false} }
  already_reflected_at = Array.new($lines.length) {|e| e = Array.new($lines[0].length) {|f| f= false} }

  num_energized_tiles=1
  energized_tiles[y][x]=true

  while lines_to_do_later.length>0 do
    beam = lines_to_do_later.pop()
    x=beam[0]
    y=beam[1]
    dir_x=beam[2] #right
    dir_y=beam[3]

    while x>=0 and x<$lines[0].length and y>=0 and y<$lines.length do
      # change direction based on current tile
      char=$lines[y][x]
      if char == '|' and dir_y==0 then
        if not already_reflected_at[y][x] then
          dir_x=0
          dir_y=1
          lines_to_do_later.append([x,y,0,-1])
          already_reflected_at[y][x] = true
        else #kill this beam
          x=-10
          y=-10
          break
        end
      elsif char == '-' and dir_x == 0 then
        if not already_reflected_at[y][x] then
          dir_x=1
          dir_y=0
          lines_to_do_later.append([x,y,-1,0])
          already_reflected_at[y][x] = true
        else #kill this beam
          x=-10
          y=-10
          break
        end
      elsif char =='/' then
        # reflect in  line y=-x (swap axes and negate)
        tmp=dir_x
        dir_x=-dir_y
        dir_y=-tmp
      elsif char == '\\' then
        # reflect in line y=x (just swap axes)
        tmp=dir_x
        dir_x=dir_y
        dir_y=tmp
      end

      # energize this tile if not already
      if energized_tiles[y][x] == false then
        energized_tiles[y][x] = true
        num_energized_tiles+=1
      end

      # advance in new direction
      x+=dir_x
      y+=dir_y
    end
  end
  # for j in 0..($lines.length-1)
  #   for i in 0..($lines[0].length-1)
  #     if $lines[j][i] == '.' and energized_tiles[j][i] then
  #       print('#')
  #     else
  #       print($lines[j][i])
  #     end
  #   end
  #   print("\n")
  # end
  return num_energized_tiles
end

max_num_energized_tiles = -1

def max (a,b)
  a>b ? a : b
end

# beam array is [x,y,dir_x, dir_y]

# LEFTS & RIGHTS
for j in 0..($lines.length-1)
  max_num_energized_tiles = max(
    num_energized_when_starting_at(0,j,1,0),
    max_num_energized_tiles
  )
  max_num_energized_tiles = max(
    num_energized_when_starting_at($lines[0].length-1,j,-1,0),
    max_num_energized_tiles
  )
end
# TOPS & BOTTOMS
for i in 0..($lines[0].length-1)
  max_num_energized_tiles = max(
    num_energized_when_starting_at(i,0,0,1),
    max_num_energized_tiles
  )
  max_num_energized_tiles = max(
    num_energized_when_starting_at(i,$lines.length-1,0,-1),
    max_num_energized_tiles
  )
end

puts "NUM_ENERGIZED_TILES = " + max_num_energized_tiles.to_s
