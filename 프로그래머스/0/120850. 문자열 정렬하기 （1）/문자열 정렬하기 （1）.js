function solution(my_string) {
    var answer = [];
    for(let char of my_string){
        if(!isNaN(char)){
            answer.push(parseInt(char));
        }
    }
    answer.sort((a, b) => a - b);
    return answer;
}