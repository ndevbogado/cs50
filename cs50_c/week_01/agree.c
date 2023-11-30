#include <stdio.h>

int main(void)
{
    char my_char;

    printf("Type a Character\n");
    scanf("%c", &my_char);

    printf("Your selected Character is: %c\n", my_char);

    if (my_char == 'y' || my_char == 'Y')
    {
        printf("Agreed.\n");
    } else if (my_char == 'n' || my_char == 'N')
    {
        printf("Not Agreed.\n");
    } else
    {
        printf("Not a valid Character!\n");
    }

}

