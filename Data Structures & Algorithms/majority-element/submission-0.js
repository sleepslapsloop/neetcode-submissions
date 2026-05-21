class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let freq = new Map();
        for (let num of nums) {
            freq.set(num, (freq.get(num) || 0)+1);
        }
        let n = Math.floor(nums.length/2);
        let majElem = 0;
        freq.forEach((value, key) => {
            if (value > n) {
                majElem = key;
            }
        });
        return majElem;
    }
}
