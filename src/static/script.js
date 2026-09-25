document.addEventListener("DOMContentLoaded", () => {
    // Verificar autenticação
    const token = localStorage.getItem('token');
    if (!token && !window.location.href.includes('login.html')) {
        window.location.href = '/static/login.html';
        return;
    }

    // Carregar dados iniciais do painel
    carregarPainel();
});

async function carregarPainel() {
    try {
        // 1. Buscar Clientes
        const resClientes = await fetch('/api/clientes/');
        const clientes = resClientes.ok ? await resClientes.json() : [];

        // 2. Buscar Agendamentos
        const resAgendamentos = await fetch('/api/agendamentos/');
        const agendamentos = resAgendamentos.ok ? await resAgendamentos.json() : [];

        // --- ATUALIZAR ESTATÍSTICAS ---
        const elClientes = document.getElementById('stat-clientes');
        const elAgendamentos = document.getElementById('stat-agendamentos');
        const elFaturamento = document.getElementById('stat-faturamento');
        const elServicos = document.getElementById('stat-servicos');

        if (elClientes) elClientes.innerText = clientes.length;
        if (elAgendamentos) elAgendamentos.innerText = agendamentos.length;

        // Calcular faturamento total somando os preços
        let faturamentoTotal = agendamentos.reduce((acc, curr) => acc + (curr.preco || 0), 0);
        if (elFaturamento) elFaturamento.innerText = `R$ ${faturamentoTotal.toFixed(2)}`;

        if (elServicos) elServicos.innerText = agendamentos.length;

        // --- RENDERIZAR CLIENTES RECENTES COM CPF ---
        const gridClientes = document.getElementById('grid-clientes');
        if (gridClientes) {
            if (clientes.length === 0) {
                gridClientes.innerHTML = `<p class="text-sm text-gray-500 col-span-2">Nenhum cliente registado ainda.</p>`;
            } else {
                gridClientes.innerHTML = clientes.map(cliente => `
                    <div class="bg-[#0B0B0C] border border-[#27272A] p-4 rounded-xl flex items-center justify-between">
                        <div>
                            <h4 class="font-bold text-white text-sm">${cliente.nome}</h4>
                            <p class="text-xs text-gray-400 mt-0.5">
                                <i class="fa-regular fa-envelope mr-1"></i> ${cliente.email || 'Sem e-mail'} | 
                                <i class="fa-solid fa-phone ml-1 mr-1"></i> ${cliente.telefone || 'Sem telemóvel'}
                            </p>
                            <p class="text-xs text-[#D4AF37] mt-1">
                                <i class="fa-solid fa-id-card mr-1"></i> CPF: ${cliente.cpf || 'Não informado'}
                            </p>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="text-xs bg-[#D4AF37]/10 text-[#D4AF37] px-2.5 py-1 rounded-lg font-medium border border-[#D4AF37]/20">Ativo</span>
                            <button onclick="removerCliente(${cliente.id})" class="text-gray-500 hover:text-red-400 p-2 transition cursor-pointer" title="Remover Cliente">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </div>
                    </div>
                `).join('');
            }
        }

    } catch (error) {
        console.error("Erro ao carregar dados do painel:", error);
    }
}

// --- FUNÇÕES DO MODAL ---
function abrirModalCliente() {
    const modal = document.getElementById('modal-cliente');
    if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    }
}

function fecharModalCliente() {
    const modal = document.getElementById('modal-cliente');
    if (modal) {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
    }
    const form = document.getElementById('form-novo-cliente');
    if (form) form.reset();
}

// --- VALIDAÇÕES E REGISTO DE CLIENTE ---
async function registarCliente(event) {
    event.preventDefault();

    const nome = document.getElementById('cliente-nome').value.trim();
    const telefone = document.getElementById('cliente-telefone').value.trim();
    const email = document.getElementById('cliente-email').value.trim();
    const cpf = document.getElementById('cliente-cpf').value.trim();

    // Validação 1: Nome com pelo menos 3 carateres
    if (nome.length < 3) {
        alert('O nome deve ter pelo menos 3 carateres.');
        return;
    }

    // Validação 2: Formato de E-mail
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email)) {
        alert('Por favor, insira um endereço de e-mail válido.');
        return;
    }

    // Validação 3: Telemóvel (mínimo de 8 carateres)
    const regexTelefone = /^[0-9\-\+\s\(\)]{8,15}$/;
    if (!regexTelefone.test(telefone)) {
        alert('Por favor, insira um número de telemóvel válido.');
        return;
    }

    // Validação 4: CPF com 11 dígitos
    const cpfLimpo = cpf.replace(/\D/g, '');
    if (cpfLimpo.length !== 11) {
        alert('O CPF deve conter exatamente 11 dígitos numéricos.');
        return;
    }

    try {
        const response = await fetch('/api/clientes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nome, telefone, email, cpf })
        });

        if (response.ok) {
            fecharModalCliente();
            carregarPainel(); 
        } else {
            const erroData = await response.json();
            alert(erroData.detail || 'Erro ao registar o cliente.');
        }
    } catch (error) {
        console.error("Erro na requisição:", error);
        alert('Erro de ligação com o servidor.');
    }
}

// --- FUNÇÃO PARA REMOVER CLIENTE ---
async function removerCliente(id) {
    if (!confirm("Tem certeza que deseja remover este cliente?")) return;

    try {
        const response = await fetch(`/api/clientes/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            carregarPainel(); 
        } else {
            alert('Erro ao remover o cliente.');
        }
    } catch (error) {
        console.error("Erro ao apagar cliente:", error);
        alert('Erro de ligação com o servidor.');
    }
}