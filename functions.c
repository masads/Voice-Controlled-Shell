#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
void run_command(char* command)
{	printf("%s \n",command);
    system(command);

}

char * checkFile(char* filename,char *path)
{
	struct dirent *de; 
	DIR *dr = opendir(path);
	if (dr == NULL) 
	{
		printf("Could not open current directory" );
		return 0;
	}
	char string[256]=" ";
	while ((de = readdir(dr)) != NULL)
	{
			if(strcasecmp(de->d_name,filename)==0)
			{
				strcpy(string, de->d_name);
				break;
			}
	}
	closedir(dr);	
     	char *result = (char *)malloc(strlen(string)+1);
    	strcpy(result,string);
	return result;
}
void crtFileOrDirec(char * filename,char * path, char * command)
{
    char *filename1 = (char *)malloc(strlen(filename)+1);
    filename1=checkFile(filename,path);
    struct stat buffer;
    int exist = stat(filename1,&buffer);
    if (exist == 0){

         printf("%s already exsists \n",filename1);
        return ;
    }else
    {
    	run_command(command);
    	printf("file created successfully");
    	return ;
    }

    printf("Error in making file or directory\n");

}






