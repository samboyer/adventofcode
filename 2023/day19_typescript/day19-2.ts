

const INPUT=`px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}`


enum Attrib {
  X = "x",
  M = "m",
  A = "a",
  S = "s",
}

type MetalPart={ [id in Attrib]: number; };

enum Operator {
  Lt = "<",
  Gt = ">",
}

type WorkflowPredicate = [Attrib,Operator,number] | null

// predicate(optional), id to jump to
type WorkflowStep = [WorkflowPredicate, string]
type WorkflowMap =  { [id: string] : WorkflowStep[]; }

const workflows:WorkflowMap = Object.assign({}, ...INPUT.split('\n\n')[0].split('\n').map(s=>{
    const name = s.split('{')[0]

    var steps_str = s.split('{')[1]
    steps_str = steps_str.substring(0,steps_str.length-1)

    const steps:WorkflowStep[] = steps_str.split(',').map(step_str=>{
        const parts = step_str.split(':')
        if (parts.length==1)
            return [null, parts[0]]
        else{
            const attrib = parts[0].charAt(0) as Attrib
            const pred = parts[0].charAt(1) as Operator
            const amnt = Number(parts[0].substring(2))

            return [[attrib, pred, amnt], parts[1]]
        }
    })

    return {
        [name]:steps
    }
}))

interface PartRange {
    min_x:number;
    max_x:number;
    min_m:number;
    max_m:number;
    min_a:number;
    max_a:number;
    min_s:number;
    max_s:number;
}

function numAcceptingCombinations(range:PartRange, workflow_id:string):number{
    console.log('entering', range, workflow_id)

    if (workflow_id == 'A')
        return Math.max((range.max_x - range.min_x+1) * (range.max_m - range.min_m+1) * (range.max_a - range.min_a+1) * (range.max_s - range.min_s+1),0)
    else if (workflow_id =='R')
        return 0
    else{
        var acceptingCombos = 0;
        for(const step of workflows[workflow_id]){
            if(step[0] == null) {
                //no predicate; all remaining combos go here
                acceptingCombos+=numAcceptingCombinations(range, step[1])

            } else{
                const attrib = step[0][0]
                const op = step[0][1]
                console.log(step[0])
                const comp = step[0][2]
                const new_range:PartRange = {...range}; // to be passed down the 'true' branch

                // The Nastiest Imperative Hack: construct the variable name(s) that'll change, then apply below 
                // if operator is '<', then the 'max' value will go down for the branch following this, and the 'min' value will go up
                var new_key, new_value, old_key, old_value;
                if (op == '<'){
                    new_key = 'max_'+attrib
                    new_value = comp-1
                    old_key = 'min_'+attrib
                    old_value = comp
                } else{ // >
                    new_key = 'min_'+attrib
                    new_value = comp+1
                    old_key = 'max_'+attrib
                    old_value = comp   
                }
                // terrifying
                eval(`new_range.${new_key} = new_value`)
                eval(`range.${old_key} = old_value`)
                acceptingCombos+=numAcceptingCombinations(new_range, step[1])
            }
        }
        return acceptingCombos;
    }
}

const starting_range = {
    min_x:1,
    max_x:4000,
    min_m:1,
    max_m:4000,
    min_a:1,
    max_a:4000,
    min_s:1,
    max_s:4000,
}

const ANSWER = numAcceptingCombinations(starting_range, 'in');
console.log(`ANSWER IS: ${ANSWER}`)