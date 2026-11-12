import { useEffect, useState } from 'react'
import { listEvents, register } from './api.js'

export default function App() {
  const [events, setEvents] = useState([])
  const [userId, setUserId] = useState(1)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [message, setMessage] = useState('')
  const [submittingId, setSubmittingId] = useState(null)

  useEffect(() => {
    listEvents()
      .then(data => setEvents(data))
      .catch(() => setError('Não foi possível carregar os eventos.'))
      .finally(() => setLoading(false))
  }, [])

  async function handleRegister(eventId) {
    setSubmittingId(eventId)
    setError('')
    setMessage('')

    try {
      await register(eventId, userId)
      const updatedEvents = await listEvents()
      setEvents(updatedEvents)
      setMessage('Inscrição realizada com sucesso!')
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmittingId(null)
    }
  }

  function formatSlots(slots) {
    if (slots === 1) {
      return '1 vaga disponível'
    }
    return `${slots} vagas disponíveis`
  }

  return (
    <main className="page">
      <header>
        <p className="eyebrow">Trilha · Laboratório Full Stack</p>
        <h1>Eventos</h1>
        <p>Encontre uma atividade e garanta sua vaga.</p>
      </header>

      <label className="user-picker">
        Participante de demonstração
        <select value={userId} onChange={event => setUserId(Number(event.target.value))}>
          <option value="1">Pessoa 1</option>
          <option value="2">Pessoa 2</option>
        </select>
      </label>

      {message && <p role="status">{message}</p>}
      {error && <p role="alert">{error}</p>}

      <section aria-label="Lista de eventos" className="events">
        {loading && <p>Carregando eventos...</p>}
        {!loading && !error && events.length === 0 && <p>Nenhum evento encontrado.</p>}
        {!loading &&
          events.map(event => (
            <article key={event.id} className="card">
              <p className="date">{event.date}</p>
              <h2>{event.title}</h2>
              <p>{formatSlots(event.available_slots)}</p>
              <button
                type="button"
                disabled={submittingId === event.id || event.available_slots <= 0}
                onClick={() => handleRegister(event.id)}
              >
                Inscrever-se
              </button>
            </article>
          ))}
      </section>
    </main>
  )
}
