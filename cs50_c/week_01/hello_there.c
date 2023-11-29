#include <stdio.h>

int main(void)
{
    printf("Type your name: ");
    char full_name[30];

    fgets(full_name, sizeof(full_name)-1,stdin);
    printf("\nHello There, %s !\n",full_name);


}
