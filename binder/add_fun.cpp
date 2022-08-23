#include<iostream>
#include<pybind11/pybind11.h>

namespace py = pybind11;

float add_fun(float arg1, float arg2){
	return arg1+arg2;
}

PYBIND11_MODULE(module_name, handle) {
	handle.doc() = "This is the module document";
	handle.def("Add_Py", &add_fun);
}

