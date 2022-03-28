#include <iostream>
#include <string>

int main() {
    std::string formula;
    std::cin >> formula;
    int pos{};

    while((pos = formula.find(" ", 0)) != std::string::npos) {
        formula.erase(pos);
        std::cout << formula << std::endl;
    }

    
}