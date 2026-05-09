class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]) {

        // Variables
        let stack: [number, number][] = []// pair [temp, index]
        let res: number[] = new Array(temperatures.length).fill(0)
        
        for(let i = 0; i < temperatures.length; i++){
            const temp = temperatures[i] // get curr temp 
            while(stack.length > 0 && temp > stack[stack.length - 1][0]){
                const [stackTemp, stackIndex] = stack.pop()
                res[stackIndex] = i - stackIndex                
            }
            stack.push([temp, i])
        
        }
        return res

    }
}
