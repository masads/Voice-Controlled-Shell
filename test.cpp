#include <iostream>
#include <pybind11/embed.h>

namespace py = pybind11;
using namespace std;

int main()
{
    cout<<"C++"<<endl;
    py::scoped_interpreter guard{};
    py::exce(r"(
        print("hello")
    )");
}