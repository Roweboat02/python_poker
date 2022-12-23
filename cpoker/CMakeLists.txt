cmake_minimum_required(VERSION 3.23)
project(cpoker)

set(CMAKE_CXX_STANDARD 14)

add_library(cpoker SHARED library.cpp assessor.h)
