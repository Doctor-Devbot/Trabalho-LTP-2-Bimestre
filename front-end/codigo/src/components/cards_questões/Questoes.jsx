function Questoes(){
const enunciado = "Bruh"
num_alternativas = 4

    function createAlternativas(){
        let listaAlternativas = ["bruh1", "bruh2", "bruh3", "bruh4"]
        for (let i = 0; i < listaAlternativas.length; i++){
            textoAlternativa = ""
            alternativa = i
            textoAlternativa.innerText(alternativa)
            
        }
        return(textoAlternativa)
    }

    
    
    return(
        <>
            <h1>Selecione a alternativa correta</h1>
            <div>
                <h4>{enunciado}</h4>
                <h4>Dica</h4>
            </div>            
            <button>{createAlternativas}</button>
            <button>Verificar</button>   
        
        </>
            
    )
}

export default Questoes