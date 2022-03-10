const save_course_btn = document.querySelector('#save_course_btn');

const id_course_name = document.querySelector('#id-course-name');

const id_course_subtitle = document.querySelector('#id-course-subtitle');

const id_course_details = document.querySelector('#id-course-details');

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const add_course_form = document.querySelector('#new-course-form');

const course_image_form = document.querySelector('#course-image-form');

const course_syllabus_form = document.querySelector('#course-syllabus-form'); 

const step_1 = document.querySelector('#step-1');
const step_2 = document.querySelector('#step-2');
const step_3 = document.querySelector('#step-3');

const course_title = document.querySelector('#course_title');
id_course_name.addEventListener('keyup', (event) => {
    course_title.innerHTML = event.target.value;
});


const saveCourse = async () => {
    const response = await fetch('/institutes/courses/', {
        method: "POST",

        body: JSON.stringify({
            course_name: id_course_name.value,
            course_subtitle: id_course_subtitle.value,
            course_details: id_course_details.value,
        }),

        headers: {
            "Content-type": "application/json; charset=UTF-8",
            "X-CSRFToken": csrftoken
        }
    });

    return response.text();
};

save_course_btn.addEventListener('click', () => {
    saveCourse().then((data)=>{
        console.log(data);
        if(data=='false'){

        }else{
            add_course_form.style.display = 'none';
            course_image_form.style.display = 'block';  
            step_1.classList.remove('active');   
            step_2.classList.add('active');   
        }
    }).catch((err)=>{
        console.log(err);
    });
});



//################## Dropzone Pic ##################
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

let dropzone = new Dropzone('#picup', {url: '/institutes/course_pic_upload/'});

dropzone.on('success', () => {
    setTimeout(()=>{
        course_image_form.style.display = 'none';
        course_syllabus_form.style.display = 'block';
        step_2.classList.remove('active');
        step_3.classList.add('active');
    }, 2000);    
});


let btn = document.querySelector('#btn');
btn.addEventListener('click',()=>{
    dropzone.processQueue();
});


//################## Dropzone Syllabus ##################
Dropzone.autoDiscover = false;

Dropzone.options.picup2 = {
    paramName: 'file',
    maxFilesize: 10,
    uploadMultiple: false,
    createImageThumbnails: true,
    maxFiles: 1,
    acceptedFiles: '.pdf',
    addRemoveLinks: true,
    autoProcessQueue: false
};

let dropzone2 = new Dropzone('#picup2', {url: '/institutes/course_syllabus_upload/'});

dropzone2.on('success', () => {
    setTimeout(()=>{
        window.location = '/institutes/courses';
    }, 2000);
});


let btn2 = document.querySelector('#btn2');
btn2.addEventListener('click',()=>{
    dropzone2.processQueue();
});