<?php

  $INPUT="1,0,1~1,2,1
  0,0,2~2,0,2
  0,2,3~2,2,3
  0,0,4~0,2,4
  2,0,5~2,2,5
  0,1,6~2,1,6
  1,1,8~1,1,9";

  ob_implicit_flush(true);

  ob_start();

  echo "wazzup<br>";
  ob_flush();
  flush();
  set_time_limit(30);

  function coords_equal($a, $b){
    return $a[0] == $b[0] && $a[1] == $b[1] && $a[2] == $b[2];
  }

  //return true if block_above sits on block_below
  function block_on_top($block_below, $block_above){
    foreach($block_above as $piece_above){
      $below = [$piece_above[0], $piece_above[1], $piece_above[2]-1];
      foreach($block_below as $piece_below){
        if(coords_equal($piece_below, $below)){
          return true;
        }
      }
    }
    return false;
  }


  $lines=explode("\n", $INPUT);
  $bricks = [];
  $GRID=[];
  $MINX=0;
  $MAXX=0;
  $MINY=0;
  $MAXY=0;
  $MINZ=0;
  $MAXZ=0;
	foreach($lines as $line){
	  array_push($lines, $line);
	  $coord_strs = explode("~", trim($line));
	  $ends = [];
	  foreach($coord_strs as $coord_str){
	    $coord = explode(",", $coord_str);
	    array_push($ends, [intval($coord[0]), intval($coord[1]), intval($coord[2])]);
	  }
	  $minx = min($ends[0][0], $ends[1][0]);
    $maxx = max($ends[0][0], $ends[1][0]);
    $miny = min($ends[0][1], $ends[1][1]);
    $maxy = max($ends[0][1], $ends[1][1]);
    $minz = min($ends[0][2], $ends[1][2]);
    $maxz = max($ends[0][2], $ends[1][2]);

    $pieces =[];
	  for ($x = $minx; $x <= $maxx; $x++) {
      for ($y = $miny; $y <= $maxy; $y++) {
        for ($z = $minz; $z <= $maxz; $z++) {
          array_push($pieces, [$x, $y, $z]);
        }
      }
	  }

	  array_push($bricks, $pieces);
    $MINX = min($MINX, $minx);
    $MAXX = max($MAXX, $maxx);
    $MINY = min($MINY, $miny);
    $MAXY = max($MAXY, $maxy);
    $MINZ = min($MINZ, $minz);
    $MAXZ = max($MAXZ, $maxz);
  }
  // initialise $GRID with falses
  for ($x = $MINX; $x <= $MAXX; $x++) {
    $yz_slice = [];
    for ($y = $MINY; $y <= $MAXY; $y++) {
      $z_slice = [];
      for ($z = $MINZ; $z <= $MAXZ; $z++) {
        array_push($z_slice, false);
      }
      array_push($yz_slice, $z_slice);
    }
    array_push($GRID, $yz_slice);
  }

  // fill in $GRID with trues where bricks lie
  foreach($bricks as $brick){
    foreach($brick as $piece){
      $GRID[$piece[0]][$piece[1]][$piece[2]] = true;
    }
  }

  // var_dump($bricks);
  echo count($bricks) . " bricks<br>";
  ob_flush();
  flush();

  // pull all the blocks down
  $iters =1;
  $all_stable = false;
  while(!$all_stable){
    echo "iter $iters<br>";
    ob_flush();
    $all_stable = true;

    $iters+=1;
    $bi=0;
    for($bi=0; $bi<count($bricks); $bi++){
    // foreach($bricks as $brick){
      $brick = $bricks[$bi];
      // echo "$bi\n";

      $should_move_down = true;

      while($should_move_down){
        // echo $bi . ": (".$brick[0][0].", ".$brick[0][1].", ".$brick[0][2].")\n";

        $minz =10000;
        foreach($brick as $piece) {
          if($piece[2] == 1){ // already on ground
            $should_move_down = false;
            break;
          }
          $minz=min($minz, $piece[2]);
        }
        if(!$should_move_down){break;}
        foreach($brick as $piece) {
          if ($GRID[$piece[0]][$piece[1]][$minz-1] == true) { // piece below is occupied
            $should_move_down = false;
            break;
          }
        }
        if($should_move_down){
          // echo "moving brick $bi down\n";
          for($pi=0;$pi<count($brick); $pi++){
            $GRID[$brick[$pi][0]][$brick[$pi][1]][$brick[$pi][2]] = false;
            $GRID[$brick[$pi][0]][$brick[$pi][1]][$brick[$pi][2]-1] = true;

            $brick[$pi][2] -=1;
          }
          $all_stable = false;
        }
      }
      $bricks[$bi]=$brick;
    }
  }


  echo "fininshed falling\n";
  ob_flush();
  flush();


  // Now check which bricks can be broken.
  $num_bricks_can_be_broken = 0;
  for($bi=0; $bi<count($bricks); $bi++){
    $brick = $bricks[$bi];

    $can_be_broken = true;

    for($bj=0; $bj<count($bricks); $bj++){
      if($bj == $bi){continue;}
      if(block_on_top($brick, $bricks[$bj])){
        // see if bj can be supported by another brick.
        $supported_by_other = false;
        for($bk=0; $bk<count($bricks); $bk++){
          if($bk == $bi || $bk == $bj){continue;}
          if(block_on_top($bricks[$bk], $bricks[$bj])){
            $supported_by_other = true;
            break;
          }
        }
        if(!$supported_by_other){
          $can_be_broken = false;
          break;
        }
      }
    }
    if($can_be_broken){
      $num_bricks_can_be_broken += 1;
    }
  }

  echo "$num_bricks_can_be_broken CAN BE BROKEN";

  ob_end_flush();

?>