import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Footer from "../Footer/Footer";

const Home = () => {
  const [userData, setUserData] = useState(() => {
    const storedData = localStorage.getItem('userData');
    return storedData ? JSON.parse(storedData) : {
      user_Name: "User",
      user_type: "student",
      imgUrl: "/public/images/ai.jpg",
      comments_count: 0,
      likes_count: 0,
      saved_videos_count: 0
    };
  });

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const storedUserData = localStorage.getItem('userData');
        const userData = storedUserData ? JSON.parse(storedUserData) : null;
        
        const response = await fetch(`http://localhost:5000/profile?user_id=${userData.user_id}`);
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        const data = await response.json();

        setUserData(data);
        localStorage.setItem('userData', JSON.stringify(data));
      } catch (error) {
        console.error("Failed to fetch user data:", error);
      }
    };

    fetchUserData();
  }, []);

  useEffect(() => {
    const handleStorageChange = () => {
      const storedData = localStorage.getItem('userData');
      if (storedData) {
        setUserData(JSON.parse(storedData));
      }
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, []);

  return (
    <div>
      <section className="home-grid">
      <h1 className="heading">quick options</h1>
      <div className="box-container">
        <div className="box">
          <h3 className="title">likes and comments</h3>
          <p className="likes">
            total likes : <span>{userData.likes_count}</span>
          </p>
          <Link to="#" className="inline-btn">likes</Link>
          <p className="likes">
            total comments : <span>{userData.comments_count}</span>
          </p>
          <Link to="#" className="inline-btn">comments</Link>
          <p className="likes">
            saved playlists : <span>{userData.saved_videos_count}</span>
          </p>
          <Link to="#" className="inline-btn">playlists</Link>
        </div>
        <div className="box">
          <h3 className="title">top categories</h3>
          <div className="flex">
            <Link to="#">
              <i className="fas fa-code"></i>
              <span>development</span>
            </Link>
            <Link to="#">
              <i className="fas fa-chart-simple"></i>
              <span>business</span>
            </Link>
            <Link to="#">
              <i className="fas fa-pen"></i>
              <span>design</span>
            </Link>
            <Link to="#">
              <i className="fas fa-chart-line"></i>
              <span>marketing</span>
            </Link>
            <Link to="#">
              <i className="fas fa-music"></i>
              <span>music</span>
            </Link>
            <Link to="#">
              <i className="fas fa-camera"></i>
              <span>photography</span>
            </Link>
            <Link to="#">
              <i className="fas fa-cog"></i>
              <span>software</span>
            </Link>
            <Link to="#">
              <i className="fas fa-vial"></i>
              <span>science</span>
            </Link>
          </div>
        </div>
        <div className="box">
          <h3 className="title">popular topics</h3>
          <div className="flex">
            <Link to="#">
              <i className="fab fa-html5"></i>
              <span>HTML</span>
            </Link>
            <Link to="#">
              <i className="fab fa-css3"></i>
              <span>CSS</span>
            </Link>
            <Link to="#">
              <i className="fab fa-js"></i>
              <span>javascript</span>
            </Link>
            <Link to="#">
              <i className="fab fa-react"></i>
              <span>react</span>
            </Link>
            <Link to="#">
              <i className="fab fa-php"></i>
              <span>PHP</span>
            </Link>
            <Link to="#">
              <i className="fab fa-bootstrap"></i>
              <span>bootstrap</span>
            </Link>
          </div>
        </div>
        <div className="box">
          <h3 className="title">become a tutor</h3>
          <p className="tutor">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit.
            Perspiciatis, nam?
          </p>
          <Link to="/teachers" className="inline-btn">get started</Link>
        </div>
      </div>
    </section>
    {/* "Our Courses" Section */}
    <section className="courses">
        <h1 className="heading">our courses</h1>
        <div className="box-container">
          <div className="box">
            <div className="tutor">
              <img src="images/pic-2.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-1.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete HTML tutorial</h3>
            <Link to="/playlist/1" className="inline-btn">view playlist</Link>
          </div>

          <div className="box">
            <div className="tutor">
              <img src="images/pic-3.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-2.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete CSS tutorial</h3>
            <Link to="/playlist/2" className="inline-btn">view playlist</Link>
          </div>

          <div className="box">
            <div className="tutor">
              <img src="images/pic-4.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-3.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete JS tutorial</h3>
            <Link to="/playlist/3" className="inline-btn">view playlist</Link>
          </div>

          <div className="box">
            <div className="tutor">
              <img src="images/pic-5.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-4.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete Bootstrap tutorial</h3>
            <Link to="/playlist/4" className="inline-btn">view playlist</Link>
          </div>

          <div className="box">
            <div className="tutor">
              <img src="images/pic-6.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-5.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete JQuery tutorial</h3>
            <Link to="/playlist/5" className="inline-btn">view playlist</Link>
          </div>

          <div className="box">
            <div className="tutor">
              <img src="images/pic-7.jpg" alt="" />
              <div className="info">
                <h3>john deo</h3>
                <span>21-10-2022</span>
              </div>
            </div>
            <div className="thumb">
              <img src="images/thumb-6.png" alt="" />
              <span>10 videos</span>
            </div>
            <h3 className="title">complete SASS tutorial</h3>
            <Link to="/playlist/6" className="inline-btn">view playlist</Link>
          </div>
        </div>

        <div className="more-btn">
          <Link to="/courses" className="inline-option-btn">view all courses</Link>
        </div>
      </section>
      
      <Footer />
    </div>
  );
};

export default Home;
