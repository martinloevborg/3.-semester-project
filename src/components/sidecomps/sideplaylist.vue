<template>

    <div id="sideplaylist">
        <div class="playlistTitle">YOUR PLAYLISTS</div>
        <router-link to="/library/createplaylist" id="routing"><i id="playlistIcon" class="material-icons">add_circle_outline</i></router-link>
            <div class="playlistsSide">
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
                <div class="menu_item">
                    <router-link to="/playlist/secret" id="routing">Secret playlist</router-link>
                </div>
            </div>
    <!--
        TODO: Generate automatic playlist routes for according to userstate
    -->
    </div>
</template>

<script>
export default {
    name: 'SidePlaylist',
    data() {
        return {
        }
    },
}
</script>