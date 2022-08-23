cmake_minimum_required(VERSION 3.4)
project(Project_Bind)
add_subdirectory(pybind11)
pybind11_add_module(module_name add_fun.cpp)


