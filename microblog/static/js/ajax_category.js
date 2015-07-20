$(document).ready(function(){
    var path = window.location.pathname;
    var re = new RegExp('[0-9]+');
    var id = re.exec(path);
    var types = new Array();


    $('#home').click(function(){
        window.location = '/index/' + id + '/';
    })

    $('#myself').click(function(){
        window.location = '/myself/' + id + '/';
    })
    $('#logout').click(function(){
        window.location = '/logout/' + id + '/';
    })
    
    $('#myblog').click(function(){
        window.location = '/myblog/' + id +'/';
    })

    $('#category').click(function(){
        var type_xmlhttp = $.ajax({
            url: '/category/' + id + '/',
            type: 'GET',
            async: false  
        })
        var categories = eval(type_xmlhttp.responseText)
        for(var i=0; i<categories.length; i++){
            var blog_type = categories[i].fields.blog_type;
            types.push(blog_type);
            $('#btn_box').append('<button type="button" id="'+blog_type+'" class="btn btn-primary btn-lg">'+blog_type+'</button>');
        }
        for(var j=0; j<types.length; j++){
            $('#'+types[j]).click(function(){
                var blogs_xmlhttp = $.ajax({
                    url: '/blog/',
                    type: 'GET',
                    async: false  
                });
                var blogs = eval(blogs_xmlhttp.responseText);
                for(var j=0; j<blogs.length; j++){
                    account_id = blogs[j].fields.author;
                    account_xmlhttp = $.ajax({
                        url: '/account/' + account_id + '/',
                        type: 'GET',
                        async: false  
                    });
                    var account = eval(account_xmlhttp.responseText);
                    if(blogs[j].fields.blog_type == this.id){
                         $('#main').append("<div class='panel-default'><div class='panel-heading'><h3>" + blogs[j].fields.title + "("+blogs[j].fields.blog_type+")</h3></div><div class='panel-body'><p>" + blogs[j].fields.content + "</p><img src=" + blogs[j].fields.src + " /></div><div class='panel-footer'><p>" + account[0].fields.username + "("+blogs[j].fields.date+")</p></div></div>") 
                    }
                }
                $('.panel-default').css({
                    "display": "inline-block",
                    "border": "1px solid grey",
                    "border-radius": "10px",
                    "width": "202px",
                    "margin": "15px",
                    "float": "left",
                    "padding": "10px",
                    "height": "auto"
                })               
            }
        )}
    })
})
