#include "lists.h"

/**
 * is_palindrome - checks if the given linked list is palindrome
 * @head: a pointer to the list
 * Return: 1 if the linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int i, j, count;
	int array[SIZE];

	for (i = 0; ptr != NULL; i++)
	{
		array[i] = ptr->n;
		ptr = ptr->next;
	}

	if (i <= 1)
		return (1);

	count = i;

	for (i = 0, j = count - 1; i < (count / 2); i++, j--)
	{
		if (array[i] != array[j])
			return (0);
	}

	return (1);
}

