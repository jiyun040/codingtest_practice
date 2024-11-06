function solution(numbers, k) {
    let people = 1;
    for(i = 0; i < k - 1; i++){
        people += 2;
        
        if(people > numbers.length){
            people -= numbers.length;
        }
    }
    return people;
}