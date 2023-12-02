-- PARSE INPUT
CREATE table game_input(input TEXT);
insert into game_input VALUES(
$$Game 1: 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue
Game 2: 9 red, 7 green, 3 blue; 15 green, 2 blue, 5 red; 10 red, 3 blue, 13 green
Game 3: 3 red, 1 blue, 4 green; 6 red, 3 green, 2 blue; 6 red, 16 blue, 1 green
Game 4: 2 blue, 2 green, 19 red; 3 blue, 11 red, 16 green; 18 blue, 13 green, 20 red; 18 red, 12 blue, 16 green; 8 green, 16 blue, 16 red
Game 5: 8 green, 1 red, 12 blue; 10 green, 6 red, 13 blue; 1 red, 3 blue, 6 green; 14 blue, 2 red, 7 green
Game 6: 1 red; 1 blue; 2 green, 1 blue; 1 red, 3 blue; 1 red, 2 blue, 2 green; 1 green, 7 blue, 1 red
Game 7: 2 red, 1 blue, 5 green; 5 green, 1 red; 3 red, 7 blue; 8 blue, 1 red, 4 green
Game 8: 6 green, 4 blue; 10 green, 7 blue; 5 blue; 1 red, 7 blue; 11 green, 1 red
Game 9: 2 green, 2 blue; 8 red, 5 blue, 6 green; 11 green, 6 blue, 8 red; 4 blue, 3 green, 8 red; 2 green, 10 red, 5 blue
Game 10: 2 blue, 8 green, 2 red; 10 blue, 3 green; 12 blue, 1 green, 2 red; 9 green, 2 red; 3 green, 2 red, 5 blue
Game 11: 12 red, 1 green, 1 blue; 7 green, 1 red; 2 blue, 1 red, 3 green; 15 green, 8 red
Game 12: 4 red, 10 green, 4 blue; 3 red, 10 blue, 18 green; 5 red, 2 blue, 18 green; 8 blue, 16 green, 2 red
Game 13: 3 green, 1 blue, 8 red; 8 blue, 2 green, 6 red; 6 blue, 3 green, 11 red; 2 red, 13 blue; 1 blue, 5 red, 2 green; 6 red
Game 14: 3 blue, 15 green, 10 red; 7 green, 6 red, 6 blue; 8 red, 13 green, 4 blue; 4 green, 1 blue, 9 red; 9 red, 7 blue
Game 15: 8 green, 9 blue, 4 red; 8 blue, 4 green, 4 red; 8 green, 7 blue, 10 red
Game 16: 12 red, 8 blue, 2 green; 4 green, 10 red, 4 blue; 9 green, 4 blue, 5 red; 7 red, 1 blue
Game 17: 1 blue, 4 red, 6 green; 1 blue; 6 red, 8 blue, 10 green; 2 blue, 2 red, 3 green; 8 green, 14 red, 6 blue
Game 18: 5 blue, 1 green, 5 red; 1 green, 11 blue; 3 green, 18 red, 8 blue
Game 19: 2 blue, 2 red, 16 green; 5 blue, 2 red, 17 green; 10 green, 6 blue; 2 blue, 11 green; 15 green, 3 blue, 5 red; 18 green, 8 red
Game 20: 7 red, 6 green, 3 blue; 7 red, 16 green; 1 blue, 6 green; 1 green, 7 red
Game 21: 10 red, 10 blue; 16 green, 4 blue, 7 red; 2 red, 9 blue, 11 green
Game 22: 12 green, 7 red, 2 blue; 6 blue, 3 red, 10 green; 11 red, 12 green, 3 blue; 8 red, 3 green, 3 blue; 3 red, 4 green, 7 blue
Game 23: 7 red, 9 blue; 5 red, 1 green, 4 blue; 8 green, 9 blue, 10 red; 8 green, 9 red, 11 blue
Game 24: 4 blue, 2 red, 15 green; 1 green, 4 blue; 7 green, 2 blue
Game 25: 12 red, 12 green; 11 red, 5 blue, 15 green; 15 green, 5 red, 3 blue; 15 green, 6 blue, 10 red; 3 blue, 1 green, 5 red
Game 26: 7 red, 18 green, 6 blue; 3 red, 2 green, 7 blue; 1 red, 1 green, 1 blue; 16 green, 5 red, 2 blue; 5 blue, 4 red; 12 red, 2 blue
Game 27: 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue
Game 28: 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green
Game 29: 15 green, 10 blue; 6 green, 5 blue, 2 red; 19 green, 5 blue
Game 30: 10 red, 13 green, 2 blue; 5 blue, 14 green, 1 red; 9 green, 14 red, 3 blue; 14 blue, 14 green, 17 red; 15 blue, 9 green, 16 red
Game 31: 6 green, 1 blue, 8 red; 12 red, 8 green; 5 red, 8 green; 9 green, 11 red
Game 32: 6 red, 7 green; 12 green, 1 blue, 2 red; 2 red, 3 green; 4 red, 13 green; 7 red, 9 green
Game 33: 3 red, 7 blue, 10 green; 4 blue, 3 red, 15 green; 6 red, 7 blue, 18 green; 5 red, 10 green, 10 blue; 2 blue, 6 red, 10 green; 7 blue, 3 green, 6 red
Game 34: 1 red, 6 blue, 3 green; 2 green, 13 blue, 2 red; 2 red, 7 green, 5 blue; 4 red, 2 blue, 5 green; 3 red, 4 blue, 3 green
Game 35: 3 red, 4 blue; 3 green, 6 red, 2 blue; 8 green, 4 blue, 3 red; 11 red, 4 blue, 3 green; 5 green, 1 blue, 6 red; 8 red, 7 green
Game 36: 2 blue, 8 red, 2 green; 11 green, 14 red; 14 red, 1 green; 7 green, 2 blue, 11 red
Game 37: 2 green, 10 red; 1 green, 5 red; 5 red, 11 green; 1 blue, 11 green, 2 red
Game 38: 11 red, 1 green, 11 blue; 9 red, 1 green; 5 red, 2 blue, 1 green; 2 red, 6 blue
Game 39: 3 red; 2 green, 18 red, 2 blue; 2 green; 6 red, 2 green; 12 red; 3 green, 11 red
Game 40: 3 blue, 4 red; 2 red; 7 red, 1 green, 2 blue; 1 green, 1 blue; 5 green; 2 green, 2 red, 1 blue
Game 41: 5 green, 3 blue, 10 red; 6 green, 3 blue, 12 red; 2 blue, 5 green, 7 red; 2 blue, 3 green, 2 red
Game 42: 11 green, 1 red; 6 green, 4 red; 4 red, 4 blue, 7 green; 11 green, 5 red, 5 blue
Game 43: 1 blue; 6 green, 16 blue; 7 green, 1 red; 2 red, 15 green, 7 blue; 2 red, 16 green, 3 blue; 3 red, 14 blue
Game 44: 3 green, 1 red, 5 blue; 9 blue, 1 red; 14 blue; 7 blue, 1 green, 2 red
Game 45: 1 blue, 1 red; 1 blue, 1 red; 3 green, 1 red; 1 green, 1 blue
Game 46: 1 green, 8 red, 2 blue; 13 blue, 7 red, 2 green; 3 red, 4 blue; 2 green, 18 blue, 5 red; 4 red, 5 green, 9 blue; 3 red, 7 blue, 1 green
Game 47: 8 blue, 1 red, 8 green; 2 red, 6 green, 1 blue; 2 green, 6 blue, 5 red; 6 blue, 6 red, 6 green; 6 green, 9 blue, 7 red
Game 48: 5 blue, 14 green, 8 red; 7 blue, 10 green, 7 red; 9 green, 9 blue, 6 red; 9 green, 5 blue, 17 red
Game 49: 10 green, 6 blue, 2 red; 3 blue, 5 green, 4 red; 8 red, 8 blue, 11 green; 5 red, 6 green, 5 blue
Game 50: 3 red, 2 green; 1 red, 8 blue; 2 red, 2 green, 3 blue
Game 51: 4 green, 8 red; 8 red, 5 blue, 13 green; 3 red, 11 blue, 14 green; 5 blue, 11 green, 3 red; 5 red, 9 blue, 11 green; 6 green, 4 red, 12 blue
Game 52: 2 green, 1 red, 1 blue; 3 blue, 2 green, 2 red; 1 green, 3 blue, 4 red; 2 blue; 8 red, 2 blue
Game 53: 18 blue, 4 green, 9 red; 6 blue, 9 green; 14 blue, 9 green, 9 red
Game 54: 2 red, 7 blue, 3 green; 6 green, 3 red, 2 blue; 1 blue, 3 green, 3 red; 2 green, 4 red, 9 blue
Game 55: 3 green, 6 blue; 6 green, 8 blue, 6 red; 5 green, 3 red; 4 blue, 8 green, 1 red; 1 red, 2 blue
Game 56: 4 green; 2 blue, 4 green, 1 red; 3 blue, 6 green
Game 57: 15 red, 3 green; 15 red, 1 blue, 2 green; 15 red, 1 green
Game 58: 1 red, 5 blue; 5 green; 6 green, 8 blue, 2 red; 1 red, 6 blue, 6 green
Game 59: 3 green, 8 blue, 5 red; 1 green, 12 blue, 4 red; 2 green, 18 blue; 2 red, 4 green; 16 blue, 3 red, 1 green
Game 60: 7 green, 6 blue, 2 red; 6 blue, 2 red, 4 green; 11 green, 5 blue; 4 green, 4 blue, 3 red; 2 red, 7 green, 8 blue; 6 green, 4 red, 1 blue
Game 61: 6 green, 6 red; 1 green, 3 blue; 6 green, 1 red, 7 blue; 5 red, 19 green, 7 blue
Game 62: 3 red, 4 green; 2 red, 4 blue; 1 red, 13 blue, 5 green
Game 63: 2 red, 13 green, 4 blue; 10 green, 5 red, 10 blue; 13 blue, 6 red, 3 green
Game 64: 5 blue, 2 green; 1 blue, 1 red, 6 green; 3 blue, 11 green; 2 blue, 8 green, 1 red
Game 65: 4 red, 5 green, 2 blue; 2 blue, 4 red, 1 green; 3 red, 5 green, 4 blue; 6 red, 3 blue; 3 blue, 2 green, 5 red; 2 green, 3 red
Game 66: 14 red, 17 green, 1 blue; 2 red, 12 green, 2 blue; 1 blue, 4 green, 14 red
Game 67: 7 green, 4 red, 10 blue; 11 blue, 4 green; 7 green, 2 red, 3 blue; 11 blue, 3 red, 9 green
Game 68: 5 blue, 4 red; 10 blue, 8 green, 5 red; 1 green, 1 red, 10 blue
Game 69: 1 red, 15 blue, 2 green; 16 blue, 15 green; 1 red, 15 green, 14 blue; 2 red, 5 green, 11 blue; 5 green, 1 red, 13 blue; 2 blue, 16 green
Game 70: 1 red, 2 blue, 9 green; 2 green, 1 red; 7 green, 4 blue
Game 71: 5 blue, 1 green; 2 green, 5 blue; 2 blue, 1 red, 1 green; 1 red, 5 blue; 1 red
Game 72: 5 green, 5 blue; 8 green, 3 red; 7 blue, 8 green
Game 73: 1 green, 4 red, 3 blue; 5 green, 5 blue, 3 red; 8 blue, 7 green, 1 red; 3 blue, 3 red, 9 green; 13 green, 2 red, 10 blue
Game 74: 2 red, 4 green, 5 blue; 3 blue, 6 green, 4 red; 2 blue, 6 green, 5 red
Game 75: 10 red, 20 green, 14 blue; 9 blue, 15 green, 17 red; 8 green, 18 blue, 6 red
Game 76: 7 green, 1 red, 9 blue; 1 green, 3 red; 3 red, 3 green; 4 blue, 20 red, 9 green; 12 red, 7 blue
Game 77: 1 blue, 9 green, 7 red; 5 green, 7 red; 4 red, 1 green, 1 blue; 6 green, 3 red, 3 blue; 3 blue, 5 green, 18 red
Game 78: 11 red, 4 green, 4 blue; 12 red, 3 green, 4 blue; 11 red, 4 green, 13 blue; 8 red, 5 blue, 6 green
Game 79: 1 blue, 16 red; 9 red, 2 green, 2 blue; 2 blue, 12 red; 3 green, 12 red
Game 80: 2 blue, 3 green, 5 red; 5 red, 8 blue, 3 green; 10 blue, 8 red, 8 green; 5 blue, 4 red
Game 81: 1 green, 3 red; 6 blue; 6 red, 1 green, 8 blue; 1 green, 8 blue
Game 82: 4 blue, 2 red; 7 blue, 10 green, 3 red; 7 green, 1 red
Game 83: 12 blue, 9 green; 10 green, 7 blue; 7 green, 1 red, 12 blue; 5 green, 12 blue
Game 84: 1 green, 2 blue, 1 red; 2 green, 9 red; 14 red, 1 blue, 2 green; 2 green, 9 red; 4 blue, 2 green, 9 red
Game 85: 1 blue, 8 red, 8 green; 1 green, 4 red, 4 blue; 8 red, 7 green, 18 blue; 5 green, 3 red, 15 blue; 11 blue, 1 red, 4 green; 4 green, 3 red, 1 blue
Game 86: 14 green, 11 red, 14 blue; 9 green, 14 blue; 12 red, 4 green, 13 blue; 14 green, 9 blue, 2 red; 5 red, 17 green, 1 blue
Game 87: 3 red, 3 green, 7 blue; 3 green, 2 red, 20 blue; 12 green, 9 blue; 3 blue, 3 red, 8 green; 12 green, 9 blue, 2 red
Game 88: 4 green, 1 red, 4 blue; 1 green, 3 red, 1 blue; 2 green, 3 blue, 3 red; 5 green, 1 blue
Game 89: 8 blue, 1 red; 4 red, 6 blue, 1 green; 12 blue, 3 red; 1 red, 4 blue; 3 red, 5 blue, 1 green; 7 red, 7 blue
Game 90: 3 red, 2 green; 4 blue, 13 red; 1 blue, 7 red
Game 91: 8 blue, 2 red, 9 green; 5 blue, 17 green; 2 green, 7 blue, 1 red; 8 blue, 11 green, 3 red; 2 red, 5 blue, 1 green
Game 92: 8 red, 11 blue; 7 green, 9 blue, 2 red; 6 red, 3 green, 3 blue; 4 green, 8 blue, 2 red; 9 blue, 12 green, 8 red; 6 red, 14 blue
Game 93: 4 blue, 1 red, 3 green; 7 green, 1 red, 3 blue; 6 green, 1 red, 3 blue; 3 blue, 10 green, 1 red; 3 blue, 7 green
Game 94: 11 red, 13 green, 3 blue; 4 green, 15 red, 5 blue; 1 red, 7 green
Game 95: 4 green, 10 blue, 6 red; 4 green, 9 blue; 8 blue, 9 red, 5 green; 7 green, 12 blue; 12 blue, 8 green, 3 red; 2 green, 5 red
Game 96: 2 red, 2 green, 1 blue; 1 red, 4 green; 1 green
Game 97: 4 red, 5 green; 5 blue, 3 red; 8 blue, 2 green, 1 red
Game 98: 1 blue; 2 green, 1 red; 5 red, 2 green; 4 red, 1 green; 2 red, 2 green, 2 blue
Game 99: 6 blue, 5 red, 2 green; 9 red, 1 blue; 2 green, 2 red, 5 blue; 10 blue, 2 green; 11 blue, 1 green, 4 red
Game 100: 1 blue, 13 green, 14 red; 11 green, 11 blue, 7 red; 2 red, 1 blue, 2 green; 10 blue, 15 red$$
);

CREATE table games(line TEXT);
INSERT into games
SELECT unnest(regexp_split_to_array(input,'\n')) from game_input;

CREATE table showing_strs(
  game_id INT,
  line TEXT
);

INSERT INTO showing_strs
WITH nested_showing_strs AS (
SELECT
  (regexp_matches(games.line, 'Game ([0-9]+)'))[1]::int as foo_game_id,
  regexp_split_to_array(
    split_part(line, ':', 2),
    ';'
  ) as showing_strs
FROM games)
SELECT foo_game_id, foo_showing_str
FROM nested_showing_strs
CROSS JOIN unnest(showing_strs) as foo_showing_str;


CREATE TABLE showings(
  game_id INT,
  num_red INT,
  num_green INT,
  num_blue INT
);
INSERT INTO showings
SELECT
  game_id,
  NULLIF(
    (regexp_matches(line, '([0-9]+) red'))[1],
    ''
  )::int,
  NULLIF(
    (regexp_matches(line, '([0-9]+) green'))[1],
    ''
  )::int,
  NULLIF(
    (regexp_matches(line, '([0-9]+) blue'))[1],
    ''
  )::int
FROM showing_strs;

UPDATE showings
SET num_red = 0
WHERE num_red is NULL;
UPDATE showings
SET num_green = 0
WHERE num_green is NULL;
UPDATE showings
SET num_blue = 0
WHERE num_blue is NULL;

CREATE TABLE possible_contents(
  max_red INT,
  max_green INT,
  max_blue INT
);
INSERT INTO possible_contents VALUES(12,13,14);

-- ACTUAL LOGIC
WITH bad_showings as(
  SELECT game_id
  FROM showings
  WHERE
    (
      num_red > (SELECT max_red FROM possible_contents)
      OR num_green > (SELECT max_green FROM possible_contents)
      OR num_blue > (SELECT max_blue FROM possible_contents)
    )
  group by game_id
)
SELECT sum(distinct game_id) AS PART_1_ANSWER
FROM showings
WHERE game_id NOT IN (SELECT * from bad_showings);


-- PART 2
WITH powers AS(
SELECT
  max(num_red) * max(num_green) * max(num_blue) as power
FROM showings
GROUP BY game_id
)
SELECT sum(power) as PART_2_ANSWER from powers;
