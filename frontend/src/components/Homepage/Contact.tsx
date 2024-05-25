import React, { useState } from 'react';
import emailjs from 'emailjs-com';

const Contact: React.FC = () => {
  const [formState, setFormState] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [submitMessage, setSubmitMessage] = useState('');
  const [consent, setConsent] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormState({
      ...formState,
      [e.target.id]: e.target.value,
    });
  };

  const handleConsentChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setConsent(e.target.checked);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    emailjs
      .send('transfermax', 'template_bqevorg', formState, 'W0uLdj1znLzYkLAQN')
      .then(
        (result) => {
          console.log(result.text);
          setSubmitMessage('Message sent successfully!');
          resetForm();
        },
        (error) => {
          console.log(error.text);
          setSubmitMessage('Failed to send the message, please try again.');
          resetForm();
        }
      );
  };

  const resetForm = () => {
    setFormState({
      name: '',
      email: '',
      subject: '',
      message: '',
    });
    setConsent(false);
  };

  return (
    <div className="container mx-auto p-8" id="contact">
      <div className="flex flex-wrap -mx-4">
        <div className="w-full md:w-1/2 px-4 flex items-center">
          <img
            alt="Students celebrating success"
            className="mb-6 rounded w-full h-auto"
            src="https://campustechnology.com/-/media/EDU/CampusTechnology/Images/2017/08/20170810success.jpg"
          />
        </div>
        <div className="w-full md:w-1/2 px-4">
          <h1 className="text-3xl font-bold text-blue-700 mb-4">How can we help?</h1>
          <h2 className="text-xl font-semibold mb-2">Connect with TransferMax</h2>
          <p className="text-gray-600 mb-6">
            Contact us today for personalized assistance in finding community college equivalent courses.
          </p>
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label className="block text-gray-700 font-bold mb-2" htmlFor="name">
                Name <span className="text-red-500">*</span>
              </label>
              <input
                className="w-full px-3 py-2 border border-gray-300 rounded"
                id="name"
                type="text"
                value={formState.name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700 font-bold mb-2" htmlFor="email">
                Email address <span className="text-red-500">*</span>
              </label>
              <input
                className="w-full px-3 py-2 border border-gray-300 rounded"
                id="email"
                type="email"
                value={formState.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700 font-bold mb-2" htmlFor="subject">
                Subject
              </label>
              <input
                className="w-full px-3 py-2 border border-gray-300 rounded"
                id="subject"
                type="text"
                value={formState.subject}
                onChange={handleChange}
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700 font-bold mb-2" htmlFor="message">
                Message
              </label>
              <textarea
                className="w-full px-3 py-2 border border-gray-300 rounded"
                id="message"
                rows={4}
                value={formState.message}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            <div className="mb-4">
              <label className="inline-flex items-center">
                <input
                  className="form-checkbox text-blue-600"
                  type="checkbox"
                  checked={consent}
                  onChange={handleConsentChange}
                  required
                />
                <span className="ml-2 text-gray-700">
                  I allow this website to store my submission so they can respond to my inquiry.{' '}
                  <span className="text-red-500">*</span>
                </span>
              </label>
            </div>
            <div>
              <button className="w-full bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">
                SUBMIT
              </button>
            </div>
            {submitMessage && (
              <p className={`text-center mt-4 ${submitMessage.includes('successfully') ? 'text-green-500' : 'text-red-500'}`}>
                {submitMessage}
              </p>
            )}
          </form>
        </div>
      </div>
    </div>
  );
};

export default Contact;
