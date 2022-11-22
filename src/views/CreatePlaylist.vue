<template>

  <div class="createPlaylist">
    <h1>This is the create playlist page</h1>
    <button @click="createPlaylist()"><b>Create Playlist</b></button>
    <input v-model="playlistName" placeholder="Enter playlist name"> 
    <button @click="deletePlaylist()"><b>Delete Playlist</b></button>
    <ul id="playlists">
        <li v-for="playlist in playlists" :key="playlist.id">
            <img :src=getImgUrl(playlist.thumbnailUrl) width="25" height="25">
            <b>{{ playlist.title }}</b> created by {{playlist.creator}}
        </li>
    </ul>
  </div>
</template>

<script>
import { PlaylistService } from '@/services/PlaylistService'
import { baseURL } from "@/helpers/URLHelper"

export default {
  name: 'createPlaylist',
    data(){
      return{
        playlist: [],
        playlists: [],
        playlistName: '',
        };
      },
      created() {
        this.loadPlaylists();
      },
      methods:{
        async createPlaylist() {
        try {
        const username = "testuser"; //This should be loaded from the cookie 
        const jsonPlaylist = '{"title": "' + this.playlistName + '","creator":"'+ username +'", "thumbnailUrl": "thumbnails/truelove" }'
        this.playlist = await PlaylistService.postPlaylist(username, jsonPlaylist);
        }
        catch (error) {
        console.log(error.message);
      }
    },
    async deletePlaylist() {
        try {
        const username = "testuser"; //This should be loaded from the cookie 
        this.playlist = await PlaylistService.deletePlaylist(username);
        }
        catch (error) {
        console.log(error.message);
      }
    },
    async loadPlaylists() {
      try {
        const username = "testuser"; //This should be loaded from the cookie 
        this.playlists = await PlaylistService.getPlaylists(username);
      } catch (error) {
        console.log(error.message);
      }
    },
    getImgUrl(img) {
        return baseURL + img;
    }
  }
}

</script>