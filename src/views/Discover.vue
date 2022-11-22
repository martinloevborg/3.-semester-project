<template>
  <div class="discover">
    <div>
      <table style="width: 25%; text-align: left;">
        <tr>
            <td><button type="button">Play</button></td>
            <td><button type="button">Refresh</button></td>
            <td><button type="button" style="margin-left: 950%">Filter</button></td>
        </tr>
      </table>
    </div>
    <br>
    <div id="Playlist">
      <ul id="popPlaylists">
          <li v-for="playlist in playlists" :key="playlist.id">
              <img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150">
              <br/>
              <b>{{ playlist.title }}</b>
              <br/>
              {{playlist.creator}}
          </li>
      </ul>
    </div>
    <br>
    <div id="Playlist">
      <ul id="popPlaylists">
          <li v-for="playlist in playlists" :key="playlist.id">
              <img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150">
              <br/>
              <b>{{ playlist.title }}</b>
              <br/>
              {{playlist.creator}}
          </li>
      </ul>
    </div>
    <br>
    <div id="Playlist">
      <ul id="popPlaylists">
          <li v-for="playlist in playlists" :key="playlist.id">
              <img :src=getImgUrl(playlist.thumbnailUrl) width="150" height="150">
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