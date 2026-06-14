import { useNavigate } from 'react-router-dom';
import './Home.css';

export default function Home() {
  const navigate = useNavigate();

  return (
    <section id="caminhoPrincipal">
      <h1>1- Introdução</h1>
      <button className="btn-circulo" onClick={() => navigate('/atividade')}>
        1
      </button>
      <button className="btn-circulo" onClick={() => navigate('/atividade')}>
        2
      </button>
    </section>
  );
}