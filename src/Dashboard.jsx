export default function Dashboard() {
  return (
    <div style={{ padding: '40px', fontFamily: 'Arial', background: '#f4f6fa', minHeight: '100vh' }}>
      <h1 style={{ color: '#0B2545' }}>✅ Dashboard El Niño 2026/2027</h1>
      <p style={{ color: '#666', marginTop: '20px' }}>🚀 Servidor rodando em produção!</p>
      
      <div style={{ marginTop: '40px', background: '#fff', padding: '20px', borderRadius: '8px' }}>
        <h2 style={{ color: '#0B2545', marginBottom: '15px' }}>Informações</h2>
        <ul style={{ color: '#666', lineHeight: '2' }}>
          <li>✅ React + Vite</li>
          <li>✅ Vercel (produção)</li>
          <li>✅ GitHub (versionamento)</li>
          <li>✅ Pronto para Supabase</li>
        </ul>
      </div>
    </div>
  )
}