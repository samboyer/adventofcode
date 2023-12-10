#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

// ty https://stackoverflow.com/a/9210560
char** str_split(char* a_str, const char a_delim)
{
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}



int get_next_term_in_sequence(int *nums, int nums_len){
    // if all zeroes, return zero
    int i;
    bool all_zeroes = true;
    for(i=0;i<nums_len;i++){
        if(nums[i]!=0){
            all_zeroes = false;
            break;
        }
    }
    if (all_zeroes){ return 0; }

    // else make a new list containing the diffs and recurse
    int *diffs = malloc(sizeof(int) * (nums_len-1));
    for (i=0; i<nums_len-1; i++){
        diffs[i] = nums[i+1]-nums[i];
    }
    return nums[nums_len-1] + get_next_term_in_sequence(diffs, nums_len-1);
}

// ty https://stackoverflow.com/a/174552
char *read_file_into_str(char *filename){
    char * buffer = 0;
    long length;
    FILE * f = fopen (filename, "rb");

    if (f)
    {
        fseek (f, 0, SEEK_END);
        length = ftell (f);
        fseek (f, 0, SEEK_SET);
        buffer = malloc (length);
        if (buffer)
        {
            fread (buffer, 1, length, f);
        }
        fclose (f);
    }

    return buffer;
}



int main(void){
    int sum = 0;

//     char prog_input[] = "0 3 6 9 12 15\n\
// 1 3 6 10 15 21\n\
// 10 13 16 21 30 45";

    char* prog_input = read_file_into_str("input");


    // FILE *fptr;
    // fptr = fopen("input_test.txt", "r");

    char** lines = str_split(prog_input, '\n');

    for (int i=0; *(lines+i); i++){
        char* line = *(lines+i);
        char** nums_strs = str_split(line, ' ');

        // convert nums_strs to int list
        int nums_len;
        for (nums_len = 0; *(nums_strs+nums_len); nums_len++){}
        // printf("length=%d\n", nums_len);
        int* nums = malloc(sizeof(int)*nums_len);

        for (int j=0; *(nums_strs+j); j++){
            nums[j] = atoi(nums_strs[j]);
        }

        sum += get_next_term_in_sequence(nums, nums_len);
    }


    printf("SUM = %d\n", sum);
    return 0;
}