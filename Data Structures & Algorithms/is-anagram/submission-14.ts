class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {

        if (s.length != t.length)
            return false

        let map = new Map<string, number>()

        for (let i = 0; i < s.length; i++){
            let sChar = s[i]
            let tChar = t[i]    

            map.set(sChar, (map.get(sChar) ?? 0) + 1); // if null or undefined set to 0
            map.set(tChar, (map.get(tChar) ?? 0) - 1);
        }    

        // compare values, if all 0 return true
        for (const value of map.values()){
            if (value !== 0)
                return false
        }

        return true
    }
}
