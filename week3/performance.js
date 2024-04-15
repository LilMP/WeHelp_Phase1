// 影響程式執行最終花費時間的因素
/*
    - 跑了幾個loop
    - 策略遊戲: stellaris
    - 資料量大小
    - 網路速度
    - request來回
    - 硬體效能
    - 做了幾次加減乘除
    - 電腦目前的忙碌程度

    node performance.js

*/
// 測試javascript程式執行速度
// console.time();
// let n=1;
// while(n<1000){
//     n++;
// }
// console.timeEnd();

// 怎麼評估哪個演算法效率較好
/*
    要滿足兩個目標
    1. 排除硬體效能的影響 包括電腦目前的忙碌程度
    2. 資料量變大的時候所需要執行時間的成長幅度 (不在意資料量小的狀況)
/*
    輸入兩個未排序過的正整數陣列 找出從其中各取一個數字後 兩兩相乘的最大值

    時間複雜度
    // 2n^2+1 : 高
    // 4n+2: 中
    // 2nlogn: 低

    // 時間複雜度 time complexity
    // BigO Notation / omega notation / ...
    // BigO 講的是上限
    
    n^2 belong O(n^2) if 如果存在一個正整數常數n0 任何n>n0 那麼 c*n^2>4n+2
        n0取5時會成立 ---> 資料量的成長率
    4n+2 belong O(n) if 如果存在一個正整數常數n0 任何n>n0 那麼 c*n^2>4n+2

    f(n) belong O(g(n)) if there exists positive constant c, n0, where any n>n0, cg(n)>f(n)
    

*/

// 假設輸入的資料量分別是 n1 跟 n2
// 跟n1 n2無關的話 就是一個單位的時間(常數時間)

// function1: 2n1*n2+1
function maxProduct1(ns1,ns2){
    let max=ns1[0]*ns2[0]; // 1
    for(let i=0;i<ns1.length;i++){
        for(let j=0;j<ns2.length;j++){
            // n1*n2
            if(ns1[i]*ns2[j]>max){ // 1: 判斷
                max=ns1[i]*ns2[j] // 1: 乘法
            }
        }
    }
    console.log(max);
}
// 1+2n+1+2n = 4n+2
function maxProduct2(ns1,ns2){
    let max1=ns1[0]; //1
    for(let i=0;i<ns1.length;i++){ //2n
        if(ns1[i]>max1){
            max1=ns1[i];
        }
    }
    let max2=ns2[0]; //1
    for(let i=0;i<ns1.length;i++){ //2n
        if(ns2[i]>max2){
            max2=ns2[i];
        }
    }
    console.log(max1*max2);
}



// 1+2n+1+2n = 4n+2
function maxProduct22(ns1,ns2){
    let max1=ns1[0]; //1
    ns1.forEach((n)=>{
        if(n>max1){
            max1=n
        }
    });
    let max2=ns2[0]; //1
    ns2.forEach((n)=>{
        if(n>max2){
            max2=n
        }
    });
    console.log(max1*max2);
}



// 2nlogn
function maxProduct3(ns1,ns2){
    ns1.sort( (n1, n2)=>{return n2-n1;}); // nlogn
    ns2.sort( (n1, n2)=>{return n2-n1;}); // nlogn
    console.log(ns1[0]*ns2[0]);
}

// let data1=[3,1,5,2];
// let data2=[9,2,1,7];


let data1=[];
for(let i=0;i<100000000;i++){
    data1.push(parseInt(Math.random()*100+1));
}

let data2=[];
for(let i=0;i<100000000;i++){
    data2.push(parseInt(Math.random()*100+1));
}

// console.time();
// maxProduct1(data1,data2);
// console.timeEnd();

console.time();
maxProduct2(data1,data2);
console.timeEnd();

console.time();
maxProduct22(data1,data2);
console.timeEnd();

// console.time();
// maxProduct3(data1,data2);
// console.timeEnd();

