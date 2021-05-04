#include <stdio.h>
#include <stdlib.h>	//to use system()
#include <string.h> //to use strcpy()

int main()
{
	char cmd[100];
	sprintf(cmd, "/bin/ls ls");
	system(cmd);
}