// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;
using System.Collections.Generic;


enum ModuleType{
    Generic,
    FlipFlop,    // '%'
    Conjunction, // '&'
    // Output,
}

class Module{
    public string[] outputs;
    public string name;
    public bool is_high;
    public ModuleType type;
    public Dictionary<string, bool> input_memories; // null unless Conjunction type.
    
    public override string ToString()
        => $"Module('{name}' ({type}), {(is_high ? "high" : "low")}, [{String.Join(", ", outputs)}])";
}



public class Day20
{
    static string EXAMPLE_1 = @"broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a";
static string EXAMPLE_2 = @"broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output";

    static string INPUT=@"@@@";

    static int BUTTON_PRESSES = 1000;
    static bool LOW = false;
    static bool HIGH = true;
    
    static Dictionary<string, Module> MakeCircuit(string input){
        Dictionary<string, Module> modules = new Dictionary<string, Module>();
        
        // add dummy Module for 'output'
        // Module out_mdl = new Module();
        // out_mdl.outputs = new string[0];
        // modules.Add("output", out_mdl);

        string[] lines = input.Split("\n");
        foreach(string line in lines){
            //Console.WriteLine(line);
            
            Module module = new Module();
            
            string[] parts = line.Split(" -> ");
            string name=parts[0];
            module.type = ModuleType.Generic;
            if (name.StartsWith("%")){
                module.type = ModuleType.FlipFlop;
                name = name.Substring(1);
            } else if(name.StartsWith("&")){
                module.type = ModuleType.Conjunction;
                name = name.Substring(1);
                module.input_memories = new Dictionary<string, bool>();
            }
            module.outputs = parts[1].Replace(" ", "").Split(","); //outputs
            module.is_high = false;
            module.name = name;
            modules.Add(name, module);
        }
        
        // Populate input_memories
        foreach(var kvp in modules){
            // Console.WriteLine(kvp.Key);
            Module mdl = kvp.Value;
            foreach(string output in mdl.outputs){
                // Console.WriteLine(output);
                if(modules.ContainsKey(output) && modules[output].input_memories!=null){
                    modules[output].input_memories.Add(kvp.Key, LOW);
                }
            }
        }

        return modules;
    }

    

    static void SimulateOnePress(Dictionary<string, Module>  modules,  Dictionary<bool,int> pulses){

        // (to, from, is_high)
        var signalQueue = new Queue<(string, string, bool)>();
        signalQueue.Enqueue(("broadcaster","button", LOW));
        pulses[LOW]+=1;

        while (signalQueue.Count>0){
            (string, string, bool) signal = signalQueue.Dequeue();
            string module_name = signal.Item1;
            string signal_from = signal.Item2;
            bool is_high = signal.Item3;

            // Console.WriteLine($"{signal_from} -{(is_high?"high":"low")}-> {module_name}");

            Module module = modules[module_name];
            bool should_i_send = true;
            bool what_to_send = is_high;

            switch(module.type){
                case ModuleType.Generic:
                    // default behaviour
                    break;
                case ModuleType.FlipFlop:
                    if(!is_high){
                        // flip the flop
                        // Console.WriteLine($"{module_name} flipping from {module.is_high} to {!module.is_high}");
                        module.is_high = !module.is_high;
                        should_i_send = true;
                        what_to_send = module.is_high;
                    } else{
                        should_i_send = false;
                    }
                    break;
                case ModuleType.Conjunction:
                    module.input_memories[signal_from] = is_high;
                    //if all its memories are high, send low, otherwise send high
                    what_to_send = false;
                    foreach(var mem in module.input_memories){
                        what_to_send |= !mem.Value;
                    }
                    break;
            }
            if(should_i_send){
                pulses[what_to_send] += module.outputs.Length;
                foreach (string dest in module.outputs){
                    if(modules.ContainsKey(dest)){
                        signalQueue.Enqueue((dest, module_name, what_to_send));
                    }
                }
            }
        }
    }

    static void Simulate(Dictionary<string, Module>  modules){
        var pulses = new Dictionary<bool,int>{{LOW, 0}, {HIGH, 0}};

        for(int i=0; i<BUTTON_PRESSES; i++){
            SimulateOnePress(modules, pulses);
        }

        int low_pulses = pulses[false];
        int high_pulses = pulses[true];
        Console.WriteLine($"{low_pulses}L*{high_pulses}H={low_pulses*high_pulses}");
    }

    public static void Main(string[] args)
    {
        var modules = MakeCircuit(EXAMPLE_1);
        // foreach(var kvp in modules){
        //     Console.WriteLine(kvp.Value.ToString());
        // }
        Simulate(modules);
        modules = MakeCircuit(EXAMPLE_2);
        Simulate(modules);
        modules = MakeCircuit(INPUT);
        Simulate(modules);
    }
}