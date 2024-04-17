

// console.log("hello world");

// 處理展開右上角panel
function ExpendPanelToggle(params) {
    // console.log("expand panel");
    
    // getElementsByClassName: 注意回傳的是 array
    // document.getElementsByClassName("panel").item(0).style.position = "fixed";
    // document.getElementsByClassName("navbar_item").style.display = "inherit";

    // 處理 navbar 在不同螢幕寬度下的行為
    var items = document.getElementsByClassName('navbar_item');
    // console.log(items[0].style.display);
    // 手機版時 navbar_item display是none; 非手機版時 navbar_item display是block
    if(items[0].style.display == ""){
        for (var i = 0; i < items.length; i++) {
            // console.log(items[i]);
            items[i].style.display = "flex";
        }
        document.getElementsByClassName("panel").item(0).style.display = "block";
    }else{
        for (var i = 0; i < items.length; i++) {
            // console.log(items[i]);
            items[i].style.display = "";
        }
        document.getElementsByClassName("panel").item(0).style.display = "flex";
    }
    
    // 點選hamburger 打開右上角 expand panel
    document.getElementsByClassName("navbar_right").item(0).classList.toggle('panel_expand');

    // console.log(document.getElementsByClassName("navbar_right").item(0));
    if(document.getElementsByClassName("navbar_right").item(0).classList.contains("panel_expand")){
        document.getElementsByClassName("topright_btn").item(0).innerHTML = "<p onclick='ExpendPanelToggle()'>X</p>";
    }else{
        document.getElementsByClassName("topright_btn").item(0).innerHTML = '<img id="hamburger" onclick="ExpendPanelToggle()" src="./img/hamburger.png" alt="hamburger"></img>';
    }
}

function CreateImg(imgUrl,imgTitle,imgClass){
    
    // img
    let newImg = document.createElement("img");
    newImg.classList.add(imgClass);
    newImg.src = imgUrl;
    newImg.alt = imgTitle;
    // console.log(newImg);
    return newImg;
}

function CreateP(title){
    
    // text
    let newP = document.createElement("p");
    newP.classList.add("text");
    let newTitle = document.createTextNode(title);  
    newP.appendChild(newTitle); 
    // console.log(newP);
    return newP;
}


function loadMore(){
    // document.querySelector('mark:last-child')
    
    let parent = document.querySelector(".main");
    let loadBtn = document.querySelector("#moreBtn");
    let newBbwrapper = document.createElement("div");
    newBbwrapper.classList.add("bbwrapper");
    
    let end = 10;
    if(titles.length<10){
        end = titles.length;
        loadBtn.innerHTML = "已經到底了";
        loadBtn.classList.add("disabled");
    }
    for (let i =0; i < end; i++) {
        let newBigbox = document.createElement("div");
        newBigbox.classList.add("bb");
        if(i==8){
            newBigbox.classList.add("bb_wide1");
        }else if(i==9){
            newBigbox.classList.add("bb_wide2");
        }
        
        let newStar = CreateImg(imgUrl="./img/star.png", imgTitle="star", imgClass="star");
        let newImg = CreateImg(imgUrl=imgUrls[i], imgTitle=titles[i], imgClass="spot");
        let newP = CreateP(title=titles[i]);

        // add the newly created element and its content into the DOM
        newBigbox.appendChild(newStar);
        newBigbox.appendChild(newImg);
        newBigbox.appendChild(newP);
        // lastBbwrapper.insertBefore(newBigbox, lastBigbox.nextSibling);
        newBbwrapper.appendChild(newBigbox);
        
    }
    parent.insertBefore(newBbwrapper, loadBtn);
    for(let i=0;i<end;i++){
        // remove the items form the list.
        titles.shift();
        imgUrls.shift();
    }

}

// 處理 fetch
let dataUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";
let imgUrls = [];
let titles = [];
fetch(dataUrl)
    .then(function(response){
        // return response.text();
        return response.json();
    }).then(function(data){
        // console.log(data.data.results);
        return target = data.data.results;
        
    }).then(function(target){

        // 取得資料後做的事情: 
        for(let i=0;i<target.length;i++){
            // 處理圖片網址
            // console.log(target[i].filelist);
            let imgs = target[i].filelist;
            let targetImgUrl = "https://"+imgs.split("https://")[1];
            // console.log(targetImgUrl);
            imgUrls.push(targetImgUrl);

            // 處理景點名稱
            let title = target[i].stitle;
            // console.log(title);
            titles.push(title);
        }

        // why 如果寫在外面會是空?
        // console.log(titles);
        // console.log(imgUrls);

        // 處理 render 圖片

        // smallboxes
        // console.log(document.querySelectorAll(".sb").length);
        let smallboxes = document.querySelectorAll(".sb");
        // console.log(smallboxes.length);
        for (let i =0; i < smallboxes.length; i++) {

            let newImg = CreateImg(imgUrl=imgUrls[i], imgTitle=titles[i], imgClass="spot");
            let newP = CreateP(title=titles[i]);

            // add the newly created element and its content into the DOM
            smallboxes[i].appendChild(newImg);
            smallboxes[i].appendChild(newP);
        
        }
        for(let i=0;i<smallboxes.length;i++){
            // remove the items form the list.
            titles.shift();
            imgUrls.shift();
        }
        // console.log(titles.length);
        // console.log(titles);

        let bigboxes = document.querySelectorAll(".bb");
        // console.log(bigboxes.length);
        for (let i =0; i < bigboxes.length; i++) {
            
            let newStar = CreateImg(imgUrl="./img/star.png", imgTitle="star", imgClass="star");
            let newImg = CreateImg(imgUrl=imgUrls[i], imgTitle=titles[i], imgClass="spot");
            let newP = CreateP(title=titles[i]);

            // add the newly created element and its content into the DOM
            bigboxes[i].appendChild(newStar);
            bigboxes[i].appendChild(newImg);
            bigboxes[i].appendChild(newP);
            
        }
        for(let i=0;i<bigboxes.length;i++){
            // remove the items form the list.
            titles.shift();
            imgUrls.shift();
        }
        // console.log(titles.length);
        // console.log(titles);
    });




