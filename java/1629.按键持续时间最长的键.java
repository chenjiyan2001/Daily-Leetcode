class Solution {
    // 1. O(n) t:1ms(90%) m:38.5M(41%)
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int max_t = releaseTimes[0];
        char max_k = keysPressed.charAt(0);
        for (int i = 1; i < releaseTimes.length; i++){
            int t = releaseTimes[i] - releaseTimes[i-1];
            char k = keysPressed.charAt(i);
            if (t > max_t) {
                max_t = t;
                max_k = k;
            }else if (t == max_t && k > max_k){
                max_k = k;
            }
        }
        return max_k;
    }
}