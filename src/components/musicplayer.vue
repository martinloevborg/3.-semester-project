<template>
    <div id="musicplayer"> Music Player
        <audio controls id="audio">
          <source :src="firstMp3" type="audio/mpeg"/>
        </audio>
        <ul id="playlists">
        <li v-for="playlist in playlists" :key="playlist.id">
        <button @click="changeSong(playlist.title)"><b>{{ playlist.title }}</b></button> {{playlist.Artist}}
        </li>
    </ul>
    </div>
</template>

<script>
import { MusicService } from '@/services/MusicService'
import { mp3URL } from "@/helpers/URLHelper"

export default {
  name: 'Music',
  data() {
    return {
      playlists: [],
      searchLists: [],
      publicPath: process.env.BASE_URL,
      firstMp3: mp3URL + "Confusion"
    };
  },
  created() {
    this.loadPlaylists();
  },
  methods: {
    async loadPlaylists() {
      try {
        const username = "testuser"; //This should be loaded from the cookie 
        this.playlists = await MusicService.getMusic(username);
      } catch (error) {
        console.log(error.message);
      }
    },
    async loadSearch(songName) {
      try {  
        this.searchLists = null;
        this.searchLists = await MusicService.getMusic(songName);
      } catch (error) {
        console.log(error.message);
      }
    },
    async getSong(songName) {
        const audio = document.getElementById("audio").src = "http://localhost:5000/mp3/" + songName;
        audio.load();
        audio.play();
    },  
    changeSong(songName) {
      const audio = document.getElementById("audio");
      audio.src = '/music/' + songName + '.mp3'
      audio.load();
      audio.play();
    }
  }
}

</script>

