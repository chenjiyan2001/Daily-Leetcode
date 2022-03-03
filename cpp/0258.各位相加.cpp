class Solution {
public:
    // // 1. O(lognum) t:4ms(40%) O(1) m:5.8M(86%)
    // int addDigits(int num) {
    //     while (num > 9){
    //         int sum = 0;
    //         while (num > 0){
    //             sum += num % 10;
    //             num /= 10;
    //         }
    //         num = sum;
    //     }
    //     return num;
    // }

    // [题解]2. O(lognum) t:0ms(100%) O(1) m:5.9M(14%)
    int addDigits(int num) {
        while (num > 9){
            int sum = 0;
            while (num > 0){
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
};