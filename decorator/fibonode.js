var time = require('time');

function fibonaci(n){
    if(n==0){
        return 0;
    }
    else if(n==1){
        return 1;
    }
    else{
        return fibonaci(n-1) + fibonaci(n-2);
    }
}

console.time("fibotime");
var value = fibonaci(45);
var t2 = time.time();
console.timeEnd("fibotime");
console.log('Return value : ' + value.toString());
