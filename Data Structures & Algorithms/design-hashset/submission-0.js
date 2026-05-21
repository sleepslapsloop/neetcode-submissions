class MyHashSet {
    constructor() {
        this.hashSet = new Set();
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        this.hashSet.add(key);
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.hashSet.delete(key);
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        return this.hashSet.has(key)
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
