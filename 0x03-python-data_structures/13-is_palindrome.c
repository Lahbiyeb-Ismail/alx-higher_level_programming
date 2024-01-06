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
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *current = slow;
	listint_t *temp;

	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}

	listint_t *left = *head;
	listint_t *right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);

		left = left->next;
		right = right->next;
	}

	return (1);
}

