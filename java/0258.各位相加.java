class Solution {
    // // 1. O(lognum) t:0ms(100%) O(1) m:38.8M(11%)
    // public int addDigits(int num) {
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

    // 2. O(1) t:0ms(100%) O(1) m:38.9M(10%)
    public int addDigits(int num) {
        int ans;
        if (num == 0){
            ans = 0;
        }else if(num % 9 == 0){
            ans = 9;
        }else{
            ans = num % 9;
        }
        return ans;
    }
}