

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

const parts:MetalPart[] = INPUT.split('\n\n')[1].split('\n').map(s=>{
    const matches = s.matchAll(/[0-9]+/g);
    if (matches !== null){
        const nums=[...matches].map(Number)
        return {
            'x': nums[0],
            'm':nums[1],
            'a':nums[2],
            's':nums[3],
        }
    }
    else return {
            'x': 0,
            'm':0,
            'a':0,
            's':0,
        }
});

// console.log(parts[0]);
// console.log(workflows['in']);

// var ctr = 100;

const ANSWER = parts.filter(part => {
    var pos = 'in';
    while(pos != 'A' && pos != 'R'){
        const steps = workflows[pos]
        for(const step of steps){
            // console.log(step)
            // ctr-=1;
            if (step[0] == null){ //no predicate
                pos = step[1]
                break
            } else {
                if ((step[0][1]=='<' && part[step[0][0]] < step[0][2])
                 || (step[0][1]=='>' && part[step[0][0]] > step[0][2])

                ){
                    pos = step[1]
                    break
                }
            }
        }
    }
    return pos == 'A'
}).map(part => part['x']+part['m']+part['a']+part['s']).reduce((a,b)=>a+b,0);

console.log(`ANSWER IS: ${ANSWER}`)