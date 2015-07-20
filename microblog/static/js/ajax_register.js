$(document).ready(function(){
    $('#confirm').click(function(){
        var username = $('#re_username').val()
        var password = $('#re_password').val()
        var confirm_passeord = $('#confirm_password').val()
        var email = $('#email').val()
        var sex = $('#man').val() || $('#woman').val()
        var age = $('#age').val()
        var city = $('#city').val()
    
        var result_register = $.ajax({
            url:'/account/',
            type:'POST',
            async:false,
            data:{
                'username':username,
                'password':password,
                'email':email,
                'city':city,
                'age':age,
                'sex':sex,
                'is_online':'false'    
            }
        })    
        var data = eval(result_register.responseText);
        if(data[0].pk){
            if (confirm('Create An Account! Login Now!')){
                window.location = '/login/'
            }else{
                window.location = '/login/'    
            }
        }
    })

    $('#cancel').click(function(){
        window.location = '/login/'    
    })
})
