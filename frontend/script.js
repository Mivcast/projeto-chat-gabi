function adicionarMensagem(origem, texto) {
  const chatBox = document.getElementById("chat-box");
  const msg = `<div class="${origem === 'Você' ? 'msg-usuario' : 'msg-bot'}"><strong>${origem}:</strong> ${texto}</div>`;
  chatBox.innerHTML += msg;
  chatBox.scrollTop = chatBox.scrollHeight;
}

function mostrarDigitando() {
  const chatBox = document.getElementById("chat-box");
  const typing = document.createElement("div");
  typing.id = "digitando";
  typing.innerHTML = "<em>Digitando...</em>";
  chatBox.appendChild(typing);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removerDigitando() {
  const typing = document.getElementById("digitando");
  if (typing) typing.remove();
}

function respostaBotao(botao) {
  switch (botao) {
    case 'falar':
      adicionarMensagem("GabiBot", "Claro! 💬 Já te levo pro Matheus. <br><a href='https://wa.me/5517997061273' target='_blank'>📲 Clique aqui pra falar com ele direto no WhatsApp</a>");
      break;
    case 'agendar':
      adicionarMensagem("GabiBot", `Agenda aberta! 🗓️ A reunião de consultoria custa R$ 100,00.<br><a href='https://pay.infinitepay.io/matheusnjtj/VC1D-h8EdXoJhH-300,00' target='_blank'>💳 Pagar agora</a><br>Depois me manda o comprovante aqui e já agendo com o Matheus!`);
      break;
    case 'servicos':
      adicionarMensagem("GabiBot", "Esses são os principais serviços da MivCast: <br>✅ Criação de Sites<br>✅ Lojas Virtuais<br>✅ Landing Pages<br>✅ Identidade Visual<br>✅ Tráfego Pago<br>✅ Redes Sociais<br>✅ Artes e Vídeos<br>✅ Consultorias & Mentorias<br><br>Me diga qual te interessou pra eu te explicar melhor 😉");
      break;
    case 'quemSomos':
      adicionarMensagem("GabiBot", "Somos a Agência MivCast 🚀 Profissionais em marketing digital, branding e estratégias pra pequenas empresas brilharem online. Estamos aqui pra te ajudar com tudo! 😎");
      break;
  }
}

async function enviarMensagem() {
  const input = document.getElementById("user-input");
  const msg = input.value.trim();
  if (!msg) return;

  adicionarMensagem("Você", msg);
  input.value = "";
  mostrarDigitando();

  // URL fixa para ambiente local (ajustável para produção)
const URL_API = window.location.hostname.includes("localhost") || window.location.hostname === "127.0.0.1"
  ? "http://127.0.0.1:8000/responder"
  : "https://projeto-chat-gabi.onrender.com/responder";

  console.log("📤 Enviando para:", URL_API);

  try {
    const resposta = await fetch(URL_API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: msg })
    });

    const dados = await resposta.json();
    console.log("📥 Resposta recebida:", dados);

    removerDigitando();

    if (!dados.resposta || dados.resposta.length < 10) {
      adicionarMensagem("GabiBot", "Não consegui te responder certinho agora 😕<br>Se quiser, posso te levar pro WhatsApp com o Matheus: <a href='https://wa.me/5517997061273' target='_blank'>📲 Falar no WhatsApp</a>");
    } else {
      adicionarMensagem("GabiBot", dados.resposta);
    }
  } catch (e) {
    removerDigitando();
    console.error("❌ Erro de conexão:", e);
    adicionarMensagem("GabiBot", "Tivemos um probleminha técnico 😅<br>Se preferir, fale direto com o Matheus: <a href='https://wa.me/5517997061273' target='_blank'>📲 WhatsApp</a>");
  }
}
