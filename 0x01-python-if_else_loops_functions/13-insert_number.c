#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: a pointer to the list
 * @number: the number to insert in the new node
 * Return: the new created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *node, *ptr, *last;

	ptr = *head;

	node = malloc(sizeof(listint_t));
	node->n = number;

	while (ptr != NULL)
	{
		if (number < ptr->n)
		{
			temp = ptr;
			ptr = node;
			ptr->next = temp;
			last->next = node;
			return (node);
		}

		last = ptr;
		ptr = ptr->next;
	}

	temp = ptr;
	ptr = node;
	ptr->next = temp;

	return (node);
}

