#!/bin/bash
INPUT_FILE="input"
INSTRUCTIONS=$(head -n 1 $INPUT_FILE)

CURRENT_POS="AAA"
STEPS=0
INSTRUCTION_POS=0

echo "$CURRENT_POS"
while [ "$CURRENT_POS" != "ZZZ" ]; do
    INSTRUCTION_POS=$((INSTRUCTION_POS+1))
    if [ "$INSTRUCTION_POS" -gt "${#INSTRUCTIONS}" ]; then
        INSTRUCTION_POS=1
    fi

    MAP_LINE=$(grep "^$CURRENT_POS = " $INPUT_FILE)
    INSTRUCTION=$(echo "$INSTRUCTIONS" | head -c $INSTRUCTION_POS | tail -c 1)

    # echo "$INSTRUCTION"

    if [ "$INSTRUCTION" == "L" ]; then
        CURRENT_POS=$(echo "$MAP_LINE" | head -c 10 | tail -c 3)
    else
        CURRENT_POS=$(echo "$MAP_LINE" | head -c 15 | tail -c 3)
    fi
    # echo "$CURRENT_POS"

    STEPS=$((STEPS+1))
done

echo "Done in $STEPS steps"