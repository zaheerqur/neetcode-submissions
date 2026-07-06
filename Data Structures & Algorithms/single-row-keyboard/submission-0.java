class Solution {
    public int calculateTime(String keyboard, String word) {
        int[] position = new int[26];
        for (int i = 0; i < keyboard.length(); i++)
            position[keyboard.charAt(i) - 'a'] = i;

        int totalTime = 0;
        int currentIndex = 0;

        for (char c : word.toCharArray()) {
            int targetIndex = position[c - 'a'];
            totalTime += Math.abs(targetIndex - currentIndex);
            currentIndex = targetIndex;
        }

        return totalTime;
    }
}