#include <stdio.h>
#include <stdbool.h>
int main(void) 
{
    int my_int;
    printf("Type an int : ");
    scanf("%i", &my_int);

    int *my_int_ptr = &my_int;

    printf("value my_int=%i\n",my_int);
    printf("address of my_int=%p\n", &my_int);
    printf("address of *my_int_ptr=%p\n", my_int_ptr);

    if (&my_int == my_int_ptr)
        printf("Addresses are equal!\n");

    printf("value of **my_int_ptr=%i\n", *my_int_ptr);

    if (my_int == *my_int_ptr)
        printf("Values are equal!\n");
}
