<template>
  <div class="about">
    <div>
      <h1 style="text-align: left;">Moodes & Genres</h1>
      <table>
        <tr>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Pop</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Sad</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Dance</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Happy</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Friday</button></td>
        </tr>
        <br/>
        <tr>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Mood Mood</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Pop</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Dubstep</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Epic</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Saturday Night</button></td>
        </tr>
        <br/>
        <tr>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Hip Hop</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Fire</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Life</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Spicy</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Hype</button></td>
        </tr>
        <br/>
        <tr>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Pop</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Chill</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Bangers</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Pop</button></td>
            <td><button v-bind:class="'rcButton' + (Math.floor(Math.random() * (6 - 1) + 1))">Pop</button></td>
        </tr>
      </table>
    </div>
    <br>
    <h1 style="text-align: left;">Trending</h1>
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
    <h1 style="text-align: left;">New Releases</h1>
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
    <h1 style="text-align: left;">Charts</h1>
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
        playlists: [],
        randomColor: true,
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
td {
  padding: 16px;
}

  li {
    padding: 5px;
  }
  img {
    border-radius: 5px;
  }
  button {
    width: 140px;
  }

  .rcButton1 {
    background: #AB5959 !important;
  }

  .rcButton2 {
    background: #7AA8AB !important;
  }

  .rcButton3 {
    background: #8E4EB5 !important;
  }

  .rcButton4 {
    background: #47965D !important;
  }

  .rcButton5 {
    background: #BEB55E !important;
  }

  </style>