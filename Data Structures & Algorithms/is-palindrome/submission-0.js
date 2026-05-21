class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const cleaned = s.replace(/[^a-z0-9]/gi, '').toLowerCase();
        const len = cleaned.length;
        for (let i = 0; i < Math.floor(len / 2); i++) {
            if (cleaned[i] !== cleaned[len - 1 - i]) return false;
        }
        return true;
    }
}
