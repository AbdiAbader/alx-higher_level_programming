#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
* Return: Noting
*/
void print_python_list(PyObject *p)
{
long int size, i;
PyListObject *list;
PyObject *obj;
fflush(stdout);
printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
setbuf(stdout, NULL);
return;
}

size = ((PyVarObject *)(p))->ob_size;
list = (PyListObject *)p;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
obj = list->ob_item[i];
printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

if (PyBytes_Check(obj))
print_python_bytes(obj);
if (PyFloat_Check(obj))
print_python_float(obj);
}
}
/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

fflush(stdout);

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)p)->ob_size >= 10)
size = 10;
else
size = ((PyVarObject *)p)->ob_size + 1;

printf("  first %ld bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", bytes->ob_sval[i]);
if (i == (size - 1))
printf("\n");
else
printf(" ");
}
}

/**
* print_python_float - Prints basic info about Python float objects.
* @p: object
* Return: Noting
*/
void print_python_float(PyObject *p)
{
char *buffer = NULL;
PyFloatObject *float_obj = (PyFloatObject *)p;
fflush(stdout);
printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", buffer);
PyMem_Free(buffer);
}
