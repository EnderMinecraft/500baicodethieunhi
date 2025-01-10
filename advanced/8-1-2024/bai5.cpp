#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string datei;
    std::cout << "Date(dd/mm/yyyy): ";
    std::getline(std::cin, datei);

    std::stringstream ss(datei);
    std::string segment;
    std::vector<std::string> date_parts;

    while (std::getline(ss, segment, '/')) {
        date_parts.push_back(segment);
    }

    std::cout << "Ngày " << date_parts[0] << " tháng " << date_parts[1] << " năm " << date_parts[2] << std::endl;

    return 0;
}