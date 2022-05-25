#include <iostream>
#include <map>
using namespace std;

// 柳: 只能有一个P一个T，中间末尾和开头可以随便插入A。
// 但是必须满足开头的A的个数 * 中间的A的个数 = 结尾的A的个数，
// 而且P和T中间不能没有A～
int main()
{
    int n, p = 0, t = 0;
    cin >> n;
    string s;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        map<char, int> m;
        for (int j = 0; j < s.size(); j++)
        {
            m[s[j]]++;
            if (s[j] == 'P') p = j;
            if (s[j] == 'T') t = j;
        }
        if (m.size() == 3 && m['P'] == 1 && m['T'] == 1 && p < t - 1 && p * (t - p - 1) == s.size() - t - 1)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
