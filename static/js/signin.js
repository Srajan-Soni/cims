const form = document.querySelector('form');

const usernameField = document.querySelector('#id_username');
const passwordField = document.querySelector('#id_password');

usernameField.setAttribute('class', 'form-control');
passwordField.setAttribute('class', 'form-control');

//~~~~~~~~~~~~~~ VALIDATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const result = {
    username: false,
    password: false,
}; 

form.addEventListener('submit', function(event){
    //alert(result.username+''+result.email+''+result.password+''+result.contact);
    if(result.username && result.password){
        return true;
    }

    event.preventDefault();
    return false;
}); 

const inputs = document.querySelectorAll('input');

const patterns = {
    username: /^[a-zA-Z\d_]{5,15}$/,
    password: /^[a-zA-Z\d-_]{8,20}$/
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

        validate(field, pattern);
    });
});


//~~~~~~~~~~~~~~ VIEW PASSWORD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//const passwordField = document.querySelector('#id_password');
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


