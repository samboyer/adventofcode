const fs = require("fs");

const lines = fs.readFileSync(process.argv[2]).toString().split("\n");
console.log(lines);

const ignore_slopes = process.argv[3] === "--ignore-slopes";

const SIZE_X = lines[0].length;
const SIZE_Y = lines.length;
const cell = (x, y) => lines[y].charAt(x);

// 'route' is an object with 2 keys:
//  'places': dict of places visited
//  'end': [x, y] of last place visited

const flatten = (x, y) => y * SIZE_X + x;

const start_flat = flatten(1, 1);
const potentialRoutes = [
  {
    places: {
      start_flat: true,
    },
    end: [1, 0],
  },
];
const DEST_X = SIZE_X - 2;
const DEST_Y = SIZE_Y - 1;

var max_route_length = 0;
var max_route = null;

var iters = 0;
var t0 = new Date();
const ITERS_PER_TICK = 10000;

while (potentialRoutes.length > 0) {
  iters += 1;
  if (iters % ITERS_PER_TICK == 0) {
    const t1 = new Date();
    const secs = (t1 - t0) / 1000;
    const itersPerSec = Math.round(ITERS_PER_TICK / secs);
    console.log(
      `iters: ${iters}, routes: ${potentialRoutes.length}. max_route_length: ${max_route_length}. ${itersPerSec} iters/sec`
    );
    t0 = t1;
  }

  const route = potentialRoutes.pop();

  const x = route.end[0];
  const y = route.end[1];

  //   console.log(`(${x}, ${y})`);

  if (x === DEST_X && y === DEST_Y) {
    const len = Object.keys(route.places).length;
    if (len > max_route_length) {
      max_route_length = len;
      max_route = route;
    }
    continue;
  }

  //consider adjacent cells
  var adjs = [
    [x + 1, y],
    [x, y + 1],
    [x - 1, y],
    [x, y - 1],
  ];

  var placesToGo = [];
  adjs.forEach((adj) => {
    const x1 = adj[0];
    const y1 = adj[1];
    if (x1 < 0 || x1 >= SIZE_X || y1 < 0 || y1 >= SIZE_Y) return;
    const flat = flatten(x1, y1);
    if (route.places[flat]) return;
    if (cell(x1, y1) === "#") return;
    if (!ignore_slopes) {
      if (cell(x1, y1) === "v" && y != y1 - 1) return; // cell is a v and not directly below
      if (cell(x1, y1) === "^" && y != y1 + 1) return; // cell is a ^ and not directly above
      if (cell(x1, y1) === ">" && x != x1 - 1) return; // cell is a > and not directly right
      if (cell(x1, y1) === "<" && x != x1 + 1) return; // cell is a < and not directly left
    }
    placesToGo.push(adj);
  });
  if (placesToGo.length == 1) {
    //don't need to clone route
    const flat = flatten(placesToGo[0][0], placesToGo[0][1]);
    route.places[flat] = true;
    route.end = placesToGo[0];
    potentialRoutes.push(route);
  } else {
    placesToGo.forEach((placeToGo) => {
      const flat = flatten(placeToGo[0], placeToGo[1]);
      const new_places = structuredClone(route.places);
      new_places[flat] = true;
      potentialRoutes.push({
        places: new_places,
        end: placeToGo,
      });
    });
  }
}

for (var y = 0; y < SIZE_Y; y++) {
  for (var x = 0; x < SIZE_X; x++) {
    if (max_route.places[flatten(x, y)]) {
      process.stdout.write("O");
    } else {
      process.stdout.write(cell(x, y));
    }
  }
  process.stdout.write("\n");
}

console.log(`Max route length: ${max_route_length - 1}`);
