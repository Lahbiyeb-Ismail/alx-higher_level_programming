#include <stdio.h>
#include <Python.h>


/**
 * print_python_list_info - Prints information about a Python list.
 *
 * This function takes a pointer to a PyObject representing a Python list
 * and prints various information about the list, including its size,
 * allocated memory, and the type of each element in the list.
 *
 * @p: A pointer to the PyObject representing the Python list.
 */

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
