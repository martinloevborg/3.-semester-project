<!-- TODO : Add more stuff to match design and route, and fix addresses. -->
<template>
<div id="sidecontainer">
    <div class="sidebarmenu_container">
        <div class="sideprofile_container">
          <SideUserMenu/>
        </div>
        <div class="menu_container">
          <div class="menu_item">
            <router-link to="/" id="routing_main"><i id="menuicon" class="fas fa-home"></i>Home</router-link>
          </div>
          <div class="menu_item">
            <router-link to="/browse" id="routing_main"><i id="menuicon" class="fas fa-globe-asia"></i>Browse</router-link>
          </div>
          <div class="menu_item">
            <router-link to="/discover" id="routing_main"><i id="menuicon" class="fas fa-search-plus"></i>Discover</router-link>
          </div>
          <div class="menu_item">
            <router-link to="/addsong" id="routing_main"><i id="menuicon" class="fas fa-music"></i>Add Song</router-link>
          </div>
          <div class="sidelibrary_container">
            <SideLibrary/>
          </div>
          <div class="sideplaylist_container">
            <SidePlaylist/>
           </div>
        </div>
    </div>
</div>
</template>

<script>
import SideLibrary from '@/components/sidecomps/sidelibrary.vue'
import SidePlaylist from '@/components/sidecomps/sideplaylist.vue'
import SideUserMenu from '@/components/sidecomps/sideusermenu.vue'

export default {
  name: 'EditProfile',
  components: {
    SideLibrary,
    SidePlaylist,
    SideUserMenu
  },
  data () {
    return {
    };
  },
}
</script>

