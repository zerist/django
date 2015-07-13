$(document).ready(function(){
    $("#button").click(function(){
        for (var i in $.ajax({url:'/accounts/',async:false}).responseText){
            alert(i);    
        }
    })    
})
