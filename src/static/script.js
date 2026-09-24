// Lógica de navegação entre as secções do Dashboard
function mudarSecao(secaoId) {
    // Esconde todas as secções
    const secoes = document.querySelectorAll('.secao-conteudo');
    secoes.forEach(secao => secao.classList.add('hidden'));

    // Mostra a secção selecionada
    const secaoAtiva = document.getElementById(`secao-${secaoId}`);
    if (secaoAtiva) {
        secaoAtiva.classList.remove('hidden');
    }

    // Atualiza o título do header com base na aba
    const titulos = {
        'dashboard': 'Dashboard Geral',
        'agendamentos': 'Gestão de Agendamentos',
        'clientes': 'Base de Clientes',
        'barbeiros': 'Nossa Equipa',
        'servicos': 'Catálogo de Serviços',
        'agenda': 'Agenda Diária',
        'financeiro': 'Relatório Financeiro'
    };
    
    const tituloElemento = document.getElementById('page-title');
    if (tituloElemento && titulos[secaoId]) {
        tituloElemento.innerText = titulos[secaoId];
    }

    // Atualiza classes ativas do menu lateral
    const links = document.querySelectorAll('.nav-link');
    links.forEach(link => {
        link.classList.remove('active-tab', 'text-[#D4AF37]');
        link.classList.add('text-gray-400');
        if(link.getAttribute('href') === `#${secaoId}`) {
            link.classList.add('active-tab', 'text-[#D4AF37]');
            link.classList.remove('text-gray-400');
        }
    });

    // Fecha a sidebar em dispositivos móveis ao clicar
    const sidebar = document.getElementById('sidebar');
    if (window.innerWidth < 768 && sidebar) {
        sidebar.classList.add('-translate-x-full');
    }
}

// Funções de controlo da Sidebar em Mobile
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
        sidebar.classList.toggle('-translate-x-full');
    }
}

// Controlo de Modais (Agendamento e Cliente)
function abrirModalAgendamento() {
    document.getElementById('modal-agendamento').classList.remove('hidden');
}
function fecharModalAgendamento() {
    document.getElementById('modal-agendamento').classList.add('hidden');
}

function abrirModalCliente() {
    document.getElementById('modal-cliente').classList.remove('hidden');
}
function fecharModalCliente() {
    document.getElementById('modal-cliente').classList.add('hidden');
}

// Sistema de Notificações Toast
function mostrarToast(mensagem) {
    const toast = document.getElementById('toast');
    const msgSpan = document.getElementById('toast-msg');
    if (toast && msgSpan) {
        msgSpan.innerText = mensagem;
        toast.classList.remove('translate-y-32');
        setTimeout(() => {
            toast.classList.add('translate-y-32');
        }, 3500);
    }
}

// Simulação de salvamento de agendamento
function salvarAgendamento(e) {
    e.preventDefault();
    fecharModalAgendamento();
    mostrarToast('Agendamento criado com sucesso!');
}

// Simulação de salvamento de cliente
function salvarCliente(e) {
    e.preventDefault();
    fecharModalCliente();
    mostrarToast('Cliente registado com sucesso!');
}

// Inicialização do Gráfico Financeiro com Chart.js
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('chartFaturamento');
    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
                datasets: [{
                    label: 'Faturamento (€)',
                    data: [1200, 1900, 1500, 2200, 2800, 3500, 3100],
                    borderColor: '#D4AF37',
                    backgroundColor: 'rgba(212, 175, 55, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: { ticks: { color: '#9CA3AF' }, grid: { color: '#27272A' } },
                    y: { ticks: { color: '#9CA3AF' }, grid: { color: '#27272A' } }
                }
            }
        });
    }
});