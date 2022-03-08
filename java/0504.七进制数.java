class Solution {
    public String convertToBase7(int num) {
        boolean flag = num < 0;
        if (flag) num = -num;
        StringBuilder ans = new StringBuilder();
        do {
            ans.append(num % 7);
            num /= 7;
        } while (num > 0);
        ans.reverse();
        return flag ? '-' + ans.toString() : ans.toString();
    }
}