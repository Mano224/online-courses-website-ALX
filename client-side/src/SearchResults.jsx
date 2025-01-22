import React, { useState, useEffect } from 'react';

const SearchResults = () => {
  const [results, setResults] = useState({
    playlists: [],
    videos: [],
    users: []
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Get search query from URL
  const queryParams = new URLSearchParams(window.location.search);
  const searchQuery = queryParams.get('q');

  useEffect(() => {
    const fetchResults = async () => {
      try {
        setLoading(true);
        if (!searchQuery) {
          setResults({ playlists: [], videos: [], users: [] });
          return;
        }

        const response = await fetch(`http://localhost:5000/search?q=${encodeURIComponent(searchQuery)}`);
        if (!response.ok) {
          throw new Error('Failed to fetch search results');
        }

        const data = await response.json();
        setResults(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, [searchQuery]);

  if (loading) {
    return (
      <div className="min-h-screen p-8 flex items-center justify-center">
        <div className="text-xl">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen p-8 flex items-center justify-center">
        <div className="text-xl text-red-500">Error: {error}</div>
      </div>
    );
  }

  const navigateToCourse = (playlistId) => {
    window.location.href = `/courses/${playlistId}`;
  };

  return (
    <div className="min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-8">Search Results for: {searchQuery}</h1>
      
      {/* Playlists Section */}
      {results.playlists?.length > 0 && (
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Courses</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {results.playlists.map((playlist) => (
              <div 
                key={playlist.id} 
                className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer p-6"
                onClick={() => navigateToCourse(playlist.id)}
              >
                <h3 className="text-lg font-semibold mb-2">{playlist.title}</h3>
                {playlist.thumbnail && (
                  <img 
                    src={playlist.thumbnail} 
                    alt={playlist.title}
                    className="w-full h-48 object-cover rounded-md"
                  />
                )}
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Videos Section */}
      {results.videos?.length > 0 && (
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Videos</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {results.videos.map((video) => (
              <div 
                key={video.id} 
                className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6"
              >
                <h3 className="text-lg font-semibold mb-2">{video.title}</h3>
                {video.thumbnail && (
                  <img 
                    src={video.thumbnail} 
                    alt={video.title}
                    className="w-full h-48 object-cover rounded-md mb-4"
                  />
                )}
                <p className="text-sm text-gray-600 dark:text-gray-400">{video.description}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Show message if no results found */}
      {!results.playlists?.length && !results.videos?.length && (
        <div className="text-center py-8">
          <p className="text-xl text-gray-600 dark:text-gray-400">No results found for your search.</p>
        </div>
      )}
    </div>
  );
};

export default SearchResults;