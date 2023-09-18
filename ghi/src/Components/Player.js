import React, { useState, useEffect } from "react";
import playlistData from "../playlist.json";
import "../stylesheets/player.css";

function Player() {
  const [playlist] = useState(playlistData);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [audioPlayer, setAudioPlayer] = useState(null);
  const [hasUserInteracted, setHasUserInteracted] = useState(false);

  useEffect(() => {
    setAudioPlayer(document.getElementById("audio-player"));
    return () => {
      setAudioPlayer(null);
    };
  }, []);

  useEffect(() => {
    if (audioPlayer && hasUserInteracted) {
      audioPlayer.load();

      const playPromise = audioPlayer.play();
      if (playPromise !== undefined) {
        playPromise.catch((error) => {
          console.log("Play interrupted: ", error);
        });
      }
    }
  }, [audioPlayer, playlist, currentIndex, hasUserInteracted]);

  const handleEnd = () => {
    setCurrentIndex((prevIndex) => {
      return (prevIndex + 1) % playlist.length;
    });
  };

  const handlePlay = () => {
    setHasUserInteracted(true);
  };

  return (
    <div className="player-container">
      <h1>Live Bootlegs</h1>
      <div id="player">
        <p>Now Playing:</p>
        <img src={playlist[currentIndex].art} alt="album cover" />{" "}
        <p>Track: {playlist[currentIndex].name}</p>
        <p>Artist: {playlist[currentIndex].artist}</p>
        <p>Album: {playlist[currentIndex].album}</p>
        <audio
          id="audio-player"
          controls
          onEnded={handleEnd}
          onPlay={handlePlay}
          src={playlist[currentIndex].src}
        >
          <source id="audio-source" type="audio/mp3" />
        </audio>
      </div>
    </div>
  );
}

export default Player;
