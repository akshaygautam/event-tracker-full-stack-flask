import React, { useEffect, useState } from "react"
import axios from 'axios'
import {format} from 'date-fns'
import '../App.css';

const Events = ()=> { 
    const baseUrl = 'http://localhost:8080'
    const [description, setDescription] = useState("")
    const [editDescription, setEditDescription] = useState("")
    const [eventsList, setEventsList] = useState([])
    const [eventId, setEventId] = useState(null)
    const handleChange = (e, create) => {
      create ? setDescription(e.target.value) : setEditDescription(e.target.value)
    }
    const handleSubmit = async(e) => {
      try {
        e.preventDefault();
        if (editDescription) {
          const response = await axios.put(`${baseUrl}/events/${eventId}`, {'description':editDescription})
          const updatedEvent = response.data
          const updatedList = eventsList.map(event => (event.id == eventId) ? updatedEvent : event)
          setEventsList(updatedList)
        } 
        else {
          const response  = await axios.post(`${baseUrl}/events`, {description})
          setEventsList([...eventsList, response.data])
        }
        setDescription('')
        setEditDescription('')
        setEventId(null)
      } catch (err) {
        console.error(err.message)
      }
    }
    const fetchEvents = async()=> {
      const response = await axios.get(`${baseUrl}/events`)
      setEventsList(response.data)
    }
  
    const handleDelete = async(id) => {
      try {
        const response = await axios.delete(`${baseUrl}/events/${id}`)
        fetchEvents()
      } catch (err) {
        console.error(err.message)
      }
  
    }
  
    useEffect(() => {
      fetchEvents()
    }, [])
  
    const toggleEdit = (events) => {
      setEventId(events.id)
      setEditDescription(events.description)
    }
    return (<div>
        <section>
          <form onSubmit={handleSubmit}>
            <label htmlFor='description'>Discription</label>
            <input name = "description" id = 'description' type = 'text' value={description}
            onChange={(e)=>handleChange(e, true)} placeholder='Enter some event'/>
            <button type='submit'>Submit</button>
          </form>
        </section>
        <section>
          <ul>
            {eventsList.map(events=> {
              if (eventId == events.id) {
                return(<li style={{display:'flex'}} key={events.id}>
                  <form onSubmit={handleSubmit}>
                    <input name = "description" id = 'description' type = 'text' value={editDescription}
                    onChange={(e)=>handleChange(e, false)}/>
                    <button type='submit'>Submit</button>
                  </form>
                </li>)
              } else { 
                return(<li style={{display:'flex'}} key={events.id}>
                  {format(new Date(events.created_at), 'dd-mm-yyy p')}
                  {"\t"+ events.description}
                  <button onClick={()=>toggleEdit(events)}>Edit</button>
                  <button onClick={()=>handleDelete(events.id)}>X</button>
                </li>)
              }
              })
            }
          </ul>
        </section>
    </div>)
}

export default Events