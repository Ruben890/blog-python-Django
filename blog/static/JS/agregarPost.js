const archivo_img = document.getElementById("id_img");
const btn_img = document.querySelector(".btn_img");
const form = document.querySelector("form");
const titulo = document.getElementById("id_title");
const descripsion = document.getElementById("id_descriction");

//? validar formulario
form.addEventListener("submit", (e) => {
  if (titulo.value.length == 0) {
    e.preventDefault();
    document.querySelector(".error").innerHTML =
      "El título debe tener más de 8 caracteres";
  } else if (descripsion.value.length == 0) {
    e.preventDefault();
    document.querySelector(".error").innerHTML = "Debe tener una descripción";
  }
  
});

//* ver la imagenes del input files
btn_img.addEventListener("click", (e) => {
  e.preventDefault();
  archivo_img.click();
});
archivo_img.addEventListener("change", (e) => {
  for (let i = 0; archivo_img.files.length; i++) {
    const element = URL.createObjectURL(archivo_img.files[i]);
    const img = document.createElement("img");
    img.src = element;
    document.querySelector(".img").appendChild(img);
  }
});
