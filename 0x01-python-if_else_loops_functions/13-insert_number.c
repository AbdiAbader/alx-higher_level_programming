#include "lists.h"
/**
*insert_node - insert node at index where number
*@head: head of the list
*@number: number
*Return: NULL if failed or head list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp, *hold;
hold = *head;
temp = malloc(sizeof(listint_t));
if (temp == NULL)
return (NULL);
temp->n = number;
temp->next = NULL;
if (*head == NULL)
*head = temp;
else
{
while (hold->next != NULL)
{
if (number < hold->n || number <hold->next->n)
break;
hold = hold->next;
}
if (*head == hold)
  {
    
    temp->next = hold;
    *head = temp;
    return (*head);
  }
temp->next = hold->next;
hold->next = temp;
}
return (*head);
}
