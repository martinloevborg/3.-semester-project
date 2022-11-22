<template>
  <div class="home">
    <h1></h1>
    <h2>Recently played</h2>
    <div id="Playlist">
        <ul id="popPlaylists">
            <li v-for="playlist in playlists" :key="playlist.id">
                <router-link to="/playlist"><img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150"/></router-link>
                <br/>
                <b>{{ playlist.title }}</b>
                <br/>
                {{playlist.creator}}
            </li>
        </ul>
      </div>
    <h2>Popular playlists</h2>
      <div id="Playlist">
        <ul id="popPlaylists">
            <li v-for="playlist in playlists" :key="playlist.id">
                <router-link :to="getPlaylistUrl(playlist.title)" ><img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150"/></router-link>
                <br/>
                <b>{{ playlist.title }}</b>
                <br/>
                {{playlist.creator}}
            </li>
        </ul>
      </div>
    <h2>Friday mood</h2>
    <div id="Playlist">
        <ul id="popPlaylists">
            <li v-for="playlist in playlists" :key="playlist.id">
                <router-link to="/playlist"><img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150"/></router-link>
                <br/>
                <b>{{ playlist.title }}</b>
                <br/>
                {{playlist.creator}}
            </li>
        </ul>
      </div>
  </div>
</template>

<script>
import { PlaylistService } from '@/services/PlaylistService'
import { baseURL } from "@/helpers/URLHelper"

export default {
  name: 'Home',
  data() {
    return {
      playlists: []
    };
  },
  created() {
    this.loadPlaylists();
  },
  methods: {
    async loadPlaylists() {
      try {
        this.playlists = await PlaylistService.getPlaylists("popular");
      } catch (error) {
        console.log(error.message);
      }
    },
    getImgUrl(img) {
      return baseURL + img;
    },
    getPlaylistUrl(playlist) {
      return "playlist/" + playlist.toLowerCase();
    },
    message() {
      alert("alert");
    }
  }
}
</script>

<style scoped>
li {
  padding: 5px;
}
img {
  border-radius: 5px;
}
</style>
