function toggleMenu() {
  const menu = document.querySelector(".menu");
  menu.classList.toggle("active");
}

document.addEventListener("DOMContentLoaded", () => {
  const menuIcon = document.querySelector(".menu-icon");
  const menu = document.querySelector(".menu");

  // Toggle the menu when the menu icon is clicked
  menuIcon.addEventListener("click", () => {
    menu.classList.toggle("active");
  })

  // Hide menu when a link is clicked
  const menuLinks = document.querySelectorAll(".menu a");
  menuLinks.forEach(link => {
    link.addEventListener("click", () => {
      menu.classList.remove("active");
    });
  });

  // Hide menu when the user clicks outside of it
  document.addEventListener("click", event => {
    if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
      menu.classList.remove("active");
    }
  });
});
