#include<stdio.h>
#include<Python.h>
#include<math.h>
#include <stdio.h>
#include <stdlib.h>	

static PyObject *rcmdError;
int run_cmd(char *cmd)
{
	system(cmd);
}

static PyObject* run_cmd_py(PyObject *self,PyObject *args)
{
	char *n;
	if(!PyArg_ParseTuple(args,"s",&n))
	{
		return NULL;
	}
	else
	{
		return Py_BuildValue("s",run_cmd(n));
	}
}

static PyMethodDef rcmdMethods[]=
{
	{"run_cmd_py",run_cmd_py,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initrcmd()
{
	Py_InitModule("rcmd",rcmdMethods);
}
