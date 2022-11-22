<template>
<div class="profile">
    <div class="userHeader">
        <div class="grid_item">
            <img :src='accImg' alt="Avatar"> 
        </div>
        <div class="grid_item" id="userinfo">
            USER:
            <h1>{{ accUserName }}</h1>
            <!--Todo: implement js for nr of followers-->
            <p>[number] Followers</p>
        </div>
    </div> <br/><br/>

    <div class="redirect">
        <div class="grid_item">
            <button :class="{btnActive:overviewVis}" @click="overviewVis = true, followingVis = false, followersVis = false" > OVERVIEW </button>
        </div>
        <div class="grid_item">
            <button :class="{btnActive:followingVis}" @click="overviewVis = false, followingVis = true, followersVis = false" > FOLLOWING </button>
        </div>
        <div class="grid_item">
            <button :class="{btnActive:followersVis}" @click="overviewVis = false, followingVis = false, followersVis = true" > FOLLOWERS </button>
        </div>
    </div> <br/><br/>

    <div class="profileOverview">
        <div id="overview" v-if="overviewVis">
            <h2> Public playlists </h2><br/>
            <div>
                some text
            </div><br/>
            <h2> Private playlists </h2><br/>
            <div>
                some text
            </div>
            <!--
            Todo: Public playlists
            Todo: Private playlists
            -->
        </div>

        <div id="following" v-if="followingVis">
            <h2> Todo: middle content </h2>
            <!--
            grid of people (img avatar, name below)
            4 columns, many rows?
            -->
        </div>

        <div id="followers" v-if="followersVis">
            <h2> Todo: right content </h2>
            <!--
            grid of people (img avatar, name below)
            4 columns, many rows?
            -->
        </div>
    </div>
    <br><br>
    
</div>
</template>

<style scoped>
/* CSS for ALL of Profile.vue */
.grid_item{
    text-align: left;
    max-height: 125px;
}
h2{
    float: left;
}
.profileOverview{
    display: grid;
    justify-content: left;
    text-align: left;
}

/*CSS for Header with user info*/
.userHeader{
    display: grid;
    grid-template-columns: 25% 25%;
    height: 225px;
}
#userinfo{
    text-align: left;
    padding-top: 25%;
}
img{
    border-radius: 50%;
    max-width: 15rem;
}

/* CSS for navbar with buttons */
.redirect{
    display: grid;
    grid-template-columns: 20% 20% 20%;
    justify-content: left;
}
button{
    border-radius: 2px;
    margin: 5px;
    background: #232323;
}
button:hover{
    background: #292929;
}
.btnActive{
    background: orange!important;
    -webkit-transition: background-color 0.5s ease-out;
    -moz-transition: background-color 0.5s ease-out;
    -o-transition: background-color 0.5s ease-out;
    transition: background-color 0.5s ease-out;
}
</style>

<script> 
export default {
    name: 'Profile',
    data () {
        return {
            overviewVis: true,
            followingVis: false,
            followersVis: false,
            // placeholder username and avatar
            accUserName: "John Doe",
            accImg: require("@/assets/userMenuImg.png"),
        }
    }
}
</script>