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
		<li><a href="mom_bday/index.html>妈妈生日快乐</a></li>
            </ul>
        </nav>
    `;

    document.getElementById("navbar").innerHTML = navbar;
});

document.addEventListener('DOMContentLoaded', (event) => {
    var footer = `
        <section class="container">
            <p>Copyright &copy; Xinzhou He 2024-2024</p>
            <p>Ann Arbor, MI USA</p>
        </section>
        <section class="alternate-link">
            <a href="https://www-personal.umich.edu/~xinzhouh" class="project-link">Alternative Link</a>
        </section>
        <link rel="stylesheet" href="styles.css">
    `;

    document.getElementById("footer").innerHTML = footer;
});
