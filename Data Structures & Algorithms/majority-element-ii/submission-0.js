class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        const n = Math.floor(nums.length / 3);
        let arr = [];

        let map = new Map();
        for (let val of nums) {
            map.set(val, map.get(val) + 1 || 1);
        }

        map.forEach(
            (val, key) => {
                if (val > n) {
                    arr.push(key);
                }
            }
        )

        return arr;
    }
}
