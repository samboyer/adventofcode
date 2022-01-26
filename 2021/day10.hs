import qualified Data.Text    as Text
import qualified Data.Text.IO as Text
import Data.List as List

data Outcome = Complete | Incomplete String | Corrupted Char
  deriving (Show, Eq)

lookupScore ')' = 3
lookupScore ']' = 57
lookupScore '}' = 1197
lookupScore '>' = 25137

lookupScore' ')' = 1
lookupScore' ']' = 2
lookupScore' '}' = 3
lookupScore' '>' = 4

checkChunk :: String -> Outcome
checkChunk s = check s []
  where check :: String -> [Char] -> Outcome
        check ('(':s) stack = check s (')':stack)
        check ('[':s) stack = check s (']':stack)
        check ('{':s) stack = check s ('}':stack)
        check ('<':s) stack = check s ('>':stack)
        check (')':s) stack = if (head stack) == ')' then check s (tail stack) else (Corrupted ')')
        check (']':s) stack = if (head stack) == ']' then check s (tail stack) else (Corrupted ']')
        check ('}':s) stack = if (head stack) == '}' then check s (tail stack) else (Corrupted '}')
        check ('>':s) stack = if (head stack) == '>' then check s (tail stack) else (Corrupted '>')
        check "" (c:stack) = Incomplete (c:stack)
        check "" "" = Complete

score :: Outcome -> Integer
score (Corrupted c) = lookupScore c
score Complete = 0
score (Incomplete s) = 0

score' :: Outcome -> Integer
score' Complete = 0
score' (Corrupted c) = 0
score' (Incomplete s) = scr s 0
  where scr ""    i = i
        scr (c:s) i = scr s (i*5+(lookupScore' c))


tests2 = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","(((({<>}<{<{<>}{[]{[]{}","{<[[]]>}<{[{[{[]{()[[[]","<{([{{}}[<[[[<>{}]]]>[]]"]

midpoint :: [a] -> a
midpoint as = as !!((length as) `div` 2)

main = do
    -- print (checkChunk "{([(<{}[<>[]}>{[]{[(<()>")
    -- print (checkChunk "[[<[([]))<([[{}[[()]]]")
    -- print (checkChunk "[{[{({}]{}}([{[{{{}}([]")
    -- print (checkChunk "[<(<(<(<{}))><([]([]()")
    -- print (checkChunk "<{([([[(<>()){}]>(<<{{")

    chunks <- (fmap Text.lines (Text.readFile "day10.txt"))
    print(sum (map (score.checkChunk) (map Text.unpack chunks)))

    print(midpoint(filter (/=0) (List.sort (map (score'.checkChunk) (map Text.unpack chunks)))))

