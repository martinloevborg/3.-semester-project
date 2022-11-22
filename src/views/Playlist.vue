<template>
  <div id="Playlist">
    <div>
            <table style="width: 100%; text-align: left;">
                <tr>
                    <td>
                        <img :src="getImgUrl(playlist.thumbnailUrl)" alt="True Love" width="200" height="200">
                    </td>
                    <td>
                        <h4>Playlist</h4>
                        <h1>{{ playlist.title }}</h1>  
                        <h4>Created by {{ playlist.creator }} • x hours x minutes • {{ songs.length }} songs • 71,812 followers</h4>
                        <h4>{{ playlist.des }}</h4>  		  
                    </td>
                </tr>
            </table>
            <table style="width: 25%; text-align: left;">
                <tr>
                    <td><button type="button">Play</button></td>
                    <td><button type="button">Add playlist</button></td>
                    <td><button type="button">***</button></td>
                </tr>
            </table>
            <br>	
            <table style="width: 100%; text-align: left;">
                <tr>
                    <th>Title</th>
                    <th>Artist</th> 
                    <th>Album</th>
                    <th>Duration</th>
                </tr>
                <tr v-for="song in songs" :key="song.id">
                    <td><img :src=getImgUrl(song.thumbnailUrl) width="25" height="25"><b>{{ song.title }}</b></td>
                    <td><b>{{ song.creator }}</b></td>
                    <td><b>{{ song.album }}</b></td>
                    <td><b>{{ songDuration(song.duration) }}</b></td>
                </tr>
            </table>
    </div>
  </div>
</template>

<script>
import { PlaylistService } from '@/services/PlaylistService'
import { baseURL } from "@/helpers/URLHelper"

export default {
  name: 'Playlist',
  data() {
    return {
      playlist: {},
      songs: []
    };
  },
  created() {
    this.loadPlaylist(this.$route.params.id);
    this.loadSongsInPlaylist(this.$route.params.id);
    this.loadPlaylists();
  },
  methods: {
    async loadPlaylist(playlistName) {
      try {
        this.playlist = await PlaylistService.getPlaylists(playlistName);
      } catch (error) {
        console.log(error.message);
      }
    },
    async loadSongsInPlaylist(playlistName) {
      try {
        this.songs = await PlaylistService.getSongsInPlaylist(playlistName);
      } catch (error) {
        console.log(error.message);
        }
      },
      getImgUrl(img) {
        return baseURL + img;
    },
    songDuration: function(duration) {
      const min = (duration-(duration%60)) / 60;
      const sec = duration % 60;
      return min + ":" + sec;
    }
  }
}
</script>
