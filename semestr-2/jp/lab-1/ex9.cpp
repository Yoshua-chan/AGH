#include <iostream>

int main() {
    double n, m;
    do {
        std::cout << "podaj n: ";
        std::cin >> n;
    } while(n <= 0);

    do {
        std::cout << "podaj m: ";
        std::cin >> m;
    } while(m <= 0);

    double current {};

    while(true){
        current += n;
        if (current > m)
            break;
        std::cout << current << " ";
    }
}