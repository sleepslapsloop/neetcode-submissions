class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    

    isValid(s) {
        function closingOf(str) {
            if (str === '(') return ')';
            else if (str === '{') return '}';
            else if (str === '[') return ']';
            else return -1;
        }
        
        if (s.length % 2 === 1) return false;

        let stack = [];
        for (let i = 0; i < s.length; i++) {
            if (['(', '{', '['].includes(s[i])) {
                stack.push(s[i]);
            } else {
                if (closingOf(stack.pop()) !== s[i]) return false;
            }
        }
        return (stack.length === 0);
    }
}
