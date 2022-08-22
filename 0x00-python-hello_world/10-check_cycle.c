#include "lists.h"
/**
*check_cycle - checks for cycle in linked list
*@list: list of  or head of the list
*Return: 0 if no cycle otherwise 1
*/
int check_cycle(listint_t *list)
{
listint_t *prt1 = list, *prt2 = list;
if (prt1 == NULL || prt1->next == NULL)
return (0);
while (prt1->next != NULL && prt2->next->next != NULL)
{
prt1 = prt1->next;
prt2 = prt2->next->next;
if (prt1 == prt2)
return (1);
}
return (0);
}
