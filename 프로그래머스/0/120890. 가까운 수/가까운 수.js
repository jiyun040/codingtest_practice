function solution(array, n) {
    array.sort((a, b) => {
        const differA = Math.abs(a - n); 
        const differB = Math.abs(b - n); 

        if (differA === differB) {
            return a - b;
        }
        return differA - differB;
    });
    return array[0];
}