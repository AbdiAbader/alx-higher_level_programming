#include "lists.h"
#include <stdio.h>
/**
 *is_palindorome - palindrome checker
 *@head: head of list
 *Return: 1 if palindrome  otherwise 0
 */
int is_palindrome(listint_t **head)
{
  int len = 0, i = 0;
  listint_t *hold1 , *tail ,*temp ,*hold2;
if (*head == NULL)
return 1;
tail = malloc(sizeof(listint_t));
if (tail == NULL)
return 0;
hold1 = *head;
temp = *head;
while (temp)
   {
   if ( len == 0)
     {
	 tail->n = temp->n;
	 tail->next = NULL;
	 hold2 = tail;
       }

   else
     {
       temp = temp->next;
       tail->next = temp;
       tail = temp;
      
     }
   len++;
   }
     while (hold1 && hold2)
       {
	 if ( i == len / 2)
	   break;
	   
	 if (hold1->n != hold2->n)
	   return 0;
	 hold1 = hold1->next;
	 hold2 = hold2->next;
	 i++;
       }
 return 1;
}
