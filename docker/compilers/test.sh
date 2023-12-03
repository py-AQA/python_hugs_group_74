#!/bin/bash
echo --== Free Pascal ==--
fpc hw_pascal.pas
./hw_pascal

echo --== GNU C++ ==--
g++ -o hw_cpp hw_cpp.cpp
./hw_cpp

echo --== DMD D ==--
dmd hw_d.d
./hw_d

echo --== Mono C# ==--
mcs hw.cs
mono hw.exe

echo --== Python ==--
./hw_python.py
