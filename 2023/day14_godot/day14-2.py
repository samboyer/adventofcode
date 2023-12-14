lines = [l.strip() for l in open("input.txt").readlines()]


# print("\n".join(lines))


def tilt_table(direction):
    changed = True
    while changed:
        changed = False
        for j in range(0, len(lines)):
            for i in range(0, len(lines[0])):
                if direction == "left":
                    down_i = i - 1
                    down_j = j
                elif direction == "right":
                    down_i = i + 1
                    down_j = j
                elif direction == "up":
                    down_i = i
                    down_j = j - 1
                elif direction == "down":
                    down_i = i
                    down_j = j + 1

                if (
                    down_i < 0
                    or down_i >= len(lines[0])
                    or down_j < 0
                    or down_j >= len(lines)
                ):
                    continue

                if lines[j][i] == "O" and lines[down_j][down_i] == ".":
                    changed = True
                    lines[j] = lines[j][:i] + "." + lines[j][i + 1 :]
                    lines[down_j] = (
                        lines[down_j][:down_i] + "O" + lines[down_j][down_i + 1 :]
                    )


state_after_last_cycle = ""

prev_states = [""]

STOP_POINT = 1000000000

for iters in range(STOP_POINT):
    # push in all 4 directions
    tilt_table("up")
    tilt_table("left")
    tilt_table("down")
    tilt_table("right")

    state = "\n".join(lines)
    if state in prev_states:
        i = iters + 1
        loop_i = prev_states.index(state)
        final_state = (STOP_POINT - loop_i) % (i - loop_i) + loop_i
        print(
            f"found loop: {loop_i}->{i}. so at {STOP_POINT} we'd be at state {final_state}"
        )
        lines = prev_states[final_state].split("\n")
        break

    prev_states.append(state)

    if iters % 10 == 0:
        print(iters)


print("\n".join(lines))


print("DONE")

# calculate score
score = 0
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if lines[j][i] == "O":
            score += len(lines) - j

print(f"SCORE={score}")


# with open("expected_test.txt", "w") as f:
#     f.write("\n".join(lines))
