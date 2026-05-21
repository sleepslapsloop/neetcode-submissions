class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let res = [];
        let hashMap = new Map();
        for (let num of nums) {
            hashMap.set(num, (hashMap.get(num) || 0) + 1);
        }
        hashMap = [...hashMap].sort((a, b) => b[1]-a[1])
        for(let i = 0; i < k; i++){
            res.push(hashMap[i][0]);
        }
        return res;
    }
}
