<!-- Yapay Zeka Asistanı Modal -->
<div class="ai-assistant-modal" id="aiAssistantModal">
    <div class="ai-assistant-content">
        <div class="ai-assistant-header">
            <h3><i class="fas fa-robot"></i> Futbol Asistanı</h3>
            <button class="close-btn" id="closeAIBtn">&times;</button>
        </div>
        <div class="ai-chat-container">
            <div class="ai-messages" id="aiMessages">
                <div class="ai-message bot-message">
                    <div class="message-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="message-content">
                        Merhaba! Ben ftblzone futbol asistanıyım. Maçlar, takımlar, istatistikler 
                        veya futbol hakkında her şeyi sorabilirsin. Size nasıl yardımcı olabilirim?
                    </div>
                </div>
            </div>
            <div class="ai-input-container">
                <input type="text" id="aiInput" placeholder="Futbol hakkında bir şey sorun...">
                <button id="sendAIBtn">
                    <i class="fas fa-paper-plane"></i>
                </button>
            </div>
        </div>
        <div class="ai-quick-questions">
            <div class="quick-question" data-question="Bugünkü önemli maçlar neler?">
                <i class="fas fa-futbol"></i>
                Bugünkü maçlar
            </div>
            <div class="quick-question" data-question="Galatasaray'ın son performansı nasıl?">
                <i class="fas fa-chart-line"></i>
                Takım analizi
            </div>
            <div class="quick-question" data-question="Şampiyonlar Ligi'nde hangi takımlar var?">
                <i class="fas fa-trophy"></i>
                Şampiyonlar Ligi
            </div>
        </div>
    </div>
</div>

<!-- Maç Analiz Modal -->
<div class="match-analysis-modal" id="matchAnalysisModal">
    <div class="analysis-content">
        <div class="analysis-header">
            <h3><i class="fas fa-chart-bar"></i> Yapay Zeka Maç Analizi</h3>
            <button class="close-btn" id="closeAnalysisBtn">&times;</button>
        </div>
        <div class="analysis-body" id="analysisBody">
            <div class="loading-analysis">
                <i class="fas fa-spinner fa-spin"></i>
                <p>Maç analizi hazırlanıyor...</p>
            </div>
        </div>
    </div>
</div>

<style>
    /* Yapay Zeka Asistanı Stilleri */
    .ai-assistant-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        display: none;
        justify-content: center;
        align-items: center;
        z-index: 1003;
    }

    .ai-assistant-content {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: var(--radius);
        width: 90%;
        max-width: 500px;
        max-height: 80vh;
        display: flex;
        flex-direction: column;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .ai-assistant-header {
        padding: 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .ai-assistant-header h3 {
        color: white;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .close-btn {
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
    }

    .ai-chat-container {
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 20px;
    }

    .ai-messages {
        flex: 1;
        overflow-y: auto;
        margin-bottom: 20px;
        max-height: 300px;
    }

    .ai-message {
        display: flex;
        margin-bottom: 15px;
        gap: 10px;
    }

    .bot-message {
        flex-direction: row;
    }

    .user-message {
        flex-direction: row-reverse;
    }

    .message-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--secondary);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .user-message .message-avatar {
        background: var(--primary);
    }

    .message-content {
        background: rgba(255, 255, 255, 0.1);
        padding: 12px 15px;
        border-radius: var(--radius);
        max-width: 80%;
        color: white;
    }

    .user-message .message-content {
        background: rgba(26, 115, 232, 0.3);
    }

    .ai-input-container {
        display: flex;
        gap: 10px;
    }

    .ai-input-container input {
        flex: 1;
        padding: 12px 15px;
        border-radius: var(--radius);
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: rgba(255, 255, 255, 0.1);
        color: white;
    }

    .ai-input-container button {
        padding: 12px 20px;
        background: var(--secondary);
        color: white;
        border: none;
        border-radius: var(--radius);
        cursor: pointer;
    }

    .ai-quick-questions {
        display: flex;
        gap: 10px;
        padding: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        flex-wrap: wrap;
    }

    .quick-question {
        padding: 8px 12px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: var(--radius);
        cursor: pointer;
        font-size: 0.8rem;
        display: flex;
        align-items: center;
        gap: 5px;
        transition: var(--transition);
    }

    .quick-question:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    /* Maç Analiz Modal */
    .match-analysis-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        display: none;
        justify-content: center;
        align-items: center;
        z-index: 1003;
    }

    .analysis-content {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: var(--radius);
        width: 90%;
        max-width: 600px;
        max-height: 80vh;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .analysis-header {
        padding: 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .analysis-header h3 {
        color: white;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .analysis-body {
        padding: 20px;
        color: white;
        max-height: 60vh;
        overflow-y: auto;
    }

    .loading-analysis {
        text-align: center;
        padding: 40px;
    }

    .loading-analysis i {
        font-size: 2rem;
        margin-bottom: 15px;
        color: var(--secondary);
    }

    /* Ana arayüze AI butonu ekle */
    .ai-assistant-btn {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
    }
</style>

<script>
    // Yapay Zeka Fonksiyonları
    const aiAssistantModal = document.getElementById('aiAssistantModal');
    const matchAnalysisModal = document.getElementById('matchAnalysisModal');
    const aiMessages = document.getElementById('aiMessages');
    const aiInput = document.getElementById('aiInput');
    const sendAIBtn = document.getElementById('sendAIBtn');
    const closeAIBtn = document.getElementById('closeAIBtn');
    const closeAnalysisBtn = document.getElementById('closeAnalysisBtn');
    const quickQuestions = document.querySelectorAll('.quick-question');

    // API endpoint'i - Flask sunucusunun adresini buraya yazın
    const API_BASE_URL = 'http://localhost:5000';

    // Yapay zeka asistanını aç
    function openAIAssistant() {
        aiAssistantModal.style.display = 'flex';
        aiInput.focus();
    }

    // Yapay zeka asistanını kapat
    function closeAIAssistant() {
        aiAssistantModal.style.display = 'none';
    }

    // Maç analizini aç
    function openMatchAnalysis(matchData) {
        matchAnalysisModal.style.display = 'flex';
        analyzeMatch(matchData);
    }

    // Maç analizini kapat
    function closeMatchAnalysis() {
        matchAnalysisModal.style.display = 'none';
    }

    // Mesaj gönder
    async function sendMessage() {
        const message = aiInput.value.trim();
        if (!message) return;

        // Kullanıcı mesajını ekrana ekle
        addMessage(message, 'user');
        aiInput.value = '';

        // Yapay zekadan cevap al
        try {
            const response = await fetch(`${API_BASE_URL}/api/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    context: 'futbol'
                })
            });

            const data = await response.json();
            
            if (data.success) {
                addMessage(data.response, 'bot');
            } else {
                addMessage('Üzgünüm, şu anda cevap veremiyorum. Lütfen daha sonra tekrar deneyin.', 'bot');
            }
        } catch (error) {
            console.error('AI hatası:', error);
            addMessage('Bağlantı hatası oluştu. Lütfen internet bağlantınızı kontrol edin.', 'bot');
        }
    }

    // Maç analizi yap
    async function analyzeMatch(matchData) {
        try {
            const response = await fetch(`${API_BASE_URL}/api/match-analysis`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    match_data: matchData
                })
            });

            const data = await response.json();
            
            const analysisBody = document.getElementById('analysisBody');
            if (data.success) {
                analysisBody.innerHTML = `
                    <div class="analysis-result">
                        <h4>Maç Analizi</h4>
                        <div class="analysis-text">
                            ${data.analysis.replace(/\n/g, '<br>')}
                        </div>
                    </div>
                `;
            } else {
                analysisBody.innerHTML = `
                    <div class="analysis-error">
                        <i class="fas fa-exclamation-triangle"></i>
                        <p>Maç analizi şu anda yapılamıyor.</p>
                    </div>
                `;
            }
        } catch (error) {
            console.error('Analiz hatası:', error);
            document.getElementById('analysisBody').innerHTML = `
                <div class="analysis-error">
                    <i class="fas fa-exclamation-triangle"></i>
                    <p>Analiz servisine bağlanılamadı.</p>
                </div>
            `;
        }
    }

    // Mesajı ekrana ekle
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `ai-message ${sender}-message`;
        
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-${sender === 'bot' ? 'robot' : 'user'}"></i>
            </div>
            <div class="message-content">
                ${text}
            </div>
        `;
        
        aiMessages.appendChild(messageDiv);
        aiMessages.scrollTop = aiMessages.scrollHeight;
    }

    // Event listener'ları ekle
    document.addEventListener('DOMContentLoaded', function() {
        // AI asistan butonunu header'a ekle
        const headerControls = document.querySelector('.header-controls');
        const aiBtn = document.createElement('button');
        aiBtn.className = 'btn ai-assistant-btn';
        aiBtn.innerHTML = '<i class="fas fa-robot"></i> AI Asistan';
        aiBtn.addEventListener('click', openAIAssistant);
        headerControls.appendChild(aiBtn);

        // Basit arayüz için de AI butonu ekle
        const simpleHeaderControls = document.querySelector('#simpleInterface .header-controls');
        if (simpleHeaderControls) {
            const simpleAiBtn = document.createElement('button');
            simpleAiBtn.className = 'btn ai-assistant-btn';
            simpleAiBtn.innerHTML = '<i class="fas fa-robot"></i> AI Asistan';
            simpleAiBtn.addEventListener('click', openAIAssistant);
            simpleHeaderControls.appendChild(simpleAiBtn);
        }

        // Event listener'lar
        sendAIBtn.addEventListener('click', sendMessage);
        closeAIBtn.addEventListener('click', closeAIAssistant);
        closeAnalysisBtn.addEventListener('click', closeMatchAnalysis);

        aiInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        // Hızlı sorular
        quickQuestions.forEach(question => {
            question.addEventListener('click', function() {
                const questionText = this.getAttribute('data-question');
                aiInput.value = questionText;
                sendMessage();
            });
        });

        // Maç öğelerine analiz butonu ekle
        document.addEventListener('click', function(e) {
            if (e.target.closest('.match-item')) {
                const matchItem = e.target.closest('.match-item');
                const teams = matchItem.querySelector('.match-teams').textContent;
                const score = matchItem.querySelector('.match-score').textContent;
                
                // Sağ tık menüsü veya özel buton ile analiz açılabilir
                // Örnek: matchItem.addEventListener('contextmenu', ...)
            }
        });
    });

    // Örnek maç analizi fonksiyonu
    function analyzeCurrentMatch() {
        const matchData = {
            team1: 'Galatasaray',
            team2: 'Fenerbahçe',
            score: '2-1',
            stats: {
                possession: '54% - 46%',
                shots: '15 - 12',
                shotsOnTarget: '6 - 4',
                corners: '7 - 5',
                fouls: '14 - 16'
            },
            highlights: [
                '15. dakika: Galatasaray golü',
                '34. dakika: Fenerbahçe golü',
                '67. dakika: Galatasaray galibiyet golü'
            ]
        };
        
        openMatchAnalysis(matchData);
    }
</script>
