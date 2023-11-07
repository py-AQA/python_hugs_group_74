#include <iostream>

int main() {
    std::cout << "== Программа на C++ ==" << std::endl;
    for(int i = 2; i <= 7; ++i)
        std::cout << "Квадрат числа " << i << " равен " << i * i << std::endl;
    return 0;
}
