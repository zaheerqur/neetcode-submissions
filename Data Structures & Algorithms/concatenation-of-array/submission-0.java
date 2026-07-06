class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = 2 * nums.length;
        int[] ans = new int[length];
        for (int i = 0; i < length / 2; i++) {
            ans[i] = nums[i];
        }
        for (int i = length / 2, j = 0; i < length; i++, j++) {
            ans[i] = nums[j];
        }
        return ans;
    }
}