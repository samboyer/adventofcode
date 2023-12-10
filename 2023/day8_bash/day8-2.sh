#!/usr/bin/env bash
# INPUT_FILE="input_test_3"
INPUT_FILE="input"
INSTRUCTIONS=$(head -n 1 $INPUT_FILE)

CURRENT_POSITIONS_STR=$(grep -e '..A = ' $INPUT_FILE | cut -c-3)
CURRENT_POSITIONS=(${CURRENT_POSITIONS_STR//$'\n'/ })

echo "${#CURRENT_POSITIONS[@]} starting positions: ${CURRENT_POSITIONS[@]}"

STEPS=0
INSTRUCTION_POS=0

# put map file into a dict for faster lookups
# declare -A map_dict_lefts
# declare -A map_dict_rights



echo "parsing map..."
MAP=$(cat $INPUT_FILE | tail -n +3)
while read line; do
  KEY=${line:0:3}
  LEFT=${line:7:3}
  RIGHT=${line:12:3}

#   echo "key is $KEY, left is $LEFT, right is $RIGHT"
#   map_dict_lefts[$KEY]=$LEFT
#   map_dict_rights[$KEY]=$RIGHT
  declare "map_dict_L_$KEY=$LEFT"
  declare "map_dict_R_$KEY=$RIGHT"
done <<< "$MAP"


test_list(){
    for POS in "${CURRENT_POSITIONS[@]}"; do
        if [[ "$POS" != *Z ]]; then
            return 0
        fi
    done
    return 1
}

echo "starting loop..."

while test_list ; do

    if [ "$INSTRUCTION_POS" -ge "${#INSTRUCTIONS}" ]; then
        INSTRUCTION_POS=0
    fi
    INSTRUCTION=${INSTRUCTIONS:$INSTRUCTION_POS:1}
    # echo "$INSTRUCTION"

    # MAP_LINE=$(grep "^$CURRENT_POS = " $INPUT_FILE)


    for i in "${!CURRENT_POSITIONS[@]}"; do
        POS="${CURRENT_POSITIONS[$i]}"
        varname="map_dict_${INSTRUCTION}_$POS"
        CURRENT_POSITIONS[i]="${!varname}"
    done

    # echo "positions are now ${CURRENT_POSITIONS[@]}"
    # read -p "Press Enter to continue" </dev/tty
    # sleep 0.25

    if [[ $(($STEPS % 1000)) == 0 ]] ; then
        echo "$STEPS"
        # echo "positions are now ${CURRENT_POSITIONS[@]}"
    fi

    STEPS=$((STEPS+1))
    INSTRUCTION_POS=$((INSTRUCTION_POS+1))

done

echo "Done in $STEPS steps"

