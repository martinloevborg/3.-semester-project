<template>
    <div id="searchbar">
      <!--
        old search:
        <input v-model="search" placeholder="Enter song name">
        <button @click="loadSearch(search)"><b>Search</b></button>
        <router-link :to="'/search/' + search">Search</router-link> 
        -->
        <i id="searchicon" class='fas fa-search'></i>
        <input id="sInputField" v-model="search" 
        v-on:keyup.enter="loadSearch(search),searchDirect(search), cleanInput()"
        :placeholder='searchPlaceholder'>
        <li v-for="song in searchLists" :key="song.id">
        <button @click="changeAudio(song.title)"><b>{{ song.title }}</b></button> {{song.Artist}}
        </li>
    </div>
</template>

<script>
import { MusicService } from '@/services/MusicService'

export default {
    name: 'Music',
  data() {
    return {
      searchLists: [],
      search: '',
      searchPlaceholder: ("Search for Songs, Artist, or Playlists"),
    };
  },
  ready:function(){
    this.searchDirect();
    this.cleanInput();
  },
  methods: {
    searchDirect(songName) {
      location.replace("#/search/" + songName)
    },
    cleanInput() {
      this.search = '';
    },
    async loadSearch(songName) {
      try {  
        this.searchLists = null;
        this.searchLists = await MusicService.getMusic(songName);
      } catch (error) {
        console.log(error.message);
      }
    },
  }
}
</script>