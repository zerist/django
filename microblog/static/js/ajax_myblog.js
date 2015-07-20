$(document).ready(function(){
    var path = window.location.pathname
    var re = new RegExp('[0-9]+')
    var id = re.exec(path)

    $('#home').click(function(){
        window.location = '/index/' + id + '/';
    })

    $('#category').click(function(){
        window.location = '/category/' + id +'/';
    })
    $('#myself').click(function(){
        window.location = '/myself/' + id + '/';
    })
    $('#logout').click(function(){
        window.location = '/logout/' + id + '/';
    })
    
    $('#myblog').click(function(){
        var xmlhttp = $.ajax({
            url: '/myblog/' + id + '/',
            type:'GET',
            async:false   
        })  
        var data = eval(xmlhttp.responseText)
        for(var i=0; i<data.length; i++){
            var account_xmlhttp = $.ajax({
                url:'/account/' + id + '/',
                type:'GET',
                async:false  
            })
            var account = eval(account_xmlhttp.responseText)
            $('#main').append("<div class='panel-default'><div class='panel-heading'><h3>" + data[i].fields.title + "("+data[i].fields.blog_type+")</h3></div><div class='panel-body'><p>" + data[i].fields.content + "</p><img src=" + data[i].fields.src + " /></div><div class='panel-footer'><p>" + account[0].fields.username + "("+data[i].fields.date+")</p></div></div>") 
        }
        $('.panel-default').css({
            "display": "inline-block",
            "border": "1px solid grey",
            "border-radius": "10px",
            "width": "202px",
            "margin": "15px",
            "padding": "10px",
            "float": "left",
            "height": "auto"
        })
    })    
})
