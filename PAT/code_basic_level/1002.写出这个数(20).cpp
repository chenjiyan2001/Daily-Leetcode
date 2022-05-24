#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    string str[10] = {"ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"};
    int res = 0;
    for (int i = 0; i < s.length(); i++)
    {
        res += s[i] - '0';
    }
    string num = to_string(res);
    for (int i = 0;  i < num.length(); i++)
    {
        if (i != 0) cout << " ";
        cout << str[num[i] - '0'];
    }
    return 0;
}
