#include <Python.h>
#include <string>
#include <iostream>

using namespace std;

extern "C"
const char *return_string(char* name){
    cout<<strlen(name)<<endl;
    cout<<name<<endl;
    static string s = "hello ";
    s += name;
    return s.c_str();
}