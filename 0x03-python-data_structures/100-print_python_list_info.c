#include <Python.h>

void print_python_list_info(PyObject *p)
{
int x = 0, s = Py_SIZE(p);
PyListObject *obj = (PyListObject *)p;
printf("[*] Size of the Python List =  %d\n",s);
printf("[*] Allocated = %li\n", obj->allocated); 
while (x < s)
{
printf("Element %d: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
x++;
}
}
