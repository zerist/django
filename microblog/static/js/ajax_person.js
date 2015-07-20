$(document).ready(function(){
    var path = window.location.pathname;
    var re = new RegExp('[0-9]+');
    var id = re.exec(path);

    $('#home').click(function(){
        window.location = '/index/' + id + '/';
    })

    $('#logout').click(function(){
        window.location = '/logout/' + id + '/';
    })
    
    $('#myblog').click(function(){
        window.location = '/myblog/' + id +'/';
    })
    $('#category').click(function(){
        window.location = '/category/' + id + '/'
    })

    var raw_data = $.ajax({url:'/account/'+id+'/', type:'GET', async:false});
    var data = eval(raw_data.responseText);
    $('#usernamebutton').click(function(){
        var username = prompt("Please input the new name", data[0].fields.username);
        alert(typeof username)
        if(username != null){
            $.ajax({
                url:'/account/' + id + '/',
                type:"PATCH",
                async:false,
                data:{'username':username}
            })
            $('#username').text(username)
        }
    })

    $('#emailbutton').click(function(){
        var email = prompt("Please input the new email", data[0].fields.email);
        if(email != null){
            $.ajax({
                url:'/account/' + id +'/',
                type:'PATCH',
                async:false,
                data:{
                    'email':email    
                }  
            })
            $('#email').text(email)
        }
           
    })

    $('#citybutton').click(function(){
        var city = prompt("Please input the new city name", data[0].fields.city);
        if(city != null){
            $.ajax({
                url:'/account/' + id +'/',
                type:'PATCH',
                async:false,
                data:{
                    'city':city    
                }   
            })
            $('#city').text(city)
        }    
    })
    
    $('#followbtn').click(function(){
        var follow_xmlhttp = $.ajax({
            url: '/follow/',
            type: 'GET',
            async:false  
        })
        var follow_data = eval(follow_xmlhttp.responseText)
        for(var i=0; i<follow_data.length; i++){
            if(follow_data[i].fields.followe_account == id){
                var account_xmlhttp = $.ajax({
                    url: '/account/' + follow_data[i].fields.followed_account + '/',
                    type: 'GET',
                    async: false  
                })
                var account_data = eval(account_xmlhttp.responseText)
                $('#followbody').append('<p>'+account_data[0].fields.username+'</p>')
            }
        }    
    })

    $('#likebtn').click(function(){
        var like_xmlhttp = $.ajax({
            url: '/likeblog/',
            type: 'GET',
            async: false  
        })

        var like_data = eval(like_xmlhttp.responseText)
        for(var i=0; i<like_data.length; i++){
            var blog_xmlhttp = $.ajax({
                url: '/blog/' + like_data[i].fields.like_blog + '/',
                type: 'GET',
                async: false  
            })
            var blog_data = eval(blog_xmlhttp.responseText)
            if(like_data[i].fields.like_account == id){
                $('#likebody').append('<p>'+blog_data[0].fields.title+'</p>')
            }
        }    
    })

    $('#replybtn').click(function(){
        var reply_xmlhttp = $.ajax({
            url: '/replyblog/',
            type:'GET',
            async: false  
        })    
        var reply_data = eval(reply_xmlhttp.responseText)
        for(var i=0; i<reply_data.length; i++){
            var blog_xmlhttp = $.ajax({
                url: '/blog/' + reply_data[i].fields.reply_blog + '/',
                type:'GET',
                async: false  
            })
            var blog_data = eval(blog_xmlhttp.responseText)
            if(reply_data[i].fields.reply_account == id){
                $('#replybody').append('<p>'+blog_data[0].fields.title+'</p>')
            }
        }
    })

})
