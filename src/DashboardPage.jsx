import { useEffect, useState } from 'react'

export default function DashboardPage() {
  const [htmlContent, setHtmlContent] = useState('')

  useEffect(() => {
    fetch('/NT_ElNino_2026-27_COMPLETA_AUDITAVEL.html')
      .then(res => res.text())
      .then(html => setHtmlContent(html))
      .catch(err => console.error('Erro ao carregar:', err))
  }, [])

  return (
    <div dangerouslySetInnerHTML={{ __html: htmlContent }} />
  )
}