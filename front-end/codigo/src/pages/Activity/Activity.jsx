import { useState } from 'react';
import './Activity.css';
import dicaImg from '../../assets/images/dica.png';
import dicaDisableImg from '../../assets/images/dicaDisableTransparente.png';

export default function Activity() {
  const [opcoes, setOpcoes] = useState(["DROP", "INSERT", "UPDATE", "SELECT"]);
  const [selecionada, setSelecionada] = useState(null);
  const [verificado, setVerificado] = useState(false);
  const [usouDica, setUsouDica] = useState(false);

  const respostaCorreta = "UPDATE";

  const handleDica = () => {
    if (usouDica || verificado) return;
    setOpcoes(["DROP", "UPDATE"]); // Remove as erradas conforme sua lógica
    setUsouDica(true);
    if (selecionada === "INSERT" || selecionada === "SELECT") {
        setSelecionada(null); // Limpa se ele tinha selecionado uma que sumiu
    }
  };

  const handleVerificar = () => {
    if (selecionada) setVerificado(true);
  };

  const getEstiloBotao = (opcao) => {
    if (verificado) {
      if (opcao === respostaCorreta) return "botao-correto";
      if (opcao === selecionada) return "botao-errado";
      return "botao-desabilitado";
    }
    return opcao === selecionada ? "botao-selecionado" : "botao-opcao";
  };

  return (
    <div id="containerPrincipal">
      <section id="menuPrincipal">
        <h1>Selecione a alternativa correta</h1>
        <h2>
          Comando utilizado para atualizar dados de uma tabela:
          <button 
            id="dicaBotao" 
            onClick={handleDica} 
            disabled={usouDica || verificado}
            className={usouDica || verificado ? 'dica-disable' : ''}
          >
            <img src={(usouDica || verificado) ? dicaDisableImg : dicaImg} alt="Dica" />
          </button>
        </h2>

        <ul>
          {opcoes.map((opcao) => (
            <li key={opcao}>
              <button
                className={getEstiloBotao(opcao)}
                onClick={() => !verificado && setSelecionada(opcao)}
                disabled={verificado}
              >
                {opcao}
              </button>
            </li>
          ))}
        </ul>
      </section>

      <button 
        id="verificarBotao" 
        onClick={handleVerificar}
        disabled={verificado || !selecionada}
      >
        Verificar
      </button>
    </div>
  );
}