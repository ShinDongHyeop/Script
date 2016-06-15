#include "python.h" 
#include <stdio.h>

static PyObject *

comprare(const void* a, const void* b) {
	return strcmp((char*)a, (char*)b);
}

spam_listsort(PyObject *self, PyObject *args)
{
	
	char strlist[1000][1000];
    const char* str=NULL;
	char strsend[1000];
    int size = 0; 
	int len = 0;
	char tempstr[1000];
    if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 
	int i;
	for (i = 0; str[i] != '\0'; ++i)
	{
		if (str[i] == ',')
			size++;
		tempstr[i] = str[i];
	}
	tempstr[i] = '\0';

	for (i = 0; tempstr[i] != '\0'; ++i)
	{
		int j;
		if (tempstr[i] == '\'')
		{
			int z = 0;
			for (j = i + 1; tempstr[j] != '\''; ++j)
				strlist[len][z++] = tempstr[j];
			strlist[len][z] = '\0';
			i = j;
			len++;
		}
	}

	qsort(strlist, len, sizeof(strlist[0]), comprare);

	int z = 0;
	strsend[z++] = '[';
	for (int i = 0; i < len; ++i)
	{
		strsend[z++] = '\'';
		for (int j = 0; strlist[i][j] != '\0'; ++j)
			strsend[z++] = strlist[i][j];
		strsend[z++] = '\'';
		strsend[z++] = ',';
	}
	strsend[z++] = ']';
	strsend[z] = '\0';
	
	

    return Py_BuildValue("s", strsend);
}



static PyMethodDef SpamMethods[] = {
{"strlen", spam_listsort, METH_VARARGS,
 "count a string length."},
 {NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
