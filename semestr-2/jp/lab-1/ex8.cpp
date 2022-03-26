#include <iostream>

int main() {
    while(true) {
        char op;
        double a{}, b{}, result{};

        std::cout << "op: ";
        std::cin >> op;

        if(op == 'q' || op == 'Q')
            return 0;

        std::cout << "a: ";
        std::cin >> a;
        std::cout << "b: ";
        std::cin >> b;

        switch(op) {
            case '*':
                result = a * b;
            break;
            case '/':
                result = a / b;
            break;
            case '+':
                result = a + b;
            break;
            case '-':
                result = a - b;
            break;
            case 'Q':
            case 'q':
                return 0;
            break;
        }

        std::cout << a << op << b << "=" << result << std::endl << std::endl;
    }
}