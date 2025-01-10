#include <iostream>
#include <vector>
#include <set>
#include <string>

int main() {
    std::vector<int> d;
    for (int i = 100; i < 477; ++i) {
        if (i % 2 == 0) {
            std::string str_i = std::to_string(i);
            std::set<char> unique_digits(str_i.begin(), str_i.end());
            if (unique_digits.size() == 3) {
                d.push_back(i);
            }
        }
    }
    for (int num : d) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    std::cout << d.size() << std::endl;
    return 0;
}