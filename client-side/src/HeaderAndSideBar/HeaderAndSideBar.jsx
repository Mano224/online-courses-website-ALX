import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';

const HeaderAndSideBar = ({ onSearch }) => {
  const [sideBarActive, setSideBarActive] = useState(false);
  const [darkMode, setDarkMode] = useState(localStorage.getItem('dark-mode') === 'enabled');
  const [profileActive, setProfileActive] = useState(false);
  const [searchActive, setSearchActive] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const toggleSideBar = () => {
    setSideBarActive(!sideBarActive);
    document.body.classList.toggle('active', !sideBarActive);
  };

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
    localStorage.setItem('dark-mode', darkMode ? 'enabled' : 'disabled');
  }, [darkMode]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    onSearch(searchQuery);
    navigate('/search');
  };

  return (
    <>
      <header className="header">
        <section className="flex">
          <Link to="/" className="logo">Educa.</Link>
          <form onSubmit={handleSearchSubmit} className={`search-form ${searchActive ? 'active' : ''}`}>
            <input
              type="text"
              name="search_box"
              required
              placeholder="search courses..."
              maxLength="100"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            <button type="submit" className="fas fa-search"></button>
          </form>
          <div className="icons">
            <div id="menu-btn" className="fas fa-bars" onClick={toggleSideBar}></div>
            <div id="search-btn" className="fas fa-search" onClick={() => setSearchActive(!searchActive)}></div>
            <div id="user-btn" className="fas fa-user" onClick={() => setProfileActive(!profileActive)}></div>
            <div id="toggle-btn" className={`fas ${darkMode ? 'fa-moon' : 'fa-sun'}`} onClick={toggleDarkMode}></div>
          </div>
          <div className={`profile ${profileActive ? 'active' : ''}`}>
            <img src="../images/pic-1.jpg" className="image" alt="" />
            <h3 className="name">shaikh anas</h3>
            <p className="role">student</p>
            <Link to="/profile" className="btn">view profile</Link>
            <div className="flex-btn">
              <Link to="/login" className="option-btn">login</Link>
              <Link to="/register" className="option-btn">register</Link>
            </div>
          </div>
        </section>
      </header>

      <div className={`side-bar ${sideBarActive ? 'active' : ''}`}>
        <div id="close-btn" onClick={toggleSideBar}>
          <i className="fas fa-times"></i>
        </div>
        <div className="profile">
          <img src="images/pic-1.jpg" className="image" alt="Profile" />
          <h3 className="name">shaikh anas</h3>
          <p className="role">student</p>
          <Link to="/profile" className="btn">view profile</Link>
        </div>
        <nav className="navbar">
          <Link to="/">
            <i className="fas fa-home"></i>
            <span>home</span>
          </Link>
          <Link to="/about">
            <i className="fas fa-question"></i>
            <span>about</span>
          </Link>
          <Link to="/courses">
            <i className="fas fa-graduation-cap"></i>
            <span>courses</span>
          </Link>
          <Link to="/teachers">
            <i className="fas fa-chalkboard-user"></i>
            <span>teachers</span>
          </Link>
          <Link to="/contact">
            <i className="fas fa-headset"></i>
            <span>contact us</span>
          </Link>
        </nav>
      </div>
    </>
  );
};

export default HeaderAndSideBar;
