extends Node2D


@export
var SPHERE_ROCK:PackedScene;
@export
var STATIC_ROCK:PackedScene;
@export
var V_BARRIER:PackedScene;
@export
var H_BARRIER:PackedScene;

@export
var GRID_TO_WORLD_SCALE=10.0;

@export var score_count:Label;

var rock_instances = [];

var exp_positions = [];

# Called when the node enters the scene tree for the first time.
func _ready():
	var file = FileAccess.open("input.txt", FileAccess.READ)
	var content = file.get_as_text()
	var lines=content.split("\n")
	file.close()

	# reverse lines
	lines.reverse()

	var continue_making = true

	for j in range(len(lines)):
		for i in range(len(lines[j])):
			var pos = Vector2(i*(GRID_TO_WORLD_SCALE+1), j*GRID_TO_WORLD_SCALE)
			if lines[j][i]=="#":
				var rock = STATIC_ROCK.instantiate()
				rock.position = pos
				self.add_child(rock)
			elif lines[j][i]=="O" and continue_making:
				var sphere = SPHERE_ROCK.instantiate()
				sphere.position = pos
				self.add_child(sphere)
				rock_instances.append(sphere)
				# continue_making = false

	# add vertical & bottom barrier
	var hbar = H_BARRIER.instantiate()
	hbar.position = Vector2(0, len(lines)*GRID_TO_WORLD_SCALE-5); #@@@ this might need to be 5px lower
	self.add_child(hbar)

	for i in range(len(lines[1])+1):
		var vbar = V_BARRIER.instantiate()
		vbar.position = Vector2(i*(GRID_TO_WORLD_SCALE+1) - 5, 0)
		self.add_child(vbar)


	# # DEBUG: get expected positions
	# file = FileAccess.open("expected.txt", FileAccess.READ)
	# content = file.get_as_text()
	# lines=content.split("\n")
	# file.close()
	# lines.reverse()
	# for j in range(len(lines)):
	# 	for i in range(len(lines[j])):
	# 		if lines[j][i]=="O":
	# 			exp_positions.append(Vector2(i,j));

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	var score=0
	for rock in rock_instances:
		# var col;
		# print(rock.position)
		# var grid_position = Vector2(round(rock.position.x/(GRID_TO_WORLD_SCALE+1)), round(rock.position.y/GRID_TO_WORLD_SCALE))
		# print(grid_position)
		# if grid_position in exp_positions:
		# 	col = Color(1, 1, 1)
		# else:
		# 	col = Color(1, 0,0)
		# rock.find_child('Sprite2D').modulate = col
		# if abs(rock.position.y - round(rock.position.y/GRID_TO_WORLD_SCALE)*GRID_TO_WORLD_SCALE) > 4:
		#     print("ALERT "+str(rock.position.y))
		#     rock.find_child('Sprite2D').modulate = Color(1, 0, 0)
		# else:
		#     rock.find_child('Sprite2D').modulate = Color(1, 1,1)

		score+=int(round((rock.position.y / GRID_TO_WORLD_SCALE)+1))
	# print(poss)
	score_count.text="Score: "+str(score)
