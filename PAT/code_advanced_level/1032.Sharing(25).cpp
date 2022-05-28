#include<iostream>
using namespace std;

struct NODE
{
    char key;
    int next;
    bool flag;
}node[100000];

int main()
{
    int n1, n2, n;
    scanf("%d%d%d", &n1, &n2, &n);
    char data;
    int a, b;
    for (int i = 0; i < n; i++)
    {
        scanf("%d %c %d", &a, &data, &b);
        node[a] = {data, b, false};
    }
    for (int i = n1; i != -1; i = node[i].next)
    {
        node[i].flag = true;
    }
    for (int i = n2; i != -1; i = node[i].next)
    {
        if (node[i].flag == true)
        {
            printf("%05d", i);
            return 0;
        }
    }
    printf("-1");
    return 0;
}
