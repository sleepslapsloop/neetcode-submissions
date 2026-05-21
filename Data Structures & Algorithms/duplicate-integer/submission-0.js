class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let numsAsSet = new Set(nums);
        if (nums.length > numsAsSet.size) return true;
        else return false;
    }
}
