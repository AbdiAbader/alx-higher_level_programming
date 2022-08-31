#include <Python.h>                                                                                              
#include <stdio.h>                                                                                                                
void print_python_bytes(PyObject *p)                                            {
  int i;
printf("[.] bytes object info\n");                                                                                               
if (PyBytes_Check(p))                                                                                                             
{                                                                                                                                 
printf(" size: %ld\n", ((PyVarObject *)p)->ob_size); 
printf(" trying string: %s\n",((PyBytesObject *)p)->ob_sval);
if (((PyVarObject *)p)->ob_size > 10)
printf(" first 10 bytes");
else
printf(" first %ld bytes", PyBytes_Size(p));
for (i = 0; i < ((PyVarObject *)p)->ob_size && i < 10; i++)                                                                               
printf("%02X", ((PyBytesObject *)p)->ob_sval);                                                                                           
printf("\n");                                                                                                                     
}                                                                                                                                 
else                                                                                                                              
{                                                                                                                                 
printf("[ERROR] Invalid Bytes Object\n");                                                                                         
}                                                                                                                                 
}                                                                                                                                 
void print_python_list(PyObject *p)                                                                                               
{                                                                                                                                 
printf("[*] Python list info\n");                                                                                                 
 printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);                                                                        
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);                                                                  
for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)                                                                                       
{                                                                                                                                 
printf("Element %ld: %s\n", i, ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);                                               
if (strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name,"bytes") == 0)                                                           
print_python_bytes(((PyListObject *)p)->ob_item[i]);                                                                            
}                                                                                                                                 
}                                                                                                                                 
                   
