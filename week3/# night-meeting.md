# 2024.04.15 night meeting

### 請分析第二週第一題程式的時間複雜度？

中醫師ellen分享~

可能變動因子:
- 捷運站主線站數x
- 支線站數y
- 不重複總站數s
- 訊息字數平均長度m
- messages數量n


時間複雜度

bigO notation
1. 隨著資料增加 執行時間受影響而增加的趨勢
2. 考慮最糟情形: worst case

ex:
- O(1): 常數 表示執行時間不會隨資料輸入變化而變化
``` javascript
function getFirst(arr){
    return arr[0];
}
```
- O(n): 線性 執行時間跟輸數資料成正比
``` javascript
function sumArr(arr){
    let total = 0;
    for(let num of arr){
        toral += num; //每個元素都要加到
    }
    return total;
}
```
- O(n^2): 平方時間 常見於雙重迴圈
``` javascript
function sumMatrix(martrix){
    let total = 0;
    for(let i = 0; i<matrix.length; i++){
        for(let j=0;j < matrix[i].length; j++){
            total += matrix[i][j];
        }
    }
    return total;
}
```


### JavaScript 的 var 和 let 差異？

1. var: 是「可」重複宣告相同變數，區塊語法用var宣告可能會感染全域變數。
2. let: 是「不可」重複宣告相同變數，其作用域僅在「區塊作用域(Block Scope)」，一旦離開則會無作用，顯示無定義。

var: function-scoped 函式作用域
var 是function scope ，console.log在函式外，無法在console.log(i)取到i

let: block-csoped 區塊作用域

``` javascript

var i = 0;

function test(){
    for(var i=0;i<3;i++){
       console.log("Hello");
    }
}
test();


```


### JavaScript 的 == 和 === 差異？

> 會連型別也比較
``` javascript
console.log(1 == '1'); // True
console.log(1 === '1'); // false
```

### 如何逐一取得物件中的 Key/Value Pairs 並印出來？
``` javascript

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};


for (const key in messages) {
    console.log(key+","+messages[key]);
}

Object.keys(messages);
Object.values(messages);

// js列出key/values的寫法
// console.log(Object.keys(messages));
// console.log(Object.values(messages));


let dict = {"a":1,"b":2, "c":3};
for (let key in dict) {
    console.log("key: "+key+" value: "+dict[key]);
}

for (key in dict) {
    console.log(`Key: ${key}, Value: ${dict[key]}`);
}

for (let [key,value] of Object.entries(dict)){
    console.log(key+":"+value);
}


```


### 如何把物件中的 Values 轉換成一個陣列儲存？

``` javascript

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};

values_array = []
for (const key in messages) {
    values_array.push(messages[key]);
}
console.log(values_array);

```


### Python 的 == 和 is 的差異？

== 是判斷兩個變數之間的『值』是否相同
is 是判斷兩個變數之間的『記憶體位址』是否相同。

<!-- 可以用id()查看記憶體位置

== 和 is 的返回值都一樣啊？
這是因為在 Python 中，在到 -5 ~ 256 的數值都是固定的記憶體位址，可以直接開兩個終端機分別看看，無論如何都是固定的，很有趣！不過從 257 開始，每個值都會有其申請的記憶體位址，也就是說每次都會不一樣。

```python
a = 1000
b = 1000

id(a)
140042294421360
id(b)
140042294420272

a == b
True
a is b
False -->


```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1
l4 = l1[:]
print(id(l1))
print(id(l2))
print(id(l3))
print(id(l4))
print(l1 == l2) # True
print(l1 is l2) # False
print(l1 is l3) # True
print(l1 is l4) # False
```

ref:
[小知識：== 和 is 的差異](https://clay-atlas.com/blog/2020/08/04/python-cn-equal-is-difference/)



### Python 的 pass 指令有什麼作用？
pass：不做任何事情，所有的程式都將繼續[^1]

pass 就像是 To do 的概念，在寫程式的時候，有時候想的比實際寫出來的速度快，例如定義一個函數，但還沒有實作出來，空著內容不寫又會產生語法錯誤🤦‍♂️，這時就會使用 pass 來替代，當作是個指標，提醒自己之後要來完成。

Python pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句[^2]。

```python
def get_function():
    pass

get_function()
```

ref:

[^1]: [1 分鐘搞懂 Python 迴圈控制：break、continue、pass](https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8)

[^2]: [Python pass 语句](https://www.runoob.com/python/python-pass-statement.html)

### 如何逐一取得字典中的 Key/Value Pairs 並印出來？

```python
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
print(type(messages))

for e in messages:
    print(e+":"+messages[e])

print(messages.keys())
```

### 如何把字典中的 Keys 轉換成一個列表儲存？

```python
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
print(type(messages))

values = [ messages[key] for key in messages ]

values2 = [ key for key in messages.items() ]

print(values)
print(values2)
# ["I'm at home near Xiaobitan station.", "I'm at Ximen MRT station.", 'I have a drink near Jingmei MRT station.', 'I just saw a concert at Taipei Arena.', "I'm at Xindian station waiting for you."] 

```

### 變數命名的常見規則/習慣有哪些？
camel
underscore
function name begins with verb

JavaScript 使用駝峰式命名：stationName
Python 使用下畫線命名：station_name

函式宣告：使用動詞開頭
避免使用保留字，例如不要用 let

Class 類別命名：首字母都大寫
Constant 常數：都大寫，可以用底線隔開單字