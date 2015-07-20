$(document).ready(function(){
    var path = window.location.pathname;
    var re = new RegExp('[0-9]+');
    var id = re.exec(path);

    

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
        window.location = '/category/' + id + '/';
    })

    $('#home').click(function(){

        var blog_xmlhttp = $.ajax({
            url: '/index/' + id + '/',
            type:'GET',
            async:false   
        });
        var blogs = eval(blog_xmlhttp.responseText);
        for(var i=0; i<blogs.length; i++){
            account_id = blogs[i].fields.author;
            account_xmlhttp = $.ajax({
                url: '/account/' + account_id + '/',
                type: 'GET',
                async: false  
            });
            var account = eval(account_xmlhttp.responseText);
            $('#main').append("<div class='panel-default'><div class='panel-heading'><h3 id='blog"+blogs[i].pk+"'>" + blogs[i].fields.title + "("+blogs[i].fields.blog_type+")</h3></div><div class='panel-body'><p>" + blogs[i].fields.content + "</p><img src=" + blogs[i].fields.src + " /></div><div class='panel-footer'><p>" + account[0].fields.username + "("+blogs[i].fields.date+")</p><button type='button' class='btn btn-default btn-sm' id='like"+blogs[i].pk+"'>like</button><button type='button' class='btn btn-default btn-sm' id='follow"+blogs[i].pk+"'>follow</button><button type='button' class='btn btn-default btn-sm' id='transform"+blogs[i].pk+"'>transform</button></div></div>") 
        
            $('#blog'+blogs[i].pk).click(function(){
                window.location = "/showblog/" + id +'/' + re.exec(this.id) +'/';
            })

            $('#like'+blogs[i].pk).click(function(){
                var like_xmlhttp = $.ajax({
                    url: '/likeblog/', 
                    type: 'POST',
                    async: false,
                    data: {
                        'blog_id': re.exec(this.id),
                        'author': account[0].fields.username
                    }
                })
                var like_data = eval(like_xmlhttp.responseText)
                if(like_data[0].pk){
                    alert('like it')
                }
            })
            
            $('#follow'+blogs[i].pk).click(function(){
                var follow_xmlhttp = $.ajax({
                    url: '/follow/',
                    type: 'POST',
                    async: false,
                    data: {
                        'followed_account': account[0].pk,
                        'follow_account': id
                    }
                })  
                var follow_data = eval(follow_xmlhttp.responseText)
                if(follow_data[0].pk){
                    alert('follow it')
                }  
            })

            $('#transform'+blogs[i].pk).click(function(){
                var tmp_blog = $.ajax({
                    url: '/blog/' + re.exec(this.id) + '/',
                    type: 'GET',
                    async: false   
                })
                var tmp_blog_data = eval(tmp_blog.responseText)
                var transform_xmlhttp = $.ajax({
                    url: '/blog/',
                    type: 'POST',
                    async: false,
                    data: {
                        'title': tmp_blog_data[0].fields.title,
                        'content': tmp_blog_data[0].fields.content,
                        'src': tmp_blog_data[0].fields.src,
                        'blog_type': tmp_blog_data[0].fields.blog_type,
                        'author_id[]': tmp_blog_data[0].fields.author,
                        'is_transformed': true
                    }  
                })
                var transform_data = eval(transform_xmlhttp.responseText)
                if(transform_data[0].pk){
                    alert('transform it');
                }
            })
        }    
    
        $('.panel-default').css({
            "display": "inline-block",
            "border": "1px solid grey",
            "border-radius": "10px",
            "width": "250px",
            "margin": "15px",
            "padding": "10px",
            "float": "left",
            "height": "auto"
        })
    }) 

    $('#submit').click(function(){
        var title = $('#title').val();
        var blog_type = $('#blogtype').val();
        var content = $('#content').val();
        var image_src = $('#imgsrc');
        console.log(image_src)

        var xmlhttp = $.ajax({
            url: '/blog/' ,
            type: 'POST',
            async: false, 
            data: {
                'title': title,
                'content': content,
                'src': image_src,
                'blog_type': blog_type,
                'author_id': id,
                'is_transformed': false
            }
        })    
        var result = eval(xmlhttp.responseText);
        if(result[0].pk){
            alert('new microblog created')
        }
    })
})
