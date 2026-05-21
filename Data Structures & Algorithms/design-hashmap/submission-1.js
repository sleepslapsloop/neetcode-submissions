class MyHashMap {
    constructor() {
        this.hashMap = new Map();
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        this.hashMap.set(key, value);
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (!this.hashMap.has(key)) {
            return -1;
        } else return this.hashMap.get(key);
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.hashMap.delete(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
