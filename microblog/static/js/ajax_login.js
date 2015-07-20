$(document).ready(function(){
    $('#login').click(function(){
        var username = $('#username').val();
        var password = $('#password').val();
        
        var data = $.ajax({url:'/account/',dataType:'json',async:false}).responseText;
        data = eval(data)
        //var data = JSON.parse(raw_data);
        for(var i=0; i<data.length; i++){
            if(data[i].fields.username == username && data[i].fields.password == password){
                var result_account = $.ajax({
                    url:'/account/'+data[i].pk+'/', 
                    type:"PATCH",
                    async:false,
                    data:{'is_online':'true'}
                });
                
                window.location = "/index/" + data[i].pk + '/'

            }
        }    
    }) 
    
    $('#register').click(function(){
        window.location = "/register/"
    }) 
})
