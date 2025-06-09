// Collapse navbar if user either clicks link or clicks outside navbar
document.addEventListener("click", function (event) {
  const navbarToggler = document.querySelector(
    ".navbar-toggler"
  );
  const navbarCollapse = document.getElementById(
    "navbarNavAltMarkup"
  );

  if (
    navbarCollapse.classList.contains("show") &&
    !navbarCollapse.contains(event.target) &&
    !navbarToggler.contains(event.target)
  ) {
    navbarToggler.click();
  }

  if (
    navbarCollapse.classList.contains("show") &&
    event.target.classList.contains("nav-link")
  ) {
    navbarToggler.click();
  }
});
