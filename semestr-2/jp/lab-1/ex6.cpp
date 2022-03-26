#include <iostream>
#include <cinttypes>

int main() {
    uint64_t liczba;

    std::cin >> liczba;
    for(int i = 0; i < sizeof(liczba) * 8; i++) {
        if(((1 << (63 - i)) & liczba) != 0)
            std::cout << "1";
        else
            std::cout << "0";

        if(i % 4 == 3)
            std::cout << " ";
    }

}