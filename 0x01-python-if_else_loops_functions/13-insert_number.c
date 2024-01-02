#include "lists.h"

/**
 * insert_node - inserts a new node
 * at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 * Return: the address of the new node, or NULL if it
 * failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;
	int i;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (number == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	for (i = 0; i < number - 1; i++)
	{
		if (!current->next)
			return (NULL);
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
