#include <Python.h>
void print_python_bytes(PyObject *p)
{
Py_ssize_t size;
char *s;
printf("[.] bytes object info\n");
if (PyBytes_CheckExact(p))
{
PyBytes_AsStringAndSize(p, &s, &size);
printf("  size: %ld\n  trying string: %s\n  first %ld bytes:", size,s,size < 10 ? size + 1 : 10);
for (int i = 0; i <= size  && i < 10; i++)
printf(" %02hhx", s[i]);
printf("\n");
}
else
printf("  [ERROR] Invalid Bytes Object\n");
}
void print_python_list(PyObject *p)
{
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
for (int i = 0; i < PyList_Size(p); i++)
{
printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
if (PyBytes_Check(PyList_GET_ITEM(p, i)))
print_python_bytes(PyList_GET_ITEM(p, i));
}
}
