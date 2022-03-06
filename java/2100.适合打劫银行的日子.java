class Solution {
    // [题解]1. O(n) t:7ms(74%) O(n) m:60.4M(5%)
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        int n = security.length;
        int[] l = new int[n], r = new int[n];
        for (int i = 1; i < n; i++){
            if (security[i] <= security[i - 1]){
                l[i] = l[i - 1] + 1;
            }
            if (security[n - i - 1] <= security[n - i]){
                r[n - i - 1] = r[n - i] + 1;
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++){
            if (l[i] >= time && r[i] >= time){
                ans.add(i);
            }
        }
        return ans;
    }
}