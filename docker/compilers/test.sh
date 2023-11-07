#!/bin/bash
echo --== Free Pascal ==--
fpc hw_pascal.pas
./hw_pascal

echo --== GNU C++ ==--
g++ -o hw_cpp hw_cpp.cpp
./hw_cpp

echo --== Python ==--
./hw_python.py
