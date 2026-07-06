class Solution {
    /**
     * @param {string} keyboard
     * @param {string} word
     * @return {number}
     */
    calculateTime(keyboard, word) {
        const position = {};
        for (let i = 0; i < keyboard.length; i++)
            position[keyboard[i]] = i;

        let totalTime = 0;
        let currentIndex = 0;

        for (const c of word) {
            const targetIndex = position[c];
            totalTime += Math.abs(targetIndex - currentIndex);
            currentIndex = targetIndex;
        }

        return totalTime;
    }
}