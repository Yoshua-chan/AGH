#include <iostream>
#include <cmath>

int main() {
    double a,b,c;

    std::cout << "Podaj wspolczynnik a: ";
    std::cin >> a;
    std::cout << "Podaj wspolczynnik b: ";
    std::cin >> b;
    std::cout << "Podaj wspolczynnik c: ";
    std::cin >> c;

    int delta = b * b - 4 * a * c;
    if(delta > 0) {
        double x1 = (-b - sqrt(delta)) / (2*a);
        double x2 = (-b + sqrt(delta)) / (2*a);
        std::cout << "x1: " << x1 << "\nx2: " << x2 << std::endl;
    } else if (delta == 0) {
        double x1 = (-b)/(2*a);
        std::cout << "x: " << x1 << std::endl;
    } else {
        std::cout << "No real roots\n";
    }
}