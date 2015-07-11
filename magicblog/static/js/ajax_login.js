post_username = getById('username').value || ''
post_password = getById('password').value || ''
is_login = getById('login').value || ''
is_register = getById('register').value || ''

message_username_elem = getById('message_username');
message_password_elem = getById('message_password');

if(is_login){
    id = alter_username_to_id(post_username);
    if (id){
	    var xmlhttp = new XMLHttpRequest();
	    xmlhttp.onreadystatechange = function(){
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
                password = json_get(xmlhttp, 'password');
                if(password == post_password){
                    redirect('index/');
                }
            }    
        }
        xmlhttp.open(GET, ROOT_URL + 'accounts/' + id +'/', true)
        xmlhttp.send()
    }else{
        message_username_elem.value = "No Such Account";
    }
}
