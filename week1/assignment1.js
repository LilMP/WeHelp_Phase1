

console.log("hello world");

function ExpendPanelToggle(params) {
    console.log("expand panel");
    // document.getElementById("hamburger").style.backgroundColor = "red";
    // console.log(document.getElementsByClassName("navbar_right"));
    // document.getElementsByClassName("navbar_right").item(0).style.backgroundColor = "green";
    // document.getElementsByClassName("navbar_right").item(0).style.height = "100%";
    // document.getElementsByClassName("panel").item(0).style.border = "1px solid red";

    // document.getElementsByClassName("panel").item(0).style.position = "fixed";
    // document.getElementsByClassName("panel").item(0).style.display = "block";
    // document.getElementsByClassName("panel").item(0).style.display = "block";
    // document.getElementsByClassName("panel").item(0).style.display = "block";
    // document.getElementsByClassName("navbar_item").style.display = "inherit";

    // var items = document.getElementsByClassName('navbar_item');
    
    // if(items[0].style.display == "none"){
    //     for (var i = 0; i < items.length; i++) {
    //         // console.log(items[i]);
    //         items[i].style.display = "block";
    //     }
    // }else{
    //     for (var i = 0; i < items.length; i++) {
    //         // console.log(items[i]);
    //         items[i].style.display = "none";
    //     }
    // }
    
    // document.getElementById("hamburger").style.position = "relative";
    
    var panel_status = document.getElementsByClassName("panel").item(0).style.display;
    if(panel_status = "none"){
        document.getElementsByClassName("panel").item(0).style.display = "block";
    }else{
        document.getElementsByClassName("panel").item(0).style.display = "none";

    }


    document.getElementsByClassName("navbar_right").item(0).classList.toggle('panel_expand');

    document.getElementsByClassName("topright_btn").item(0).innerHTML = "<p onclick='ExpendPanelToggle()'>x</p>";

    // <img id="hamburger" onclick="ExpendPanelToggle()" src="./img/hamburger.png" alt="hamburger"></img>

}