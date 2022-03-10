const form = document.querySelector('form');

//~~~~~~~~~~~~~~ VIEW PASSWORD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const passwordField = document.querySelector('#id_password');
const viewPassword = document.querySelector('#view-password');

let passVisible = false;
viewPassword.addEventListener('click', function(event){
    if(!passVisible){
        passwordField.attributes.type.value = 'text';
        passVisible = true;
    }else{
        passwordField.attributes.type.value = 'password';
        passVisible = false;
    }
});

//~~~~~~~~~~~~~~ UNIQUE USERNAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const usernameField = form.username;

const error_message = error_username.innerHTML;

const ajaxRequest = async () => {
    const response = await fetch('/home/check_username/?username='+usernameField.value);

    return response.text();
};

const checkUsername = () => {
    if(result['username']){
        ajaxRequest().then((data)=>{
            //console.log('success', data);
            const help_username = document.querySelector('#help_username');
            const error_username = document.querySelector('#error_username');
            
            if(data==='True'){
                usernameField.classList.replace('success', 'fail');
                help_username.classList.replace('show', 'hide');
                error_username.classList.replace('hide', 'show');
                error_username.innerHTML = 'An account already exists with the given username!!';
                result['username'] = false;
            }else{
                
            }
        }).catch((error)=>{
            console.log('fail');
        });
    }    
};

usernameField.addEventListener('blur', checkUsername);


//~~~~~~~~~~~~~~ VALIDATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const result = {
    username: false,
    email: false,
    password: false,
    contact: false
}; 



form.addEventListener('submit', function(event){
    //alert(result.username+''+result.email+''+result.password+''+result.contact);
    if(result.username && result.email && result.password && result.contact){
        return true;
    }

    event.preventDefault();
    return false;
}); 

const inputs = document.querySelectorAll('input');

const patterns = {
    username: /^[a-zA-Z\d_]{5,15}$/,
    email: /^([a-zA-Z\d\.-_]+)@([a-zA-Z\d-_]{2,})\.([a-zA-Z]{2,5})(\.[a-zA-Z]{2,5})?$/,
    password: /^[a-zA-Z\d-_]{8,20}$/,
    contact: /^[5-9][0-9]{9}$/    
};

function validate(field, pattern){
    let help_username = document.querySelector('#help_'+field.attributes.name.value);
    let error_username = document.querySelector('#error_'+field.attributes.name.value);
    
    if(pattern.test(field.value)){
        field.classList.replace('fail', 'success');
        help_username.classList.replace('hide', 'show');
        error_username.classList.replace('show', 'hide');
        result[field.attributes.name.value] = true;
    }else{
        if(field.classList.contains('success')){
            field.classList.replace('success', 'fail');
            help_username.classList.replace('show', 'hide');
        }
        field.classList.add('fail');
        help_username.classList.add('hide');
        error_username.classList.replace('hide', 'show');

        result[field.attributes.name.value] = false;
    }
}

inputs.forEach(function(input){
    input.addEventListener('keyup', function(event){
        let pattern = patterns[event.target.attributes.name.value];
        let field = event.target;

        if(field.attributes.name.value==='username'){
            const error_username = document.querySelector('#error_username');
            error_username.innerHTML = error_message;
        }

        validate(field, pattern);
    });
});


