#include <stdio.h>
#include <stdlib.h>
int main()
{
    char *s = malloc(10);

    printf("Type a name: ");
    scanf("%4s", s);
    
    if (s == NULL)
        return 1;

    s[4] = '\0';

    printf("Hello there! %s\n", s);

    free(s);


    return 0;

}





