#include <Python.h>
#include <stdio.h>
void print_python_bytes(PyObject *p)
{
printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
printf(" size: %ld\n", PyBytes_Size(p));
printf(" trying string: %s\n", PyBytes_AsString(p))   
printf(" first %ld bytes", PyBytes_Size(p));
for (int i = 0; i < PyBytes_Size(p) && i < 10; i++)
printf("%02X", PyBytes_AsString(p)[i]);
printf("\n");
}
else
{
printf("[ERROR] Invalid Bytes Object\n");
}
}
void print_python_list(PyObject *p)
{
char s;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)
{
printf("Element %ld: %s\n", i, s = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
if (strcmp(s,"bytes"))
print_python_bytes(((PyListObject *)p)->ob_item[i])
 
}
