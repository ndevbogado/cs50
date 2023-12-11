# include <stdio.h>
# include <stdbool.h>

int length(char my_str[]);

int main(void)
{
    char my_str[15];

    printf("Type anything: ");
    scanf("%s", my_str);

    printf("String's length: %i characters.\n", length(my_str));
    printf("%c", my_str[8]);
}

int length(char my_str[]) 
{
    int count = 0;
    
    while (my_str[count] != '\0')
        count++;
    return count;
}
