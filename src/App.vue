<template>
  <div id="app">
    <div class="container">
      <div class="menu_column"> 
        <sidebarmenu/>
      </div>
      <div class="middle_column">
        <div class="toprow_wrapper"> 
          <searchbar/>
        </div>
        <div class="middlewrapper">
          <router-view/>
        </div>
      </div>
      <div class="music_column"> 
        <musicplayer/>
      </div>
    </div>
  </div>
</template>


<script>
  import musicplayer from '@/components/musicplayer.vue';
  import sidebarmenu from '@/components/sidebarmenu.vue';
  import searchbar from '@/components/searchbar.vue';

export default {
  components: {
    musicplayer,
    sidebarmenu,
    searchbar,
  },
}
</script>
