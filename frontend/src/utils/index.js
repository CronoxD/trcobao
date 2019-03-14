
function getToken() {
    let name = "csrftoken=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


const URL_API = 'http://localhost:8000/api/';
const URL_BACK = 'http://localhost:8000/'


export {
    URL_API,
    URL_BACK,
    getToken
}