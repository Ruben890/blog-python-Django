const vista1 = document.querySelectorAll(".vista1");
const ver_mas = document.querySelectorAll(".ver_mas");
const ver_menos = document.querySelectorAll(".ver_menos");
const vista_compl = document.querySelectorAll(".vista_compl");


//? boton de ver texto completo
ver_mas.forEach((btn) => {
  vista1.forEach((texto) => {
    vista_compl.forEach((comple) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        texto.style.display = "none";
        comple.style.display = "block";
      });
    });
  });
});

//? boton de Ocultar texto
ver_menos.forEach((btn) => {
  vista1.forEach((texto) => {
    vista_compl.forEach((comple) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        comple.style.display = "none";
        texto.style.display = "block";
      });
    });
  });
});

//? ver comentarios
function VerComentarios(post_id) {
const comentarios = document.getElementById(post_id)

if(comentarios.classList.contains('active')){
comentarios.classList.remove('active')
}else{
comentarios.classList.add('active')
}
}

 