document.addEventListener('DOMContentLoaded', (event) => {
    var navbar = `
        <nav>
            <ul>
                <li class="current"><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="courses.html">Courses</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="research.html">Research</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    `;

    document.getElementById("navbar").innerHTML = navbar;
});

