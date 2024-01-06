#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 *
 * This function determines whether the given linked list is a palindrome,
 * i.e., whether it reads the same backward as forward. It does so by
 * comparing values from the beginning and end of the list, moving towards
 * the center. The function returns 1 if the list is a palindrome and 0
 * otherwise.
 *
 * @head: A pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tail;
	listint_t *current_node;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current_node = *head;

	while (current_node->next)
		current_node = current_node->next;

	tail = current_node;

	while (*head != tail)
	{
		if ((*head)->n != tail->n)
			return (1);

		*head = (*head)->next;
		tail = get_previous_node(*head);
	}

	return (0);
}

/**
 * get_previous_node - Retrieves the previous node of a given node
 * in a linked list.
 *
 * This function traverses the linked list starting from the
 * given node and returns the node that precedes it.
 * If the given node is the head of the list or if the list is empty,
 * it returns NULL.
 *
 * @node: A pointer to the node for which the previous node needs to be found.
 *
 * Return: A pointer to the previous node, or NULL if the given
 * node is the head of the list or if the list is empty.
 */

listint_t *get_previous_node(listint_t *node)
{
	listint_t *prev = NULL;
	listint_t *current = node;

	while (current && current->next)
	{
		prev = current;
		current = current->next;
	}

	return (prev);
}
