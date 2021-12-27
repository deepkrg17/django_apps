window.onload = () => {
    if(location.pathname!='/'){
        localStorage.recent = location.href;
    }
    if(sessionStorage.html!=undefined){
        p = sessionStorage.p;
        v = sessionStorage.v;
        container.innerHTML = sessionStorage.html;
        heading.innerText = `Aladdin Episode ${p}-${v}`;
    }
};

function change() {
    let style = document.getElementById('float').style;
    if(float.style.bottom == '26px'){
        console.log(float.style.bottom);
        console.log('running if');
        float.style.removeProperty('bottom');
        float.style.top = '26px';
    }else{
        console.log(style.getPropertyValue('bottom') +' else');
        float.style.removeProperty('top');
        float.style.bottom = '26px';
    }
}

function goto() {
    a = prompt('Enter episode number:');
    if (isNaN(a) == false && a>0 && a<=572) {
        sessionStorage.clear();
        location.assign(location.origin+`/alla/${a}/`);
    }else{
        html = `<div class="alert alert-warning alert-dismissible fade show m-2" role="alert"><strong>Nope!</strong> You should check the episode number. It can't be <span class="text-danger">${a}</span>.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;
        document.querySelector('h2').insertAdjacentHTML('afterend', html);
    }
}

async function add(pos, a) {
    let container = document.getElementById('container');
    let res = await fetch(`/alla/api/${a}/`);
    let data = await res.text();
    container.insertAdjacentHTML(pos,data);
    heading.innerText = `Aladdin Episode ${p}-${v}`;
    sessionStorage.html = container.innerHTML;
    sessionStorage.p = p;
    sessionStorage.v = v;
    
}

const prev = () => {
    p--;
    if(p==0){
        alert('At beggining');
        return; 
    }
    add('afterbegin', p);
};

const next = () => {
    v++;
    if(p==573){
        alert('At end');
        return; 
    }
    add('beforeend', v);
};