#include <Python.h>
#include <object.h>
#include <listobject.h>


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
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
