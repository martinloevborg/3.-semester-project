<template>
<div class="account">
    <div class="gridWrapper">
    <div id="ui_header">Account</div>
    <!-- fix in router index -->

    <div class="infoOverhead">Account overview</div>
    <div class="grid_container"> 
        <div class="grid_item1">  
            <p>Username</p>
            <p>E-mail</p>
            <p>Date of birth</p>
            <p>Password</p>
        </div>

        <div class="grid_item1">
            <!--Todo: fetch user info. currently static placeholders-->
            <p id="uInfo_username">(username)</p>
            <p id="uInfo_email">(email)</p>
            <p id="uInfo_dateBirth">(date of birth)</p>
            <p id="uInfo_password">(hidden password)</p>
        </div> <!--Should we use slot? https://www.htmlquick.com/reference/tags/slot.html-->
    </div><br/>

    <div class="epButton" id="buttonEdit">
        <button @click="$router.push('./profile/editprofile')">Edit profile</button>
    </div> 
 
    <div class="infoOverhead3">Manage subscription</div>
    <div class="grid_container subscription">
        <div class="grid_item2 sub">
            <div class="infoOverhead2">Premium</div>
            <ul class="premium_list">
                <li> Listen to music add-free </li>   
                <li> Change colour </li>
                <li> On-demand playback </li>
            </ul>
        </div>

        <div class="inlineFiller"></div>

        <div class="grid_item2 nonsub">
            <div class="infoOverhead2">Free</div>
            <ul class="freemium_list">
                <li> Play music in shuffle play only </li>   
                <li> Ads </li>
            </ul>
        </div>

        <!--Button under premium (not functional)-->
    </div>
    </div>
</div>
</template>

<style scoped>
.epButton{
    text-align: left;
    padding-bottom: 6.6%;
}

.infoOverhead{
    font-size: 18px;
    text-align: left;
    padding-bottom: 10px;
}

.infoOverhead2{
    font-size: 24px;
    text-align: center;
    padding-bottom: 14px;
}

.infoOverhead3{
    font-size: 18px;
    text-align: left;
    padding-bottom: 16px;
}

.account{
    justify-content: center;
    display: flex;
    flex-direction: row;
    width: 80%;
    margin: 0 auto;
}

.gridWrapper{
    display: flex;
    flex-direction: column;
    width: 100%;
}

.grid_container{
    display: flex;
    position: relative;
    flex-direction: row;
    text-align: left;
    width: 100%;
}

.grid_item1 {
    display:flex;
    flex-direction: column;
    text-align: left;
    width: 100%;
    font-weight: 400;
}

.grid_item2 {
    display:flex;
    flex-direction: column;
    text-align: left;
    width: 100%;
    font-weight: 700;
}

.subscription {
    background: #181818;
    border-radius: 6px;
    padding: 24px 70px;
    flex-direction: row;
    display: flex;
    width: 85%;
    height: 280px;
}

.sub {
    padding-top: 24px;
    width: 50%;
    height: 95%;
    background: linear-gradient(150.89deg, #E75353 -4.38%, #FED97B 118.74%);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
}

.inlineFiller {
    width: 40%;
    display: flex;
    flex-direction: column;
}

.nonsub {
    padding-top: 24px;
    width: 50%;
    height: 95%;
    background: #292929;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
}

.premium_list{
    padding-left: 16px;
}

.freemium_list{
    padding-left: 16px;
}

/* removing the default list bullet point and then adding custom check mark bullet points*/
li{
    list-style: none;
    text-align: left;
    display: flex;
    padding-bottom: 10px;
} 
li:before{
    content: "\2713";
    display: flex;
}
</style>

<script> 
/*
export default {
name: 'Account',
    data: {

    },
    methods: {
        
    }
} 
*/
</script>
