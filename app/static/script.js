// Animação de scroll suave
const links = document.querySelectorAll(".nav-links a");
links.forEach((link) => {
    link.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = link.getAttribute("href").substring(1);
        document.getElementById(targetId).scrollIntoView({
            behavior: "smooth",
            block: "start",
        });
    });
});
