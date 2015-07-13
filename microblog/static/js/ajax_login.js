$(document).ready(function(){
    $('#login').click(function(){
        var username = $('#username').val();
        var password = $('#password').val();
        
        var data = $.ajax({url:'/accounts/',dataType:'text',async:false}).responseText;
        alert(data[0].username)
        //var data = JSON.parse(raw_data);
        for(var i=0; i<data.length; i++){
            if(data[i].username == username && data[i].password == password){
                alert(3);
                $.post('/login/', {'login': 'true', 'username': username, 'id': data[i].id});
            }
        }    
    })   
})
