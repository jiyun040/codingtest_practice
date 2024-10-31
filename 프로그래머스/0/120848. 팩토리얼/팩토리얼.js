function solution(n) {
    let i = 1;
    let facto = 1;
    while(facto <= n) {
        i += 1;
        facto *= i;
    }
    return i - 1;
}