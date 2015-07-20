window.onload = function(){
    waterfall("main", "panel-default");   
}

function waterfall(parentName, boxName){
    var parentDiv = document.getElementById(parentName);
    var elemArray = getByClass(parentDiv, boxName);
    var elemWidth = 202;
    var totalWidth = document.documentElement.clientWidth;
    var cols = Math.floor(totalWidth / elemWidth);

    parentDiv.style.cssText = "width:" + cols * elemWidth + "px; margin: 0 auto";
    var subArray = [];

    for(var i=0; i<elemArray.length; i++){
        if(i < cols){
            subArray.push(elemArray[i].offsetHeight);
        }else{
            var minHeight = Math.min.apply(null, subArray);
            var index = getMinHIndex(subArray, minHeight);
            elemArray[i].style.position = "absolute";
            elemArray[i].style.top = minHeight + "px";
            elemArray[i].style.left = index * elemWidth + "px";
            subArray[index] += elemArray[i].offsetHeight;
        }

    }
}

function getMinHIndex(subArray, minH){
    for(var i=0; i<subArray.length; i++){
        if(subArray[i] == minH){
            return i;
        }
    }
}

function getByClass(parentDiv, clsName){
    var elemArray = [];

    var tagArray = parentDiv.getElementsByTagName("*");
    for(var i=0; i<tagArray.length; i++){
        if(tagArray[i].className == clsName){
            elemArray.push(tagArray[i]);
        }
    }
    return elemArray;
}
