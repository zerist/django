$(document).ready(function(){
    var path = window.location.pathname;
    var re = new RegExp('[0-9]+');
    var id = re.exec(path);
    
    $('#home').click(function(){
        window.location = '/index/' + id + '/';
    })

    $('#myself').click(function(){
        window.location = '/myself/' + id + '/';
    })

    
    $('#myblog').click(function(){
        window.location = '/myblog/' + id +'/';
    })

    $('#category').click(function(){
        window.location = '/category/' + id +'/';
    }) 

    $('#logout').click(function(){
        var xmlhttp = $.ajax({
            url:'/account/' + id + '/',
            async:false,
            type:'PATCH',
            data:{
                'is_online':'false'     
            }    
        })
        var data = eval(xmlhttp.responseText);
        console.log(data)
        if (data[0].fields.username){
            alert('You Have Logged out!') 
        }
    })
    return false;
})
