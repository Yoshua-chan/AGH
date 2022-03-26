#include <iostream>

int main() {
    int periods {};
    double money{}, interest{};
    std::cout << "Podaj poczatkowy kapital: ";
    std::cin >> money;
    std::cout << "Podaj liczbe okresow kapitalizacji: ";
    std::cin >> periods;
    std::cout << "Podaj oprocentowanie (w %): ";
    std::cin >> interest;
    
    for(int i = 0; i < periods; i++) {
        money *= 1 + (interest/100.0);
    }

    std::cout << "Kapital po wszystkich okresach kapitalizacji wynosi: " << money << std::endl;
}