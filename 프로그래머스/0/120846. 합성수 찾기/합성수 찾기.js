function solution(n) {
    var answer = [];
    for(let i = 1; i <= n; i++){
        answer.push(i);
    }
    return answer.filter(n => {
        for(let i = 2; i < n; i++){
            if(n % i === 0)
                return n
        }
    }).length;
}