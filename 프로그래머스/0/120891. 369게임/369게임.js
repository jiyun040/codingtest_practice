function solution(order) {
    let count = 0;
    let targets = ['3', '6', '9'];

    for (let char of order.toString()) {
        if (targets.includes(char)) {
            count += 1;
        }
    }
    
    return count;
}