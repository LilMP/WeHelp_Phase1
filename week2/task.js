


// task1

const green_line_stations = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian","Xiaobitan"];

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};

// let friends_location = ["","","Copper","","","","","Bob","","","","","","","Mary","","","","Vivian","Leslie"];

let friends_location=[];

for (const key in messages) {
    // if (Object.hasOwnProperty.call(messages, key)) {
    //     const element = messages[key];
    //     console.log(element);
    // }
    // console.log(messages[key]);
    let friend_idx = green_line_stations.map(e => messages[key].search(e)).findIndex(e => e>-1)
    friends_location[friend_idx] = key;
}
// console.log(friends_location);

let friends_index = [];
for (let index = 0; index < friends_location.length; index++) {
    if(friends_location[index]!== undefined){
        friends_index.push(index);
    }
}
console.log(friends_index);



function calulateStops(friend, current){
    // 確認存在
    // console.log("friend: "+friend);
    // console.log("current: "+current);

    let stop_count;

    // 朋友在小碧潭、自己不在小碧潭
    if(friend==19 & current!=19){
        // 計算從七張到自己所在地的間隔站數後+1
        stop_count = Math.abs(16 - current)+1;
    }
    // // 朋友在小碧潭、自己在小碧潭
    // else if(friend==19 & current==19){
    //     stop_count = 0;
    // }
    // 朋友不在小碧潭、自己在小碧潭
    else if(friend!=19 & current==19){
        stop_count = Math.abs(friend - 16)+1;
    }
    // 朋友不在小碧潭、自己不在小碧潭 OR 朋友在小碧潭、自己在小碧潭
    else {
        stop_count = Math.abs(friend - current);
    }

    // 計算站數
    // let stop_count = green_line_stations.indexOf(start) - green_line_stations.indexOf(end);

    return stop_count;
}

function findAndPrint(messages, currentStation){
    // your code here
    // 找到自己位置的捷運站 index
    let current_index = green_line_stations.indexOf(currentStation);


    let distance = friends_index.map( e => calulateStops(e,current_index )) ;
    // console.log(distance);
    
    // console.log(Math.min(...distance));
    // 朋友所在站的index
    // console.log(friends_index[distance.indexOf(Math.min(...distance))]);
    // console.log("the nearst is:")
    console.log(friends_location[friends_index[distance.indexOf(Math.min(...distance))]]);
    // console.log(green_line_stations[friends_index[distance.indexOf(Math.min(...distance))]]);
    // console.log("stop count: "+Math.min(...distance));
    
}




console.log("=== task1 ===");

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// task2

let time_table = Array.from({length: 24}, (_, i) => ["John","Bob","Jenny"]);

// console.log(time_table);
// console.log(time_table[15]);

function compare(available_consultants, criteria){

    if(available_consultants==""){
        return "no service";
    }
    if(criteria=="price"){
        // return lowest price from available_consultants
        return available_consultants.reduce((a, b ) => a.price < b.price ? a : b).name;

    }else if(criteria=="rate"){
        // return highest rate from available_consultants
        return available_consultants.reduce((a, b ) => a.rate > b.rate ? a : b).name;
    }else{
        return "exception";
    }
}

function book(consultants, hour, duration, criteria){
    // your code here
    
    // get who is available with the hour/duration
    // 取出各個時段有空的顧問
    let available_consultants = [];
    for (let index = hour; index < hour+duration; index++) {
        available_consultants.push(time_table[index]);
    }
    // console.log(available_consultants);

    // 取交集,得到可預約的顧問名單
    available_consultants_list = available_consultants.reduce((a, b) => a.filter(c => b.includes(c)));
    // console.log("return available consultant name:");
    // console.log("可預約的顧問名單");
    // console.log(available_consultants_list);

    // var options = ["a", "b"];
    // var results = ["c", "b", "a"];
    // var filtered = results.filter(result => options.indexOf(result) !== -1);

    let available_consultants_new = consultants.filter(consultant => available_consultants_list.indexOf(consultant.name) !== -1 )
    
    // return consultants based on criteria
    let recommendation = compare(available_consultants_new, criteria);
    // console.log("建議顧問:");
    console.log(recommendation);
    
    // update time_table
    for (let index = hour; index < hour+duration; index++) {
        let to_delete_index = time_table[index].indexOf(recommendation);
        if(to_delete_index!=-1){
            time_table[index].splice(to_delete_index,1);
        }
        // console.log(time_table[index]);
    }

    // print updated time_table
    // console.log(time_table);

}
const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];


console.log("=== task2 ===");
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John


// task3
function getMiddleName(name){
    let len = name.length;
    switch(len){
        case 2:
            return name[1];
        case 4:
            return name[2];
        default:
            return name[Math.floor(name.length/2)];
    }

}
function func(...data){
    // ...data的意思
    // The rest parameter (...) allows a function to treat an indefinite number of arguments as an array:
    let str = [];
    let count = [];
    for (let arg of data) {
        let middle = getMiddleName(arg);
        // console.log(middle);
        if(str.indexOf(middle)==-1){
            str.push(middle);
            count[str.indexOf(middle)]=1;
            // console.log(str);
            // console.log(count);
        }else{
            str.push(middle);
            count.push(-1); // 表示該位置前面已經加總過了
            count[str.indexOf(middle)]++;
            // console.log(str);
            // console.log(count);
        }
    }
    // console.log(str);
    // console.log(count);
    // unique: 找出count陣列中只出現過一次的index
    let unique = count.indexOf(1);
    
    if(unique!=-1){
        console.log(data[unique]);
    }else{
        console.log("沒有");
    }
    
}
console.log("=== task3 ===");
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安
// func("郭宣雅", "夏曼藍波安"); // print 夏曼藍波安

// task4

// 0,4,8,7,11,15,14,18,22,21,25...
// 取3餘數:
// 餘0: 前項-1
// 餘1: 前項+4
// 餘2: 前項+4

function getSequence(index){
    // 首項為0
    if(index == 0){
        return 0;
    }
    // 例外狀況
    else if(index<0){
        return false;
    }
    var idx = index%3;
    switch (idx) {
        case 1:
            // 餘1:前項+4
            return getSequence(index-1)+4;
            
        case 2: 
            // 餘2:前項+4
            return getSequence(index-1)+4;
            

        default:
            // 餘0:前項-1
            return getSequence(index-1)-1;
            
    }
}


function getNumber(index){
    console.log(getSequence(index));
}

console.log("=== task4 ===");
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70


// task5

let return_available_index = (stat) => {
    let available_car = [];
    for (let index = 0; index < stat.length; index++) {
        if(stat[index]==1) available_car.push(index);
    }
    return available_car;
}

function find(spaces, stat, n){
    // your code here
    

    for (let index = 0; index < stat.length; index++) {
        if(stat[index]==0) spaces[index]=-1;
    }
    // console.log(spaces);
    if(Math.max(...spaces) <n){console.log(-1);}
    else{
        // let smallest_i = 0;
        // for (let i = 0; i < spaces.length; i++) {
            
        //     if(spaces[i]>=n){
        //         if(spaces[smallest_i]>=spaces[i]){ smallest_i = i;}
        //     }else{
        //         smallest_i++;
        //     }   
            
        // }
        // let x = spaces.filter(e => e>=n);
        
        // console.log( spaces.indexOf(Math.min(...x)) );
        console.log(spaces.indexOf(Math.min(...spaces.filter(e => e>=n))));

        // console.log(spaces.findIndex(function(e){
        //     Math.min(e);
        // }));

        // console.log(smallest_i);
    }
    
    
}

console.log("=== task5 ===");
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
