#include "lists.h"
#include <stdio.h>
/**
*is_palindorome - palindrome checker
*@head: head of list
*Return: 1 if palindrome  otherwise 
*/
int is_palindrome(listint_t **head)
{
int len = 0, i = 0 , buff[BUFSIZ];
listint_t *temp;
if (*head == NULL || (*head)->next == NULL)
return (1);
temp = *head;
while (temp)
{
buff[len] = temp->n;
len++;
temp = temp->next;
}
len--;
while (i <= len / 2)
{
if(buff[i] != buff[len - i])
return (0);
i++;
}
return (1);
}
