

const courseInput = document.getElementById('courseInput');
const courseForm = document.getElementById('courseForm');
const csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]');
const coursesList = document.getElementById('coursesList')
const courseMessage = document.getElementById('courseMessage');
const token = csrfmiddlewaretoken.value;
/**
 *  Get all teacher's courses
 */
function getCourses(){

    coursesList.innerHTML = '';

    fetch('/courses/', { headers: {'X-CSRFToken' : token }})
        .then(resp=> resp.json())
        .then(resp => {

            const courses = resp.data;
            
            courses.map( course => {
                coursesList.innerHTML +=
                    `<li> ${course.name}
                        <div class="icons-container">
                            <i data-course-id="${course.id}" class="far fa-trash-alt button-delete"></i>
                            <i data-course-id="${course.id}" class="far fa-edit button-edit"></i>
                        </div>
                    </li>`;
            });
            // Asignar evento onclic en lo iconos borrar
            const buttonDeleteCourse = document.getElementsByClassName('button-delete');
            for(let button of buttonDeleteCourse) {
                button.onclick = deleteCourse;
            }

            const buttonEditCourse = document.getElementsByClassName('button-edit');
            for(let button of buttonEditCourse) {
                button.onclick = (ev) => console.log('Editar', ev.toElement.getAttribute('data-course-id'));
            }
        });
}
getCourses();
/*
*   Save course
*/
courseForm.onsubmit = (e)=> {
    e.preventDefault();

    const courseName = courseInput.value;
    courseInput.value='';

    const payload = {
        courseName
    }
    
    const settings = {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'X-CSRFToken' : token
        }
    }

    fetch('/courses/', settings)
        .then(resp=> resp.json())
        .then(json => {
            const message = json.message;
            courseMessage.innerText = message;
            if (json.code != '201') {
                courseMessage.style.color = 'red';
            } else {
                courseMessage.style.color = '#28a745';
            }
            getCourses();
        })
}

/**
 * Detete Course
 */

function deleteCourse(param) {

    const courseId = param.toElement.getAttribute('data-course-id');
    const settings = {
        method: 'DELETE',
        headers: {
            'X-CSRFToken' : token
        }
    }
    fetch(`/courses/${courseId}/`, settings)
        .then(resp => resp.json())
        .then(response => {
            getCourses();
        });
}