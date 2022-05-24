#include<iostream>
using std::scanf, std::printf;

int main() {
    float c[1001] = {0};
    int k, exp;
    float coef;
    scanf("%d", &k);
    for (int i = 0; i < k; i++) {
        scanf("%d%f", &exp, &coef);
        c[exp] += coef;
    }
    scanf("%d", &k);
    for (int i = 0; i < k; i++) {
        scanf("%d%f", &exp, &coef);
        c[exp] += coef;
    }
    int cnt = 0;
    for (int i = 0; i < 1001; i++) {
        if (c[i] != 0) cnt++;
    }
    printf("%d", cnt);
    for (int i = 1000; i >= 0; i--) {
        if (c[i] != 0.0) {
            printf(" %d %.1f", i, c[i]);
        }
    }
    return 0;
}
