#include <iostream>

int largest_dividor(int n) {
    int largest{};
    for(int i = 1; i < n; i++) {
        if(n % i == 0)
            largest = i;
    }
    return largest;
}

int main() {
    int n{0};
    do {
        std::cout << "Wprowadz liczbe: ";
        std::cin >> n;
    } while(n <= 2);
    std::cout << largest_dividor(n) << std::endl;
}