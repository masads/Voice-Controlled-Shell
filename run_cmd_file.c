#define PY_SSIZE_T_CLEAN
#include<stdio.h>
#include<Python.h>
#include<stdlib.h>	


static PyObject* run_cmd_py(PyObject *self,PyObject *args)
{
	char *cmd;
	if(!PyArg_ParseTuple(args,"s",&cmd))
	{
		return NULL;
	}
	else
	{
		system(cmd);
		return PyLong_FromLong(0);
	}
}

static PyMethodDef rcmdMethods[]=
{
	{"run_cmd_py",run_cmd_py,METH_VARARGS},
	{NULL,NULL,0,NULL}
};
static PyModuleDef rcmdModule = {
    PyModuleDef_HEAD_INIT, "rcmd", NULL, -1, rcmdMethods,
    NULL, NULL, NULL, NULL
};
PyMODINIT_FUNC
PyInit_rcmd(void)
{
    return PyModule_Create(&rcmdModule);
}
//static PyObject* PyInit_rcmd(void)
//{
//    return PyModule_Create(&rcmdModule);
//}
//PyMODINIT_FUNC initrcmd()
//{
//Py_InitModule("rcmd",rcmdMethods);
//}

int main()
{
	PyImport_AppendInittab("rcmd", PyInit_rcmd);
	Py_Initialize();
	PyImport_ImportModule("rcmd");

}
