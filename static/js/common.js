const city_ = document.querySelector('#city_');

const getUserCity = async () => {
    const response = await fetch('/home/user_city');
    return response.text();
};

getUserCity().then((data)=>{
    city_.value = data;
    collectAllCities();
}).catch((err)=>{

});



const _city_list_ = document.querySelector('#_city_list_');

const _getCityList = async () => {
    const response = await fetch('/home/cities');
    return await response.json();
};

const collectAllCities = () => {
    _getCityList().then((cities)=>{
        //console.log(city_.value, '+++++~~~');
        cities.forEach((city)=>{
            //console.log(city);
            let opt = document.createElement('option');
            opt.value = city.pk;
            if(opt.value==city_.value)
                opt.selected = true;
            opt.innerHTML = city.fields.city;
            _city_list_.append(opt);
        });   
        //console.log(city_.value, '+++++~~~##');

        const student_city = document.querySelector('#student_city');
        if(student_city)
            //console.log(city_.value, '++++++++++');
            student_city.value = city_.value;
    }).catch((error)=>{
        console.log(error);
    });
}