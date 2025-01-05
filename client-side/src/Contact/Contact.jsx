import { useState } from 'react';
import Footer from '../Footer/Footer';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    number: '',
    message: ''
  });
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const userId = JSON.parse(localStorage.getItem('userData'))?.user_id;
      console.log('Retrieved userId:', userId);
      
      if (!userId) {
        setError('Please login first');
        return;
      }

      const response = await fetch('http://localhost:5000/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: String(userId), // Convert userId to string
          name: formData.name,
          email: formData.email,
          number: formData.number,
          message: formData.message
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage('Message sent successfully!');
        setError('');
        setFormData({
          name: '',
          email: '',
          number: '',
          message: ''
        });
      } else {
        setError(data.error || 'Failed to send message');
        setMessage('');
      }
    } catch (error) {
      setError('Failed to send message. Please try again later.');
      setMessage('');
    }
  };

  return (
    <>
      <section className="contact">
        <div className="row">
          <div className="image">
            <img src="/images/contact-img.svg" alt="contact" />
          </div>
          
          <form onSubmit={handleSubmit}>
            <h3>get in touch</h3>
            
            {error && <div className="error-message" style={{ color: 'red', marginBottom: '1rem' }}>{error}</div>}
            {message && <div className="success-message" style={{ color: 'green', marginBottom: '1rem' }}>{message}</div>}
            
            <input
              type="text"
              placeholder="enter your name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              maxLength="50"
              className="box"
            />

            <input
              type="email"
              placeholder="enter your email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              maxLength="50"
              className="box"
            />

            <input
              type="tel"
              placeholder="enter your number"
              name="number"
              value={formData.number}
              onChange={handleChange}
              required
              maxLength="15"
              className="box"
            />

            <textarea
              name="message"
              className="box"
              placeholder="enter your message"
              value={formData.message}
              onChange={handleChange}
              required
              maxLength="1000"
              cols="30"
              rows="10"
            ></textarea>

            <input type="submit" value="send message" className="inline-btn" />
          </form>
        </div>

        <div className="box-container">
          <div className="box">
            <i className="fas fa-phone"></i>
            <h3>phone number</h3>
            <a href="tel:1234567890">123-456-7890</a>
            <a href="tel:1112223333">111-222-3333</a>
          </div>
          
          <div className="box">
            <i className="fas fa-envelope"></i>
            <h3>email address</h3>
            <a href="mailto:shaikhanas@gmail.com">shaikhanas@gmail.com</a>
            <a href="mailto:anasbhai@gmail.com">anasbhai@gmail.com</a>
          </div>
          
          <div className="box">
            <i className="fas fa-map-marker-alt"></i>
            <h3>office address</h3>
            <a href="#">flat no. 1, a-1 building, jogeshwari, mumbai, india - 400104</a>
          </div>
        </div>
      </section>
      <Footer />
    </>
  );
};

export default Contact;