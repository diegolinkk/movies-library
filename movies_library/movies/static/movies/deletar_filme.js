deletar = document.querySelectorAll('a.deletar-filme')
    
for (i=0; i < deletar.length; i ++){
    deletar[i].addEventListener('click', function(event){
        event.preventDefault()
        var choice = confirm("Confirma deletar esse filme ?")

        if(choice){
            window.location.href = this.getAttribute('href')
        }
    })
}