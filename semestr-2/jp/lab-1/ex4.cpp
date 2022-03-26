#include <iostream>
#include <iostream>
#include <ctime>

int main() {
    srand(time(NULL));
    
    int number{rand() % 101}, lives{5};
    int guess{};
    
    while(lives > 0) {
        std::cout << "Podaj liczbe: ";
        std::cin >> guess;

        if(guess == number) {
            std::cout << "Zgadles!\n";
            return 0;
        }

        if(guess > number)
            std::cout << "Za duzo\n";
        else if(guess < number)
            std::cout << "Za malo\n";

        lives--;
    }

    std::cout << "przegrales :c\nprawidlowa liczba to " << number;
}