class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prod = 1, zeros = 0;
        for (let num of nums) {
            if (num === 0) {
                zeros++;
            } else {
                prod *= num;
            }
        }
        let ans = new Array(nums.length).fill(0);
        if (zeros > 1) {
            return ans;
        } else if (zeros === 1) {
            for (let i = 0; i < nums.length; i++) {
                nums[i] === 0 ? ans[i] = prod : ans[i] = 0;
            }
        } else {
            for (let i = 0; i < nums.length; i++) {
                ans[i] = prod / nums[i];
            }
        }
        return ans;
    }
}
