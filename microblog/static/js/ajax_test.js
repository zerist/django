$(document).ready(function(){
    $("#button").click(function(){
        xmlhttp = $.ajax({url:'/account/', dataType:"json", async:false});
        data = eval(xmlhttp.responseText)
        console.log(data[0].fields.age)
        //console.log(xmlhttp.responseText)
    })    
})
