class Solution {
    // // 1. O(∩^2) t:12ms(16%) m:44.5M(93%) array 尾插
    // public List<Integer> grayCode(int n) {
    //     List<Integer> ans = new ArrayList<>();
    //     ans.add(0);
    //     while (n-- > 0) {
    //         int m = ans.size();
    //         for (int i = m - 1; i >= 0; i--) {
    //             ans.set(i, ans.get(i) << 1);
    //             ans.add(ans.get(i) + 1);
    //         }
    //     }
    //     return ans;
    // }
    
    // 2. O(∩^2) t:6ms(73%) m:45.6M(42%) array 首插
    public List<Integer> grayCode(int n) {
        List<Integer> ans = new ArrayList<>();
        ans.add(0);
        int num = 1;
        while (n-- > 0) {
            int m = ans.size();
            for (int i = m - 1; i >= 0; i--) {
                ans.add(ans.get(i) + num);
            }
            num *= 2;
        }
        return ans;
    }
}