
package main
import (
    "fmt"
    "strings"   
    "strconv"
    // "regexp"
)

const INPUT = `@@@`

func expand_unknowns(record string) []string{
    expanded := []string{""}
    for i := 0; i<len(record); i++{
        // if known, just add char to each expanded string
        if record[i] == '.' || record[i] == '#'{
            for j := 0; j<len(expanded); j++{
                expanded[j] = expanded[j] + string(record[i])
            }
        } else{
            // if '?', duplicate expanded, first with .s, then with #s
            exp_2 := make([]string, len(expanded), len(expanded))

            // copy(expanded, exp_2)
            for j := 0; j<len(expanded); j++{
                exp_2[j] = expanded[j] + "#"
                expanded[j] = expanded[j] + "."
            }
            expanded = append(expanded,exp_2...)
        }
    }
    // fmt.Printf("eppanded:%#v\n", expanded)

    return expanded
}

func allowed_record(record string, nums []int) bool{
    damaged_groups := strings.Fields(strings.Replace(record, "."," ", -1))

    if len(damaged_groups) != len(nums) {
        return false
    }

    for i, s := range damaged_groups{
        if nums[i] != len(s){
          return false
        }
    }
    return true
}



func main() {
    var lines = strings.Split(INPUT,"\n")

    sum := 0
    for _, line := range lines {
        // parse line
        var parts = strings.Split(line," ")
        var num_strs = strings.Split(parts[1],",");
        nums := make([]int, len(num_strs))
        for i, num_str := range num_strs{
            nums[i], _ = strconv.Atoi(num_str)
        }
        // fmt.Printf("Foo %#v\n", nums)

        var expanded_records = expand_unknowns(parts[0]);
        allowed_lines := 0;
        for _, record := range expanded_records {
            if allowed_record(record, nums){
                allowed_lines += 1;
            }
        }
        // fmt.Printf("%s has %d options\n", parts[0], allowed_lines)
        sum += allowed_lines
    }

    fmt.Printf("SUM = %d\n", sum)

}
