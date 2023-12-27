#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct node
{
    int number;
    struct node *next;

} node;

int main (int argc, char *argv[])
{
    if (argc == 1)
    {
        printf("No argument passed!\n");
        return 1;
    }

    node *list = NULL;
    int number;
    for (int i = 1; i < argc; i++)
    {
        number = atoi(argv[i]);
        node *n = malloc(sizeof(node));

        if (n == NULL)
            return 2;

        n -> number = number;
        n -> next = NULL;
        
        n -> next = list;

        list = n;

    }
    
    node *ptr = list;

    while (ptr != NULL)
    {
        printf("%i\n", ptr -> number);

        ptr = ptr -> next;
    }

    ptr = list;

    while (ptr != NULL)
    {
        node *next = ptr->next;

        free(ptr);

        ptr = next;
    }

    return 0;
}
