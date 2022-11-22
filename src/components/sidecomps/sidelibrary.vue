<template>
    <div id="sidelibrary">YOUR LIBRARY
        <div class="menu_item">
            <router-link to="/library/madeforyou" id="routing"><i id="menuicon" class="fas fa-star"></i>Made for you</router-link>
        </div>
        <div class="menu_item">
            <router-link to="/library/likedsongs" id="routing"><i id="menuicon" class="fas fa-heart"></i>Liked songs</router-link>
        </div>
        <div class="menu_item">
            <router-link to="/library/artists" id="routing"><i id="menuicon" class="fas fa-user"></i>Artists</router-link>
        </div>
        <div class="menu_item">
            <router-link to="/library/albums" id="routing"><i id="menuicon" class="fas fa-compact-disc"></i>Albums</router-link>
        </div>
        <div class="menu_item">
            <router-link to="/library/podcasts" id="routing"><i id="menuicon" class="fas fa-microphone"></i>Podcasts</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SideLibrary',
    data() {
        return {
        }
    },
}
</script>