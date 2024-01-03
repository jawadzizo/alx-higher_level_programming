#include "lists.h"

#define SIZE 128

/**
 * check_cycle - checks if there is a cycle in a singly linked list
 * @list: the list to check
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	int i, j;
	struct listint_s *storages[SIZE];

	for (i = 0; list != NULL; i++)
	{
		for (j = 0; j < i; j++)
		{
			if (list == storages[j])
				return (1);
		}

		storages[i] = list;
		list = list->next;
	}

	return (0);
}

