POST = 'POST'
GET = 'GET'
PUT = 'PUT'
PATHC = 'PATCH'
DELETE = 'DELETE'

ROOT_URL = "http://127.0.0.1:8000/"

function alter_username_to_id(username){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            var accountArray = json_get_all(xmlhttp);
            for(var i=0; i<accountArray.length; i++){
                var account_username = accountArray[i]['username']
                if(username == account_username){
                    id = accountArray[i]['id'];
                    return id;    
                }    
            }
        }    
    }
    xmlhttp.open(GET, ROOT_URL + 'accounts/', true);
    xmlhttp.send();
}

function json_get_all(xmlhttp){
    return eval('('+xmlhttp.responseText+')');    
}

function json_get(xmlhttp, field){
    return eval("("+xmlhttp.responseText+")")[field];
}

function json_list_get(xmlhttp, index, field){
    return eval("("+xmlhttp.responseText+")")[index][field];
}

function redirect(url){
    window.location = "http://127.0.0.1:8000/" + url;    
}

function getById(id){
    return document.getElementById(id);    
}
