using System;
using System.Text;

class HW {
    static void Main() {
        Console.OutputEncoding = Encoding.UTF8;
        Console.WriteLine("== Программа на C# ==");
        for(int i = 2; i <= 7; ++i)
            Console.WriteLine($"Квадрат числа {i} равен {i * i}");
    }
}