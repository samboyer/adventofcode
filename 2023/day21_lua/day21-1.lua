INPUT = io.read("*a")

NUM_STEPS = 64

lines = {}
for line in string.gmatch(INPUT, "[^%s]+") do
    table.insert(lines, line)
end

possiblePoses = {}

for j = 1, #lines do
    si = string.find(lines[j], 'S')
    if si ~= nil then
        table.insert(possiblePoses, { j, si })
        break
    end
end

-- print(frontier[1][1], frontier[1][2])

function setContains(set, key)
    return set[key] ~= nil
end

function tablelength(T)
    local count = 0
    for _ in pairs(T) do
        count = count + 1
    end
    return count
end

for iters = 1, NUM_STEPS do
    newPoses = {}
    newPosSet = {}

    -- print()
    for n = 1, #possiblePoses do
        j = possiblePoses[n][1]
        i = possiblePoses[n][2]

        --maybe add adjacents to frontier
        adjs = { { j - 1, i }, { j + 1, i }, { j, i - 1 }, { j, i + 1 } }
        for k, adj in pairs(adjs) do
            aj = adj[1]
            ai = adj[2]
            marker = aj .. ',' .. ai
            if string.sub(lines[aj], ai, ai) ~= '#' and not setContains(newPosSet, marker) then
                table.insert(newPoses, { aj, ai })
                newPosSet[marker] = true
                -- print('adding '..aj..','..ai)
            end
        end
    end
    possiblePoses = newPoses
    -- posSet = newPosSet
end

print(#possiblePoses, "possible positions")

-- print(tablelength(posSet), "possible positions")
-- find gardens adjacent to Os