document.addEventListener("DOMContentLoaded", function () {
    // Function to create a course gallery item
    function createCourseGallery(course) {
        const galleryDiv = document.createElement('div');
        galleryDiv.className = 'gallery';

        const imgLink = document.createElement('a');
        imgLink.href = `/course_description_page/?course_id=${course.course_id}`;

        const img = document.createElement('img');
        img.src = course.image_url;
        img.alt = course.course_name;
        img.width = 350; // Fixed width for the image
        img.height = 200; // Fixed height for the image

        imgLink.appendChild(img);
        galleryDiv.appendChild(imgLink);

        const descDiv = document.createElement('div');
        descDiv.className = 'desc';
        descDiv.textContent = course.course_name;
        galleryDiv.appendChild(descDiv);

        const button = document.createElement('button');
        button.className = 'button-29';
        button.role = 'button';
        button.textContent = 'View Course';
        button.addEventListener('click', function () {
            // Navigate to course description page
            window.location.href = `/course_description_page/?course_id=${course.course_id}`;
        });
        galleryDiv.appendChild(button);

        return galleryDiv;
    }

    const courseContainer = document.getElementById('course-container');

    fetch("/all_courses/") // Fetch courses from the server using the URL "/courses/
        .then(response => response.json())
        .then(data => {
            const courses = data.courses;
            courses.forEach(course => {
                const galleryDiv = createCourseGallery(course);
                courseContainer.appendChild(galleryDiv);
            });
        })
        .catch(error => console.error('Error fetching courses:', error));
});
