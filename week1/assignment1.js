

// console.log("hello world");

function ExpendPanelToggle(params) {
    console.log("expand panel");
    // getElementById
    // document.getElementById("hamburger").style.backgroundColor = "red";
    
    // getElementsByClassName: 注意回傳的是 array
    // document.getElementsByClassName("navbar_right").item(0).style.backgroundColor = "green";
   

    // document.getElementsByClassName("panel").item(0).style.position = "fixed";
    // document.getElementsByClassName("navbar_item").style.display = "inherit";

    var items = document.getElementsByClassName('navbar_item');
    // console.log(items[0].style.display);
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
    
    


    document.getElementsByClassName("navbar_right").item(0).classList.toggle('panel_expand');

    // console.log(document.getElementsByClassName("navbar_right").item(0));
    if(document.getElementsByClassName("navbar_right").item(0).classList.contains("panel_expand")){
        // console.log("yes");
        document.getElementsByClassName("topright_btn").item(0).innerHTML = "<p onclick='ExpendPanelToggle()'>X</p>";

    }else{
        // console.log("no");
        document.getElementsByClassName("topright_btn").item(0).innerHTML = '<img id="hamburger" onclick="ExpendPanelToggle()" src="./img/hamburger.png" alt="hamburger"></img>';


    }

}