class Solution {
    // O(1) t:0ms(100%) m:35.4M(15%)
    public int totalMoney(int n) {
        int week = n / 7;
        int day = n % 7;
        return 28 * week + week*(week-1)*7/2 + day*(day+1+2*week)/2;
    }
}