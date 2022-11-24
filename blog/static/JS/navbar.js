const btn = document.getElementById("btn");
const submenu = document.querySelector("#submenu");
const login = document.querySelector(".login");
const imagen_perfil = document.getElementById("imagen_perfil");

btn.addEventListener("click", (e) => {
  e.preventDefault();
  submenu.classList.toggle("active");
});

login.addEventListener("click", () => {
  location.href = "login";
});

