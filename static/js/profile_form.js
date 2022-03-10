const details_form = document.querySelector('#details_form'); 
const submit_btn = document.querySelector('#submit_btn');
const id_contact = document.querySelector('#id_contact');
const otp_box = document.querySelector('#otp_box');
const id_otp = document.querySelector('#id_otp');
const check_otp = document.querySelector('#check_otp');


submit_btn.style.display = 'none';


details_form.addEventListener('submit', (event)=>{
    id_contact.disabled = false;

    return true;
});

const sendOTP = async ()=>{
    response = await fetch('/home/sendotp/?contact='+id_contact.value)
    return response.text()
};

const sendotp_btn = document.querySelector('#sendotp_btn');

sendotp_btn.addEventListener('click', ()=>{
    id_contact.disabled = true;
    sendotp_btn.style.display = 'none';
    otp_box.style.display = 'block';

    sendOTP().then((data)=>{
        console.log(data);
    }).catch((error)=>{
        console.log(error);
    });   
});


//------------------------------------
const checkOTP = async () => {
    response = await fetch('/home/check_otp/?otp='+id_otp.value);
    return response.text()
};

check_otp.addEventListener('click', ()=>{    
    checkOTP().then((data)=>{
        console.log(data);
        if(data=='True'){
            otp_box.style.display = 'none';
            submit_btn.style.display = 'inline';
        }
    }).catch((error)=>{
        console.log(error);
    });
});