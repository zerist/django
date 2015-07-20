$(document).ready(function(){
    var path = window.location.pathname
    var re = new RegExp('[0-9]+\/[0-9]+')
    var ids = re.exec(path)[0].split('/')
    var account_id = ids[0]
    var blog_id = ids[1]

    $('#home').click(function(){
        window.location = '/index/' + account_id + '/';
    })

    $('#myblog').click(function(){
        window.location = '/myblog/' + account_id +'/';
    })

    $('#category').click(function(){
        window.location = '/category/' + account_id +'/';
    })
    
    $('#myself').click(function(){
        window.location = '/myself/' + account_id + '/';
    })
    $('#logout').click(function(){
        window.location = '/logout/' + account_id + '/';
    })

    var showblog_xmlhttp = $.ajax({
        url:'/showblog/' + account_id + '/' + blog_id + '/',
        type: 'GET',
        async: false    
    })
    var showblog_data = eval(showblog_xmlhttp.responseText)
    $('#bloghead').append('<h3>'+showblog_data[1].fields.title+'('+showblog_data[1].fields.blog_type+')</h3>')
    $('#blogbody').append('<img src="'+showblog_data[1].fields.src+'"/><hr /><p>'+showblog_data[1].fields.content+'</p>')   
    $('#blogfooter').append('<p>'+showblog_data[0].fields.username+'('+showblog_data[1].fields.date+')</p><hr />')
    $('#blogprimary').append("<div class='alert alert-info'><h3>other's reply here</h3></div>")
    
    var reply_xmlhttp = $.ajax({
        url: '/replyblog/',
        type: 'GET',
        async: false    
    })
    var reply_data = eval(reply_xmlhttp.responseText)
    for(var i=0; i<reply_data.length; i++){
        if(reply_data[i].fields.reply_blog == blog_id){
            var account_xmlhttp = $.ajax({
                url: '/account/' + reply_data[i].fields.reply_account + '/',
                type: 'GET',
                async: false    
            })
            var account_data = eval(account_xmlhttp.responseText)
            $('#blogprimary').append('<div class="panel-success"><div class="panel-heading"><h5>'+account_data[0].fields.username+'('+reply_data[i].fields.date+')'+'</h5></div><div class="panel-body"><p>'+reply_data[i].fields.content+'</p></div>') 
        }
    }

    $('#replybtn').click(function(){
        var input_content = $('#replycontent').val()
        var reply_xmlhttp = $.ajax({
            url: '/replyblog/',
            type: 'POST',
            async: false,
            data: {
                'content': input_content,
                'reply_account': account_id,
                'reply_blog': blog_id
            }  
        })    
        var reply_data = eval(reply_xmlhttp.responseText)
        if(reply_data[0].pk){
            alert('reply it')
        }
    })
})
