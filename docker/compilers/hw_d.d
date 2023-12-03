import std.stdio;

void main() {
    writeln("== Программа на D ==");
    for(int i = 2; i <= 7; ++i)
        writeln("Квадрат числа ", i, " равен ", i * i);
}