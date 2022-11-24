const eliminar = document.querySelectorAll(".eliminar");
const btn_eliminar = document.querySelectorAll(".btn_eliminar");
const btn_alert = document.getElementById("alert");
const btn_si = document.querySelector(".Si");

//* ventana emergente
btn_eliminar.forEach((btn_eleiminar) => {
  btn_eleiminar.addEventListener("click", (e) => {
    e.preventDefault();
    btn_alert.classList.toggle("activate");
  });
});
//*Boton de NO
document.querySelector(".No").addEventListener("click", () => {
  btn_alert.classList.toggle("activate");
});

//* boton de si
eliminar.forEach((btn) => {
  btn_si.addEventListener("click", () => {
    btn.click();
  });
});

