#include<iostream>
int main() {
    int a, b;
    std::cin >> a >> b;
    std::string s = std::to_string(a + b);
    int l = s.length();
    for (int i = 0; i < l; i++) {
        std::cout << s[i];
        if (s[i] == '-') continue;
        if ((i + 1) % 3 == l % 3 && i != l - 1) std::cout << ",";
    }
    return 0;
}
