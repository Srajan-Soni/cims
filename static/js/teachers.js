const new_teacher_btn = document.querySelector('#new-teacher-btn');
const teacher_form_box = document.querySelector('#teacher-form-box');
const close = document.querySelector('#close');

const teacher_form = document.querySelector('#teacher-form');
const add_teacher_button = document.querySelector('#add-teacher-button');

const teacher_pic_box = document.querySelector('#teacher-pic-box');
const teacher_title = document.querySelector('#teacher-title');



const addTeacher = async () => {
    let response = await fetch(`/teachers/add_teacher/?first_name=${teacher_form.first_name.value}`+
                                `&last_name=${teacher_form.last_name.value}`+
                                `&email=${teacher_form.email.value}`+
                                `&password=${teacher_form.password.value}`+
                                `&gender=${teacher_form.gender.value}`+
                                `&dob=${teacher_form.dob.value}`+
                                `&address=${teacher_form.address.value}`+
                                `&city_id=${teacher_form.city_id.value}`+
                                `&contact=${teacher_form.contact.value}`+
                                `&qualification=${teacher_form.qualification.value}`+
                                `&experience=${teacher_form.experience.value}`);
    return response.text();
};

add_teacher_button.addEventListener('click', () => {
    addTeacher().then((data)=>{
        console.log(data);
        if(data=='True'){
            teacher_form.style.display = 'none';
            teacher_pic_box.style.display = 'block'; 
            teacher_title.innerHTML = teacher_form.first_name.value+' '+teacher_form.last_name.value;
        }else{
            //TO-DO: ---------------
        }
    }).catch((err)=>{
        console.log(err);
    });
});


//###############################################################
close.addEventListener('click', () => {
    teacher_form_box.style.display = 'none';
});

//###############################################################
new_teacher_btn.addEventListener('click', () => {
    teacher_form_box.style.display = 'block';
});


//#############################################################
Dropzone.autoDiscover = false;

Dropzone.options.picup = {
    paramName: 'file',
    maxFilesize: 1,
    uploadMultiple: false,
    createImageThumbnails: true,
    maxFiles: 1,
    acceptedFiles: '.jpeg,.png,.gif,.jpg',
    addRemoveLinks: true,
    autoProcessQueue: false
};

let dropzone = new Dropzone('#picup', {url: '/teachers/teacher_pic_upload/'});

dropzone.on('success', ()=>{
    window.location = '/teachers/teacher'
});

let btn = document.querySelector('#btn');
btn.addEventListener('click',()=>{
    dropzone.processQueue();
});