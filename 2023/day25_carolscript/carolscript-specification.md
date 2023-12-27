# Carolscript - Language specification

Carolscript is a fun, festive, dynamically-typed programming language indended for use in carrier-class internet routers.

## Style guide

- Indentation is not recommended. Carol books are not indented.
- Lines may end in commas, full stops, or exclamation marks, depending on the flow of the carol.
- Capitalisation is ignored, but lines should start with a capital letter. 'Christmas' should always be capitalised.


## Data types & artihmetic

| pseudocode | Carolscript |
| --- | --- |
|`False`, `True` | `naughty`, `nice` |
| `{}` | `a silent night`
| `0` | `naught`
| `reindeer+1` |`reindeer and one` |
| `10*elves` | `ten of elves` |
| `days == 12 `| `days is twelve`
| `snow != 1` | `snow is not one`

## Variables & operations

| pseudocode | Carolscript |
| --- | --- |
| `var = 1` | `May your var be one` |
| `var, var2[,...] = {expr}` | `May your var and your var2 [and your ...] be {expr}` |
| `nice_list=["Santa", "Rudolph", "Frosty"]` | `He's making a nice_list, he's checking it three times, he's gonna find out who's "Santa" and "Rudolph" and "Frosty"` |
| `naughty_list=[]` | `He's making a naughty_list, he's checking it three times, he's gonna find out who's "Santa" and "Rudolph" and "Frosty"` |
| `xs[0]` | `The first day of xs`*
| `dict["key"]` | `The key[-]th day of dict`
| `xs.append(y)` | `Deck the xs with boughs of y`
| `result = {str}.split({sep})` | `Last Christmas, I gave you {str}, but the very next {sep}, you gave it to result.`
| `len(xs)` | `Top to toe in xs`|
| `print(x)` | `Hark! x`
| `shuffle_list(xs)` | `Mix and a-mingle in the xs`
| `lines = [`<br>`  line.strip()`<br>`  for line in open('input_file').readlines()`<br>`]` | `I dont't want a lot for lines, there is just 'input_file' I need.`


_\* list indexes start at one in Carolscript. Nobody sings about the zero-th day of christmas!_


## Program flow

| pseudocode | Carolscript |
| --- | --- |
| `if {expr}:`<br>`  {branch}` | `He knows if {expr},`<br>`{branch},`<br>`So be good for goodness sake.` |
| `while(True):`<br>`  {body}` | `Rockin' around the christmas tree,`<br>`{body},`<br>`In a new old-fashioned way!` |
| `for true_love in {xs}:`<br>`  {body}` | `On the first day of {xs}, my true_love gave to me,`<br>`{body},`<br>`And a partridge in a pear tree.` |
| `continue` | `FIIIIVE GOOOLD RIIIINGS!`*
| `def foo():`<br>`  {body}` | `It's beginning to look a lot like foo,`<br>`{body}`<br>`Right within your heart.` |
| `return {expr}` | `{expr}; I wrapped it up and sent it.` |
| `result = foo()` | `May your result be the most wonderful foo of the year`

_\* the 'I' and 'O' characters can be repeated as many times as you prefer._

# Examples

- [Sam Boyer's Advent of Code 2023/day 25 solution in Carolscript](day25-1.carolscript)

- _Have you written in Carolscript yet? Add your link here!_

# Learn more

todo