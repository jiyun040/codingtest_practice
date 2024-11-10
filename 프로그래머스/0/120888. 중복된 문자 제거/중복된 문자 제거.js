function solution(my_string) {
    let answer = [];
    my_string.split('').map(str =>{
        if(!answer.includes(str)){
            answer.push(str);
        }
    })
    return answer.join('');
}